# Rune Delver: Player's Guide

---

## How Rolls Work

Three resolution systems, each for its own domain:

- **Combat:** d20 + STR or DEX vs 10 + opponent STAT. Player-facing. Players roll to attack and to defend. Monsters are static numbers.
- **Saving throws:** d20 + relevant stat vs 16.
- **Tasks:** d6, X-in-6 where X is ceil(relevant stat / 2). Skills add +1 to X.

All rolls are **player-facing**. Players roll for themselves, their hirelings, retainers, familiars, and summoned creatures. Monsters never roll.

---

## Character Creation

### 1. Choose a Job
Your job recommends a starting stat spread and grants two starting traits and a gear package. See Jobs below. Your job also determines how you distribute your starting stat points.

### 2. Assign Stat Points
All three stats begin at 1. Your job recommends where to spend 2 additional points. Then assign 1 free point to any stat. No stat may exceed 3 at character creation or 8 over the course of a career.

**Example:** Hunter recommends STR 3 / DEX 1 / WIL 1. That means spend both points on STR, then put the free point into DEX or WIL.

Stats have a derived value **X** equal to ceil(stat / 2), used for task rolls and some trait effects.

### 3. Starting HP
**6 + STR.** A character with STR 1 starts with 7 HP. STR 2 starts with 8 HP. STR 3 starts with 9 HP.

### 4. Record Starting Traits
Your job grants two starting traits. Note them in your Traits section with their subtype tag in parentheses. See Traits below.

### 5. Take Starting Gear
Your job provides a specific gear package. See Jobs below.

---

## Stats

Three stats cover everything a character does.

**STR** covers melee attacks and defense, HP, feats of physical force, and endurance. X used for tasks involving strength, athletics, and physical labor.

**DEX** covers ranged attacks and defense, stealth, speed, and precision. X used for tasks involving agility, sleight of hand, and fine motor control.

**WIL** covers magic (if a spellcasting trait is taken), saves vs mental effects, and knowledge. X used for tasks involving persuasion, lore, and willpower.

Stats increase by 1 at each level up. The maximum stat for a PC is 8.

---

## Combat

### Round Sequence
1. **Declare spells:** characters casting a rune this round announce it before initiative. The spell resolves at the end of the round. Any damage taken before resolution loses the spell and the slot.
2. **Roll initiative:** each side rolls d6. Winning side acts first. Ties resolve simultaneously.
3. **Missiles:** ranged attacks in initiative order.
4. **Movement:** characters move in initiative order.
5. **Melee:** melee attacks in initiative order.
6. **Spells:** declared spells resolve in initiative order.

### Actions
Each round a character may:
- Move 1 zone and take an action: attack, use an item, cast a spell, attempt a task, aid another
- Move 2 zones and take no action

### Attacking
**Melee:** d20 + STR vs 10 + opponent STR

**Ranged:** d20 + DEX vs 10 + opponent DEX

**Defense:** when a monster attacks, the targeted player rolls d20 + STR (melee) or d20 + DEX (ranged) vs 10 + monster STAT. Ties go to the defender. A shield means ties always go to the defender.

### Damage
On a hit, roll weapon die and subtract target DR. Minimum 1 damage.

**A max die roll bypasses DR entirely.** A d6 rolling 6 deals 6 damage regardless of armor.

| Weapon | Die | Hands |
|--------|-----|-------|
| Light (dagger, handaxe) | d4 | 1 |
| Medium (sword, spear) | d6 | 1 |
| Heavy (greatsword, maul) | d8 | 2 |
| Unarmed | d6 | — |

**Dual wield:** add d6 to your attack roll. No effect on damage die.

### Stunts
On a hit, choose: deal damage OR apply a stunt (push, disarm, trip, grab). A natural 20 on an attack lets you do both simultaneously.

### Ranged Combat
Defenders cannot counterattack ranged attackers. Ranged weapons cannot be used in melee and cannot safely target enemies engaged in melee.

**Ammunition:** tracked with 3 bubbles. After each fight involving ranged attacks, roll d6: on 4-6 mark one bubble. When all 3 bubbles are marked, one shot remains. Resupply clears all bubbles.

### Mounted Combat
A mount grants +1 ATK and DEF in melee. A mounted charge, moving at least 1 zone before attacking, grants +2 ATK on the attack.

### Defeat
At 0 HP a character is **defeated:** not automatically dead. The referee determines consequences: capture, unconsciousness, grievous injury.

### Fleeing Melee
A character who flees a melee zone gives opponents a free attack before leaving.

---

## Armor

| Armor | DR | Slots |
|-------|----|-------|
| Light (leather, hide) | 1 | 1 body |
| Heavy (chainmail, plate) | 2 | 2 body |
| Magic armor | 3+ | varies |
| Shield | +1 DR | 1 hand |

Shield DR adds to worn armor. A character in heavy armor with a shield has DR 3.

No armor penalty to DEX. Heavy armor does impede stealth and swimming.

---

## Saving Throws

**Target: 16.** Roll d20 + relevant stat. Meet or beat to succeed.

| Threat | Stat |
|--------|------|
| Poison, disease, physical harm | STR |
| Breath weapons, traps, area effects | DEX |
| Beguilement, fear, compulsion, illusions | WIL |

Failed saves deal **conditions** rather than HP damage. The dungeon leaves a mark that costs time and treasure to address.

---

## Task Resolution

Roll d6 equal to or under **X** (ceil of relevant stat / 2) to succeed.

| Stat | X | Base chance |
|------|---|-------------|
| 1-2 | 1 | 1-in-6 |
| 3-4 | 2 | 2-in-6 |
| 5-6 | 3 | 3-in-6 |
| 7-8 | 4 | 4-in-6 |

A relevant skill trait adds +1 to X. Maximum X is 5-in-6. 6-in-6 is never possible: something always has a chance to go wrong.

### Natural 6
A natural 6 means something went wrong. The referee calls for a saving throw using a contextually relevant stat: not necessarily the same stat used for the task. A failed climb (STR roll) might trigger a DEX save to catch yourself before falling. A botched trap disarm (DEX roll) might trigger a DEX save as it goes off. A failed ritual (WIL roll) might trigger a WIL save against magical backlash.

### Retry
Failed task rolls can usually be retried. Failure costs time or resources rather than ending the attempt permanently. The referee determines what a failure costs before the player retries.

---

## Jobs

Jobs are archetypes that define your starting stat spread, traits, and gear. They are an anchor for character identity, not a cage. Traits and skills can be gained through play regardless of starting job.

**Stat spreads:** all stats begin at 1. Your job recommends where to spend your 2 additional points, then you assign 1 free point anywhere. Jobs with a 3 in one stat spend both points there. Jobs with 2/2/1 splits spend one point in each of two stats.

### Pure Archetypes

---

**Hunter**
*STR 3 / DEX 1 / WIL 1. Free point to DEX or WIL.*

Soldiers, mercenaries, and warriors who solve problems with steel. The toughest fighters on the road.

Starting traits: Warfare (skill), Vicious

Starting gear: Chainmail (DR 2), heavy weapon, torch, bedroll

---

**Delver**
*DEX 3 / STR 1 / WIL 1. Free point to STR or WIL.*

Dungeon specialists: locksmiths, tomb robbers, ruin crawlers. Nobody reads a room like a Delver.

Starting traits: Thievery (skill), Sneak Attack

Starting gear: Leather armor (DR 1), light weapon, lockpicks, 50ft rope, torch

---

**Caster**
*WIL 3 / STR 1 / DEX 1. Free point to STR or DEX.*

Academic magic users who study rune inscriptions and carry spellbooks. Fragile but powerful.

Starting traits: Rune Magic, Arcane Lore (skill)

Starting gear: Spellbook (2 spells), dagger, ink and quill, lantern, dramatic cloak

---

### Hybrid Archetypes

---

**Ranger**
*STR 2 / DEX 2 / WIL 1. Free point to any stat.*

Wilderness fighters: hunters, scouts, outriders. Equally at home with a sword or a bow.

Starting traits: Wilderness (skill), Skirmisher

Starting gear: Leather armor (DR 1), medium weapon, bow, quiver (3 ammo), waterskin

---

**Striker**
*STR 2 / WIL 2 / DEX 1. Free point to any stat.*

Martial artists who channel inner power through discipline and rune technique. Wear no armor: their defense comes from training and awareness.

Starting traits: Rune Magic, Unarmed Strike

Starting gear: Monk's habit, bandages, incense, a coin from a dead master

---

**Noble**
*STR 2 / WIL 2 / DEX 1. Free point to any stat.*

Aristocratic warriors with a scholar's education. Can read and activate scrolls. Fights with finesse rather than brute force.

Starting traits: Warfare (skill), Scroll Use

Starting gear: Leather armor (DR 1), light weapon, scroll case (one readable scroll), signet ring (worthless outside your homeland)

---

**Seeker**
*DEX 2 / WIL 2 / STR 1. Free point to any stat.*

Scholar-delvers who combine dungeon expertise with arcane knowledge. Identifies magic items. Casts spells but not as powerfully as a dedicated Caster.

Starting traits: Arcane Lore (skill), Rune Magic

Starting gear: Leather armor (DR 1), light weapon, map fragment (one known ruin), magnifying glass, notebook

---

**Esper**
*WIL 3 / STR 1 / DEX 1. Free point to STR or DEX.*

Spirit-negotiators who draw power from pacts rather than study. Learns spells by communing with spirits rather than from books. Cannot use scrolls or craft magic items.

Starting traits: Spirit Pact, Wilderness (skill)

Starting gear: Spirit fetish, medium weapon, bundle of incense, small offering bowl, leather armor (DR 1)

---

**Outlaw**
*STR 2 / DEX 2 / WIL 1. Free point to any stat.*

Brigands, smugglers, and criminals. Fighters who know when to hit and when to run.

Starting traits: Thievery (skill), Vicious

Starting gear: Leather armor (DR 1), medium weapon, lockpicks, smoke bomb, wanted notice with your face on it

---

### Job Table (2d6)

Roll randomly or choose freely.

| 2d6 | Job |
|-----|-----|
| 2 | Noble |
| 3 | Esper |
| 4 | Seeker |
| 5 | Outlaw |
| 6 | Ranger |
| 7 | Hunter |
| 8 | Delver |
| 9 | Striker |
| 10 | Hunter |
| 11 | Delver |
| 12 | Caster |

---

## Traits

Traits are the primary source of character differentiation. They cover species heritage, background, job capabilities, martial techniques, and magical traditions. Every trait has a clear described use and can be interpreted at the edges by the referee.

Each trait has a subtype tag in parentheses:

- **(skill):** grants +1 to X on d6 task rolls within the named domain.
- **(genos):** a physical or ancestral trait, usually a permission or fictional capability.
- No tag: a rules exception or permission. Does what it says.

Traits are starting points, not complete definitions. Players can create custom traits with referee approval by describing what they are and what they imply. The trait stays true going forward once established.

**Stacking:** trait bonuses of the same type do not stack. Take the higher value. Bonuses from stats and items stack normally with trait bonuses.

### Skill Traits

**Thievery** (skill): stealth, picking locks, disarming traps, sleight of hand, picking pockets.

**Wilderness** (skill): tracking, foraging, navigation, surviving outdoors, calming animals.

**Warfare** (skill): combat tactics, weapon knowledge, military lore, siege assessment.

**Arcane Lore** (skill): identifying magic, reading ancient scripts, recalling esoteric knowledge.

**Healing** (skill): treating wounds, identifying herbs, diagnosing conditions. Successful treatment during downtime restores 1 HP per STR of the patient.

**Seafaring** (skill): sailing, navigation by stars, weather reading, maritime lore.

**Scholarship** (skill): history, languages, ancient cultures, deciphering texts.

**Streetwise** (skill): urban navigation, criminal contacts, rumors, black markets.

### Combat Traits

**Vicious:** when your damage die rolls maximum, roll it again and add the result. DR applies once.

**Sneak Attack:** when attacking from an unseen position or with a positional advantage, your damage die steps up one size: d4 to d6, d6 to d8.

**Skirmisher:** you can move before and after attacking in the same round, splitting your movement freely.

**Unarmed Strike:** your unarmed attacks deal d6 damage. Armor cannot be worn without losing this benefit.

**Defender:** once per round when an adjacent ally is hit, you may take the damage instead.

**Berserk:** when you take damage that drops you below half HP, your next attack deals damage with advantage. Resets each combat.

### Magic Traits

**Rune Magic:** you may cast spells. Your WIL stat determines your spell slots. Your maximum castable spell level is ceil(WIL/2). Spells are learned from inscriptions, teachers, or research and prepared from a spellbook after rest.

**Spirit Pact:** you may cast spells. Your WIL stat determines your spell slots. You learn spells by negotiating with spirits rather than research. Cannot use scrolls or craft magic items.

**Blood Magic:** you may cast spells by spending HP instead of spell slots at a 2:1 ratio (2 HP per spell level). Requires Rune Magic or Spirit Pact.

**Scroll Use:** you can read and activate magic scrolls. You may attempt to use wands and rods on a 2-in-6 roll.

**Hedge Magic:** you know three cantrips (minor utility effects, no slots required). Cannot learn higher spells without Rune Magic or Spirit Pact.

### Genos Traits

**Ctarl** (genos): you carry the blood of the great cats. Keen senses, a predator's instincts, and claws that deal d4 damage.

**Rito** (genos): hollow bones and vestigial wings let you glide from any height without taking fall damage. Medium or heavy armor grounds you entirely.

**Ronso** (genos): large, powerful, and cold-resistant. You carry 12 inventory slots instead of 10.

**Ygguana** (genos): you are attuned to the Ygg-link. Old-world machines, terminals, and inscriptions sometimes respond to you as if they recognize you.

**Kobold** (genos): small, quick, and difficult to pin down. You move through tight spaces and crowded fights with an ease larger creatures find unsettling.

**Chimera** (genos): you carry traits from more than one lineage. Describe your chimeric qualities with the referee and work out what they imply together.

**Construct** (genos): you are a golem, automaton, or re-awakened machine. You do not need food or sleep but require power cells. Poison and disease do not affect you.

### Background Traits

**Soldier:** you served. Military discipline, tactics, and chain of command are second nature.

**Archivist:** you spent years in formal study. Libraries, inscriptions, and old records are familiar ground.

**Criminal:** you ran with a crew at some point. The tools and habits of that life stuck with you.

**Sailor:** you know the sea. Ships, tides, knots, and port town culture are all familiar territory.

**Tracker:** you grew up in rough country. You read terrain, find food, and stay alive with little.

**Shaman:** you were initiated into a spiritual tradition. Its rites, spirits, and obligations are familiar to you.

**Machinist:** you work with old-world technology. Mechanisms, power cells, and relic devices are familiar ground.

**Performer:** stages, courts, and taverns are your natural habitat.

**Apothecary:** you know how to prepare medicinal and alchemical items in the field given the right materials.

**Houseborn:** you were raised inside a noble household or political structure. Its hierarchies, obligations, and intrigues are second nature.

### General Traits

**Mighty:** your physical power is exceptional. You can attempt feats of force others could not try.

**Quick Reflexes:** you react faster than most. Surprises rarely catch you flat-footed.

**Clever:** your mind is sharp and retentive. Languages, patterns, and old knowledge come easily.

**Hardy:** your body resists sickness and poison with unusual stubbornness.

**Silver-tongued:** people find you naturally persuasive.

**Alert:** you notice things. It is difficult to sneak up on you or hide something in plain sight.

**Slippery:** you cannot be easily grabbed, pinned, or restrained.

**Lucky:** things have a way of breaking in your direction when it counts. Not always. But enough.

**Attuned:** you sense magic, spirits, and old-world signals that others cannot. The referee tells you when something is present, not what it is.

**Magic Resistant:** spells and psychic effects slide off you. This is occasionally a problem.

---

## Inventory

Characters have **10 inventory slots**: 2 hand slots and 2 body slots (included in the 10).

- Conditions occupy slots until treated
- Most small items take less than 1 slot
- Heavy armor impedes stealth and swimming

---

## Conditions

Conditions occupy **inventory slots** until removed. Failed saves, traps, and certain monster abilities deal conditions rather than HP damage. The referee determines what a condition means for a given action in the moment.

| Type | Removed by | Cost |
|------|-----------|------|
| Injury | Healer, surgeon, or rest | 1 treasure/slot |
| Disease | Herbalist or antidote | 1 treasure/slot |
| Curse / hex | Temple or ritual | 1-3 treasure/slot |
| Magical binding | Specific ritual or component | Narrative |

| Severity | Slots | Examples |
|----------|-------|---------| 
| Minor | 1 | Sprained ankle, mild fever, minor hex |
| Major | 2 | Broken bone, serious disease, powerful curse |

---

## Magic

Magic requires a trait: **Rune Magic**, **Spirit Pact**, or **Hedge Magic**. Without one of these traits, WIL governs saves, tasks, and knowledge but generates no spell slots.

### Spell Slots
Spell slots are determined by WIL score. ceil(WIL/2) equals the highest spell level accessible.

| WIL | Max Level | 1st | 2nd | 3rd | 4th |
|-----|-----------|-----|-----|-----|-----|
| 1 | 1 | 1 | | | |
| 2 | 1 | 2 | | | |
| 3 | 2 | 3 | 1 | | |
| 4 | 2 | 4 | 2 | | |
| 5 | 3 | 4 | 2 | 1 | |
| 6 | 3 | 4 | 3 | 2 | |
| 7 | 4 | 4 | 3 | 2 | 1 |
| 8 | 4 | 4 | 3 | 3 | 2 |

Spell slots recover fully after rest.

### Casting
Declare a rune at the start of the round before initiative. It resolves at the end of the round. Any damage taken before resolution loses the spell and the slot.

Resisted spells: roll d20 + WIL vs 10 + monster STAT. Unresisted spells (healing, buffs, utility) simply work.

### Spells Known
Capped by WIL score. A character with WIL 4 can know at most 4 runes.

### Rune Invocations
Each rune has expressions at different spell levels. Higher level slots unlock qualitatively new capabilities, not just bigger numbers.

*Example: BOLT at 1st level strikes one target. At 3rd level it arcs to multiple targets. At 5th level it becomes a zone discharge.*

### Spell Damage
Damaging spells deal d6 per spell level spent and bypass DR entirely.

*[Full rune list and invocations, placeholder. See rune reference.]*

---

## Advancement

No experience points. Advance through **expeditions** and **accomplishments**.

**Level up:** when the referee determines the party has earned a level, each character gains +1 to any stat of their choice.

**HP on level up:** reroll all HD (d6 per level) and add STR to the total. If the result exceeds current HP, that becomes the new HP. If equal or lower, HP increases by 1.

| Tier | Levels | Title |
|------|--------|-------|
| 1 | 1-2 | Adventurer |
| 2 | 3-4 | Hero |
| 3 | 5-6 | Lord |
| 4 | 7-8 | Legend |
| 5 | 9-10 | Mythic |

Tier is descriptive. It affects how the world regards the character and sets the scale of appropriate threats and sites.

---

## Equipment

*[Full equipment list, placeholder. Weapon and armor tables are compatible with Rune Hunter and Rune Master with no conversion needed.]*