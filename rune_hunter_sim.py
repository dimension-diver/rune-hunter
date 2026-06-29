#!/usr/bin/env python3
"""
Rune Master / Whitebox Combat Simulator
Modular toolkit for testing different rules combinations.

ARCHITECTURE
------------
RulesModule     -- named bundle of HD, attack, AC, damage rules
CharacterDef    -- class definition referencing a RulesModule
MonsterDef      -- monster stat block
Encounter       -- party + monsters + rules context
simulate()      -- run N combats, return stats

Configure encounters at the bottom of the file.
RUNS and VERBOSE_SEED control output volume.

SOURCE SYSTEMS
--------------
WB   -- S&W Whitebox (descending AC, d6-based HD tables)
RM   -- Rune Master custom (descending AC, straight dice)
PE   -- Planet Eris house rules (0E/OD&D matrix, d6-based HD)
BTSC -- Beneath the Sunken Catacombs (ascending AC, d6 HD)
OED  -- OED/Delta's Target20 system (descending AC, d8 HD)
"""

import random
import statistics
from dataclasses import dataclass, field
from typing import List, Optional, Callable


# ─── CONFIG ──────────────────────────────────────────────────────────────────

RUNS         = 5000
VERBOSE_SEED = 42   # set to None to suppress verbose output


# ═══════════════════════════════════════════════════════════════════════════
# ATTACK PROGRESSIONS
# Index 0 = level 1. All values are flat attack bonuses added to d20 roll.
# ═══════════════════════════════════════════════════════════════════════════

# ── S&W Whitebox (derived from attack tables) ────────────────────────────
WB_FIGHTER    = [0, 1, 2, 2, 3, 4, 4, 5, 6, 6]
WB_CLERIC     = [0, 0, 0, 1, 1, 2, 2, 3, 4, 5]
WB_MAGICUSER  = [0, 0, 0, 0, 1, 1, 2, 2, 3, 3]

# ── Rune Master custom ────────────────────────────────────────────────────
RM_FAST       = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
RM_MEDIUM     = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
RM_SLOW       = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3]

# ── Planet Eris (derived from OD&D combat matrix, Jimm Johnson) ──────────
# Source: "Planet Eris House Rules" by Jimm Johnson, Scribes of Sparn
# Derived by reading the Character Combat Matrix: flat bonus = 10 - (roll needed to hit AC9)
# FM has its own row at every level (1 per level), improving by 1/level.
# Matrix caps at roll=2 at levels 9-10, so bonus tops out at +8 rather than +9.
# Cleric column shows 2-level bands (1-2, 3-4, ...), improving every 2 levels.
# MU column shows 3-level bands (1-3, 4-6, ...), improving every 3 levels.
# Thieves use Cleric progression ("Thieves use cleric's progression for combat to hit rolls").
PE_FIGHTING_MAN  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8]  # +1/level, caps at +8
PE_CLERIC_THIEF  = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]  # improves every 2 levels
PE_MAGICUSER     = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3]  # improves every 3 levels

# ── Beneath the Sunken Catacombs (Paul Bantock) ───────────────────────────
# Source: "Beneath the Sunken Catacombs 2nd Ed." by Paul Bantock
# Uses ASCENDING AC (unarmored=10, leather=12, chain=14, plate=16).
# Attack bonus is the "To Hit" column directly from each class advancement table.
# Warrior: +1 per level straight.
# Sorcerer: improves every 2 levels starting at +0.
# Priest and Thief share the same progression.
BTSC_WARRIOR   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
BTSC_SORCERER  = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
BTSC_PRIEST    = [0, 1, 2, 2, 3, 4, 5, 5, 6, 7]
BTSC_THIEF     = [0, 1, 2, 2, 3, 4, 5, 5, 6, 7]  # identical to Priest

# ── OED / Delta's Target20 (placeholder -- see note below) ───────────────
# Source: OED House Rules (Daniel "Delta" Collins, oedgames.com)
# Target20: d20 + fighter level + AC >= 20 to hit.
# This is equivalent to WB_FIGHTER with bonus = level - 1 (since d20 + (level-1) + AC >= 20
# rearranges to d20 + (level-1) >= 20 - AC = 19 - AC + 1 = needed roll in descending AC).
# Effectively: atk_bonus at level N = N - 1 (for fighters).
# Non-fighters: atk_bonus = (level // 2) for clerics, (level // 3) for MU.
OED_FIGHTER  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # level - 1
OED_CLERIC   = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]   # level // 2
OED_MAGICUSER= [0, 0, 0, 1, 1, 1, 2, 2, 2, 3]   # level // 3


# ═══════════════════════════════════════════════════════════════════════════
# HIT DICE SYSTEMS
# Each is a callable: hd_system(level) -> list of (die_size, modifier) tuples
# ═══════════════════════════════════════════════════════════════════════════

def hd_straight(die, modifier=0):
    """
    Roll die every level with optional per-die modifier, minimum 1 per die.
    hd_straight(6, +1) -> d6+1 per level, range 2-7
    hd_straight(6, -1) -> d6-1 min 1 per level, faces {1,1,2,3,4,5}
    hd_straight(8)     -> straight d8 per level
    """
    def roll(level):
        return [(die, modifier)] * level
    name = f"straight_d{die}"
    if modifier: name += f"{modifier:+d}"
    roll.__name__ = name
    return roll

def hd_wb_table(table):
    """
    Whitebox HD system from explicit (total_dice, flat_bonus) table.
    Each entry is the TOTAL hit dice at that level, not incremental.
    X+1 HD = Xd6 + 1 flat HP bonus.
    table index 0 = level 1.
    """
    def roll(level):
        idx = min(level - 1, len(table) - 1)
        dice, bonus = table[idx]
        return [(6, 0)] * dice + [(1, 0)] * bonus
    roll.__name__ = "wb_table"
    return roll

def hd_btsc_warrior():
    """
    BtSC Warrior: 1d6/level with Natural Toughness (roll twice, take higher).
    Implemented as advantage on each die roll individually.
    """
    def roll(level):
        # Each die gets rolled with advantage (two d6, take higher).
        # We encode this as a special marker: (die=6, modifier='advantage').
        # The roll_hp method handles the 'advantage' sentinel.
        return [(6, 'advantage')] * level
    roll.__name__ = "btsc_warrior_d6adv"
    return roll

def hd_btsc_sorcerer():
    """
    BtSC Sorcerer: gains 1d6 only at odd levels (L1,L3,L5,L7,L9).
    At even levels, no new die is added (character gains +1 minimum from advancement).
    Total dice at each level: 1,1,2,2,3,3,4,4,5,5
    """
    total_dice_by_level = [1,1,2,2,3,3,4,4,5,5]
    def roll(level):
        idx = min(level - 1, len(total_dice_by_level) - 1)
        dice = total_dice_by_level[idx]
        return [(6, 0)] * dice
    roll.__name__ = "btsc_sorcerer"
    return roll

def hd_btsc_cleric_thief():
    """
    BtSC Priest and Thief: 1d6/level with flat +1 HP bonus at levels 4 and 8.
    Total dice table: 1,2,3,(3+1),4,5,6,(6+1),7,8
    """
    # (dice, bonus) per level
    table = [(1,0),(2,0),(3,0),(3,1),(4,0),(5,0),(6,0),(6,1),(7,0),(8,0)]
    def roll(level):
        idx = min(level - 1, len(table) - 1)
        dice, bonus = table[idx]
        return [(6, 0)] * dice + [(1, 0)] * bonus
    roll.__name__ = "btsc_cleric_thief"
    return roll

# S&W Whitebox HD tables: (total_dice, flat_bonus) per level
WB_HD_FIGHTER   = hd_wb_table([(1,1),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0)])
WB_HD_CLERIC    = hd_wb_table([(1,0),(2,0),(3,0),(3,1),(4,0),(5,0),(6,0),(6,1),(7,0),(8,0)])
WB_HD_MAGICUSER = hd_wb_table([(1,0),(1,1),(2,0),(2,1),(3,0),(3,1),(4,0),(4,1),(5,0),(5,1)])

# Rune Master straight dice
RM_HD_D8   = hd_straight(8)
RM_HD_D6   = hd_straight(6)
RM_HD_D4   = hd_straight(4)

# d6-only variants (equivalent to variable dice)
D6ONLY_FIGHTER = hd_straight(6, +1)   # {2,3,4,5,6,7} per die -- approximates d8
D6ONLY_CLERIC  = hd_straight(6,  0)   # {1,2,3,4,5,6} per die
D6ONLY_MU      = hd_straight(6, -1)   # {1,1,2,3,4,5} per die -- approximates d4

# Planet Eris HD (same as D6ONLY -- PE explicitly specifies d6+1/d6/d6-1 by class)
PE_HD_FIGHTING_MAN = hd_straight(6, +1)   # d6+1/level
PE_HD_CLERIC_THIEF = hd_straight(6,  0)   # d6/level
PE_HD_MAGICUSER    = hd_straight(6, -1)   # d6-1/level (same as D6ONLY_MU)

# BtSC HD systems
BTSC_HD_WARRIOR      = hd_btsc_warrior()
BTSC_HD_SORCERER     = hd_btsc_sorcerer()
BTSC_HD_PRIEST_THIEF = hd_btsc_cleric_thief()

# OED HD (Delta uses d8 for fighters, d6 for clerics, d4 for MU, per his house rules)
OED_HD_FIGHTER  = hd_straight(8)
OED_HD_CLERIC   = hd_straight(6)
OED_HD_MAGICUSER= hd_straight(4)


# ═══════════════════════════════════════════════════════════════════════════
# AC SYSTEMS
# ═══════════════════════════════════════════════════════════════════════════

# Descending AC (whitebox standard): unarmored = 9, lower is better
DESCENDING_AC = {
    "unarmored":    9,
    "leather":      7,
    "chain":        5,
    "plate":        3,
    "plate_shield": 2,
}

# Ascending AC (BtSC): unarmored = 10, higher is better
ASCENDING_AC = {
    "unarmored":    10,
    "leather":      12,
    "chain":        14,
    "plate":        16,
    "plate_shield": 17,
}

def descending_to_hit(atk_bonus, target_ac):
    """Return (hit:bool, roll:int) using descending AC."""
    roll   = random.randint(1, 20)
    needed = 19 - target_ac
    return roll + atk_bonus >= needed, roll

def ascending_to_hit(atk_bonus, target_ac):
    """Return (hit:bool, roll:int) using ascending AC. Hit if d20 + bonus >= AC."""
    roll = random.randint(1, 20)
    return roll + atk_bonus >= target_ac, roll

def hit_prob_descending(atk_bonus, target_ac):
    needed = 19 - target_ac
    hits   = sum(1 for r in range(1, 21) if r + atk_bonus >= needed)
    return hits / 20

def hit_prob_ascending(atk_bonus, target_ac):
    hits = sum(1 for r in range(1, 21) if r + atk_bonus >= target_ac)
    return hits / 20


# ═══════════════════════════════════════════════════════════════════════════
# DAMAGE SYSTEMS
# ═══════════════════════════════════════════════════════════════════════════

def dmg_flat(die):
    def roll():
        return random.randint(1, die)
    roll.__name__ = f"d{die}"
    return roll

def dmg_max(die):
    def roll():
        return die
    roll.__name__ = f"max_d{die}"
    return roll

def dmg_plus_mod(base_dmg_fn, modifier):
    def roll():
        return max(1, base_dmg_fn() + modifier)
    roll.__name__ = f"{base_dmg_fn.__name__}+{modifier}"
    return roll

DMG_D4  = dmg_flat(4)
DMG_D6  = dmg_flat(6)
DMG_D8  = dmg_flat(8)
DMG_D10 = dmg_flat(10)


# ═══════════════════════════════════════════════════════════════════════════
# RULES MODULE
# A named bundle of rules that can be mixed and matched.
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class RulesModule:
    name:        str
    atk_prog:    list          # attack bonus by level (0-indexed)
    hd_system:   Callable      # hd_system(level) -> list of (die, mod) tuples
    ac_table:    dict          # armor name -> AC value
    to_hit_fn:   Callable      # to_hit_fn(atk_bonus, target_ac) -> (hit:bool, roll:int)
    hit_prob_fn: Callable      # hit_prob_fn(atk_bonus, target_ac) -> float
    dmg_fn:      Callable      # dmg_fn() -> int

    def atk_bonus(self, level):
        idx = min(level - 1, len(self.atk_prog) - 1)
        return self.atk_prog[idx]

    def roll_hp(self, level):
        """
        Reroll all HD each level. Take new roll if higher than current HP,
        otherwise current HP + 1. Simulates level-by-level advancement.
        Handles (die, 'advantage') sentinel for BtSC Warrior Natural Toughness.
        """
        hp = 0
        for lvl in range(1, level + 1):
            dice_list = self.hd_system(lvl)
            rolled = 0
            for item in dice_list:
                d, m = item
                if m == 'advantage':
                    # Roll twice, take higher (Natural Toughness)
                    r1 = random.randint(1, d)
                    r2 = random.randint(1, d)
                    rolled += max(r1, r2)
                else:
                    rolled += max(1, random.randint(1, d) + m)
            hp = max(hp + 1, rolled)
        return hp

    def ac(self, armor):
        if isinstance(armor, int):
            return armor
        return self.ac_table.get(armor, self.ac_table.get("unarmored", 9))


# ── Pre-built S&W Whitebox modules ───────────────────────────────────────

WB_FIGHTER_RULES = RulesModule(
    name        = "WB Fighter",
    atk_prog    = WB_FIGHTER,
    hd_system   = WB_HD_FIGHTER,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

WB_CLERIC_RULES = RulesModule(
    name        = "WB Cleric",
    atk_prog    = WB_CLERIC,
    hd_system   = WB_HD_CLERIC,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

WB_MU_RULES = RulesModule(
    name        = "WB Magic-User",
    atk_prog    = WB_MAGICUSER,
    hd_system   = WB_HD_MAGICUSER,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

# ── Pre-built Rune Master modules ─────────────────────────────────────────

RM_HUNTER_RULES = RulesModule(
    name        = "RM Hunter",
    atk_prog    = RM_FAST,
    hd_system   = RM_HD_D8,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

RM_DELVER_RULES = RulesModule(
    name        = "RM Delver",
    atk_prog    = RM_MEDIUM,
    hd_system   = RM_HD_D6,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

RM_CASTER_RULES = RulesModule(
    name        = "RM Caster",
    atk_prog    = RM_SLOW,
    hd_system   = RM_HD_D4,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

# ── Pre-built Planet Eris modules ─────────────────────────────────────────
# Source: "Planet Eris House Rules" (Jimm Johnson / Scribes of Sparn, 2012-2013)
# OD&D-compatible. Attack progressions derived from Character Combat Matrix.
# HD: explicitly d6+1 (FM), d6 (Cleric/Thief), d6-1 (MU) per level.

PE_FM_RULES = RulesModule(
    name        = "PE Fighting-Man",
    atk_prog    = PE_FIGHTING_MAN,
    hd_system   = PE_HD_FIGHTING_MAN,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

PE_CLERIC_RULES = RulesModule(
    name        = "PE Cleric/Thief",
    atk_prog    = PE_CLERIC_THIEF,
    hd_system   = PE_HD_CLERIC_THIEF,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

PE_MU_RULES = RulesModule(
    name        = "PE Magic-User",
    atk_prog    = PE_MAGICUSER,
    hd_system   = PE_HD_MAGICUSER,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

# ── Pre-built Beneath the Sunken Catacombs modules ────────────────────────
# Source: "Beneath the Sunken Catacombs 2nd Ed." (Paul Bantock)
# Uses ASCENDING AC. Damage is d6-based (d6-1 / d6 / d6+1 by weapon class).
# NOTE: BtSC monsters use ascending AC too. Use ASCENDING_AC for monster AC as well.

BTSC_WARRIOR_RULES = RulesModule(
    name        = "BtSC Warrior",
    atk_prog    = BTSC_WARRIOR,
    hd_system   = BTSC_HD_WARRIOR,
    ac_table    = ASCENDING_AC,
    to_hit_fn   = ascending_to_hit,
    hit_prob_fn = hit_prob_ascending,
    dmg_fn      = DMG_D6,
)

BTSC_SORCERER_RULES = RulesModule(
    name        = "BtSC Sorcerer",
    atk_prog    = BTSC_SORCERER,
    hd_system   = BTSC_HD_SORCERER,
    ac_table    = ASCENDING_AC,
    to_hit_fn   = ascending_to_hit,
    hit_prob_fn = hit_prob_ascending,
    dmg_fn      = DMG_D6,
)

BTSC_PRIEST_RULES = RulesModule(
    name        = "BtSC Priest",
    atk_prog    = BTSC_PRIEST,
    hd_system   = BTSC_HD_PRIEST_THIEF,
    ac_table    = ASCENDING_AC,
    to_hit_fn   = ascending_to_hit,
    hit_prob_fn = hit_prob_ascending,
    dmg_fn      = DMG_D6,
)

BTSC_THIEF_RULES = RulesModule(
    name        = "BtSC Thief",
    atk_prog    = BTSC_THIEF,
    hd_system   = BTSC_HD_PRIEST_THIEF,
    ac_table    = ASCENDING_AC,
    to_hit_fn   = ascending_to_hit,
    hit_prob_fn = hit_prob_ascending,
    dmg_fn      = DMG_D6,
)

# ── Pre-built OED modules ─────────────────────────────────────────────────
# Source: OED House Rules (Daniel "Delta" Collins, oedgames.com)
# Target20: d20 + level + AC >= 20. Equivalent flat bonus = level - 1 for fighters.
# Standard descending AC. Uses d8/d6/d4 HD per class.

OED_FIGHTER_RULES = RulesModule(
    name        = "OED Fighter",
    atk_prog    = OED_FIGHTER,
    hd_system   = OED_HD_FIGHTER,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

OED_CLERIC_RULES = RulesModule(
    name        = "OED Cleric",
    atk_prog    = OED_CLERIC,
    hd_system   = OED_HD_CLERIC,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

OED_MU_RULES = RulesModule(
    name        = "OED Magic-User",
    atk_prog    = OED_MAGICUSER,
    hd_system   = OED_HD_MAGICUSER,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)


# ═══════════════════════════════════════════════════════════════════════════
# COMBATANTS
# ═══════════════════════════════════════════════════════════════════════════

class Combatant:
    def __init__(self, name, rules, level, armor="chain", atk_mod=0, dmg_fn=None):
        self.name     = name
        self.rules    = rules
        self.level    = level
        self.armor    = armor
        self.ac       = rules.ac(armor)
        self.atk_mod  = atk_mod
        self.dmg_fn   = dmg_fn or rules.dmg_fn
        self.max_hp   = 0
        self.hp       = 0

    def reset(self):
        self.max_hp = self.rules.roll_hp(self.level)
        self.hp     = self.max_hp

    @property
    def atk_bonus(self):
        return self.rules.atk_bonus(self.level) + self.atk_mod

    def attack(self, target, verbose=False):
        hit, roll = self.rules.to_hit_fn(self.atk_bonus, target.ac)
        damage = 0
        if hit:
            damage  = self.dmg_fn()
            target.hp -= damage
        if verbose:
            # Display needed roll differently for ascending vs descending
            if self.rules.to_hit_fn == ascending_to_hit:
                needed = target.ac
                print(f"  {self.name} -> {target.name}: "
                      f"roll {roll} + {self.atk_bonus} = {roll+self.atk_bonus} "
                      f"vs AC{needed} ({'HIT' if hit else 'miss'})"
                      + (f" {damage}dmg [{target.hp}hp]" if hit else ""))
            else:
                needed = 19 - target.ac
                print(f"  {self.name} -> {target.name}: "
                      f"roll {roll} + {self.atk_bonus} = {roll+self.atk_bonus} "
                      f"vs {needed} ({'HIT' if hit else 'miss'})"
                      + (f" {damage}dmg [{target.hp}hp]" if hit else ""))
        return hit, damage

    def is_alive(self):
        return self.hp > 0


class Monster(Combatant):
    """
    Whitebox-style monster. AC system should match the party's rules module.
    For descending AC systems (WB/RM/PE/OED): pass ac_system=DESCENDING_AC
    For ascending AC systems (BtSC): pass ac_system=ASCENDING_AC
    atk_bonus defaults to HD (WB convention).
    """
    def __init__(self, name, hd, armor="leather", dmg_die=6,
                 atk_bonus_override=None, ac_override=None,
                 ac_system=None, ascending=False):
        if ac_system is None:
            ac_system = ASCENDING_AC if ascending else DESCENDING_AC
        to_hit = ascending_to_hit if ascending else descending_to_hit
        hit_prob = hit_prob_ascending if ascending else hit_prob_descending

        mon_atk  = [atk_bonus_override if atk_bonus_override is not None else hd] * 10
        mon_hd   = hd_straight(8)
        mon_dmg  = dmg_flat(dmg_die)
        rules    = RulesModule(
            name        = f"{hd}HD monster",
            atk_prog    = mon_atk,
            hd_system   = mon_hd,
            ac_table    = ac_system,
            to_hit_fn   = to_hit,
            hit_prob_fn = hit_prob,
            dmg_fn      = mon_dmg,
        )
        super().__init__(name, rules, level=hd,
                         armor=ac_override if ac_override is not None else armor)
        self.hd = hd
        if ac_override is not None:
            self.ac = ac_override


# ═══════════════════════════════════════════════════════════════════════════
# SIMULATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════

def run_combat(party, monsters, verbose=False):
    round_num = 0
    while True:
        round_num += 1
        if verbose:
            print(f"\n--- Round {round_num} ---")

        living_monsters = [m for m in monsters if m.is_alive()]
        if not living_monsters:
            break

        for pc in party:
            if not pc.is_alive():
                continue
            target = random.choice(living_monsters)
            pc.attack(target, verbose=verbose)
            living_monsters = [m for m in monsters if m.is_alive()]
            if not living_monsters:
                break

        living_monsters = [m for m in monsters if m.is_alive()]
        if not living_monsters:
            break

        living_pcs = [pc for pc in party if pc.is_alive()]
        if not living_pcs:
            break
        for monster in living_monsters:
            target = random.choice(living_pcs)
            monster.attack(target, verbose=verbose)
            living_pcs = [pc for pc in party if pc.is_alive()]
            if not living_pcs:
                break

        if not any(pc.is_alive() for pc in party):
            break

        if round_num >= 200:
            if verbose:
                print("  [timeout]")
            break

    living_pcs      = [pc for pc in party if pc.is_alive()]
    living_monsters = [m for m in monsters if m.is_alive()]
    party_won       = len(living_pcs) > 0 and len(living_monsters) == 0
    return party_won, round_num, living_pcs


def simulate(label, party_factory, monster_factory,
             runs=RUNS, verbose_seed=VERBOSE_SEED):
    results     = []
    rounds_list = []
    surv_list   = []

    for i in range(runs):
        if verbose_seed is not None and i == 0:
            random.seed(verbose_seed)

        party    = party_factory()
        monsters = monster_factory()
        for c in party + monsters:
            c.reset()

        verbose = (verbose_seed is not None and i == 0)
        if verbose:
            print(f"\n=== VERBOSE: {label} (seed {verbose_seed}) ===")
            for c in party:
                print(f"  PC:  {c.name} L{c.level} {c.rules.name} | "
                      f"HP {c.hp} | ATK +{c.atk_bonus} | AC {c.ac}")
            for m in monsters:
                print(f"  MON: {m.name} {m.hd}HD | "
                      f"HP {m.hp} | ATK +{m.atk_bonus} | AC {m.ac}")

        won, rounds, alive = run_combat(party, monsters, verbose=verbose)
        results.append(won)
        rounds_list.append(rounds)
        surv_list.append(len(alive))

    win_rate   = sum(results) / runs * 100
    avg_rounds = statistics.mean(rounds_list)
    avg_surv   = statistics.mean(surv_list)

    print(f"\n{'─'*55}")
    print(f"  {label}")
    print(f"  Win rate: {win_rate:5.1f}%  |  "
          f"Avg rounds: {avg_rounds:.1f}  |  "
          f"Avg survivors: {avg_surv:.1f}")
    print(f"{'─'*55}")
    return win_rate, avg_rounds


# ═══════════════════════════════════════════════════════════════════════════
# ANALYSIS TABLES
# ═══════════════════════════════════════════════════════════════════════════

def print_hp_comparison(samples=2000):
    """
    Average HP by level for each class/system.
    Simulated using reroll-with-floor advancement (always go up by at least 1).
    Handles (die, 'advantage') sentinel for BtSC Warrior Natural Toughness.
    """
    configs = [
        ("WB Fighter (d6, 1+1...10)",    WB_HD_FIGHTER),
        ("WB Cleric  (d6, cap 8)",        WB_HD_CLERIC),
        ("WB MU      (d6, cap 5+1)",      WB_HD_MAGICUSER),
        ("RM Hunter  (d8 straight)",      RM_HD_D8),
        ("RM Delver  (d6 straight)",      RM_HD_D6),
        ("RM Caster  (d4 straight)",      RM_HD_D4),
        ("PE FM      (d6+1/level)",        PE_HD_FIGHTING_MAN),
        ("PE Cleric  (d6/level)",          PE_HD_CLERIC_THIEF),
        ("PE MU      (d6-1/level)",        PE_HD_MAGICUSER),
        ("BtSC Warrior (d6 adv/level)",   BTSC_HD_WARRIOR),
        ("BtSC Sorcerer (d6 odd levels)", BTSC_HD_SORCERER),
        ("BtSC Priest (d6, +1 at L4,L8)",BTSC_HD_PRIEST_THIEF),
        ("OED Fighter (d8/level)",         OED_HD_FIGHTER),
        ("OED Cleric  (d6/level)",         OED_HD_CLERIC),
        ("OED MU      (d4/level)",         OED_HD_MAGICUSER),
    ]

    def sim_hp(hd_fn, level, n=samples):
        totals = []
        for _ in range(n):
            hp = 0
            for lvl in range(1, level + 1):
                dice_list = hd_fn(lvl)
                rolled = 0
                for item in dice_list:
                    d, m = item
                    if m == 'advantage':
                        r1 = random.randint(1, d)
                        r2 = random.randint(1, d)
                        rolled += max(r1, r2)
                    else:
                        rolled += max(1, random.randint(1, d) + m)
                hp = max(hp + 1, rolled)
            totals.append(hp)
        return sum(totals) / len(totals)

    print(f"\n── AVERAGE HP BY LEVEL (simulated, n={samples}) ──")
    header = f"  {'Class':<38}" + "".join(f"  L{l:<4}" for l in range(1, 11))
    print(header)
    for label, hd_fn in configs:
        avgs = [sim_hp(hd_fn, lvl) for lvl in range(1, 11)]
        row  = "".join(f"  {a:>5.1f}" for a in avgs)
        print(f"  {label:<38}{row}")


def print_hit_prob_table():
    """Hit probabilities for all progressions vs common ACs (both AC systems)."""
    print("\n── HIT PROBABILITY BY LEVEL -- DESCENDING AC SYSTEMS ──")
    desc_acs    = [9, 7, 5, 3, 2]
    desc_labels = ["AC9", "AC7", "AC5", "AC3", "AC2"]
    desc_configs = [
        ("WB Fighter",    WB_FIGHTER),
        ("WB Cleric",     WB_CLERIC),
        ("WB Magic-User", WB_MAGICUSER),
        ("RM Fast",       RM_FAST),
        ("RM Medium",     RM_MEDIUM),
        ("RM Slow",       RM_SLOW),
        ("PE Fighting-Man",  PE_FIGHTING_MAN),
        ("PE Cleric/Thief",  PE_CLERIC_THIEF),
        ("PE Magic-User",    PE_MAGICUSER),
        ("OED Fighter",      OED_FIGHTER),
        ("OED Cleric",       OED_CLERIC),
        ("OED Magic-User",   OED_MAGICUSER),
    ]
    for prog_name, prog in desc_configs:
        print(f"\n  {prog_name}")
        print("  " + f"{'Lvl':>3}  " + "  ".join(f"{l:>5}" for l in desc_labels))
        for lvl in range(1, 11):
            bonus = prog[lvl - 1]
            probs = [f"{hit_prob_descending(bonus, ac)*100:5.1f}%" for ac in desc_acs]
            print(f"  {lvl:>3}  " + "  ".join(probs))

    print("\n── HIT PROBABILITY BY LEVEL -- ASCENDING AC SYSTEMS (BtSC) ──")
    asc_acs    = [10, 12, 14, 16, 17]
    asc_labels = ["AC10", "AC12", "AC14", "AC16", "AC17"]
    asc_configs = [
        ("BtSC Warrior",  BTSC_WARRIOR),
        ("BtSC Sorcerer", BTSC_SORCERER),
        ("BtSC Priest",   BTSC_PRIEST),
        ("BtSC Thief",    BTSC_THIEF),
    ]
    for prog_name, prog in asc_configs:
        print(f"\n  {prog_name}")
        print("  " + f"{'Lvl':>3}  " + "  ".join(f"{l:>5}" for l in asc_labels))
        for lvl in range(1, 11):
            bonus = prog[lvl - 1]
            probs = [f"{hit_prob_ascending(bonus, ac)*100:5.1f}%" for ac in asc_acs]
            print(f"  {lvl:>3}  " + "  ".join(probs))


def print_symmetry_gap():
    """Attack bonus gap: PC level vs same-HD monster (descending AC systems)."""
    print("\n── PC vs SAME-TIER MONSTER: ATTACK BONUS GAP (descending AC) ──")
    print("  Positive = PC advantage, Negative = monster advantage")
    progs = [
        ("RM Fast",       RM_FAST),
        ("RM Med",        RM_MEDIUM),
        ("PE FM",         PE_FIGHTING_MAN),
        ("OED Fighter",   OED_FIGHTER),
        ("WB Fighter",    WB_FIGHTER),
        ("WB Cleric",     WB_CLERIC),
    ]
    header = f"  {'Lvl':>3}  " + "  ".join(f"{n:>12}" for n, _ in progs)
    print(header)
    for lvl in range(1, 11):
        monster_bonus = lvl
        gaps = [prog[lvl-1] - monster_bonus for _, prog in progs]
        row  = "  ".join(f"{g:>+12d}" for g in gaps)
        print(f"  {lvl:>3}  {row}")


def print_monster_hit_table():
    """Monster hit probability against PC armor (descending AC)."""
    pc_acs    = [9, 7, 5, 3, 2]
    ac_labels = ["AC9", "AC7", "AC5", "AC3", "AC2"]
    print("\n── MONSTER HIT PROBABILITY BY HD vs PC ARMOR (descending AC) ──")
    print("  " + f"{'HD':>3}  " + "  ".join(f"{l:>5}" for l in ac_labels))
    for hd in range(1, 11):
        probs = [f"{hit_prob_descending(hd, ac)*100:5.1f}%" for ac in pc_acs]
        print(f"  {hd:>3}  " + "  ".join(probs))


def print_progression_comparison():
    """Side-by-side attack bonus comparison across all systems."""
    print("\n── ATTACK PROGRESSION COMPARISON (all systems) ──")
    all_progs = [
        ("WB Fighter",    WB_FIGHTER),
        ("WB Cleric",     WB_CLERIC),
        ("WB MU",         WB_MAGICUSER),
        ("RM Fast",       RM_FAST),
        ("RM Medium",     RM_MEDIUM),
        ("RM Slow",       RM_SLOW),
        ("PE FM",         PE_FIGHTING_MAN),
        ("PE Cleric",     PE_CLERIC_THIEF),
        ("PE MU",         PE_MAGICUSER),
        ("BtSC Warrior",  BTSC_WARRIOR),
        ("BtSC Priest",   BTSC_PRIEST),
        ("BtSC Sorcerer", BTSC_SORCERER),
        ("OED Fighter",   OED_FIGHTER),
        ("OED Cleric",    OED_CLERIC),
        ("OED MU",        OED_MAGICUSER),
    ]
    header = f"  {'System':<18}" + "".join(f"  L{l:<2}" for l in range(1, 11))
    print(header)
    for name, prog in all_progs:
        row = "".join(f"  {b:>3}" for b in prog)
        print(f"  {name:<18}{row}")


# ═══════════════════════════════════════════════════════════════════════════
# ENCOUNTERS -- configure here
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print_progression_comparison()
    print_hp_comparison()
    print_hit_prob_table()
    print_symmetry_gap()
    print_monster_hit_table()

    print("\n\n── COMBAT SIMULATIONS ──")

    # ── Benchmark 1: RM vs WB vs PE vs OED at L1 ─────────────────────────
    goblin_factory_desc = lambda: [
        Monster("Goblin", hd=1, armor="leather"),
        Monster("Goblin", hd=1, armor="leather"),
        Monster("Goblin", hd=1, armor="leather"),
    ]

    simulate(
        "RM L1 party (Hunter+Delver+Caster) vs 3x Goblin 1HD",
        party_factory   = lambda: [
            Combatant("Hunter", RM_HUNTER_RULES, 1, armor="chain"),
            Combatant("Delver", RM_DELVER_RULES, 1, armor="leather"),
            Combatant("Caster", RM_CASTER_RULES, 1, armor="unarmored"),
        ],
        monster_factory = goblin_factory_desc,
    )

    simulate(
        "WB L1 party (Fighter+Cleric+MU) vs 3x Goblin 1HD",
        party_factory   = lambda: [
            Combatant("Fighter", WB_FIGHTER_RULES, 1, armor="chain"),
            Combatant("Cleric",  WB_CLERIC_RULES,  1, armor="chain"),
            Combatant("MU",      WB_MU_RULES,      1, armor="unarmored"),
        ],
        monster_factory = goblin_factory_desc,
    )

    simulate(
        "PE L1 party (FM+Cleric+MU) vs 3x Goblin 1HD",
        party_factory   = lambda: [
            Combatant("FM",     PE_FM_RULES,     1, armor="chain"),
            Combatant("Cleric", PE_CLERIC_RULES, 1, armor="chain"),
            Combatant("MU",     PE_MU_RULES,     1, armor="unarmored"),
        ],
        monster_factory = goblin_factory_desc,
    )

    simulate(
        "OED L1 party (Fighter+Cleric+MU) vs 3x Goblin 1HD",
        party_factory   = lambda: [
            Combatant("Fighter", OED_FIGHTER_RULES, 1, armor="chain"),
            Combatant("Cleric",  OED_CLERIC_RULES,  1, armor="chain"),
            Combatant("MU",      OED_MU_RULES,      1, armor="unarmored"),
        ],
        monster_factory = goblin_factory_desc,
    )

    # ── BtSC uses ascending AC -- goblins need ascending AC too ──────────
    goblin_factory_asc = lambda: [
        Monster("Goblin", hd=1, armor="leather", ascending=True),
        Monster("Goblin", hd=1, armor="leather", ascending=True),
        Monster("Goblin", hd=1, armor="leather", ascending=True),
    ]

    simulate(
        "BtSC L1 party (Warrior+Thief+Sorcerer) vs 3x Goblin 1HD [ascending AC]",
        party_factory   = lambda: [
            Combatant("Warrior",  BTSC_WARRIOR_RULES,  1, armor="chain"),
            Combatant("Thief",    BTSC_THIEF_RULES,    1, armor="leather"),
            Combatant("Sorcerer", BTSC_SORCERER_RULES, 1, armor="unarmored"),
        ],
        monster_factory = goblin_factory_asc,
    )

    # ── Benchmark 2: L5 party vs 5HD boss ────────────────────────────────
    simulate(
        "RM L5 party (Hunter+Delver+Caster) vs 5HD boss",
        party_factory   = lambda: [
            Combatant("Hunter", RM_HUNTER_RULES, 5, armor="chain"),
            Combatant("Delver", RM_DELVER_RULES, 5, armor="leather"),
            Combatant("Caster", RM_CASTER_RULES, 5, armor="unarmored"),
        ],
        monster_factory = lambda: [Monster("Boss", hd=5, armor="chain", dmg_die=8)],
    )

    simulate(
        "WB L5 party (Fighter+Cleric+MU) vs 5HD boss",
        party_factory   = lambda: [
            Combatant("Fighter", WB_FIGHTER_RULES, 5, armor="chain"),
            Combatant("Cleric",  WB_CLERIC_RULES,  5, armor="chain"),
            Combatant("MU",      WB_MU_RULES,      5, armor="unarmored"),
        ],
        monster_factory = lambda: [Monster("Boss", hd=5, armor="chain", dmg_die=8)],
    )

    simulate(
        "PE L5 party (FM+Cleric+MU) vs 5HD boss",
        party_factory   = lambda: [
            Combatant("FM",     PE_FM_RULES,     5, armor="chain"),
            Combatant("Cleric", PE_CLERIC_RULES, 5, armor="chain"),
            Combatant("MU",     PE_MU_RULES,     5, armor="unarmored"),
        ],
        monster_factory = lambda: [Monster("Boss", hd=5, armor="chain", dmg_die=8)],
    )

    simulate(
        "OED L5 party (Fighter+Cleric+MU) vs 5HD boss",
        party_factory   = lambda: [
            Combatant("Fighter", OED_FIGHTER_RULES, 5, armor="chain"),
            Combatant("Cleric",  OED_CLERIC_RULES,  5, armor="chain"),
            Combatant("MU",      OED_MU_RULES,      5, armor="unarmored"),
        ],
        monster_factory = lambda: [Monster("Boss", hd=5, armor="chain", dmg_die=8)],
    )


# ═══════════════════════════════════════════════════════════════════════════
# UNTOLD ADVENTURES MODULE
# ═══════════════════════════════════════════════════════════════════════════

# Source: Untold Adventures Deluxe (James M. Spahn, Barrel Rider Games)
# Two classes: Swordsman and Spellcaster.
# Swordsman Combat Specialist: +1 at L1, +1 at L3, L5, L7, L9 = max +5.
# This equals ceil(level/2) -- identical to UA monster attack (HD attack
# as Swordsman of equal level). Perfectly symmetric: PC and same-HD monster
# always have the same attack bonus.
# HD: d6 per level (Swordsman), d6-1 (Spellcaster).

UA_SWORDSMAN_PROG  = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]   # ceil(level/2)
UA_SPELLCASTER_PROG = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # no attack scaling

UA_SWORDSMAN_RULES = RulesModule(
    name        = "UA Swordsman",
    atk_prog    = UA_SWORDSMAN_PROG,
    hd_system   = RM_HD_D6,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)

UA_SPELLCASTER_RULES = RulesModule(
    name        = "UA Spellcaster",
    atk_prog    = UA_SPELLCASTER_PROG,
    hd_system   = D6ONLY_MU,
    ac_table    = DESCENDING_AC,
    to_hit_fn   = descending_to_hit,
    hit_prob_fn = hit_prob_descending,
    dmg_fn      = DMG_D6,
)


# ═══════════════════════════════════════════════════════════════════════════
# SPLIT ATTACK ENGINE
# Rule: a combatant may divide their total attack bonus across multiple
# attacks in a single round, assigning at least +1 per attack.
# Maximum attacks = total bonus. All attacks resolve in the same round.
# ═══════════════════════════════════════════════════════════════════════════

def run_combat_split(party, monsters, split_pcs=True, split_monsters=True):
    """
    Combat engine with optional split-attack support.
    split_pcs:      PCs may divide their bonus across multiple targets.
    split_monsters: Monsters may divide their bonus across multiple targets.
    Split is distributed as evenly as possible across available targets,
    up to a maximum of (total_bonus) attacks.
    """
    initial = len(party)
    rounds = 0

    def resolve_attacks(attacker, targets, allow_split):
        total_bonus = attacker.atk_bonus
        rules = attacker.rules
        if allow_split and total_bonus >= 2 and len(targets) >= 2:
            n = min(total_bonus, len(targets))
            base  = total_bonus // n
            extra = total_bonus % n
            chosen = random.sample(targets, n)
            for i, t in enumerate(chosen):
                bonus = base + (1 if i < extra else 0)
                hit, _ = rules.to_hit_fn(bonus, t.ac)
                if hit:
                    t.hp -= attacker.dmg_fn()
        else:
            t = random.choice(targets)
            hit, _ = rules.to_hit_fn(total_bonus, t.ac)
            if hit:
                t.hp -= attacker.dmg_fn()

    while True:
        rounds += 1
        living_mon = [m for m in monsters if m.is_alive()]
        living_pc  = [p for p in party   if p.is_alive()]
        if not living_mon or not living_pc: break

        for pc in living_pc:
            t = [m for m in monsters if m.is_alive()]
            if t: resolve_attacks(pc, t, split_pcs)

        living_pc = [p for p in party if p.is_alive()]
        for mon in living_mon:
            if not mon.is_alive(): continue
            t = [p for p in party if p.is_alive()]
            if t: resolve_attacks(mon, t, split_monsters)

        if rounds >= 200: break

    lp = [p for p in party if p.is_alive()]
    lm = [m for m in monsters if m.is_alive()]
    won   = len(lp) > 0 and len(lm) == 0
    deaths = initial - len(lp)
    return won, rounds, deaths


def simulate_split(label, party_fn, mon_fn,
                   split_pcs=True, split_monsters=True, runs=RUNS):
    wins, rds, deaths = [], [], []
    for _ in range(runs):
        p, m = party_fn(), mon_fn()
        for c in p+m: c.reset()
        w, r, d = run_combat_split(p, m, split_pcs, split_monsters)
        wins.append(w); rds.append(r); deaths.append(d)
    wr = sum(wins)/runs*100
    print(f"  {label:<60}  win={wr:5.1f}%  "
          f"rds={statistics.mean(rds):4.1f}  deaths={statistics.mean(deaths):.2f}")
    return wr