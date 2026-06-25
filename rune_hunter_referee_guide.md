# Rune Hunter. Referee's Guide

---

## What This Document Is

The referee runs the world. Players roll dice for everything (attacks, defenses, saves, tasks) for themselves and their hirelings, retainers, familiars, and summoned creatures. Monsters are static numbers. The referee describes outcomes, adjudicates edge cases, and keeps the fiction moving.

This document covers encounter design, dungeon procedures, overland travel, monsters, treasure, and the procedures that run the game between combats. Citation markers ¹ ² ³ refer to the Design Appendix.

---

# PART 1: ENCOUNTER DESIGN

## Tier and Challenge

Monster tier determines the scale of threat. Use the following as a baseline when designing encounters: ²

| Tier gap | Role | Feel |
|----------|------|------|
| Same tier | Standard threat | Dangerous fight, attrition risk |
| +1 tier | Lieutenant / miniboss | Expect casualties, manageable |
| +2 tiers | Solo boss | Climactic, likely casualties |
| +3 tiers | Overwhelming | Run, negotiate, or find another way |

A Tier 1 party fighting a Tier 2 boss is a hard but winnable fight. The same party fighting a Tier 3 boss is a desperate set piece. Tier 4 is effectively unsurvivable in direct combat. Structure the encounter to encourage other solutions.

Dungeon tier describes the general threat profile of a site, not a hard content ceiling. Higher tier threats can and should exist inside lower tier dungeons. ⁷

This scaling holds consistently across all tiers. ²

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
| 6 | Cowardly, goblins, hired thugs |
| 8 | Average, orcs, guards |
| 10 | Determined, veterans, fanatics |
| 12 | Unbreakable, constructs, undead, bound spirits |

---

# PART 2: MONSTER FRAMEWORK

## How Monsters Work

Monsters use **size** and **tier** as their two primary axes. Size determines HP, damage die, and base AR. Tier determines FC and point budget for customization. ³

All rolls are player-facing. Monsters never roll. Players roll to attack and to defend against monsters. A monster's FC is always expressed as a static target: players roll d20 + FC + STR/AGI vs **10 + monster FC**.

## Size × Tier Matrix

HP uses the size die at Tier 1, then adds half the die (rounded down) per additional tier.

| Size | HP die | HP increment | Damage die | Base AR |
|------|--------|-------------|------------|---------|
| Small | d4 | +2/tier | d4 | 0 |
| Medium | d6 | +3/tier | d6 | 0 |
| Large | d8 | +4/tier | d8 | 1 |
| Huge | d10 | +5/tier | d10 | 1 |
| Colossal | d12 | +6/tier | d12 | 2 |

FC = tier for all monsters. Point budget = tier (3 points at Tier 3, 5 points at Tier 5, etc.).

| Size | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Tier 5 | Tier 6 |
|------|--------|--------|--------|--------|--------|--------|
| Small | 4hp/+1 | 6hp/+2 | 8hp/+3 | 10hp/+4 | 12hp/+5 | 14hp/+6 |
| Medium | 6hp/+1 | 9hp/+2 | 12hp/+3 | 15hp/+4 | 18hp/+5 | 21hp/+6 |
| Large | 8hp/+1 | 12hp/+2 | 16hp/+3 | 20hp/+4 | 24hp/+5 | 28hp/+6 |
| Huge | 10hp/+1 | 15hp/+2 | 20hp/+3 | 25hp/+4 | 30hp/+5 | 35hp/+6 |
| Colossal | 12hp/+1 | 18hp/+2 | 24hp/+3 | 30hp/+4 | 36hp/+5 | 42hp/+6 |

Attacks per round scale with size and tier. Small and Medium start at 1 attack, gaining a second at Tier 4. Large starts at 1, gaining a second at Tier 3 and third at Tier 5. Huge starts at 1, gaining a second at Tier 3 and third at Tier 5. Colossal starts at 2, gaining a third at Tier 4. ¹

**Note on Colossal Tier 1 creatures:** A Colossal Tier 1 is not a cosmic threat. It is simply a very large animal. Its danger comes entirely from scale, not cunning or special abilities. A Tier 1 party cannot fight one fairly and survive. The encounter is a puzzle: lure it away, exploit terrain, find its weak point, prepare before engaging. A high-tier character returning to the same area can defeat one trivially. This is intentional and mirrors the JRPG feeling of outgrowing old threats.

## Customization Point Menu

Each monster has a point budget equal to its tier. Spend points to differentiate monsters within their tier. Not every monster needs a full budget. Simple monsters are fine.

**Free (referee judgment, no cost):**
Pack tactics, keen senses, morale boost, poison on hit, any flavor trait that creates fiction without changing the math.

**1 point:**
- Veteran / Champion (+1 FC)
- +1 AR (max 3 mundane, 4+ magical creatures)
- Step up damage die (d4→d6→d8→d10→d12)
- +1 extra attack per round

**2 points:**
- Regeneration (recovers HP each round, stopped by fire/acid/magic)
- Spell-like ability (1/day, Tier 1–2 equivalent)
- Frightful presence (CHA save or −1 ATK/DEF while in range)
- Grab / grapple (on hit, target held; action to escape)

**3 points:**
- Breath weapon / area attack
- Powerful magic (1/day, Tier 3+ equivalent)
- Multiple forms / phases
- Legendary resistance (once per encounter, turn a failed save into a success)

## Reading a Monster Entry

```
MONSTER NAME
Tier: X   Size: X   HP: X   FC: +X   AR: X   Attacks: X/round   Damage: die
Special: [abilities]
Morale: X   Treasure: X
Notes: [behavior, habitat]
```

## Sample Monsters

---

**GOBLIN**
Tier: 1   Size: Small   HP: 4   FC: +1   AR: 0   Attacks: 1   Damage: d4
Special: Pack tactics (free)
Morale: 6   Treasure: 1
Notes: Cowardly alone. Dangerous in numbers. Flee when half their group falls.

---

**GOBLIN SHAMAN**
Tier: 1   Size: Small   HP: 4   FC: +1   AR: 0   Attacks: 1   Damage: d4
Special: Spell-like ability, hex 1/day (1pt)
Morale: 6   Treasure: 1
Notes: Hangs back. Curses the strongest PC first. Priority target.

---

**ORC RAIDER**
Tier: 2   Size: Medium   HP: 9   FC: +2   AR: 0   Attacks: 1   Damage: d8
Special: Step up damage die → d8 (1pt). Aggressive morale (free).
Morale: 8   Treasure: 1
Notes: Hits harder than expected for their tier. Serve a warchief.

---

**ORC VETERAN**
Tier: 2   Size: Medium   HP: 9   FC: +3   AR: 0   Attacks: 1   Damage: d6
Special: Veteran +1 FC (1pt). Frightful presence (2pts). CHA save or −1 ATK/DEF.
Morale: 9   Treasure: 2
Notes: Scarred and experienced. Presence alone unsettles lesser warriors.

---

**CAVE BEAR**
Tier: 2   Size: Large   HP: 12   FC: +2   AR: 1   Attacks: 1   Damage: d8
Special: Grab/grapple (1pt). Keen senses, smell (free).
Morale: 8   Treasure: 0
Notes: On hit, can grab instead of dealing damage. Held target takes automatic damage each round. STR task to escape.

---

**KREEN WARRIOR**
Tier: 2   Size: Medium   HP: 9   FC: +3   AR: 1   Attacks: 1   Damage: d6
Special: Veteran +1 FC (1pt). Natural chitin. AR 1, no armor slot needed (free). Keen senses (free).
Morale: 9   Treasure: 1
Notes: Cannot be surprised. Natural AR from chitin counts as armor for penetration purposes.

---

**SWAMP TROLL**
Tier: 3   Size: Large   HP: 16   FC: +4   AR: 1   Attacks: 2   Damage: d8
Special: Regeneration (2pts), recovers 2 HP per round, stopped by fire or acid. Veteran +1 FC (1pt). Keen senses, smell (free).
Morale: 9   Treasure: 3
Notes: Tracks by scent. Rarely abandons a chase. Regeneration makes it effectively immortal unless wounds are cauterized.

---

**RELIC GUARDIAN**
Tier: 3   Size: Large   HP: 16   FC: +4   AR: 2   Attacks: 2   Damage: d8
Special: Veteran +1 FC (1pt). +1 AR (1pt). Never flees, morale 12 (1pt).
Morale: 12   Treasure: 3 (what it guards)
Notes: Ancient construct executing original function. Does not negotiate. Does not tire. Does not flee.

---

**BOUND SPIRIT**
Tier: 2   Size: Small   HP: 6   FC: +2   AR: 1   Attacks: 1   Damage: d4
Special: Spell-like ability 1/day (1pt). +1 AR, intangible (1pt). Keen senses (free).
Morale: 10   Treasure: 0 (what it protects)
Notes: Mundane weapons deal half damage. Magic weapons deal full damage. Fragile but elusive.

---

**STONE GIANT**
Tier: 4   Size: Huge   HP: 25   FC: +5   AR: 2   Attacks: 3   Damage: d10
Special: Veteran +1 FC (1pt). Step up damage die → d12 (1pt). Frightful presence (2pts). Boulder throw (free), ranged attack, same damage, AGI save for half.
Morale: 10   Treasure: 4
Notes: Frightful presence affects anyone in melee range. Boulders ignore defense rolls. AGI save for half damage.

---

**ANCIENT DRAGON**
Tier: 5   Size: Huge   HP: 30   FC: +6   AR: 1   Attacks: 3   Damage: d10
Special: Veteran +1 FC (1pt). Breath weapon (3pts), all in cone make AGI save or take full damage, no armor save. Frightful presence (1pt, remaining budget). Legendary resistance (free at this tier, referee discretion).
Morale: 10   Treasure: 10+
Notes: Breath weapon is the primary threat. 3 melee attacks make direct engagement punishing even without it. Highly intelligent, will not fight on unfavorable terms.

---

## Designing Monsters

- Size sets the HP and damage floor. A Large creature is always more durable and hits harder than a Small creature of the same tier.
- Tier sets FC and the point budget. A higher-tier creature is always more capable in combat.
- Special abilities create tactical texture: what makes this fight different from the last one. Regeneration, frightful presence, grab, and breath weapons all change how players approach the encounter.
- Treasure ≈ tier. Use tier as a baseline and adjust for fiction, a long-established lair has more than a recent occupant.
- Not every monster needs a full point budget. Simple monsters are fine. Save complexity for encounters that matter.
- Monster threat comes from special abilities, terrain, tactics, and numbers: not raw FC.

---

# PART 3: DUNGEON PROCEDURES

## The Excursion Site

The basic unit of dungeon design is the **excursion site**: a self-contained area of 6 rooms.

### Generating a Site
Number rooms 1–6. Roll d6 for each room to determine which room it connects to; re-roll existing connections. Connections may have complications:

- **Lengthy:** 1 full turn of movement to traverse
- **Difficult:** requires a d20 check or specific action to pass
- **Hidden:** requires foreknowledge or ingenuity to find

### Room Functions
Rooms 1–4 are **functional:**
1. Site entrance
2. NPCs with treasure
3. NPCs without treasure
4. Treasure without NPCs (possibly hidden or trapped)

Rooms 5–6 are **landmarks**: neither punish nor reward, but provide atmosphere and lore.

### Treasure per Site
Approximately equal to the sum of monster tiers in the site. Two Tier 2 encounters = roughly 4 treasure distributed across rooms.

## Dungeon Structure

A dungeon is made up of linked excursion sites. Scale to the party's tier.

| Dungeon tier | Sites | Approx. rooms | Expected treasure |
|---|---|---|---|
| 1 | 1 | 6 | 3–5 |
| 2 | 2 | 12 | 6–10 |
| 3 | 3 | 18 | 10–18 |
| 4 | 4 | 24 | 15–25 |
| 5 | 5 | 30 | 20–35 |

The dungeon's primary boss lives in the deepest or most protected site. Clearing the main objective triggers an incremental reward and may trigger a tier-unlocking Accomplishment.

## Dungeon Exploration Turns

Dungeon exploration uses **turns** of approximately 10 minutes each.

Each turn the party may:
- Move to an adjacent area and search it
- Attempt a specific action (pick a lock, search for secret doors, disable a trap)
- Rest: recover 1d4 + RES modifier HP, minimum 0; requires a full turn with no threats

After every 3 turns, roll for a **wandering encounter** (2-in-6 chance).

**Light** must be tracked. A torch lasts 6 turns. Lanterns last longer but consume oil.

## Combat Zones

Zones are defined by the referee based on terrain and fiction. A room might be one zone; a large hall two or three. Zones are abstract, their size depends on what makes tactical sense for the space.

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

Apply a reaction roll to all encounters, not every encounter is hostile.

### Supplies & Rations

1 ration = 1 inventory slot = feeds 1 character for 7 days.

Running out of rations requires foraging (task roll, difficulty by terrain) or the party begins suffering conditions at the referee's discretion.

---

# PART 5: HIRELINGS & RETAINERS

Standard B/X hireling and retainer procedures apply. CHA modifier affects loyalty and morale.

| Type | Cost | Notes |
|------|------|-------|
| Common hireling (porter, torchbearer, guard) | 1 treasure/month | No special abilities |
| Skilled hireling (guide, interpreter) | 2 treasure/month | Relevant background |
| Specialist (sage, healer, engineer) | 3+ treasure/month | Specific expertise |
| Retainer | Share of treasure | Long-term NPC companion; loyalty score 7 |

Retainers begin with loyalty 7. Loyalty increases through fair treatment, good pay, and shared success. Use B/X morale procedures modified by CHA for loyalty checks.

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
Add to **damage bonus only**: not to FC rolls. Bonus applies only on penetrating hits.

| Bonus | Effect |
|-------|--------|
| +1 | Overcomes AR 1 mundane armor reliably |
| +2 | Overcomes AR 2 mundane armor reliably |
| +3 | Overcomes all mundane armor; rarely stopped by magic armor |

## Relic Tech
Relic firearms ignore mundane armor, the armor save does not apply. Magic armor still provides its rating against firearms. Relic energy weapons bypass mundane armor similarly.

## Magic Armor
Raises armor rating beyond the mundane maximum of 3.

| Rating | Source | Rarity |
|--------|--------|--------|
| 4 | Magic +1 | Uncommon |
| 5 | Magic +2 | Rare |
| 6 | Magic +3 | Legendary |

## Rune Invocations as Treasure
Finding a new invocation of a known rune, inscribed in an old archive, held by a spirit willing to teach, written in a forbidden tome, is treasure equivalent to a magic item. Assign treasure value 2–5 depending on the tier of effect it unlocks.

## Buying & Selling Magic Items
Not a casual transaction. Finding a buyer or seller requires downtime, contacts, and often travel. Expect 50–75% of treasure value when selling; full value or above when buying.

---

# PART 7: ACCOMPLISHMENT EXAMPLES

Accomplishments emerge from the sandbox, they are not pre-assigned. The following calibrate the referee's sense of what qualifies at each tier transition.

**Tier 1 → Tier 2 (Adventurer → Hero)**
- Recover a significant relic and return it to a community that needs it / Unlock Hero or +1 stat
- Defeat a threat that has terrorized a region / Unlock Hero or +1d6 HP
- Establish a lasting alliance between two factions / Unlock Hero or +1 to all CHA-based rolls
- Return from a site others entered and did not / Unlock Hero or +1 to saves vs fear and death

**Tier 2 → Tier 3 (Hero → Lord)**
- Claim a seat of power and hold it / Unlock Lord or +1d6 HP
- Overthrow a regional power and choose what rises in its place / Unlock Lord or +1 stat
- Complete a quest of legendary difficulty / Unlock Lord or +1 to all saves
- Earn the permanent service of a powerful NPC, spirit, or faction / Unlock Lord or new significant talent

**Tier 3 → Tier 4 (Lord → Legend)**
- Conquer or liberate a city; reshape a nation / Unlock Legend or +1 stat
- Destroy or seal something that has threatened the world for generations / Unlock Legend or +1d6 HP
- Found an order, institution, or dynasty that will outlast you / Unlock Legend or +2 stat
- Make a bargain with or defeat a being of mythic power / Unlock Legend or significant magical ability

The reward is always a choice: unlock the next tier, or take a concrete bonus. Advancing a tier is a narrative commitment, the world will treat the character differently. Rejecting the tier and taking the bonus is a legitimate choice. ⁵

---

# PART 8: THE DIE OF FATE

The die of fate is the referee's oracle tool, a d6 rolled when the answer to a question depends on circumstance rather than character capability.

*Is there a guard at this post? Is the door unlocked? Does the torch last long enough?*

**Base:** 1–3 unfavorable, 4–6 favorable. Adjust the range for context, a very likely outcome might only fail on a 1; an unlikely one might only succeed on a 6.

**LUC modifier:** apply the relevant character's LUC modifier (or party average for group-affecting rolls) to the result. A party with combined LUC +1 finds things slightly more cooperative. LUC −1 means things don't break even for them.

**Burned Luck:** a player may spend 1 LUC permanently to invoke a favorable outcome without rolling. The door is unlocked. The guard is asleep. Irreversible. ⁶

---

# DESIGN APPENDIX

Design notes explaining the reasoning behind specific rules. Numbers correspond to citation markers in the text.

**¹ Attack count scaling. Huge corrected from Tier 2 to Tier 3**
Simulation confirmed that Huge gaining a second attack at Tier 2 produced same-tier encounters where the monster dropped hunters in 2.3 rounds, equivalent to a lieutenant-level threat at same tier rather than a standard fight. Moving the second attack to Tier 3 corrects this. All other attack count and AR baselines validated correctly against the tier gap targets.

**² Encounter calibration by tier gap**
Simulation of 50,000+ combat iterations confirms that a +1 tier gap produces a genuinely dangerous fight where experienced players can survive but expect pressure. A +2 gap produces a fight where casualties are likely. A +3 gap is effectively unsurvivable in direct combat. This scaling holds consistently across all tiers because the symmetric FC system keeps hit probabilities flat, a Tier 1 Hunter hitting a Tier 2 boss has the same 40% hit probability as a Tier 4 Hunter hitting a Tier 5 boss. The gap matters; the absolute tier does not.

**³ Tier 1 vs Tier 2 outlier**
At very low tiers the numbers are small enough that a +1 gap feels less punishing than at higher tiers. A Tier 2 Medium boss with 1 attack and 9 HP is dangerous but not overwhelming for a fresh Tier 1 party. This is intentional, the first major boss a Tier 1 party faces should be hard but not desperate. The gradient steepens naturally as the numbers grow.

**⁴ Monster size and tier**
The size × tier matrix was designed to produce flat hit probability scaling (the JRPG design intent) while giving the referee intuitive levers for encounter design. Size handles the physical reality of the creature, a Huge creature is simply more durable and hits harder than a Small creature of the same tier. Tier handles the creature's capability and experience. The point budget provides customization without requiring the referee to build every stat from scratch.

**⁵ Tier advancement as optional**
Inspired by AFG's accomplishment system. The key insight is that tier advancement is a narrative commitment, not just a mechanical reward. A character who accepts Lord tier is accepting that the world will treat them as a lord, with all the obligations, enemies, and complications that entails. Allowing players to decline the tier and take a concrete bonus instead preserves the Conan archetype: the capable wanderer who refuses to be tied down.

**⁶ Luck and the die of fate**
The die of fate is the referee's oracle tool, not a player-facing mechanic. LUC affects it as background radiation, the party's collective fortune slightly tilting outcomes over many rolls. Burned Luck is the player-facing version: a deliberate narrative declaration backed by real mechanical cost. Inspired by Fate RPG's invoke mechanic, but grounded in a stat that fluctuates through carousing, deeds, and jinxes rather than resetting between sessions.

**⁷ Dungeon tiers and open world design**
A dungeon's tier describes its general threat profile and expected reward, not a hard content ceiling. A Tier 1 dungeon is calibrated for Tier 1 parties but the world is not sanitized. Higher tier threats exist inside lower tier dungeons: a Tier 3 guardian placed by the original builders, a Colossal creature that wandered in, an NPC whose true power only becomes apparent gradually. These are not content for later, they are features of a living world.

Parties learn to read the signs. Scratch marks too high on the walls. Bones of things that should have won. A room that smells wrong. They route around, come back stronger, or find a clever solution. A dungeon never fully expires. The Tier 3 party returning to a Tier 1 site finds most of it trivial, but the guardian in the deep room is still there. Now it is a fair fight instead of an impossible one.

The model is FFXII and Xenoblade Chronicles, not an MMO zone system. High-tier threats in low-tier areas are not mistakes or oversights. They are the world communicating that not everything is for you yet.
