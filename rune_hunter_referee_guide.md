# Rune Hunter. Referee's Guide

---

## What This Document Is

The referee runs the world. Players roll dice for everything: attacks, defenses, saves, and tasks for themselves and their hirelings, retainers, familiars, and summoned creatures. Monsters are static numbers. The referee describes outcomes, adjudicates edge cases, and keeps the fiction moving.

This document covers encounter design, dungeon procedures, overland travel, monsters, treasure, and the procedures that run the game between combats.

---

# PART 1: ENCOUNTER DESIGN

## Level and Challenge

Monster HD determines the scale of threat relative to the party's level. Use the following as a baseline when designing encounters:

| HD gap | Role | Feel |
|--------|------|------|
| Same HD | Standard threat | Dangerous fight, attrition risk |
| +2 HD | Lieutenant / miniboss | Expect casualties, manageable |
| +4 HD | Solo boss | Climactic, likely casualties |
| +6 HD | Overwhelming | Run, negotiate, or find another way |

A level 1 party fighting a 3HD boss is a hard but winnable fight. The same party fighting a 5HD boss is a desperate set piece. A 7HD creature is effectively unsurvivable in direct combat for a level 1 party. Structure the encounter to encourage other solutions.

Dungeon level describes the general threat profile of a site, not a hard content ceiling. Higher HD threats can and should exist inside lower level dungeons. A level 1 dungeon can have a level 3 guardian. Parties learn to read the signs and route around or come back stronger.

## Encounters, Surprise, Reaction, Morale

**Surprise:** 2-in-6 chance. Surprised side loses their first round of action. Unseen or silent parties add +2 to surprise chance.

**Reaction rolls:** 2d6 + CHA modifier of party spokesperson.

| 2d6 + CHA | Reaction |
|-----------|----------|
| 2–3 | Hostile, attacks immediately |
| 4–5 | Unfriendly, hostile unless party acts carefully |
| 6–8 | Uncertain, waits and watches |
| 9–10 | Indifferent, not immediately hostile |
| 11–12 | Friendly, open to interaction |

Not every encounter is a fight. Apply reaction rolls to all encounters including monsters.

**Morale:** check when monsters take significant losses or face overwhelming odds. Roll 2d6 vs morale score. Fail = flee or surrender.

| Morale | Examples |
|--------|---------|
| 6 | Cowardly: goblins, hired thugs |
| 8 | Average: orcs, guards |
| 10 | Determined: veterans, fanatics |
| 12 | Unbreakable: constructs, undead, bound spirits |

---

# PART 2: MONSTER FRAMEWORK

## How Monsters Work

Monsters use **HD** and **size** as their two primary axes. HD determines ATK, DEF, save, and HP pool. Size determines the HP die and damage die. AR represents natural armor.

All rolls are player-facing. Monsters never roll. When a monster attacks, the targeted player rolls d20 + DEF vs 10 + monster ATK. When a monster splits attacks, all targeted players roll simultaneously.

## Monster Statistics

**ATK = HD.** A 5HD monster attacks at +5.

**DEF = 10 + floor(HD/2).** Pre-calculate and list on the stat block. Adjust for AGI equivalents or shields as needed.

**Save = 19 − floor(HD/2).** Minimum 2.

**HP** is rolled using the size die, one die per HD. Use average values for ease of reference.

**AR** represents natural armor: hide, scales, bone, plate. Listed on the stat block. Crit hits reduce AR by 1 for the fight.

## Size

| Size | HD die | Damage die | Base AR |
|------|--------|------------|---------|
| Small | d4 | d4 | 0 |
| Medium | d6 | d6 | 0 |
| Large | d8 | d8 | 1 |
| Huge | d10 | d10 | 1 |
| Colossal | d12 | d12 | 2 |

## Monster Special Abilities

Special abilities create tactical texture. Use these as a guide:

**Free (no cost, referee judgment):**
Pack tactics, keen senses, morale bonus, poison on hit, any flavor trait that creates fiction without changing the math.

**Minor:**
- +1 AR (max 3 mundane, 4+ for magical creatures)
- Step up damage die
- Additional attack per round
- Veteran (+1 ATK beyond HD baseline)

**Significant:**
- Regeneration (recovers HP each round, stopped by fire/acid/magic)
- Frightful presence (save or −1 ATK/DEF while in range)
- Grab/grapple (on hit, target held; action to escape)

**Major:**
- Area attack / breath weapon (all in zone save for half, bypasses AR)
- Powerful spell-like ability (1/day)
- Multiple phases
- Legendary resistance (once per encounter, turn a failed save into a success)

## Special Ability Damage Scaling

Area attacks and breath weapons scale with HD using the same logic as spell tiers. A monster's maximum damage dice for a special ability equals floor(HD/2) rounded up:

| HD | Max damage dice |
|----|----------------|
| 1–2 | 1 die |
| 3–4 | 2 dice |
| 5–6 | 3 dice |
| 7–8 | 4 dice |
| 9–10 | 5 dice |

Use the monster's size die. A 5HD Colossal can stomp for 3d12 (save for half). A 8HD Huge dragon breathes for 4d10 (save for half).

## Monster Split Attack

Monsters divide their ATK bonus across multiple targets the same way Hunters do: minimum +1 per attack, each attack targets a different creature. The referee declares how the monster splits its ATK before players roll defense. This makes the split a meaningful tactical decision rather than arbitrary.

## Monster Stat Block Format

```
MONSTER NAME
HD: X   Size: X   HP: X   ATK: +X   DEF: X   AR: X   Save: X+
Attacks: X/round   Damage: die
Special: [abilities]
Morale: X   Treasure: X
Notes: [behavior, habitat, tactics]
```

## Sample Monsters

---

**GOBLIN**
HD: 1   Size: Small   HP: 2   ATK: +1   DEF: 11   AR: 0   Save: 19+
Attacks: 1   Damage: d4
Special: Pack tactics (free)
Morale: 6   Treasure: 1
Notes: Cowardly alone. Dangerous in numbers. Flee when half their group falls.

---

**GOBLIN SHAMAN**
HD: 1   Size: Small   HP: 2   ATK: +1   DEF: 11   AR: 0   Save: 19+
Attacks: 1   Damage: d4
Special: Hex 1/day: one target −1 to all rolls until rest (save resists)
Morale: 6   Treasure: 1
Notes: Hangs back. Curses the strongest PC first. Priority target.

---

**ORC RAIDER**
HD: 2   Size: Medium   HP: 7   ATK: +2   DEF: 11   AR: 0   Save: 18+
Attacks: 1   Damage: d8
Special: Aggressive (free): never checks morale while warchief lives
Morale: 8   Treasure: 1
Notes: Hits harder than expected. Serve a warchief.

---

**CAVE BEAR**
HD: 3   Size: Large   HP: 12   ATK: +3   DEF: 12   AR: 1   Save: 18+
Attacks: 1   Damage: d8
Special: Grab on hit: held target takes automatic d8/round, STR task to escape. Keen scent (free).
Morale: 8   Treasure: 0
Notes: Not hostile unless cornered or protecting cubs.

---

**SWAMP TROLL**
HD: 5   Size: Large   HP: 17   ATK: +5   DEF: 12   AR: 1   Save: 17+
Attacks: 2   Damage: d8
Special: Regeneration: recovers 3 HP/round, stopped by fire or acid. Keen scent (free).
Morale: 9   Treasure: 3
Notes: Tracks by scent. Rarely abandons a chase. Effectively immortal unless wounds cauterized.

---

**IRON SENTINEL**
HD: 5   Size: Medium   HP: 15   ATK: +6   DEF: 12   AR: 3   Save: 17+
Attacks: 2   Damage: d6
Special: Veteran (+1 ATK). Never flees. Immune to poison, fear, mental effects (construct).
Morale: 12   Treasure: 4
Notes: Ancient relic guardian executing original function. Does not negotiate.

---

**STONE GIANT**
HD: 8   Size: Huge   HP: 36   ATK: +8   DEF: 14   AR: 2   Save: 15+
Attacks: 3   Damage: d10
Special: Frightful presence: save or −1 ATK/DEF while in range. Boulder throw (free): ranged, same damage, AGI save for half.
Morale: 10   Treasure: 4
Notes: Boulders bypass defense rolls. AGI save for half damage.

---

**ELDER WYVERN**
HD: 8   Size: Large   HP: 32   ATK: +9   DEF: 14   AR: 2   Save: 15+
Attacks: 3   Damage: d8
Special: Veteran (+1 ATK). Poison sting: RES save or take condition (2 slots). Frightful presence. Keen senses (free).
Morale: 9   Treasure: 5
Notes: Sting counts as third attack. Disengages freely if airborne.

---

**ANCIENT DRAGON**
HD: 10   Size: Huge   HP: 52   ATK: +10   DEF: 15   AR: 2   Save: 14+
Attacks: 3   Damage: d10
Special: Breath weapon: 5d10 fire, all in cone save for half, bypasses AR. Frightful presence. Legendary resistance (1/encounter).
Morale: 10   Treasure: 10+
Notes: Breath weapon is primary threat. Highly intelligent, will not fight on unfavorable terms.

---

**VOID COLOSSUS**
HD: 15   Size: Colossal   HP: 90   ATK: +15   DEF: 17   AR: 3   Save: 12+
Attacks: 3   Damage: d12
Special: Reality pulse 1/day: 5d12, all in area save or lose next action. Legendary resistance (2/encounter). Frightful presence: entire visible area.
Morale: 12   Treasure: 15+
Notes: Ancient construct or cosmic entity of unclear origin.

---

## Designing Monsters

- HD sets ATK, DEF, save, and HP pool. A higher HD creature is always more capable in combat.
- Size sets the HP and damage floor. A Large creature is more durable and hits harder than a Small creature of the same HD.
- AR creates tactical texture around DR and crit degradation. High AR monsters require magic weapons or clever tactics.
- Special abilities make fights memorable. Regeneration, frightful presence, grab, and breath weapons all change how players approach the encounter.
- Treasure ≈ HD/2 as a baseline. Adjust for fiction.
- Not every monster needs special abilities. Simple monsters are fine. Save complexity for encounters that matter.

---

# PART 3: DUNGEON PROCEDURES

## The Excursion Site

The basic unit of dungeon design is the **excursion site**: a self-contained area of 6 rooms.

### Generating a Site
Number rooms 1–6. Roll d6 for each room to determine which room it connects to; re-roll existing connections. Connections may have complications:

- **Lengthy:** 1 full turn of movement to traverse
- **Difficult:** requires a task roll or specific action to pass
- **Hidden:** requires foreknowledge or ingenuity to find

### Room Functions
Rooms 1–4 are **functional:**
1. Site entrance
2. NPCs with treasure
3. NPCs without treasure
4. Treasure without NPCs (possibly hidden or trapped)

Rooms 5–6 are **landmarks:** neither punish nor reward, but provide atmosphere and lore.

### Treasure per Site
Approximately equal to the sum of monster HD divided by 2 in the site.

## Dungeon Structure

A dungeon is made up of linked excursion sites. Scale to the party's level.

| Dungeon level | Sites | Approx. rooms | Expected treasure |
|---|---|---|---|
| 1–2 | 1 | 6 | 3–5 |
| 3–4 | 2 | 12 | 6–10 |
| 5–6 | 3 | 18 | 10–18 |
| 7–8 | 4 | 24 | 15–25 |
| 9–10 | 5 | 30 | 20–35 |

The dungeon's primary boss lives in the deepest or most protected site. Clearing the main objective earns an incremental reward and may trigger a level-unlocking Accomplishment.

## Dungeon Exploration Turns

Dungeon exploration uses **turns** of approximately 10 minutes each.

Each turn the party may:
- Move to an adjacent area and search it
- Attempt a specific action (pick a lock, search for secret doors, disable a trap)
- Rest: recover 1d4 + RES modifier HP, minimum 0; requires a full turn with no threats

After every 3 turns, roll for a **wandering encounter** (2-in-6 chance).

**Light** must be tracked. A torch lasts 6 turns. Lanterns last longer but consume oil.

## Combat Zones

Zones are defined by the referee based on terrain and fiction. A room might be one zone; a large hall two or three. Zones are abstract; their size depends on what makes tactical sense for the space.

---

# PART 4: OVERLAND TRAVEL

Travel is measured in **hexes** (approximately 6 miles each).

**Base rate:** 1 hex per day on foot.
**Mounted:** 2 hexes per day in open terrain; reduced or no benefit in difficult terrain.

### Encounter Rolls
Roll d6 at the end of each hex traversed.

| Terrain | Encounter on |
|---------|-------------|
| Plains / road | 1 |
| Forest / hills | 1–2 |
| Mountains / swamp | 1–3 |
| Ruins / blighted land | 1–4 |

Apply a reaction roll to all encounters.

### Supplies & Rations

1 ration = 1 inventory slot = feeds 1 character for 7 days.

Running out of rations requires foraging (task roll, difficulty by terrain) or the party begins suffering conditions at the referee's discretion.

---

# PART 5: HIRELINGS & RETAINERS

| Type | Cost | Notes |
|------|------|-------|
| Common hireling (porter, torchbearer, guard) | 1 treasure/month | No special abilities |
| Skilled hireling (guide, interpreter) | 2 treasure/month | Relevant background |
| Specialist (sage, healer, engineer) | 3+ treasure/month | Specific expertise |
| Retainer | Share of treasure | Long-term NPC companion; loyalty score 7 |

Retainers begin with loyalty 7. Loyalty increases through fair treatment, good pay, and shared success. CHA modifier affects loyalty and morale checks.

---

# PART 6: TREASURE & MAGIC ITEMS

## Treasure Scale

| Value | Examples |
|-------|---------| 
| 1 | Bag of coins, basic tools, light armor, 1 week downtime |
| 2 | Heavy armor, quality weapons, hireling for a month |
| 3 | Minor magic item, ship passage, bribing an official |
| 5 | Magic weapon or armor, small building |
| 10 | Significant magic item, manor, small military retinue |
| 20+ | Legendary artifact, keep, noble title |

1 treasure = 1 week of downtime per character. A party of 4 burns 4 treasure/week between expeditions.

## Physical Weight of Treasure
- Coins, bulky goods: 1 slot per treasure value
- Gems, jewelry, art: 1 slot per 2–3 treasure value
- Magic items: 1 slot regardless of value

## Magic Weapons

Magic weapons add their bonus to both ATK rolls and damage. The ATK bonus also expands the Hunter's split attack budget.

| Bonus | Effect |
|-------|--------|
| +1 | Overcomes AR 1 reliably; one extra split target |
| +2 | Overcomes AR 2 reliably; two extra split targets |
| +3 | Overcomes all mundane AR; three extra split targets |

## Magic Armor

Raises AR beyond the mundane maximum of 2.

| AR | Source | Rarity |
|----|--------|--------|
| 3 | Magic +1 | Uncommon |
| 4 | Magic +2 | Rare |
| 5 | Magic +3 | Legendary |

Magic armor AR degrades on crit hits like mundane armor, but repairs itself between expeditions.

## Relic Technology

Relic weapons (firearms, energy blades) bypass mundane AR. Magic AR still applies.

## Spell Invocations as Treasure

Finding a new spell or higher-tier invocation inscribed in an archive, held by a spirit willing to teach, or written in a forbidden tome is treasure equivalent to a magic item. Assign treasure value 2–5 depending on the spell tier it unlocks.

## Buying & Selling Magic Items

Not a casual transaction. Finding a buyer or seller requires downtime, contacts, and often travel. Expect 50–75% of treasure value when selling; full value or above when buying.

---

# PART 7: ACCOMPLISHMENT EXAMPLES

Accomplishments emerge from the sandbox. The following calibrate what qualifies at each level band transition.

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

The reward is always a choice: unlock the next level band, or take a concrete bonus. Advancing is a narrative commitment; the world will treat the character differently. Rejecting the advance and taking the bonus is always a legitimate choice.

---

# PART 8: THE DIE OF FATE

The die of fate is the referee's oracle tool: a d6 rolled when the answer to a question depends on circumstance rather than character capability.

*Is there a guard at this post? Is the door unlocked? Does the torch last long enough?*

**Base:** 1–3 unfavorable, 4–6 favorable. Adjust the range for context: a very likely outcome might only fail on a 1; an unlikely one might only succeed on a 6.

**LUC modifier:** apply the relevant character's LUC modifier to the result. A party with LUC +1 finds things slightly more cooperative. LUC −1 means things don't break their way.

**Burned Luck:** a player may spend 1 LUC permanently to invoke a favorable outcome without rolling. The door is unlocked. The guard is asleep. Irreversible.

---

# DESIGN APPENDIX

**On the HD gap framework**
The +2/+4/+6 HD gap guidelines replace the old tier gap table. The underlying math is similar: a +4 HD gap puts the monster at roughly double the party's ATK and DEF values, producing the same "climactic boss" feel as the old +2 tier gap. The key difference is that HD gaps are continuous rather than discrete, giving the referee more granular control over encounter difficulty.

**On monster ATK = HD**
Monsters attack at their full HD rather than half HD (which PCs use) because monsters implicitly account for magic gear, venom, special training, and raw ferocity that PCs accumulate through explicit treasure. A 10HD monster at +10 is equivalent to a L10 Hunter with a +3 magic weapon at +10. The referee doesn't need to equip monsters; the HD already assumes peak capability.

**On the defense roll**
Players roll d20 + DEF vs 10 + monster ATK rather than the referee rolling monster attacks against static PC DEF. This keeps all dice in player hands. When a monster splits attacks across multiple players, all targeted players roll simultaneously, making the split tactically exciting rather than a passive waiting period.

**On AR degradation**
Critical hits (natural 20 on attack) reduce the target's AR by 1 for the fight. This prevents high-AR monsters from becoming pure stalling exercises: the party's sustained pressure eventually strips the armor, rewarding staying power. For PCs, degraded armor requires downtime repair, making armor a meaningful resource rather than a passive stat.

**On dungeon level and open world design**
A dungeon's level describes its general threat profile, not a hard content ceiling. Higher HD threats exist inside lower level dungeons: a guardian placed by the original builders, a creature that wandered in, an NPC whose true power only becomes apparent gradually. Parties learn to read the signs: scratch marks too high on the walls, bones of things that should have won, a room that smells wrong. They route around, come back stronger, or find a clever solution. The model is FFXII and Xenoblade Chronicles, not an MMO zone system.