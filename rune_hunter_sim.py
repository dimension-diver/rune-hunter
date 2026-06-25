#!/usr/bin/env python3
"""
RUNE HUNTER COMBAT SIMULATOR
Simulates fights between a party of Hunters/Casters and a single monster.
Useful for validating encounter balance before running at the table.

Usage:
    python3 rune_hunter_sim.py

Edit the PARTY and MONSTER sections at the bottom to set up your encounter.
Set RUNS to a high number (1000+) for statistical results.
Set RUNS to 1 and VERBOSE to True for a play-by-play of a single fight.
"""

import random
import argparse

# ============================================================
# CORE MATH
# ============================================================

def modifier(score):
    if score <= 6: return -1
    if score <= 14: return 0
    return 1

def p_hit(atk_fc, def_fc, atk_mod=0):
    return max(0.05, min(0.95, (10 + atk_fc + atk_mod - def_fc) / 20))

def roll_dmg(die_sides, ar, bonus=0):
    """Roll damage die, return 0 if blocked by AR."""
    d = random.randint(1, die_sides)
    total = d + bonus
    return total if total > ar else 0

def max_dmg(die_sides, ar, bonus=0):
    """Maximum damage result, bypasses AR check (for stealth attacks and crits)."""
    return die_sides + bonus


# ============================================================
# CHARACTER / MONSTER BUILDERS
# ============================================================

def make_hunter(name, tier, str_mod=0, agi_mod=0, res_mod=0,
                weapon_die=6, armor_ar=2, talents=None):
    """
    Build a Hunter PC.
    tier: 1-6
    str_mod, agi_mod, res_mod: -1, 0, or +1
    weapon_die: 4, 6, 8, etc.
    armor_ar: 0-3
    talents: list of strings e.g. ['thief', 'blade_dancer']
    """
    hp = 8 + 4 * (tier - 1) + res_mod
    return {
        'name': name,
        'type': 'Hunter',
        'tier': tier,
        'hp': max(1, hp),
        'max_hp': max(1, hp),
        'fc': tier,
        'mp': 0,
        'str_mod': str_mod,
        'agi_mod': agi_mod,
        'weapon_die': weapon_die,
        'armor_ar': armor_ar,
        'talents': talents or [],
        'stealth_available': ('thief' in (talents or []) or
                              'assassin' in (talents or [])),
        'stealth_upgraded': False,  # set True for +2d6
        'defeated': False,
    }

def make_caster(name, tier, wis_mod=0, cha_mod=0, res_mod=0,
                mp_stat='wis', weapon_die=6, armor_ar=0, talents=None):
    """
    Build a Caster PC.
    mp_stat: 'wis' or 'cha' (which stat governs MP)
    """
    hp = 6 + 3 * (tier - 1) + res_mod
    mp_mod = wis_mod if mp_stat == 'wis' else cha_mod
    mp = max(1, tier * 2 + mp_mod)
    return {
        'name': name,
        'type': 'Caster',
        'tier': tier,
        'hp': max(1, hp),
        'max_hp': max(1, hp),
        'fc': 0,
        'mp': mp,
        'max_mp': mp,
        'wis_mod': wis_mod,
        'cha_mod': cha_mod,
        'str_mod': 0,
        'agi_mod': agi_mod if 'agi_mod' in dir() else 0,
        'weapon_die': weapon_die,
        'armor_ar': armor_ar,
        'max_mp_per_spell': tier,
        'talents': talents or [],
        'defeated': False,
    }

def make_monster(name, tier, size='Medium', extra_pts=None):
    """
    Build a monster from the size x tier matrix.
    size: 'Small', 'Medium', 'Large', 'Huge', 'Colossal'
    extra_pts: list of upgrades from the point menu e.g. ['veteran', '+1_ar']
    """
    size_data = {
        'Small':    {'hp_die': 4,  'hp_inc': 2, 'dmg_die': 4,  'ar': 0,
                     'atk': [1,1,1,2,2,2]},
        'Medium':   {'hp_die': 6,  'hp_inc': 3, 'dmg_die': 6,  'ar': 0,
                     'atk': [1,1,1,2,2,2]},
        'Large':    {'hp_die': 8,  'hp_inc': 4, 'dmg_die': 8,  'ar': 1,
                     'atk': [1,1,2,2,3,3]},
        'Huge':     {'hp_die': 10, 'hp_inc': 5, 'dmg_die': 10, 'ar': 1,
                     'atk': [1,2,2,3,3,3]},
        'Colossal': {'hp_die': 12, 'hp_inc': 6, 'dmg_die': 12, 'ar': 2,
                     'atk': [2,2,2,3,3,3]},
    }
    sd = size_data[size]
    hp  = sd['hp_die'] + sd['hp_inc'] * (tier - 1)
    fc  = tier
    ar  = sd['ar']
    atk = sd['atk'][tier - 1]
    dmg = sd['dmg_die']
    dmg_bonus = 0
    specials = []

    # Apply point budget upgrades
    pts_budget = tier
    pts_spent = 0
    for upgrade in (extra_pts or []):
        u = upgrade.lower()
        if u == 'veteran' and pts_spent + 1 <= pts_budget:
            fc += 1
            pts_spent += 1
        elif u == '+1_ar' and pts_spent + 1 <= pts_budget:
            ar = min(ar + 1, 3)
            pts_spent += 1
        elif u == 'step_dmg' and pts_spent + 1 <= pts_budget:
            dmg = min(dmg + 2, 12)  # step up die
            pts_spent += 1
        elif u == '+1_dmg' and pts_spent + 1 <= pts_budget:
            dmg_bonus += 1
            pts_spent += 1
        elif u == '+1_atk' and pts_spent + 1 <= pts_budget:
            atk += 1
            pts_spent += 1
        elif u == 'regen' and pts_spent + 2 <= pts_budget:
            specials.append('regen')
            pts_spent += 2
        elif u == 'grab' and pts_spent + 2 <= pts_budget:
            specials.append('grab')
            pts_spent += 2
        elif u == 'frightful' and pts_spent + 2 <= pts_budget:
            specials.append('frightful')
            pts_spent += 2
        elif u == 'spell' and pts_spent + 2 <= pts_budget:
            specials.append('spell')
            pts_spent += 2
        elif u == 'breath' and pts_spent + 3 <= pts_budget:
            specials.append('breath')
            pts_spent += 3
        elif u == 'legendary' and pts_spent + 3 <= pts_budget:
            specials.append('legendary')
            pts_spent += 3

    return {
        'name': name,
        'tier': tier,
        'size': size,
        'hp': hp,
        'max_hp': hp,
        'fc': fc,
        'ar': ar,
        'atk_count': atk,
        'dmg_die': dmg,
        'dmg_bonus': dmg_bonus,
        'specials': specials,
        'morale': 8,
        'grabbed': None,
        'legendary_uses': 1 if 'legendary' in specials else 0,
        'fled': False,
        'defeated': False,
    }


# ============================================================
# COMBAT ENGINE
# ============================================================

def run_fight(party, monster, seed=None, verbose=False):
    """
    Run one fight. Returns a result dict.
    party: list of character dicts from make_hunter / make_caster
    monster: dict from make_monster
    """
    if seed is not None:
        random.seed(seed)

    # Reset state
    for pc in party:
        pc['hp'] = pc['max_hp']
        pc['defeated'] = False
        pc['stealth_available'] = ('thief' in pc.get('talents', []) or
                                   'assassin' in pc.get('talents', []))
        if pc['type'] == 'Caster':
            pc['mp'] = pc['max_mp']

    monster['hp'] = monster['max_hp']
    monster['grabbed'] = None
    monster['fled'] = False
    monster['defeated'] = False
    monster['legendary_uses'] = 1 if 'legendary' in monster['specials'] else 0

    rounds = 0
    casualties = []
    events = []

    def log(msg):
        if verbose:
            print(msg)
        events.append(msg)

    for rnd in range(1, 20):
        alive = [p for p in party if not p['defeated']]
        if not alive or monster['defeated'] or monster['fled']:
            break

        rounds += 1
        damage_this_round = set()
        log(f"\n--- Round {rnd} ---")

        # Caster spell declaration
        casters = [p for p in alive if p['type'] == 'Caster' and p['mp'] >= 1]
        casting_pc = casters[0] if casters else None
        spell_mp = min(casting_pc['mp'], casting_pc['max_mp_per_spell']) if casting_pc else 0

        if casting_pc and spell_mp >= 1:
            log(f"  [DECLARE] {casting_pc['name']} declares {spell_mp} MP spell.")

        # Initiative
        p_init = random.randint(1, 6)
        m_init = random.randint(1, 6)
        party_first = p_init >= m_init
        log(f"  [INIT] Party {p_init} vs Monster {m_init}. "
            f"{'Party' if party_first else 'Monster'} first.")

        # ---- PARTY ATTACKS ----
        def party_attacks():
            for pc in alive:
                if monster['defeated']: break
                if pc == casting_pc: continue

                atk_mod = pc['str_mod']
                fc = pc['fc']

                # Stealth attack on round 1 if party goes first
                if pc.get('stealth_available') and rnd == 1 and party_first:
                    pc['stealth_available'] = False
                    bonus_dice = 2 if pc.get('stealth_upgraded') else 1
                    max_d = pc['weapon_die']
                    bonus = sum(random.randint(1,6) for _ in range(bonus_dice))
                    total = max_d + bonus + atk_mod
                    monster['hp'] = max(0, monster['hp'] - total)
                    log(f"  [STEALTH] {pc['name']}: max d{pc['weapon_die']}({max_d}) "
                        f"+ {bonus_dice}d6({bonus}) + STR({atk_mod:+}) = {total}. "
                        f"Monster HP: {monster['hp']}/{monster['max_hp']}")
                    if monster['hp'] <= 0:
                        monster['defeated'] = True
                    continue

                roll = random.randint(1, 20)
                total = roll + fc + atk_mod
                target = 10 + monster['fc']

                if roll == 20:
                    # Crit
                    dmg = pc['weapon_die'] + atk_mod
                    dmg2 = random.randint(1, pc['weapon_die']) + atk_mod
                    actual = max(0, dmg) + max(0, dmg2)
                    monster['hp'] = max(0, monster['hp'] - actual)
                    log(f"  [CRIT] {pc['name']}: {actual} dmg. "
                        f"Monster HP: {monster['hp']}/{monster['max_hp']}")
                    if monster['hp'] <= 0:
                        monster['defeated'] = True
                elif total >= target:
                    d = random.randint(1, pc['weapon_die'])
                    bonus = atk_mod
                    if d + bonus > monster['ar']:
                        actual = d + bonus
                        monster['hp'] = max(0, monster['hp'] - actual)
                        log(f"  [HIT] {pc['name']}: d{pc['weapon_die']}({d})"
                            f"{bonus:+}={d+bonus} vs AR{monster['ar']}. "
                            f"{actual} dmg. Monster HP: {monster['hp']}/{monster['max_hp']}")
                        if monster['hp'] <= 0:
                            monster['defeated'] = True
                    else:
                        log(f"  [BLOCK] {pc['name']}: {d+bonus} vs AR{monster['ar']}.")
                else:
                    log(f"  [MISS] {pc['name']}: {total} vs {target}.")

        # ---- MONSTER ATTACKS ----
        def monster_attacks():
            if monster['defeated']: return
            targets = [p for p in alive if not p['defeated']]
            if not targets: return

            # Handle grabbed target first
            if monster['grabbed'] and not monster['grabbed']['defeated']:
                tgt = monster['grabbed']
                d = random.randint(1, monster['dmg_die'])
                tgt['hp'] = max(0, tgt['hp'] - d)
                damage_this_round.add(tgt['name'])
                log(f"  [CRUSH] Monster crushes {tgt['name']}: auto {d} dmg. "
                    f"{tgt['name']} HP: {tgt['hp']}/{tgt['max_hp']}")
                if tgt['hp'] <= 0:
                    tgt['defeated'] = True
                    casualties.append(tgt['name'])
                    log(f"  {tgt['name']} DEFEATED.")
                    monster['grabbed'] = None
                    return
                esc = random.randint(1, 6)
                str_mod = tgt.get('str_mod', 0)
                esc_target = 3 - str_mod  # 3-in-6 base, STR helps
                if esc <= esc_target:
                    monster['grabbed'] = None
                    log(f"  {tgt['name']} escapes the grab!")
                return

            for _ in range(monster['atk_count']):
                if monster['defeated']: break
                targets = [p for p in alive if not p['defeated']]
                if not targets: break
                tgt = random.choice(targets)

                # Player defends
                def_mod = tgt.get('agi_mod', 0)
                dr = random.randint(1, 20)
                dt = dr + tgt['fc'] + def_mod
                dtgt = 10 + monster['fc']

                if dr == 20:
                    # Nat 20 defense: free counterattack
                    log(f"  [NAT 20 DEF] {tgt['name']} deflects + counterattack!")
                    cr = random.randint(1, 20)
                    ct = cr + tgt['fc'] + tgt.get('str_mod', 0)
                    if ct >= 10 + monster['fc']:
                        cd = random.randint(1, tgt['weapon_die'])
                        cb = tgt.get('str_mod', 0)
                        if cd + cb > monster['ar']:
                            monster['hp'] = max(0, monster['hp'] - (cd+cb))
                            log(f"    Counter HIT: {cd+cb} dmg. "
                                f"Monster HP: {monster['hp']}/{monster['max_hp']}")
                            if monster['hp'] <= 0:
                                monster['defeated'] = True
                elif dr == 1:
                    # Nat 1 defense: monster crits
                    mx = monster['dmg_die'] + monster['dmg_bonus']
                    r2 = random.randint(1, monster['dmg_die']) + monster['dmg_bonus']
                    total = mx + r2
                    tgt['hp'] = max(0, tgt['hp'] - total)
                    damage_this_round.add(tgt['name'])
                    log(f"  [MONSTER CRIT] {tgt['name']}: {total} dmg. "
                        f"HP: {tgt['hp']}/{tgt['max_hp']}")
                    if tgt['hp'] <= 0:
                        tgt['defeated'] = True
                        casualties.append(tgt['name'])
                        log(f"  {tgt['name']} DEFEATED.")
                elif dt < dtgt:
                    # Hit lands
                    can_grab = ('grab' in monster['specials'] and
                                monster['grabbed'] is None and
                                random.random() < 0.35)
                    if can_grab:
                        monster['grabbed'] = tgt
                        damage_this_round.add(tgt['name'])
                        log(f"  [GRAB] Monster grabs {tgt['name']}!")
                    else:
                        d = random.randint(1, monster['dmg_die'])
                        bonus = monster['dmg_bonus']
                        if d + bonus > tgt['armor_ar']:
                            actual = d + bonus
                            tgt['hp'] = max(0, tgt['hp'] - actual)
                            damage_this_round.add(tgt['name'])
                            log(f"  [HIT] Monster hits {tgt['name']}: "
                                f"{actual} dmg. HP: {tgt['hp']}/{tgt['max_hp']}")
                            if tgt['hp'] <= 0:
                                tgt['defeated'] = True
                                casualties.append(tgt['name'])
                                log(f"  {tgt['name']} DEFEATED.")
                        else:
                            log(f"  [BLOCK] Monster hit blocked by AR{tgt['armor_ar']}.")
                else:
                    log(f"  [DEFLECT] {tgt['name']} deflects.")

        # ---- RESOLVE SPELL ----
        def resolve_spell():
            if not casting_pc or casting_pc['defeated']: return
            if casting_pc['name'] in damage_this_round:
                casting_pc['mp'] -= spell_mp
                log(f"  [LOST] {casting_pc['name']} took damage, spell lost. "
                    f"MP: {casting_pc['mp']}/{casting_pc['max_mp']}")
                return
            if monster['defeated']: return
            casting_pc['mp'] -= spell_mp
            dmg = sum(random.randint(1,6) for _ in range(spell_mp))
            monster['hp'] = max(0, monster['hp'] - dmg)
            log(f"  [SPELL] {casting_pc['name']}: {spell_mp}d6 = {dmg} dmg bypasses AR. "
                f"Monster HP: {monster['hp']}/{monster['max_hp']} "
                f"MP: {casting_pc['mp']}/{casting_pc['max_mp']}")
            if monster['hp'] <= 0:
                monster['defeated'] = True

        # Execute round
        if party_first:
            party_attacks()
            if not monster['defeated']:
                monster_attacks()
            resolve_spell()
        else:
            monster_attacks()
            party_attacks()
            resolve_spell()

        # Status
        if verbose:
            status = f"  [STATUS] Monster:{monster['hp']}/{monster['max_hp']}"
            for pc in party:
                flag = "(DEAD)" if pc['defeated'] else \
                       "(GRABBED)" if monster['grabbed'] and \
                       monster['grabbed']['name'] == pc['name'] else ""
                status += f"  {pc['name']}:{pc['hp']}/{pc['max_hp']}{flag}"
            log(status)

        # Morale check
        if 0 < monster['hp'] <= monster['max_hp'] // 2:
            m1, m2 = random.randint(1,6), random.randint(1,6)
            if m1 + m2 < monster['morale']:
                log(f"  [MORALE] Monster fails ({m1+m2} vs {monster['morale']}+). FLEES!")
                monster['fled'] = True
                monster['hp'] = 0
                break

    # Outcome
    survivors = [p for p in party if not p['defeated']]
    if monster['fled']:
        outcome = 'monster_fled'
    elif monster['defeated']:
        outcome = 'monster_defeated'
    else:
        outcome = 'party_defeated'

    return {
        'outcome': outcome,
        'rounds': rounds,
        'casualties': casualties,
        'survivors': [p['name'] for p in survivors],
        'survivor_hp': [(p['name'], p['hp'], p['max_hp']) for p in survivors],
        'monster_final_hp': monster['hp'],
        'events': events,
    }


# ============================================================
# BATCH SIMULATION
# ============================================================

def simulate(party_factory, monster_factory, runs=1000, verbose_seed=None):
    """
    Run many fights and report statistics.
    party_factory: callable returning a fresh party list
    monster_factory: callable returning a fresh monster dict
    runs: number of iterations
    verbose_seed: if set, also run one verbose fight with this seed
    """
    results = []
    for i in range(runs):
        p = party_factory()
        m = monster_factory()
        r = run_fight(p, m, seed=i)
        results.append(r)

    total = len(results)
    defeated  = sum(1 for r in results if r['outcome'] == 'monster_defeated')
    fled      = sum(1 for r in results if r['outcome'] == 'monster_fled')
    party_def = sum(1 for r in results if r['outcome'] == 'party_defeated')
    avg_rounds = sum(r['rounds'] for r in results) / total
    casualty_fights = sum(1 for r in results if r['casualties'])

    print(f"\nRESULTS ({total} fights)")
    print(f"  Monster defeated:  {defeated:4d} ({defeated/total:.0%})")
    print(f"  Monster fled:      {fled:4d} ({fled/total:.0%})")
    print(f"  Party defeated:    {party_def:4d} ({party_def/total:.0%})")
    print(f"  Avg rounds:        {avg_rounds:.1f}")
    print(f"  Fights with casualties: {casualty_fights} ({casualty_fights/total:.0%})")

    if verbose_seed is not None:
        print(f"\n--- VERBOSE FIGHT (seed {verbose_seed}) ---")
        p = party_factory()
        m = monster_factory()
        r = run_fight(p, m, seed=verbose_seed, verbose=True)
        print(f"\nOutcome: {r['outcome']} in {r['rounds']} rounds")
        if r['casualties']:
            print(f"Casualties: {', '.join(r['casualties'])}")
        print(f"Survivors: {', '.join(f'{n} ({h}/{mh} HP)' for n,h,mh in r['survivor_hp'])}")


# ============================================================
# EXAMPLE SETUP — edit this section to configure your encounter
# ============================================================

if __name__ == '__main__':

    # ---- PARTY ----
    def make_party():
        return [
            make_hunter('Brak',   tier=1, str_mod=0,  agi_mod=0,  res_mod=0,
                        weapon_die=6, armor_ar=2),
            make_caster('Syleth', tier=1, wis_mod=0,  res_mod=0,
                        weapon_die=6, armor_ar=0),
            make_hunter('Rynn',   tier=1, str_mod=1,  agi_mod=0,  res_mod=0,
                        weapon_die=6, armor_ar=1),
            make_hunter('Vesper', tier=1, str_mod=-1, agi_mod=-1, res_mod=0,
                        weapon_die=4, armor_ar=1,
                        talents=['thief']),
        ]

    # ---- MONSTER ----
    def make_enemy():
        return make_monster(
            name='Cave Bear',
            tier=2,
            size='Large',
            extra_pts=['grab'],   # spend 1 of 2 pts on grab
        )

    # ---- RUN ----
    # Set RUNS=1 and verbose_seed=440 for a play-by-play
    # Set RUNS=1000 and verbose_seed=None for statistics
    RUNS = 1000
    VERBOSE_SEED = None   # set to an integer for a play-by-play after stats

    print("RUNE HUNTER COMBAT SIMULATOR")
    print(f"Party vs {make_enemy()['name']} (Tier {make_enemy()['tier']} {make_enemy()['size']})")

    simulate(make_party, make_enemy, runs=RUNS, verbose_seed=VERBOSE_SEED)
