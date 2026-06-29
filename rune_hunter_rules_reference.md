# Rune Hunter. Rules Reference

---

# PART 1: PLAYER RULES

## How Rolls Work

- **Combat**: d20 + ATK vs opponent DEF (attack) or d20 + DEF vs 10 + monster ATK (defense). Players always roll.
- **Saving throws**: d20 + relevant modifier vs 15 − floor(level ÷ 2).
- **Tasks**: d6, default 2-in-6, modified by ability scores and background.
- **Die of Fate**: d6 oracle roll, modified by LUC. See Luck.

All rolls are **player-facing**. Players roll for themselves, their hirelings, retainers, familiars, and summoned creatures. Monsters never roll.

---

## Character Creation

### 1. Roll Ability Scores
Roll 3d6 in order: **STR, AGI, RES, WIS, CHA, LUC**.

Swap any two once after rolling. If the sum of all modifiers is −3 or worse, reroll the entire array.

| Score | Modifier |
|-------|----------|
| 3–6   | −1       |
| 7–14  | 0        |
| 15–18 | +1       |

### 2. Choose a Background
Roll 2d6 or choose. Backgrounds give starting talents and equipment.

### 3. Choose a Class
**Hunter**, **Delver**, or **Caster**.

### 4. Starting HP
Level 1 HP = maximum HD result + RES modifier (minimum 1).

| Class | HD |
|-------|----|
| Hunter, Noble, Striker | d8 |
| Delver, Ranger, Seeker, Dabbler | d6 |
| Caster, Esper | d4 |

---

## Ability Scores

| Stat | Used for |
|------|----------|
| **STR** | Melee attack, damage bonus, feats of physical power |
| **AGI** | Ranged attack, initiative, stealth. Negated by heavy armor. |
| **RES** | HP modifier (per die). Poison and disease resistance. 0 RES = death. |
| **WIS** | Spell research, languages, lore. Caps spells known (Mage tradition). |
| **CHA** | Reaction rolls, hireling loyalty, social tasks. Saves vs beguilement. Governs spell power (Shaman tradition). |
| **LUC** | Die of fate modifier. Burnable for narrative outcomes. |

---

## Classes

### Hunter
Cannot use scrolls, cast spells, or activate magic items other than weapons and armor.

**Features:** Heavy Armor, Hunter ATK, Split Attack.

| Level | ATK | DEF |
|-------|-----|-----|
| 1  | +1 | 10 |
| 2  | +2 | 11 |
| 3  | +2 | 11 |
| 4  | +3 | 12 |
| 5  | +4 | 12 |
| 6  | +4 | 13 |
| 7  | +5 | 13 |
| 8  | +6 | 14 |
| 9  | +6 | 14 |
| 10 | +7 | 15 |

### Delver
**Features:** Light Armor, Delver ATK, Spell Scrolls, Delver Skills, Sneak Attack.

| Level | ATK | DEF | Skill | Sneak |
|-------|-----|-----|-------|-------|
| 1  | +0 | 10 | 1-2 | ×2 |
| 2  | +1 | 11 | 1-2 | ×2 |
| 3  | +1 | 11 | 1-3 | ×2 |
| 4  | +2 | 12 | 1-3 | ×3 |
| 5  | +2 | 12 | 1-3 | ×3 |
| 6  | +3 | 13 | 1-3 | ×3 |
| 7  | +3 | 13 | 1-4 | ×4 |
| 8  | +4 | 14 | 1-4 | ×4 |
| 9  | +4 | 14 | 1-4 | ×4 |
| 10 | +5 | 15 | 1-5 | ×5 |

**Delver Skills:** stealth, lockpicking, trapfinding, climbing, and similar specialist tasks. Roll d6 equal to or under the skill rating. Other classes attempt these on 1-in-6.

**Sneak Attack:** +4 ATK and damage multiplier when attacking with positional advantage (surprise, concealment, or flanking an engaged target). Referee judges the fiction.

**Spell Scrolls:** can read and activate scrolls. Attempts to use wands, rods, and other magic items on 1-3 on d6 (add WIS modifier). Cannot cast from memory.

### Caster
Cannot wear armor without penalty.

**Features:** No Armor, Caster ATK, Spellcasting, Spell Scrolls, Magic Fluency.

**Armor penalty:** armor AR adds as a bonus to enemy saves against the Caster's spells.

**Spellcasting:** prepare spells from spellbook after rest. Casting expends the slot. Damaging spells deal d6 per spell tier and bypass AR. Casting time = spell tier in rounds (Tier 1 resolves immediately).

**High stat:** WIS 15+ (Mage) or CHA 15+ (Shaman) grants +1 Tier 1 slot per day.

**Focus:** charge a staff or focus with one spell per day. Anyone can activate it.

**Magic Fluency:** read, identify, scribe, and craft magic items.

| Level | ATK | DEF | T1 | T2 | T3 | T4 | T5 |
|-------|-----|-----|----|----|----|----|-----|
| 1  | +0 | 10 | 1  | —  | —  | —  | —  |
| 2  | +0 | 11 | 2  | —  | —  | —  | —  |
| 3  | +0 | 11 | 3  | 1  | —  | —  | —  |
| 4  | +1 | 12 | 4  | 2  | —  | —  | —  |
| 5  | +1 | 12 | 4  | 2  | 1  | —  | —  |
| 6  | +1 | 13 | 4  | 2  | 2  | —  | —  |
| 7  | +2 | 13 | 4  | 3  | 2  | 1  | —  |
| 8  | +2 | 14 | 4  | 3  | 3  | 2  | —  |
| 9  | +2 | 14 | 4  | 3  | 3  | 2  | 1  |
| 10 | +3 | 15 | 4  | 4  | 3  | 2  | 2  |

### Class Variants

| | Base | Variant 1 | Variant 2 |
|---|---|---|---|
| **Hunter** | Hunter | Noble | Striker |
| **Delver** | Delver | Ranger | Seeker |
| **Caster** | Caster | Esper | Dabbler |

**Noble (Hunter):** loses Fighting Strength; gains Spell Scrolls.

**Striker (Hunter):** loses Heavy Armor, Fighting Strength, weapon access beyond dagger; gains DEF +2 unarmored, Unarmed d6, Runic Lore, Runecasting at -2 levels (touch/self only, no Runecrafting). d8 HD. Uses Hunter ATK and Split Attack.

**Ranger (Delver):** loses Delver Skills; gains Ranger Skills. Everything else identical.

**Seeker (Delver):** loses Sneak Attack, Lethal Agility, Acrobatic; gains Runecasting at -2 levels (includes Runecrafting), Runic Lore.

**Esper (Caster):** loses Runecasting, Spell Scrolls, Runic Lore; gains Spirit Summoning (CHA-based), Spirit Lore (CHA 15+), Light Armor, Ranger Skills.

**Dabbler (Caster):** loses Runic Lore, Runecrafting; gains d6 HD, Light Armor. Full Runecasting slot progression. Keeps Spell Scrolls.

---

## Combat

### Round Sequence
1. **Declare spells** (declare slot being used; Tier 1 resolves this round; higher tiers take multiple rounds; damage during casting loses spell and slot)
2. **Roll initiative** (each side rolls d6; winner acts first; ties simultaneous)
3. **Missiles** (ranged attacks in initiative order)
4. **Movement** (in initiative order)
5. **Melee** (in initiative order)
6. **Spells resolve** (declared spells in initiative order)

### Actions
- **Move 1 zone + take an action** (attack, use item, cast spell, task, aid)
- **Move 2 zones, no action**

### Attacking
**Melee:** d20 + ATK + STR vs opponent DEF

**Ranged:** d20 + ATK + AGI vs opponent DEF

**Defense:** when monster attacks, player rolls d20 + DEF vs 10 + monster ATK. When monster splits attacks, all targeted players roll simultaneously.

| Result | Effect |
|--------|--------|
| Hit | Roll weapon damage, subtract AR, min 1 |
| Miss | No effect |
| Natural 20 on attack | Critical: bypass AR, reduce target AR by 1 for fight |
| Natural 20 on defense | Avoid hit + free counterattack this round |
| Natural 1 on defense | Monster crits you |

### DEF Modifiers
| Source | Modifier |
|--------|---------|
| Shield | +1 |
| Heavy shield | +2 |
| AGI modifier | +AGI (negated by heavy armor) |
| Magic items | As listed |

### Split Attack
Hunters may divide their ATK bonus across multiple attacks in a single round: minimum +1 per attack, different enemies only. Maximum attacks = ATK bonus. Magic weapon bonus adds to the budget.

*Example: ATK +4 → one at +4, two at +2/+2, three at +2/+1/+1, or four at +1/+1/+1/+1.*

### Damage and AR
Hit → roll weapon die + STR modifier → subtract AR → minimum 1 damage.

**Critical hit:** bypass AR entirely, reduce target AR by 1 for this fight (min 0). PC armor degraded this way requires downtime repair.

### Weapons
| Option | Effect |
|--------|--------|
| One-handed | Standard damage die |
| Two-handed | Step up die (d4→d6, d6→d8) |
| Dual wield | +1 ATK; either weapon's die |
| Shield | +1 DEF |
| Heavy shield | +2 DEF |

### Ranged Combat
Ranged weapons cannot be used in melee. Cannot safely target enemies engaged in melee. Defenders cannot counterattack ranged attackers.

**Ammunition:** 3 bubbles. After each fight roll d6: on 4–6 mark one bubble. All 3 marked = one shot left. Resupply clears all.

### Defeat
At 0 HP a character is **defeated**: not automatically dead. Referee determines consequences.

### Fleeing Melee
Fleeing a melee zone gives opponents a free attack before leaving.

---

## Armor

| Armor | AR | Slots | Treasure | Notes |
|-------|----|-------|----------|-------|
| Light | 1 | 1 body | 1 | — |
| Heavy | 2 | 2 body | 3 | No stealth/swimming. Negates AGI to DEF. Casters: enemies +2 to saves. |
| Magic | 3+ | varies | 5+ | — |
| Shield | — | 1 hand | 1 | +1 DEF |
| Heavy shield | — | 1 hand | 2 | +2 DEF |

Hunters: any armor. Delvers: light only. Casters: any, but suffer armor penalty to spellcasting.

---

## Saving Throws

**Target: 15 − floor(level ÷ 2).**

| Level | Target |
|-------|--------|
| 1–2 | 15 |
| 3–4 | 14 |
| 5–6 | 13 |
| 7–8 | 12 |
| 9–10 | 11 |

| Threat | Modifier |
|--------|----------|
| Poison, disease, physical | RES |
| Breath, area effects | AGI |
| Beguilement, fear, illusion | CHA |
| Magical compulsion, death | RES or CHA |
| Fortune-dependent | LUC |

---

## Task Resolution

Default **2-in-6**. Roll d6 equal to or under target to succeed.

| Modifier | Chance |
|----------|--------|
| −1 | 1-in-6 |
| 0 | 2-in-6 |
| +1 | 3-in-6 |

Relevant background or species adds +1. Improved through downtime or accomplishment.

---

## Inventory

10 slots: 2 hand slots and 2 body slots (included). Conditions occupy slots until removed.

Heavy armor impedes stealth and swimming.

---

## Conditions

| Type | Removed by | Cost |
|------|-----------|------|
| Injury | Healer, surgeon, or rest | 1 treasure/slot |
| Disease | Herbalist or antidote | 1 treasure/slot |
| Curse / hex | Temple or ritual | 1–3 treasure/slot |
| Jinx | Spirit appeasement or quest | Narrative |
| Magical binding | Specific ritual | Narrative |

| Severity | Slots |
|----------|-------|
| Minor | 1 |
| Moderate | 2 |
| Severe | 3 |
| Catastrophic | 4+ |

**Ability damage:** injury → 1d6 STR; poison → 1d6 RES (save or repeat daily); Jinx → 1d6 LUC. 0 in any stat = severe consequences. 0 RES = death.

---

## Luck

LUC modifies die of fate rolls. **Burning Luck:** spend 1 LUC permanently for a favorable outcome without rolling. Irreversible.

**Recovery:** 1d3 per week downtime up to starting score. No hard ceiling.

---

## Advancement

No experience points. Advance through **expeditions** and **accomplishments**.

**Leveling up:** ATK, DEF, and save target advance automatically with level. HP advances by rolling full HD pool; take new result if higher than current HP, else +1. RES modifier applies per die.

**Expedition rewards** (one per significant objective completed):

| Reward | Notes |
|--------|-------|
| +1 to a d6 task | Specific task or category |
| +1 to a stat | Referee determines or player makes a case |
| +1 to a save | Permanent, tied to what was survived |
| New talent | Requires fictional justification |

**Level bands:** advancement halts at band ceiling until an Accomplishment unlocks the next.

| Levels | Title | Scale |
|--------|-------|-------|
| 1–2 | Adventurer | Unknown. Survives on luck and grit. |
| 3–4 | Hero | Local reputation. |
| 5–6 | Lord | Regional power. |
| 7–8 | Legend | Continental scale. |
| 9–10 | Mythic | Near-godlike. |

**Accomplishments:** a deed of sufficient magnitude. Reward: unlock next band OR concrete bonus (+1 to a stat, +1 to all saves of a type, or significant talent). Advancing is always optional.

---

## Spells

Casters prepare from spellbook after rest. Spells known capped by WIS score.

**Traditions:**
- **Mage:** WIS-based. Learns from books and inscriptions.
- **Shaman:** CHA-based. Learns by communing with spirits. Cannot use scrolls.
- **Artificer:** Stores prepared spells in gadgets. Anyone activates; no slot cost to activator.

---

# PART 2: REFEREE RULES

## Monster Statistics

**ATK = HD.** A 5HD monster attacks at +5.

**DEF = 10 + floor(HD ÷ 2).** Adjust for shields or exceptional agility.

**Save = 19 − floor(HD ÷ 2).** Minimum 2.

**HP:** roll size die × HD. Use averages for speed.

**AR:** 0–3 mundane; 4+ magical.

| Size | HD die | Damage die | Base AR |
|------|--------|------------|---------|
| Small | d4 | d4 | 0 |
| Medium | d6 | d6 | 0 |
| Large | d8 | d8 | 1 |
| Huge | d10 | d10 | 1 |
| Colossal | d12 | d12 | 2 |

**Special ability damage:** max dice = floor(HD ÷ 2) rounded up, using size die.

**Split attack:** monsters divide ATK bonus the same way Hunters do. Players roll defense simultaneously when multiple targets are declared.

## Monster Stat Block

```
NAME
HD: X  Size: X  HP: X  ATK: +X  DEF: X  AR: X  Save: X+
Attacks: X/round  Damage: die
Special: [abilities]
Morale: X  Treasure: X
```

## Level and Challenge

| HD gap | Role |
|--------|------|
| Same | Standard threat |
| +2 | Lieutenant / miniboss |
| +4 | Solo boss |
| +6 | Overwhelming |

## Encounter Procedures

**Surprise:** 2-in-6. Surprised side loses first round. Unseen/silent adds +2.

**Reaction:** 2d6 + CHA of spokesperson. 2–3 hostile; 4–5 unfriendly; 6–8 uncertain; 9–10 indifferent; 11–12 friendly.

**Morale:** 2d6 vs morale score when taking significant losses. Fail = flee or surrender.

## Dungeon Turns

Approximately 10 minutes each. Each turn: move and search, attempt specific action, or rest (1d4 + RES HP, min 0). Wandering encounter check every 3 turns (2-in-6). Track light: torch = 6 turns.

## Travel

1 hex ≈ 6 miles. Base rate: 1 hex/day on foot, 2 hexes/day mounted.

Encounter roll per hex traversed: plains/road on 1; forest/hills on 1–2; mountains/swamp on 1–3; ruins/blighted on 1–4.

## Treasure Scale

| Value | Examples |
|-------|---------| 
| 1 | Coins, basic gear, 1 week downtime |
| 2 | Heavy armor, quality weapon, hireling month |
| 3 | Minor magic item |
| 5 | Magic weapon or armor |
| 10 | Significant magic item, manor |
| 20+ | Legendary artifact, keep |

1 treasure = 1 week downtime per character. Party of 4 = 4 treasure/week upkeep.

## Magic Weapons

Add bonus to ATK and damage. Also expands Hunter split attack budget.

| Bonus | Effect |
|-------|--------|
| +1 | Overcomes AR 1; +1 split target |
| +2 | Overcomes AR 2; +2 split targets |
| +3 | Overcomes all mundane AR; +3 split targets |

## Magic Armor

| AR | Rarity |
|----|--------|
| 3 | Uncommon |
| 4 | Rare |
| 5 | Legendary |

Repairs itself between expeditions after crit degradation.

## Die of Fate

d6 oracle. 1–3 unfavorable; 4–6 favorable. Adjust range for context. Apply LUC modifier. Burned Luck = auto-favorable, no roll.

---

## Downtime Activities

Between expeditions characters spend treasure on upkeep and may pursue:

| Activity | Cost | Time | Result |
|----------|------|------|--------|
| Rest and recover | 1 treasure | 1 week | Full HP restoration |
| Injury treatment | 1 treasure/slot | 1 week | Clear injury condition |
| Spell research | 2 treasure | 1 week | 2-in-6 to learn new spell (higher tier = harder) |
| Carousing | 1 treasure | 1 week | 1d6 LUC restored; possible complications |
| Training | 2 treasure | 1 week | Practice specific skill or technique |
| Crafting | varies | 1–4 weeks | Produce equipment, gadgets, or scrolls |
| Networking | 1 treasure | 1 week | Establish or deepen a contact |
| Hireling recruitment | 1 treasure | 1 week | Roll to find available hirelings |

---

## Employment

Find hirelings or recruit a retainer.

**Finding Hirelings:** Roll 2d6 + CHA:

| Roll | Result |
|------|--------|
| 2–4 | No takers |
| 5–7 | 1d3 common hirelings |
| 8–10 | 2d3 common or 1 skilled |
| 11–12 | Up to 3 skilled hirelings |
| 13+ | A specialist seeks you out |

**Retainer recruitment:** CHA modifier 0+; reputation required. Roll 2d6 + CHA vs 9. Success = candidate approaches. Loyalty starts at 7.

| Type | Cost | Notes |
|------|------|-------|
| Common (porter, guard) | 1 treasure/month | No special abilities |
| Skilled (guide, sage) | 2 treasure/month | Relevant background |
| Specialist | 3+ treasure/month | Specific expertise |
| Retainer | Share of treasure | Loyalty score 7 |

---

## Accomplishment Examples

**Levels 1–2 → 3–4 (Adventurer → Hero)**
- Recover a significant relic and return it to a community that needs it
- Defeat a threat that has terrorized a region
- Establish a lasting alliance between two factions
- Return from a site others entered and did not

**Levels 3–4 → 5–6 (Hero → Lord)**
- Claim a seat of power and hold it
- Overthrow a regional power and choose what rises in its place
- Complete a quest of legendary difficulty
- Earn the permanent service of a powerful NPC, spirit, or faction

**Levels 5–6 → 7–8 (Lord → Legend)**
- Conquer or liberate a city; reshape a nation
- Destroy or seal something that has threatened the world for generations
- Found an order, institution, or dynasty that will outlast you
- Make a bargain with or defeat a being of mythic power

**Levels 7–8 → 9–10 (Legend → Mythic)**
- Reshape the political order of a continent
- Defeat a truly ancient threat
- Achieve something that changes the nature of the world itself

The reward is always a choice: unlock the next level band, or take a concrete bonus. Advancing is always optional.

---

*Talents, equipment, genos, monsters, and backgrounds are on separate reference sheets.*