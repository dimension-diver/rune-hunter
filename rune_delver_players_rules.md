# Rune Delver — Player's Rules

---

## How Rolls Work

Three resolution systems, each for its own domain:

- **Combat** — d20 + FC + STR/AGI vs 10 + opponent FC. Players roll to attack and to defend. Monsters are static numbers.
- **Saving throws** — d20 + relevant modifier vs 16 − character level.
- **Tasks** — d6, default 2-in-6, modified by ability scores and background.

All rolls are **player-facing**. Players roll for themselves, their hirelings, retainers, familiars, and summoned creatures. Monsters never roll.

---

## Character Creation

### 1. Roll ability scores
Roll 3d6 in order: **STR, AGI, RES, WIS, CHA, LUC**.

You may swap any two scores once after rolling. If the sum of all modifiers is −3 or worse, reroll the entire array.

| Score | Modifier |
|-------|----------|
| 3–6   | −1       |
| 7–14  | 0        |
| 15–18 | +1       |

### 2. Choose a background
Roll 2d6 or choose from the background table. Your background gives you starting talents and starting equipment, and establishes who you were before you started adventuring. ¹

### 3. Choose a type
**Hunter** or **Caster**. Some backgrounds specify a type; others leave the choice open. Your type determines your combat chassis.

### 4. Starting HP
**8 + RES modifier** (Hunter) or **6 + RES modifier** (Caster). Minimum 1.

---

## Ability Scores

| Stat | Used for |
|------|----------|
| **Strength (STR)** | Melee attack and defense, damage bonus, feats of physical power. Raw score determines the ceiling of what you can attempt. ² |
| **Agility (AGI)** | Ranged attack and defense, initiative, stealth. AGI modifier negated by medium and heavy armor. |
| **Resilience (RES)** | Starting HP modifier. Governs resistance to poison and disease — reaching 0 RES is fatal. |
| **Wisdom (WIS)** | Spell research, languages, knowledge and lore tasks. For Casters, raw WIS score caps spells known. |
| **Charm (CHA)** | Reaction rolls, hireling loyalty, social tasks. Saves vs beguilement, fear, and illusions. |
| **Luck (LUC)** | Fortune. Modifies die of fate rolls. Can be burned to invoke favorable outcomes. Fluctuates over the campaign. |

---

## Types

### Hunter
Handles problems without magic. FC and HP scale with tier. Hunters have 0 MP. ³

| Tier | FC | HP |
|------|----|----|
| 1 | +1 | 8 |
| 2 | +2 | 12 |
| 3 | +3 | 16 |
| 4 | +4 | 20 |
| 5 | +5 | 24 |
| 6 | +6 | 28 |

### Caster
Handles problems through magic. FC is 0 unless Hunter levels are also taken.

Casters cast spells by spending **MP (magic points)**. MP recovers fully after rest. Casting a spell costs MP equal to its tier — a Tier 1 spell costs 1 MP, a Tier 3 spell costs 3 MP. Casters can only cast spells up to their current tier. Damaging spells deal d6 per spell tier and bypass armor entirely. ⁴

**Casting time:** a spell takes a number of rounds equal to its tier to cast. Declare on round 1 and pay the MP cost; the spell resolves after the required number of rounds. Any damage taken during casting loses the spell and the MP. A Tier 1 spell resolves the same round it is declared. A Tier 5 spell takes five rounds of concentration. ⁵

**MP = (tier × 2) + WIS or CHA modifier** (choose at character creation — Shamans use CHA, scholarly Mages use WIS). Incremental rewards may add +1 MP.

| Tier | HP | Base MP | Highest spell | Casting time |
|------|----|---------|--------------|--------------|
| 1 | 6 | 2 | Tier 1 | 1 round |
| 2 | 9 | 4 | Tier 2 | 1–2 rounds |
| 3 | 12 | 6 | Tier 3 | 1–3 rounds |
| 4 | 15 | 8 | Tier 4 | 1–4 rounds |
| 5 | 18 | 10 | Tier 5 | 1–5 rounds |
| 6 | 21 | 12 | Tier 6 | 1–6 rounds |

### Multiclassing
Take levels in both types freely. Hunter levels determine FC. Caster levels determine MP and spell access. HP uses whichever type's progression applies to that level.

---

## Combat

### Round sequence
1. **Declare spells** — Casters announce their spell and pay its MP cost. Tier 1 spells resolve this round. Higher tier spells take additional rounds — declare on round 1, resolve after the required number of rounds. Any damage taken during casting loses the spell and the MP. Artificers are exempt — gadgets activate as a normal action with no prior declaration.
2. **Roll initiative** — each side rolls d6. Winning side acts first. Ties resolve simultaneously.
3. **Missiles** — ranged attacks in initiative order.
4. **Movement** — characters move in initiative order.
5. **Melee** — melee attacks in initiative order.
6. **Spells** — declared spells resolve in initiative order.

### Actions
Each round a character may:
- **Move 1 zone and take an action** — attack, use an item, cast a spell, attempt a task, aid another
- **Move 2 zones and take no action**

### Attacking
**Melee:** d20 + FC + STR vs 10 + opponent FC

**Ranged:** d20 + FC + AGI vs 10 + opponent FC

Players may use STR or AGI for melee defense — bracing uses STR, ducking uses AGI.

**Static defense:** instead of rolling, treat defense as a fixed 10 + FC + AGI bonus (or 10 + FC + 1 with a shield and no AGI bonus). Cannot be used to flee melee.

| Result | Effect |
|--------|--------|
| Hit | Roll weapon damage — armor save applies |
| Miss | No effect |
| Natural 20 on attack | Critical hit — always penetrates armor ⁶ |
| Natural 20 on defense | Free counterattack this round |
| Natural 1 on defense | Monster crits you |

### Damage and armor save
Roll weapon die + damage modifier and compare to target's armor rating:
- Total **≤** armor rating → **0 damage**
- Total **>** armor rating → **full damage**

### Critical hits
Natural 20 on attack — bypasses armor:
1. Deal max die + damage modifier
2. Roll weapon die again, add modifier
3. Both results bypass armor

*Example: sword d6, STR +1. Crit deals 6+1=7, then d6+1 again. Total 8–13.*

### Weapons
| Option | Effect |
|--------|--------|
| One-handed | Standard damage die |
| Two-handed | Step up damage die (d4→d6, d6→d8) |
| Dual wield | +1 ATK; use damage die of either weapon |
| Shield | +1 DEF when no AGI bonus applies |

### Ranged combat
Defenders cannot counterattack ranged attackers. Ranged weapons cannot be used in melee and cannot safely target enemies engaged in melee.

**Ammunition** is tracked with 3 bubbles. After each fight involving ranged attacks, roll d6: on 4–6 mark one bubble. When all 3 bubbles are marked, one shot remains. Resupply clears all bubbles.

Rare or specialist ammo marks a bubble on 3+.

### Mounted combat
A mount grants +1 ATK and DEF in melee. A mounted charge — moving at least 1 zone before attacking — grants +2 ATK on the attack.

### Stealth attacks
Attacking from stealth or an undetected position: +2 ATK and maximum weapon damage. Maximum damage always exceeds mundane armor. Stealth is lost after the attack.

### Defeat
At 0 HP a character is **defeated** — not automatically dead. The referee determines consequences: capture, unconsciousness, grievous injury.

### Fleeing melee
A character who flees a melee zone gives opponents a free attack before leaving.

---

## Armor

| Armor | Rating | Slots | Treasure | Notes |
|-------|--------|-------|----------|-------|
| Light (leather, hide) | 1 | 1 body | 1 | — |
| Medium (mail, brigandine) | 2 | 1 body | 2 | No stealth |
| Heavy (plate, relic suit) | 3 | 2 body | 3 | No stealth, no swimming |
| Magic armor | 4–6 | varies | 5+ | — |
| Shield | — | 1 hand | 1 | +1 DEF if no AGI bonus |

AGI modifier to defense is negated by medium and heavy armor. The shield bonus applies instead when carried with medium or heavy armor.

---

## Saving Throws

**Target: 16 − character tier.** Roll d20 + relevant modifier. Meet or beat to succeed.

| Threat | Stat |
|--------|------|
| Poison, disease, physical harm | RES |
| Breath weapons, area effects | AGI |
| Beguilement, fear, illusions | CHA |
| Magical compulsion, death effects | RES or CHA (referee's call) |
| Fortune-dependent outcomes | LUC (referee's call) |

Background, species, or talents may add +1 or +2 to specific saves.

---

## Task Resolution

Default **2-in-6**. Roll d6 equal to or under the target to succeed.

| Modifier | Chance |
|----------|--------|
| −1 | 1-in-6 |
| 0 | 2-in-6 |
| +1 | 3-in-6 |

Relevant background or species adds +1. Skills improved through downtime or accomplishment can stack to +2 or higher. ⁶

---

## Inventory

Characters have **10 inventory slots**: 2 hand slots and 2 body slots (included in the 10).

- Conditions occupy slots until treated
- Most small items take less than 1 slot
- Heavy armor impedes stealth and swimming

---

## Conditions

Conditions occupy **inventory slots** until removed.

| Type | Removed by | Cost |
|------|-----------|------|
| Injury | Healer, surgeon, or rest | 1 treasure/slot |
| Disease | Herbalist or antidote | 1 treasure/slot |
| Curse / hex | Temple or ritual | 1–3 treasure/slot |
| Jinx | Spirit appeasement or quest | Narrative — no simple cure |
| Magical binding | Specific ritual or component | Narrative |

| Severity | Slots | Examples |
|----------|-------|---------|
| Minor | 1 | Sprained ankle, minor hex, mild fever |
| Moderate | 2 | Broken bone, disease, moderate curse |
| Severe | 3 | Crippling wound, wasting sickness |
| Catastrophic | 4+ | Lost limb, death curse, soul binding |

Conditions may impose situational penalties — a broken arm imposes −1 on attack rolls, a hex −1 on saves.

**Ability damage:** some conditions damage ability scores directly. Injury may deal 1d6 STR damage; poison deals 1d6 RES damage on a failed save and repeats daily until treated; Jinx deals 1d6 LUC damage and requires narrative resolution. Reaching 0 in any stat has severe consequences — 0 RES is death.

---

## Luck

**Luck (LUC)** is a dynamic stat. It modifies die of fate rolls the referee makes — when things could go either way, your LUC modifier tips the balance.

**Burning Luck:** spend 1 LUC permanently to invoke a favorable die of fate outcome without rolling. *The door is unlocked. The guard is asleep.* Irreversible in the moment.

**Recovery:** LUC recovers 1d3 per week of downtime, up to your starting score. Bold deeds and carousing can restore — or reduce — it further. LUC can exceed its starting value through exceptional fortune; there is no hard ceiling.

A character at 0 LUC is cosmically cursed until it recovers.

---

## Advancement

RD uses no experience points. Characters advance through **expeditions** and **accomplishments**.

**Expeditions:** completing a significant objective — recovering a relic, slaying a threat, a successful heist, a rescue — earns an incremental reward. The referee assigns the most appropriate reward from this list:

| Reward | Notes |
|--------|-------|
| +1 HP | Permanent |
| +1 FC | Hunters only |
| +1 MP | Casters only |
| +1 to a d6 task | Specific task or category |
| +1 to a stat | Referee determines or player makes a case |
| +1 to a save | Permanent, tied to what was survived |
| New talent | Requires fictional justification |

**Tiers:** normal advancement halts at the ceiling of each tier. To cross into the next tier, complete a tier-unlocking Accomplishment. ⁷

| Tier | Title | Scale |
|------|-------|-------|
| 1 | Adventurer | Unknown. Survives on luck and grit. |
| 2 | Hero | Local reputation. Deeds matter regionally. |
| 3 | Lord | Regional power. Territory, followers, resources. |
| 4 | Legend | Continental scale. History is being made. |
| 5 | Mythic | Near-godlike. Normally NPCs only. |
| 6 | — | NPC tier. Referee use only. |

**Accomplishments:** a deed of sufficient magnitude — overthrowing a warlord, claiming a seat of power, returning from somewhere no one has returned from. The reward is always a choice: unlock the next tier, or take a concrete bonus (+1d6 HP, +1 to a stat, +1 FC, +1 spell slot, +1 to all saves of a type, or a significant talent). Advancing a tier is optional. ⁸

---

## Spells

*[Spell list by tier — placeholder. See spell reference sheet.]*

Casters access spells up to their current tier. Spells known is capped by raw WIS score. Spells are memorized from a spellbook; casting costs MP equal to the spell's tier. MP recovers fully after rest.

Shamans learn spells by communing with spirits rather than from books. Their spell list emphasizes nature, elemental effects, and communal magic. They may carry spirit vessels — objects with a spirit bound within — as backup MP sources in spirit-poor environments.

Artificers store spells in gadgets — one gadget per known spell, with charges equal to the Caster's MP divided by the spell's tier cost. Anyone can activate a gadget; no declaration required, no MP spent by the activator.

---

*Talents and equipment are on separate reference sheets.*
