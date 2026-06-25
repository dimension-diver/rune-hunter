# Rules Reference

---

# PART 1: PLAYER RULES

## How Rolls Work

Three resolution systems, each for its own domain:

- **Combat** — d20 + FC + STR/AGI, player-facing. Players roll to attack and defend. Monsters are static numbers. See Combat.
- **Saving throws** — d20 + relevant modifier vs 16 − character level. See Saving Throws.
- **Tasks** — d6, default 2-in-6 modified by ability scores and backgrounds. See Task Resolution.
- **Die of Fate** — d6 oracle roll, modified by party LUC. See Luck & the Die of Fate.

All rolls are **player-facing**. Players roll for themselves, their hirelings, retainers, familiars, and summoned creatures. Monsters never roll.

---

## Character Creation

### 1. Roll Ability Scores
Roll 3d6 in order: **STR, AGI, RES, WIS, CHA, LUC**.

Roll each in order. You may swap any two scores once after rolling. If the sum of all modifiers is −3 or worse, you may reroll the entire array.

| Score | Modifier |
|-------|----------|
| 3–6   | −1       |
| 7–14  | 0        |
| 15–18 | +1       |

Modifiers apply to d20 and d6 rolls as noted per stat. The raw score matters too — a 15 Strength and an 18 Strength both give +1, but the referee may allow the 18 to attempt things the 15 cannot (bending iron bars, lifting a portcullis alone). When raw capability is in question, the referee may call for a d20 roll-under the relevant score.

### 2. Choose Background and Type

**Background** — choose or roll 2d6 on the background table. Your background gives you one or two starting talents and a starting equipment package. It establishes who you were before you started adventuring.

**Type** — choose Hunter or Caster. Some backgrounds specify a type; others leave it open. Your type determines your combat chassis: FC progression for Hunters, spell slots for Casters.

### 3. Starting HP
**6 + RES modifier** (minimum 1). After level 1, roll d6 per HD gained.

### 4. Equipment
*[Starting equipment packages — placeholder]*

---

## Ability Scores

| Attribute | Modifier | Used for |
|-----------|----------|----------|
| Strength (STR) | +1 / 0 / −1 | Melee attack and defense rolls, damage bonus, feats of physical power. Raw score determines the ceiling of what can be attempted — STR 15 gets the modifier breaking down a door; STR 18 gets it bending iron bars. |
| Agility (AGI) | +1 / 0 / −1 | Ranged attack and defense rolls, initiative, stealth, speed tiebreakers in chases and duels. AGI bonus negated by medium and heavy armor. |
| Resilience (RES) | +1 / 0 / −1 | Starting HP modifier. Also governs physical and spiritual robustness — RES damage from poison or disease accumulates as conditions; reaching 0 RES is fatal. |
| Wisdom (WIS) | +1 / 0 / −1 | Spell research, languages, knowledge and lore tasks. For Casters, raw WIS score is the maximum number of spells that can be known at once. WIS modifier applies to spell slot recovery and resistance to magical disruption. |
| Charm (CHA) | +1 / 0 / −1 | Reaction rolls, hireling loyalty and morale, social tasks. Also covers mental resilience and spiritual fortitude — CHA modifier applies to saves vs beguilement, fear, and illusions. |
| Luck (LUC) | +1 / 0 / −1 | Applied by the referee to die of fate rolls and certain saves where fortune rather than capability is the deciding factor. LUC can be burned and fluctuates over the campaign. See Luck & the Die of Fate. |

---

## Types

Characters are one of two types: **Hunter** or **Caster**. Your type determines your combat resource progression. Everything else — who you are, what you're good at, how you engage with the world — comes from your background and talents.

### Hunter
- **HD:** d6 per Hunter level
- **FC:** ceil(Hunter levels ÷ 2)

Hunter is the default type for anyone who handles problems without magic — sellswords, rangers, priests of martial orders, cunning delvers, roguish entertainers. The label describes a capability, not a profession.

| Hunter Level | FC |
|--------------|-----|
| 1  | +1 |
| 2  | +1 |
| 3  | +2 |
| 4  | +2 |
| 5  | +3 |
| 6  | +3 |
| 7  | +4 |
| 8  | +4 |
| 9  | +5 |
| 10 | +5 |

Hunters may learn **special techniques** through training, mentorship, or significant experience — extra damage, disarms, called shots, and other martial abilities beyond the base FC progression.

*[Special techniques list — placeholder]*

### Caster
- **HD:** d6 at Caster levels 1, 3, 5, 7, and 9 only
- **FC:** 0 (unless Hunter levels are also taken)
- **Spells known:** capped by raw Intellect score
- **Spell slots** per Caster level:

| Caster Level | 1st | 2nd | 3rd | 4th | 5th |
|---|---|---|---|---|---|
| 1  | 1 | — | — | — | — |
| 2  | 2 | — | — | — | — |
| 3  | 3 | 1 | — | — | — |
| 4  | 4 | 2 | — | — | — |
| 5  | 4 | 2 | 1 | — | — |
| 6  | 4 | 2 | 2 | — | — |
| 7  | 4 | 3 | 2 | 1 | — |
| 8  | 4 | 3 | 3 | 2 | — |
| 9  | 4 | 3 | 3 | 2 | 1 |
| 10 | 4 | 4 | 3 | 2 | 2 |

### Multiclassing
Take levels in both types freely. Hunter levels determine FC. Caster levels determine spell slots. HD from both stack.

---

## Combat

### Round Sequence
Each combat round resolves in the following order:

1. **Declare spells** — any character casting a spell this round announces it before initiative is rolled. The spell resolves at the end of the round. If the caster takes any damage between declaration and resolution (steps 1–6), the spell is lost and the slot is expended with no effect. Artificers are not subject to this rule — gadgets are activated on their turn with no prior declaration.
2. **Roll initiative** — each side rolls d6. Winning side acts first within each phase. Ties are resolved simultaneously.
3. **Missiles** — ranged attacks resolve in initiative order.
4. **Movement** — characters move in initiative order.
5. **Melee** — melee attacks resolve in initiative order.
6. **Spells** — declared spells resolve in initiative order.

### Actions
Each round a character may:
- **Move 1 zone and take an action** (attack, activate a gadget, use an item, attempt a task)
- **Move 2 zones and take no action**

An action is one of: melee attack, ranged attack, activate a gadget, use an item, cast a spell (if declared), attempt a non-combat task, aid another character.

Spellcasters declare their spell at step 1 before knowing initiative. Artificers do not declare — they activate a gadget as their action on their turn, with no interruption risk.

### Initiative and Engagement
The initiative-winning side moves first. A character may move into melee to engage an opponent. If the initiative-losing side then attempts to move out of that melee zone before acting, opponents may make a free attack against them before they leave.

### Attacking
Roll **d20 + FC + STR** (melee) or **d20 + FC + AGI** (ranged) vs **10 + monster FC**.

Players may use STR or AGI for melee defense depending on how they describe it — bracing uses STR, ducking and weaving uses AGI.

A player may choose **static defense** instead of rolling — treat defense as a fixed 10 + FC + AGI bonus, or 10 + FC + 1 if using a shield and no AGI bonus applies. AGI bonus is negated by medium and heavy armor. Static defense cannot be used to flee melee. Useful when delegating rolls for hirelings, retainers, familiars, or summons.

- **Hit:** roll weapon damage (armor save applies)
- **Miss:** no effect
- **Natural 20 on attack:** critical hit
- **Natural 20 on defense:** free counterattack this round
- **Natural 1 on defense:** monster crits you

### Weapons
| Option | Effect |
|--------|--------|
| One-handed weapon | Standard damage die |
| Two-handed weapon | Step up damage die (d4→d6, d6→d8) |
| Dual wield (two one-handed weapons) | +1 ATK; roll damage die of either weapon |
| Shield | +1 DEF if no AGI bonus; negated by medium/heavy armor |

### Ranged Combat
Uses AGI. Defenders cannot counterattack ranged attackers. Ranged weapons cannot be used in melee and cannot safely target enemies engaged in melee. A failed ranged attack simply misses — no consequence to the attacker.

### Ammunition
Ammo is tracked abstractly with **3 bubbles**. At the end of each fight involving ranged attacks, roll d6:
- **4–6:** mark one bubble
- **1–3:** no mark

When all 3 bubbles are marked, the character has **one shot remaining**. Resupply clears all bubbles (costs less than 1 treasure for standard ammo).

**Rare or specialist ammo** (relic firearms, specialty arrows) marks a bubble on **3+** instead of 4+, reflecting scarcity.

All ranged weapon types use this system: bows, crossbows, slings, firearms, and thrown weapons.

### Mounted Combat
A mount grants +1 ATK and DEF in melee. A mounted charge — moving at least 1 zone before attacking — grants +2 ATK on the attack. Mounts may be targeted separately by attackers. Heavy terrain may negate mounted bonuses at referee discretion.

### Damage & Armor Save
When a hit lands, roll the weapon die + damage modifier. Compare the **total** to the target's armor rating:

- Total ≤ armor rating → **0 damage**
- Total > armor rating → **full damage (die result + modifier)**

Damage modifiers (STR, magic weapons, talents) raise the floor of the damage roll, making low results less likely to be stopped. A magic weapon against mundane armor will rarely be blocked. Mundane weapons against magic armor will rarely penetrate.

### Critical Hits
**Natural 20 on attack** — always penetrates armor:
1. Deal max die + damage modifier
2. Roll the weapon die again, add modifier
3. Both components bypass armor

*Example: greatsword d8, STR+1. Crit deals 8+1=9, then rolls d8 again +1. Total: 10–17.*

### Monster Critical Hits
**Natural 1 on defense** — the monster crits. Apply the same procedure to the monster's attack.

### Natural 20 on Defense
Deflects the attack and grants a **free counterattack** immediately.

### Shield
No armor rating. Grants **+1 DEF** when the character has no AGI modifier bonus. AGI bonus is negated by medium and heavy armor — the shield bonus applies instead if carried in those cases.

### Stealth Attacks
Any character attacking from stealth or an undetected position gains **+2 ATK** and deals **maximum weapon damage**. Maximum damage always exceeds mundane armor — the precision of the strike finds a gap. Stealth is lost after the attack regardless of outcome.

### Defeat
At **0 HP** a character is defeated — not automatically dead. The referee determines narrative consequences: capture, unconsciousness, grievous injury, etc.

### Fleeing Melee
A character who attempts to flee a melee zone gives opponents a **free attack** before leaving. Static defense cannot be used to flee. The flee attempt itself may require a roll at referee discretion.

---

## Weapons & Damage

| Weapon | Die | Notes |
|--------|-----|-------|
| Unarmed | d4 | — |
| Dagger / light weapon | d4 | — |
| Sword / medium weapon | d6 | — |
| Greatsword / heavy weapon | d8 | Two-handed |
| Martial artist (unarmed) | 2d4 | Each die checked against armor individually |

**Damage bonus** comes from STR, magic weapons, and special techniques. FC does not add to damage.

**Martial artist 2d4:** roll both dice. Each die exceeding the armor rating deals its result + bonus. Each die equal to or under the rating deals 0. Both can penetrate, neither can, or one of each.

**Spell damage** bypasses armor entirely — see Magic Rules.

---

## Armor

Armor has a **rating**. When a hit lands, roll the weapon die + damage modifier and compare the **total** to the armor rating. Totals equal to or under the rating deal 0 damage. Totals above deal full damage.

| Armor | Rating | Slots | Treasure | Restrictions |
|-------|--------|-------|----------|--------------|
| Light (leather, hide, mesh) | 1 | 1 body | 1 | — |
| Medium (mail, brigandine) | 2 | 1 body | 2 | No stealth |
| Heavy (full plate, relic suit) | 3 | 2 body | 3 | No stealth, no swimming |
| Magic armor | 4+ | varies | 5+ | — |
| Shield | — | 1 hand | 1 | +1 DEF if no AGI bonus |

**Base penetration rates (no damage modifier):**

| Die | Rating 1 (light) | Rating 2 (medium) | Rating 3 (heavy) | Rating 4 (magic) |
|-----|-----------------|-------------------|------------------|------------------|
| d4  | 25% blocked | 50% blocked | 75% blocked | 100% blocked |
| d6  | 17% blocked | 33% blocked | 50% blocked | 67% blocked |
| d8  | 12.5% blocked | 25% blocked | 37.5% blocked | 50% blocked |

Each +1 damage modifier overcomes one armor rating tier. A +2 modifier means a d4 always penetrates medium armor. A magic weapon (+3) against mundane heavy armor is almost never blocked.

AGI modifier to defense is negated by medium and heavy armor. Shield grants +1 DEF only when no AGI bonus applies.

**Magic armor** raises the rating beyond the mundane ceiling of 3:

| Rating | Source | Rarity |
|--------|--------|--------|
| 4 | Magic +1 | Uncommon |
| 5 | Magic +2 | Rare |
| 6 | Magic +3 | Legendary |

---

## Saving Throws

**Target: 16 − total character level.** Roll d20 + relevant modifier. Meet or beat to succeed.

| Threat | Attribute |
|--------|-----------|
| Poison, disease, physical harm | RES |
| Breath weapons, area effects | AGI |
| Beguilement, fear, illusions | CHA |
| Magical compulsion, death effects | RES or CHA (referee's call) |
| Fortune-dependent outcomes | LUC (referee's call) |

Race, background, or acquired abilities may add +1 or +2 to specific saves.

---

## Task Resolution

Default **2-in-6**. Roll d6, result equal to or under the target succeeds.

| Relevant modifier | Chance |
|-------------------|--------|
| −1 | 1-in-6 |
| 0  | 2-in-6 |
| +1 | 3-in-6 |

Relevant skill, background, or race: +1 per applicable trait. Skills improved through downtime or accomplishment can stack to +2 or higher.

---

## Advancement

RD uses no experience points. Characters grow through **plundering** and **accomplishments**.

---

### Expeditions

Characters gain an incremental reward whenever their party completes a significant objective at a site or in a situation rated at or above the party's current level. What counts as a significant objective depends on context — the referee recognizes it when it happens.

Examples of equivalent qualifying objectives:
- Recovering a relic or treasure from a dangerous site
- Slaying or driving off a significant threat
- Rescuing a captive from an enemy stronghold
- Completing a major commission, heist, or infiltration
- Resolving a dangerous situation through wit, negotiation, or cunning

The throughline is meaningful risk in pursuit of a clear goal, successfully resolved. The reward is chosen or assigned by the referee from the incremental rewards list below.

Normal advancement halts at the top level of each tier. To cross into the next tier, a character must complete a tier-unlocking Accomplishment.

---

### Incremental Rewards

Awarded for plundering, clever play, partial success, meaningful contribution, or noteworthy individual action. The referee assigns the most fictionally appropriate reward.

| Reward | Notes |
|--------|-------|
| +1 HP | Permanent. No maximum. |
| +1 FC | Hunters only. Advances the FC track. |
| +1 spell slot | Casters only. Any tier already accessible. |
| +1 to a d6 task roll | Specific task or category — tracking, lockpicking, etc. Can stack to +2 or higher through repeated training or accomplishment. |
| +1 to a stat | Referee determines appropriate stat or player makes a case. Crossing a modifier threshold applies immediately. |
| +1 to a specific save | Permanent. Tied to the nature of what was survived or overcome. |
| New talent | Requires fictional justification — training, mentorship, transformative experience. |

---

### Tiers

Tiers represent the scale at which a character operates in the world — not just their power, but their reputation, reach, and the kind of problems they face and create.

Crossing a tier boundary requires completing an **Accomplishment** of appropriate magnitude. The reward for an Accomplishment is a choice: **unlock the next tier** or **gain a concrete bonus** (see Accomplishment Rewards below). A player may decline the tier advance and take the bonus instead — becoming a lord is optional.

| Tier | Levels | Title | Scale |
|------|--------|-------|-------|
| 1 | 1–3 | Adventurer | Starting out. Unknown. Survives through luck and grit. |
| 2 | 4–6 | Hero | Local reputation. People know the name. Capable of deeds that matter regionally. |
| 3 | 7–9 | Lord | Regional power. Commands resources, followers, or territory. The world bends around them. |
| 4 | 10–12 | Legend | Continental scale. Name and deeds will outlive them. History is being made. |
| 5 | 13–15 | Mythic | Normally NPCs only. Godlike or near-godlike. The Saurons and Ultimacias of the setting. Requires referee permission to play. |

---

### Accomplishments

An Accomplishment is a deed of sufficient magnitude to mark a genuine change in who the character is and how the world regards them. They are not pre-assigned — they emerge from the sandbox. The referee recognizes when a deed qualifies and frames the choice.

Each Accomplishment has two parts: the deed, and the reward offered. The reward is always a choice between unlocking the next tier or a concrete bonus.

**Accomplishment Rewards (choose one):**
- Unlock next tier
- +1d6 HP
- +1 to a stat of choice
- +1 FC (Hunters)
- +1 spell slot at any accessible tier (Casters)
- +1 to all saves of a specific type
- A significant talent or ability appropriate to the deed

---

### Example Accomplishments

The following are suggestions. Actual Accomplishments emerge from the campaign. These exist to calibrate the referee's sense of what qualifies.

**Tier 1 → Tier 2 (Adventurer → Hero)**
- Recover a significant relic of the ancients and return it to a community that needs it / Unlock Hero tier or +1 to a stat of choice
- Defeat a threat that has terrorized a region and earn its gratitude / Unlock Hero tier or +1d6 HP
- Establish a lasting alliance between two factions previously in conflict / Unlock Hero tier or +1 to all PER-based rolls
- Survive and return from a site that others have entered and not come back from / Unlock Hero tier or +1 to saves vs fear and death

**Tier 2 → Tier 3 (Hero → Lord)**
- Claim a seat of power — fortress, tower, guild hall, syndicate — and hold it / Unlock Lord tier or +1d6 HP
- Overthrow a regional power and choose what rises in its place / Unlock Lord tier or +1 to a stat of choice
- Complete a pilgrimage or quest of legendary difficulty / Unlock Lord tier or +1 to all saves
- Earn the permanent service of a powerful NPC, spirit, or faction / Unlock Lord tier or new significant talent

**Tier 3 → Tier 4 (Lord → Legend)**
- Conquer or liberate a city; reshape a nation / Unlock Legend tier or +1 to a stat of choice
- Destroy or seal something that has threatened the world for generations / Unlock Legend tier or +1d6 HP
- Found an order, institution, or dynasty that will outlast you / Unlock Legend tier or +2 to a stat of choice
- Make a bargain with or defeat a being of mythic power / Unlock Legend tier or significant magical ability

---

### A Note on Tier Advancement

The tier system is not a ladder players must climb. A character can reach the mechanical ceiling of Tier 1 and remain there indefinitely, growing through incremental rewards, accumulating talents, becoming the best version of a capable adventurer without ever becoming a regional power.

The choice to advance a tier is a narrative commitment as much as a mechanical one. Accepting Lord tier means accepting that the world will treat you as a lord — with everything that entails. Rejecting it and taking the concrete bonus instead is a legitimate and interesting choice. Conan sacks a city and walks away richer and harder. The throne can wait.

---

## Inventory & Slots

Characters have **10 inventory slots**: 2 hand slots and 2 body slots (included in the 10).

- Conditions (injuries, curses, diseases) occupy slots until treated
- Heavy armor impedes stealth and swimming
- Most small items take less than 1 slot; the referee may group several as 1 slot

---

## Conditions

All conditions occupy **inventory slots** until removed and cost **treasure** to treat.

| Type | Removal | Cost |
|------|---------|------|
| Injury | Healer, surgeon, or proper rest | 1 treasure per slot |
| Disease | Herbalist, alchemist, specific antidote | 1 treasure per slot |
| Curse / hex | Temple, priest, or ritual | 1–3 treasure per slot |
| Jinx | Spirit appeasement, quest, or powerful intercession | Varies — narrative hook |
| Magical binding | Specific ritual, quest, or component | Varies — narrative hook |

**Severity:**

| Severity | Slots | Examples |
|----------|-------|---------|
| Minor | 1 | Sprained ankle, minor hex, mild fever |
| Moderate | 2 | Broken bone, disease, moderate curse |
| Severe | 3 | Crippling wound, wasting sickness, powerful curse |
| Catastrophic | 4+ | Lost limb, death curse, soul binding |

Conditions may impose situational penalties at referee discretion — a broken arm imposes −1 on attack rolls, a hex of misfortune −1 on saves. Keep penalties simple and tied to the nature of the affliction.

### Ability Damage

Some conditions deal direct damage to ability scores rather than (or in addition to) occupying slots. Track the current score separately from the base score. Modifiers update immediately when a score crosses a threshold.

**Injury** — severe physical trauma may deal 1d6 STR damage. The score does not recover until the condition is treated. Losing a STR modifier through injury is meaningful — the character loses the fictional warrant that came with it.

**Poison** — deals 1d6 RES damage on a failed save. Each day without treatment, make another RES save (target set by poison quality) or take another 1d6 RES damage. The score recovers once the poison condition is removed.

**Jinx** — a spiritual affliction from desecrating a shrine, offending a spirit, or drawing supernatural misfortune. Deals 1d6 LUC damage. Cannot be treated with treasure alone — requires appeasement of the offended spirit, a quest, or intercession from a powerful Shaman or Esper. Some Jinxes are minor and fade with time; others are persistent curses.

**Stat zeroing:**

| Stat | Effect at 0 |
|------|-------------|
| STR | Cannot act physically; helpless |
| AGI | Cannot move under own power |
| RES | Dead |
| WIS | Catatonic; cannot think or speak |
| CHA | Mentally broken; under referee control |
| LUC | Cosmically cursed; die of fate always goes worst possible way until LUC recovers above 0 |

---

## Luck & the Die of Fate

The **die of fate** is the referee's oracle tool — a d6 rolled when the answer to a question depends on circumstance rather than character capability.

*Is there a guard at this post? Is the door unlocked? Does the torch last long enough? Does the fleeing NPC make it to safety?*

**Base die of fate:**
- 1–3: unfavorable outcome
- 4–6: favorable outcome

The referee may adjust the range based on context — a very likely outcome might only fail on a 1, an unlikely one might only succeed on a 6.

**Luck modifier:** the referee applies the relevant character's LUC modifier (or the average of the party's LUC modifiers for group-affecting rolls) to die of fate results. A party with combined LUC +1 finds the world slightly more cooperative. A party with combined LUC −1 finds things don't break even for them.

### Burning Luck

A player may **burn Luck** — permanently reducing their LUC score — to invoke a die of fate outcome directly, without rolling. This is a narrative declaration backed by real cost: *my character is lucky, the door is unlocked, the guard is asleep.*

- Each burn reduces LUC by 1 permanently (until recovered through downtime or deeds)
- Crossing a modifier threshold through burning has immediate effect
- A character who burns LUC to 0 is cosmically cursed until it recovers

Burning Luck is deliberate and irreversible in the moment. Use it for outcomes that matter.

### Luck Recovery

LUC is a dynamic stat — it fluctuates over the course of a campaign.

**Downtime:** LUC recovers 1d3 points per week of rest and recuperation, up to the character's rolled starting score.

**Deeds:** significant accomplishments, acts of bravery, or completion of meaningful quests may restore LUC at the referee's discretion. Fortune favors the bold.

**Carousing:** see Downtime. Carousing has a chance to restore or reduce LUC — you're gambling with fate.

**Above starting score:** LUC can exceed its rolled value through exceptional deeds and fortune. There is no hard ceiling — a character who has earned remarkable luck may find it extends into legendary territory (LUC 18+), where the referee applies the modifier more liberally and to more favorable situations.

**Jinx condition:** reduces LUC by 1d6. Requires narrative resolution to remove — not just treasure.

---

---

# PART 2: MAGIC RULES

## Spellcasting

Casters memorize spells from their spellbook and cast from memory. A cast spell is expended until the caster rests and re-memorizes.

---

## Spell Damage

Damaging spells deal **d6 per spell level** (or as specified). Spell damage bypasses armor entirely. Magic armor may protect against spells at the referee's discretion — reserved for significant magic items.

---

## Spell Lists

*[Full spell lists by level — placeholder. Whitebox/B/X lists are the baseline.]*

---

## Spell Research & Scrolls

Full rules for spell research, scroll scribing, and magic item creation are in **Part 7: Downtime**.

---

---

# PART 3: REFEREE RULES

## Encounters

Surprise, reaction rolls, and morale use standard B/X/OD&D procedures.

**Surprise:** standard B/X (2-in-6 chance, surprised side loses a round).
**Reaction rolls:** 2d6 + CHA modifier of party spokesperson, standard B/X table.
**Morale:** standard B/X morale checks when monsters take significant losses or face overwhelming odds.

---

## Dungeon Exploration

Dungeon exploration uses standard OSR **turns** (approximately 10 minutes each).

Each turn the party may:
- Move to an adjacent area and search it
- Attempt a specific action (pick a lock, search for secret doors, disable a trap, rest)
- Rest (recover 1d4 + RES modifier HP, minimum 0; requires a full turn with no threats or interruptions)

After every 3 turns, roll for a **wandering encounter** (2-in-6 chance).

**Light** must be tracked. A torch lasts 6 turns. Lanterns last longer but consume oil.

---

## Excursion Sites

The basic unit of dungeon design is the **excursion site** — a self-contained area of 6 rooms.

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

Rooms 5–6 are **landmarks** — neither punish nor reward, but provide atmosphere and lore.

### Treasure per Site
Approximately equal to the sum of combative NPC HD in the site. Two HD 4 encounters = roughly 8 treasure distributed across rooms.

---

## Dungeon Structure

A dungeon is made up of linked excursion sites equal to its **level**.

| Dungeon Level | Sites | Approx. Rooms | Expected Treasure |
|---|---|---|---|
| 1 | 1 | 6 | 4–8 |
| 2 | 2 | 12 | 8–15 |
| 3 | 3 | 18 | 12–24 |
| 5 | 5 | 30 | 20–40 |
| 10 | 10 | 60 | 40–80 |

The dungeon's primary boss lives in the deepest or most protected site. Clearing the main objective triggers a **level-up** for a party of appropriate level.

**Monster HD ≈ treasure value.** A HD 10 dragon hoards roughly 10 treasure — more if long-established, less if a recent occupant.

---

## Combat Zones

Zones are defined by the referee based on terrain and fiction — a room might be one zone, a large hall two or three. See the Combat section in Part 1 for movement rules.

---

## Overland Travel

Travel is measured in **hexes** (approximately 6 miles each).

**Base rate:** 1 hex per day on foot.
**Mounted:** 2 hexes per day in open terrain; reduced or no benefit in difficult terrain.

### Encounter Rolls
Roll d6 at the end of each hex. Result equal to or under terrain difficulty = encounter.

| Terrain | Encounter Chance |
|---------|-----------------|
| Plains / road | 1-in-6 |
| Forest / hills | 2-in-6 |
| Mountains / swamp | 3-in-6 |
| Ruins / blighted land | 4-in-6 |

Apply a reaction roll to all encounters — not every encounter is hostile.

---

## Supplies & Rations

**1 ration** = 1 inventory slot = feeds 1 character for **7 days**.

Running out of rations requires foraging (task roll, difficulty by terrain) or the party begins suffering conditions at the referee's discretion.

---

## Hirelings & Retainers

Standard B/X hireling and retainer rules apply. Treasure value conversions:

| B/X cost | Treasure equivalent |
|----------|-------------------|
| 1–5 gp/month | < 1 treasure |
| Common hireling (torchbearer, porter) | 1 treasure/month |
| Skilled hireling (guard, guide) | 2 treasure/month |
| Specialist (sage, engineer, healer) | 3+ treasure/month |
| Retainer share of treasure | Standard B/X share rules |

Loyalty and morale use standard B/X procedures modified by CHA.

---

## Treasure & Magic Items

### Treasure Scale

| Value | Examples |
|-------|---------|
| 1 | Bag of coins, basic tools, light armor, thieves' tools, 1 week downtime |
| 2 | Heavy armor, quality weapons, hireling for a month |
| 3 | Minor magic item, ship passage, bribing an official |
| 5 | Magic weapon or armor, small building |
| 10 | Significant magic item, manor, small military retinue |
| 20+ | Legendary artifact, keep, noble title |

**1 treasure = 1 week of downtime** per character (lodging, food, resupply).
A party of 4 burns **4 treasure per week** between adventures.

### Physical Weight of Treasure
- Coins, bulky goods: 1 slot per treasure value
- Gems, jewelry, art: 1 slot per 2–3 treasure value
- Magic items: 1 slot regardless of value

### Magic Weapons
Add to **damage bonus only** — not to FC rolls. Bonus applies only on penetrating hits.

### Firearms
Relic pistols and rifles **ignore mundane armor** — the armor save does not apply. Magic armor still provides its rating against firearms. This makes firearms powerful but their scarcity, cost, reload requirement, and noise balance their use.

### Magic Armor
Raises armor rating beyond the mundane maximum of 3. Rating 4 is uncommon, rating 6 is legendary.

### Buying & Selling Magic Items
Not a casual transaction. Finding a buyer or seller requires downtime, contacts, and often travel. Expect 50–75% of treasure value when selling; full value or above when buying. Treat as dealing with private collectors, not a shop.

---

## Dungeon & Wilderness Design

*[Faction design, hex stocking, regional procedures — placeholder]*

---

---

# PART 4: MONSTER RULES

## How Monsters Work

Monsters use the same core stats as PCs. Players roll all dice — monsters are static numbers. This applies to hirelings, retainers, familiars, and summoned creatures as well: the player rolls for them, using the creature's FC as the bonus.

- **HD:** d6. Average HP = HD × 3.5.
- **FC:** ceil(HD ÷ 2). Named monsters and bosses may use HD directly. A monster's FC is always expressed as a static target — players roll against **10 + monster FC** to hit or defend.
- **Defense:** players roll d20 + FC + STR/AGI vs **10 + monster FC**.
- **Armor:** rating 0–3 from natural hide, scales, etc.
- **Attacks per round:** most monsters get 1. Multiple attacks is the primary threat lever for bosses.
- **Damage bonus:** not assigned by default. Give explicitly to named monsters or those with exceptional strength.

---

## Reading a Monster Entry

```
MONSTER NAME
HD: X    FC: +X   Armor: X   Move: X   Attacks: X/round
Damage: die [+ bonus]
Special: [abilities]
Morale: X
Treasure: X
Notes: [behavior, habitat]
```

---

## Monster List

*[Full monster list — placeholder]*

### Sample Entries

---

**GOBLIN**
HD: 1    FC: +1   Armor: 1   Move: 30'   Attacks: 1
Damage: d4
Morale: 6   Treasure: 1
Notes: Cowardly alone, bold in numbers. Flee when half their group falls.

---

**ORC**
HD: 1    FC: +1   Armor: 1   Move: 30'   Attacks: 1
Damage: d6
Morale: 8   Treasure: 1
Notes: Aggressive. May serve a warchief with higher HD.

---

**OGRE**
HD: 4    FC: +2   Armor: 1   Move: 30'   Attacks: 1
Damage: d8
Special: On a nat 1 defense roll, target is knocked prone and loses next action in addition to crit.
Morale: 9   Treasure: 4
Notes: Dim but dangerous.

---

**GIANT**
HD: 8    FC: +4   Armor: 2   Move: 40'   Attacks: 2
Damage: d8+4 (exceptional STR)
Special: Can split attacks between different adjacent targets. Throws boulders at range (d8+4).
Morale: 10   Treasure: 8
Notes: Boulders use ranged rules — no defense roll, AGI save for half.

---

**DRAGON (HD 10)**
HD: 10    FC: +5   Armor: 2   Move: 40' / 80' fly   Attacks: 3
Damage: d8 (claws ×2, bite ×1)
Special: Breath weapon (see dragon entry). Highly intelligent.
Morale: 10   Treasure: 10+
Notes: Breath weapon is the primary threat. 3 melee attacks makes direct engagement costly even without it.

---

*[Remaining monster entries — placeholder]*

---

## Designing Monsters

- **Mooks** (1–2 HD): FC +1, 1 attack/round, d4–d6, Armor 0–1. Die fast; threaten through numbers.
- **Threats** (3–6 HD): FC +2 to +3, 1–2 attacks/round, d6–d8, Armor 1–2. Challenge mid-level parties.
- **Bosses** (7+ HD): FC +4+, 2–3 attacks/round, special abilities, Armor 2–3. Multiple attacks per round is the primary danger lever.
- Named monsters may use HD directly as FC rather than ceil(HD/2).
- Armor rating 3 on a mundane creature is rare — reserve for legendaries.
- **Treasure ≈ HD.** Use HD as a ceiling; let fiction adjust.
- Monster threat comes primarily from special abilities, spells, terrain, and tactics — not raw FC.

---

---

# PART 5: EQUIPMENT

## Equipment List

Prices in **treasure value**. Items below 1 treasure may be grouped — "1 treasure of supplies" covers several small items.

### Weapons

| Weapon | Damage | Slots | Treasure | Notes |
|--------|--------|-------|----------|-------|
| Unarmed | d4 | — | — | — |
| Dagger / knife | d4 | 1 | <1 | Concealable; thrown uses AGI |
| Short sword / hand axe | d4 | 1 | <1 | Thrown axe uses STR |
| Sword / saber / mace | d6 | 1 | <1 | — |
| Spear | d6 | 1 | <1 | Brace action: +2 ATK vs mounted charge |
| Staff | d6 | 1 | <1 | Two-handed |
| Greatsword / greataxe | d8 | 1 | 1 | Two-handed; native d8 die |
| War hammer / maul | d8 | 1 | 1 | Two-handed |
| Bow | d6 | 1 | 1 | Ranged; needs quiver (1 slot) |
| Crossbow | d8 | 1 | 1 | Ranged; reload costs action (fires every other round) |
| Throwing knife / dart | d4 | <1 | <1 | Ranged; AGI; 3 per slot |
| Pistol (relic) | d6 | 1 | 3 | Ranged; ignores mundane armor; reload; ammo scarce |
| Rifle / carbine (relic) | d8 | 1 | 5 | Ranged; ignores mundane armor; reload; ammo scarce |
| Energy blade (relic) | d8 | 1 | 5 | Bypasses mundane armor |

### Armor

| Armor | Rating | Slots | Treasure | Notes |
|-------|--------|-------|----------|-------|
| Shield | — | 1 hand | 1 | +1 DEF if no AGI bonus |
| Light armor | 1 | 1 body | 1 | — |
| Medium armor | 2 | 1 body | 2 | No stealth |
| Heavy armor | 3 | 2 body | 3 | No stealth, no swimming |
| Relic light suit | 1 | 1 body | 3 | May have additional properties |
| Relic heavy suit | 3 | 2 body | 5 | May have additional properties |

### Adventuring Gear

| Item | Slots | Treasure | Notes |
|------|-------|----------|-------|
| Rations (1 week) | 1 | 1 | Feeds 1 character 7 days |
| Torch (3) | 1 | <1 | 6 turns each |
| Lantern | 1 | <1 | Longer burn; needs oil |
| Oil flask | 1 | <1 | Fuel or improvised weapon |
| Rope (50') | 1 | <1 | — |
| Grappling hook | 1 | <1 | — |
| Crowbar | 1 | <1 | +1 to relevant strength tasks |
| Lockpicks / thieves tools | 1 | 1 | Required for lock tasks |
| Healing herbs / poultice | 1 | 1 | Treat 1 minor injury (1 slot) in the field; injuries only, not curses or disease |
| Antitoxin | <1 | 1 | +2 to saves vs poison/disease |
| 10' pole | 1 | <1 | — |
| Chalk / charcoal | <1 | <1 | — |
| Mirror (small) | <1 | <1 | — |
| Tent (2-person) | 1 | <1 | — |
| Bedroll | 1 | <1 | — |
| Pack / backpack | — | <1 | Required to use general slots |
| Saddlebag | — | <1 | +4 slots while mounted |
| Healer's kit | 1 | 1 | Required to treat injuries in the field |
| Surgical tools | 1 | 2 | Treat moderate injuries without full facilities |
| Spellbook (blank) | 1 | 1 | Required for casters |
| Scroll (any spell) | <1 | 1–3 | Single use; cost by spell level |
| Relic power cell | <1 | 1 | Fuel for relic tech; scarce |
| Relic data tablet | 1 | 2 | May contain maps, schematics, or lore |
| Climbing kit | 1 | 1 | +1 to climbing tasks |
| Disguise kit | 1 | 1 | +1 to relevant deception tasks |

### Mounts & Transport

| Item | Treasure | Notes |
|------|----------|-------|
| Horse (riding) | 2 | 2 hexes/day on plains |
| Horse (war) | 3 | 2 hexes/day; combat trained |
| Mule / pack animal | 1 | 1 hex/day; carries 10 slots |
| Relic vehicle (ground) | 5+ | 3+ hexes/day on roads; needs fuel |
| Relic vehicle (air) | 10+ | Fast; very rare; needs fuel |
| Boat | 3 | River/coastal |
| Ship | 10+ | Ocean; needs crew |

### Services

Condition treatment costs here match the Conditions section in Part 1. Healing herbs (above) can treat minor injuries in the field without requiring a service.

| Service | Treasure | Notes |
|---------|----------|-------|
| 1 week lodging & resupply | 1 | Per character |
| Injury treatment (per slot) | 1 | Healer or surgeon |
| Curse/hex removal (per slot) | 1–3 | Temple or priest |
| Disease treatment (per slot) | 1 | Herbalist or alchemist |
| Hireling, common (per month) | 1 | Porter, torchbearer, guard |
| Hireling, skilled (per month) | 2 | Guide, interpreter, specialist |
| NPC spellcasting (per level) | 1–2 | Rare outside cities |
| Relic tech repair | 2–5 | Requires technician; parts extra |
| Passage, short | 1 | — |
| Passage, long | 2–3 | — |

---

---

# PART 6: DUNGEON STOCKING

================================================================================
                         DUNGEON STOCKING TABLES
================================================================================

These tables work within the excursion site framework. The aesthetic is
living fantasy built on a forgotten technological past — not ruins and
wasteland, but a world that has mythologized and grown around things it no
longer understands. Ancient mechanisms are holy relics or dangerous curiosities.
Old words on walls are scripture. Working machines are miracles.

================================================================================
                         ROOM 2: NPCs WITH TREASURE
================================================================================

Roll d10. Adjust HD to match dungeon level.

d10  ENCOUNTER                                    TREASURE TYPE
---  ------------------------------------------- ---------------------------
 1   Mercenary company holding the site for a      Pay chest, promissory
     patron who hasn't returned                    documents, employer's seal
 2   A scholar and hired guards, here to study     Research notes, instruments,
     something specific — not pleased to see you   payment from their patron
 3   Bandits using the site as a base              Stolen goods, coin, weapons
 4   A pilgrim cult that has claimed the site      Cult offerings, donated
     as sacred — armed and sincere                 wealth, ritual objects
 5   A beast in its den, territorial               Prey remains, objects
                                                   dragged in as nesting
 6   A warlord chieftain whose authority derives   Trophy weapons, tribute
     partly from old-world relics on their person  collected from followers
 7   A guardian — mechanical, ancient, still        The site's own holdings;
     executing original function                   what it was built to protect
 8   A spirit bound to a place or object here      Whatever it was bound to
     who manifests as hostile to intruders         protect or commemorate
 9   A merchant who has set up inside for          Trade goods, coin, maps,
     safety — doing brisk business with locals     information for sale
10   A noble's agent, here on undisclosed          Agent's commission, sealed
     business, with professional muscle            documents, quality gear

================================================================================
                         ROOM 3: NPCs WITHOUT TREASURE
================================================================================

Roll d10.

d10  ENCOUNTER                                    HOOK
---  ------------------------------------------- ---------------------------
 1   Pilgrims who got lost in the deeper           Need guidance out; have
     passages — genuinely devout, not dangerous    heard things in the dark
 2   A rival party of adventurers                  Competition, alliance,
                                                   or betrayal depending on
                                                   how this goes
 3   A hermit who has lived here for years         Knows the site intimately;
     by choice — suspicious of visitors            eccentric but not hostile
 4   An animal pack that has moved in              Not aggressive unless
                                                   cornered; knows the layout
                                                   instinctively
 5   A local militia patrol, here because          Jurisdiction question;
     something came out of this site last week     not hostile but suspicious
 6   A ghost or remnant — the echo of someone      Carries information about
     who died here, not fully gone                 the site's past; has a
                                                   request
 7   An apprentice scholar, separated from         Their master is somewhere
     their master, frightened                      deeper; useful ally if
                                                   steadied
 8   Someone seeking the same objective            Their agenda may align
     as the party, already inside                  or conflict; unclear yet
 9   A functioning guardian, dormant until         Activates on specific
     triggered — not yet aware of the party        conditions the party
                                                   may accidentally meet
10   A figure from local legend, recognizable      Their presence here is
     — somehow real and present                    significant; they know it

================================================================================
                         ROOM 4: TREASURE WITHOUT NPCs
================================================================================

Roll d10.

d10  TREASURE                                     COMPLICATION
---  ------------------------------------------- ---------------------------
 1   Coin and portable valuables hidden here       Concealed; takes a turn
     by someone who didn't come back               to find without a clue
 2   A sealed vessel or reliquary — old,           Requires specific knowledge
     clearly significant, clearly sealed           or tool to open safely
 3   Alchemical or medicinal stores, preserved     Fragile; some unstable;
     from another age                              labels in old script
 4   A weapon cache, quality arms                  Heavy; 1 slot each; 2d6
                                                   pieces; some unusual makes
 5   Artworks — carvings, weavings, records        High value; bulky; some
     made beautiful                                depict things no one
                                                   living remembers
 6   Components of something larger — parts        Inert alone; a scholar
     that belong together, currently apart         could say what they are
 7   A library: physical texts, inscribed          Treasure 1-2 in sellable
     tablets, preserved records                    knowledge; may hold a
                                                   spell or technique
 8   A locked vault                                Trap; the reward inside
                                                   is 1.5x expected value
 9   A hidden cache, not on any obvious path       Requires search; treasure
                                                   = dungeon level + 2
10   A body, notable — dressed, arranged,          Personal effects treasure
     clearly someone who mattered                  2-4; documents with weight

================================================================================
                         ROOMS 5-6: LANDMARKS
================================================================================

Roll d12. Landmarks are atmosphere and lore. They reward curiosity.
They do not punish. They do not reward directly.

d12  LANDMARK
---  -----------------------------------------------------------------------
 1   A chamber so large the ceiling is lost in darkness. Something moves
     up there, unhurried, following a circuit it has followed for centuries.

 2   A mosaic or carved frieze covering every wall — a narrative in images.
     The story ends abruptly. The last panel is unfinished.

 3   A spring or basin of clean water, still flowing. The stone around it
     is worn smooth by generations of hands. Someone left an offering here
     recently.

 4   A mechanism that still operates — gears turn, something moves, a
     rhythm persists. Its purpose is not apparent. It does not stop.

 5   A garden, long untended, that has found its own equilibrium. Strange
     growths. Strange light from growths that should not glow.

 6   A collapse that opened a view downward — a glimpse of lower chambers,
     deeper passages, something that might be a light source far below.

 7   A wall of names. Thousands of names, some with dates, some with small
     symbols. The most recent additions are in a different hand. Still recent.

 8   A sealed door with a viewport. Something on the other side is aware
     of you. It does not move. It simply watches.

 9   A bridge over a drop, made of material no one in the party can identify.
     It holds. It should not hold. It holds.

10   Writing in many hands, many languages, many ages — visitors have been
     leaving marks here for a very long time. The oldest marks are symbols
     no one in the party recognizes.

11   A room where something happened, once, and the room has not recovered.
     Everything in it is where it was at that moment. The moment was not
     peaceful.

12   A surface that responds — to touch, to voice, to proximity. What it
     responds with is information in a script the party may or may not
     be able to read. It has been waiting to tell someone something.

================================================================================
                         TRAPS
================================================================================

Roll d8. Scale severity to dungeon level.

d8   TRAP                          EFFECT
---  ----------------------------- -----------------------------------------
 1   Pressure trigger              d6 damage; AGI save to avoid
 2   Needle or puncture            d4 + poison; RES save or condition 1 slot
 3   Pit                           d6 per 10ft; AGI save to catch edge
 4   Noxious release               RES save or condition 1 slot
 5   Structural collapse           d8 to all in room; AGI save for half
 6   Alarm — sound or signal       Nearest NPCs alerted; roll encounter now
 7   Binding effect                WIS save or held until broken or dispelled
 8   Old-world discharge           d8, ignores mundane armor; AGI save half

================================================================================
                         DUNGEON DRESSING
================================================================================

Roll d12. Add texture to any room that needs it.

d12  DETAIL
---  -----------------------------------------------------------------------
 1   Old bones. Some have personal objects still with them — rings, tokens,
     small things people carry and do not give away easily.

 2   Signs of long habitation — not recent, not ancient. Someone lived here
     for years. The traces are domestic. Worn patches. Arranged objects.

 3   Old mechanisms, silent. Some are clearly incomplete. Some may have
     been functional once. None are now.

 4   A smell with no obvious source. Not unpleasant. Not familiar.

 5   Marks on the walls — some territorial, some navigational, some that
     look like neither and may be devotional.

 6   A container, sealed or locked. Empty. Opened from the inside.

 7   A passage that ends in solid wall. The wall is the same age as the
     passage. It was always a wall. The passage leads here on purpose.

 8   Evidence of a conflict — old enough to be abstract, recent enough
     to still be specific in places.

 9   A light source of uncertain origin. Steady. Dim. Has been burning
     for longer than it should have been burning.

10   Liquid pooled in a low point. Still. Clear enough to see bottom.
     The bottom is further down than it should be.

11   A draft from no visible source. Consistent direction. Consistent
     temperature. Something is moving air somewhere in this complex.

12   Silence that is not natural. Sounds from outside this room do not
     enter it. Sounds made inside it do not carry. The silence is old.


---

---

# PART 8: TALENTS & BACKGROUNDS

## Stealth Attacks

Any character who attacks from stealth or an undetected position gains **+2 ATK** and deals **maximum weapon damage** on a hit. Maximum damage always exceeds mundane armor ratings — the strike finds a gap by precision rather than force. Stealth is lost after the attack regardless of outcome.

---

## Talents & Backgrounds

Talents represent training, background, and accumulated expertise beyond the base class progression. They are available to any class at character creation or as rewards for significant accomplishment or downtime training.

**Design principles:**
- Any class may take any talent unless otherwise noted
- Bonuses from talents do not stack with other talent bonuses of the same type — take the higher value
- Bonuses from magic items and ability scores stack normally with talent bonuses
- Most talents carry an armor restriction as their primary cost

---

### Ranger
+1 to d6 rolls for wilderness survival, tracking, and stealth in outdoor environments. Critical hit range expands to 19–20 against beasts. No heavy armor.

---

### Blade Dancer
+1 to melee ATK and DEF when wielding a medium weapon. No heavy armor, no shield.

*A caster with blade dancer can hold their own against minor threats without expending spells, reserving magic for encounters that genuinely require it.*

---

### Fencer
Free counterattack on a natural 19–20 on a defense roll when wielding a single medium sword, or a medium sword and dagger. No medium or heavy armor, no shield.

---

### Swashbuckler
+1 ATK with light or medium weapons. +1 to d6 rolls for sailing, sea lore, and open-water survival. No heavy armor.

---

### Thief
+1 to d6 rolls for lockpicking, sleight of hand, stealth, climbing, and similar roguish tasks. Stealth attacks deal maximum weapon damage + roll the weapon die again (second roll checks armor normally). No heavy armor, no shield.

---

### Assassin
+1 to d6 rolls for stealth, disguise, poison preparation, and poison handling. Stealth attacks deal maximum weapon damage + roll the weapon die again (second roll checks armor normally). No heavy armor, no shield.

*Thief and assassin are parallel options with different skill sets rather than a progression. A character may have training from both — skill bonuses apply to their respective tasks, combat bonuses do not stack.*

---

### Blessed / Ordained
Cure once per day: heal 1d6 + WIS modifier HP on touch. +1 to d6 rolls for religious lore, ceremony, and faith-based persuasion. Any armor.

*A fighter with this talent is a paladin. A caster with this talent is a priest who also has spells.*

---

### Hex
Curse once per day: one target suffers −1 to all rolls until they rest (WIS save at target 13 resists). +1 to d6 rolls for occult lore and curse identification. Any armor.

---

### Wildling
Speak with animals at will — simple communication, animals are not compelled to cooperate. Commune with nature once per day: ask the referee one question about the local natural environment and receive an honest answer. No heavy armor.

---

### Archer / Gunner / Slinger
+1 ATK and damage with a chosen ranged weapon type (bow, firearm, or sling — chosen at creation). No shield, no heavy armor, no heavy melee weapons.

---

### Sniper
+1 to d6 rolls for stealth and concealment in outdoor or elevated positions. Stealth attacks with ranged weapons deal maximum damage + roll the weapon die again (second roll checks armor normally). Can engage targets at extreme range not normally possible for other characters — across a chasm, through a narrow window, from a hilltop — at referee discretion. No shield, no heavy armor, no heavy melee weapons.

---

### Jester
+1 to d6 rolls for performance, deception, and reading a crowd. On a successful ranged defense roll against a small thrown weapon, catch it and immediately make a ranged attack to return it — up to 3 times per round. Once per day, reroll any single die that affects you, including dice you did not roll yourself. Light armor only, no shield.

---

## Magic Traditions

The default caster learns magic academically — ancient words of power, runic formulae, WIS-driven research. Other traditions access the same spell slot framework through different fictional means. Each tradition is a lateral shift rather than a power change: different flavor, different spell list, different associated ability score where relevant.

Choosing a magic tradition is a talent taken at character creation or through significant in-world training. Casters only.

---

### Shaman
Magic comes from negotiation with elemental and natural spirits who perform the actual casting. WIS replaces WIS for all magic-related rolls including spell research, scroll scribing, and knowledge tasks. Different spell list emphasizing nature, spirits, elemental effects, and communal magic. No additional restrictions.

*Other tradition examples: witch (WIS, curses and nature magic), oracle (WIS, divination and fate), war mage (WIS, combat and destruction spells), blood mage (RES, sacrifice-fueled magic).*

---

### Artificer
Magic is stored in constructed devices — wands, gadgets, weapons, mechanisms — rather than memorized and cast directly. Casters only.

**Gadgets:** one gadget per spell level known (maximum 5). Each gadget holds one specific spell with charges equal to the artificer's spell slots for that level. Example: a level 5 artificer knows 1st, 2nd, and 3rd level spells — they have 3 gadgets with 4, 2, and 1 charge respectively.

**Recharging:** gadgets recharge like normal spell slots after rest. No downtime action required.

**Swapping spells:** the spell stored in a gadget cannot be changed while on an expedition. Swapping requires returning to town (downtime) or spending a camp action during travel to swap one gadget's spell.

**Activating gadgets:** anyone can activate a gadget as their action. No declaration at the start of the round required. No verbal or somatic components — works when silenced, grappled, or otherwise impaired. The artificer or any party member holding the gadget simply activates it on their turn.

**Inventory:** gadgets occupy inventory slots (1 each). An artificer carries 1–5 slots of gadgets versus a standard caster's 1-slot spellbook.

**Item loss:** the artificer carries more items and is statistically more likely to lose one to a failed save, a natural 1, or a referee consequence. However losing one gadget is manageable — the others remain functional. A standard caster losing their spellbook loses all magical capability until it is replaced.

**In combat:** the artificer does not need to declare spells at the start of the round and is not at risk of losing a spell to damage before it resolves. They move and activate a gadget on their turn like any other action.

---

### Item Loss as Consequence

When a character fails a save, rolls a natural 1, or suffers a referee-determined consequence that involves losing or damaging an item, roll d10 to determine which inventory slot is affected. Items in hand slots are most vulnerable (referee may target these first for thrown weapons, disarms, etc.).

This mechanic is especially meaningful for casters:
- **Standard caster:** 1 vulnerable item (spellbook) — low exposure, catastrophic if lost
- **Artificer:** 3–5 vulnerable items (gadgets) — higher exposure, each loss manageable

---

### Poison Rules
Poisons cause conditions (1 slot) until treated. A RES save (target set by poison quality) resists the effect entirely or halves duration. Assassins apply poisons without detection and may craft poisons with higher save targets through downtime and appropriate materials.

| Poison quality | Save target | Effect |
|---|---|---|
| Common | 10 | Minor condition 1 slot, 1 day |
| Refined | 13 | Moderate condition 2 slots, until treated |
| Masterwork | 16 | Severe condition 3 slots, until treated |


---

---

# APPENDIX: QUICK REFERENCE

## Combat (Player-Facing)

**Attack:** d20 + FC + STR/AGI vs 10 + monster FC → hit → roll weapon die → armor save → damage
**Defense:** d20 + FC + STR/AGI vs 10 + monster FC → success = deflect, fail = take damage
**Nat 20 attack:** crit (max + bonus, roll again + bonus, bypass armor)
**Nat 20 defense:** free counterattack
**Nat 1 defense:** monster crits you

## Armor Save
Raw die vs rating. Equal or under = 0 damage. Over = die + bonus through.

## Saving Throw
**16 − total level.** d20 + relevant modifier. Apply race/background bonuses where appropriate.

## Task Resolution
**2-in-6** base. −1 modifier = 1-in-6. +1 modifier = 3-in-6. Skills and background add +1 each.

## Advancement
**Incremental reward:** recover significant treasure from a site ≥ party level. Choose: +1 HP / +1 FC (Hunter) / +1 spell slot (Caster) / +1 d6 task / +1 stat / +1 save / new talent.
**Tier advance:** complete an Accomplishment of appropriate magnitude. Choose: unlock next tier OR concrete bonus (+1d6 HP, +1 stat, etc.).
**Tiers:** Adventurer (1–3) → Hero (4–6) → Lord (7–9) → Legend (10–12) → Mythic (13–15).

## Treasure
**1 treasure = 1 week downtime per character.** Party of 4 burns 4 treasure/week.
Monster HD ≈ treasure value of its hoard.

## Overland
1 hex/day on foot. 2 hexes/day mounted (open terrain).
Encounter roll: 1-in-6 plains, 2-in-6 hills/forest, 3-in-6 mountains/swamp, 4-in-6 ruins.

## Dungeon Turns
~10 minutes each. Move + search, or 1 action per turn. Wandering encounter every 3 turns (2-in-6). Torch = 6 turns.

## Downtime
1 treasure/week per character. Actions: Carousing, Medical Care, Training, Research, Construction, Market, Employment. One action per week.

---

---

# PART 7: DOWNTIME

Each week of downtime costs **1 treasure per character** (lodging, food, basic resupply). Each downtime action represents approximately **1 week** of focused activity, though some actions require multiple weeks.

A character can only pursue one downtime action per week.

---

# PART 7: DOWNTIME

Each week of downtime costs **1 treasure per character** (lodging, food, basic resupply). Each downtime action represents approximately **1 week** of focused activity, though some actions require multiple weeks.

A character can only pursue one downtime action per week.

---

## Carousing

Spend treasure on food, drink, entertainment, and social engagement with the local population.

**Cost:** 1 additional treasure (on top of normal living expenses).
**Duration:** 1 week.

**Benefits (choose or roll d6):**

| d6 | Benefit |
|----|---------|
| 1–2 | Gain a **rumor** — a specific lead on an adventuring site, faction, or opportunity in the region |
| 3–4 | Gain a **contact** — an NPC who owes you a favor or is well-disposed toward you |
| 5 | Gain an **incremental reward** — +1 to a relevant task roll based on what you got up to (referee determines) |
| 6 | Both a rumor and a contact |

**Optional complication (roll d6 if spending 2+ extra treasure on a big night):**

| d6 | Complication |
|----|-------------|
| 1 | Enemies made — someone took offense |
| 2 | Debt — you promised something you shouldn't have |
| 3 | Condition — minor injury or illness (1 slot) |
| 4 | Missing item — something was lost or stolen |
| 5–6 | No complication — just a good time |

---

## Medical & Magical Care

Seek treatment for conditions — injuries, diseases, curses, hexes, or magical bindings.

**Cost:** see Conditions table (1 treasure per slot for injuries and disease; 1–3 treasure per slot for curses; varies for magical bindings).
**Duration:** 1 week per condition slot treated.

Multiple conditions can be treated in the same week if the character pays for all of them and stays in town. Treatment requires access to an appropriate facility or NPC (healer, temple, etc.) — not all treatments are available everywhere.

---

## Training

Improve a skill, gain a talent, or increase an ability score through dedicated practice, study, or mentorship.

**Requires:** a teacher, training partner, facility, or access to relevant materials. Cannot train in a vacuum.

| Goal | Cost | Duration | Notes |
|------|------|----------|-------|
| +1 to a specific task roll | 1 treasure/week | 2 weeks | Requires relevant teacher or materials |
| Learn a special technique / talent | 2 treasure/week | 3–4 weeks | Requires a master or rare text |
| +1 to an ability score | 2 treasure/week | 4 weeks | Referee determines which scores can be trained; not all are equally trainable |

Ability score training is the hardest to justify fictionally — a character training STR makes sense; training CHA through deliberate practice is unusual. The referee should require a credible fiction for each.

---

## Research & Rumors

Dig into libraries, question locals, consult sages, or pursue spell research.

### Gathering Rumors & Information
**Cost:** 1 treasure per week.
**Duration:** 1 week.
**Result:** d3 specific rumors, leads, or pieces of lore about a topic of the player's choice. Quality depends on the settlement size and what's knowable.

### Spell Research
Develop a new spell or adapt an existing one. Research costs exactly **double** the scroll cost for the same spell level — you're creating a permanent addition to your spellbook rather than a single-use item.

**Requirements:** access to a library or laboratory; WIS modifier applies (high WIS shortens research, low WIS extends it).

| Spell Level | Scroll cost | Research cost | Minimum weeks |
|---|---|---|---|
| 1st | 1 treasure | 2 treasure | 2 weeks |
| 2nd | 2 treasure | 4 treasure | 2 weeks |
| 3rd | 3 treasure | 6 treasure | 3 weeks |
| 4th | 4 treasure | 8 treasure | 4 weeks |
| 5th | 5 treasure | 10 treasure | 5 weeks |

Note that research costs are paid on top of normal weekly living expenses (1 treasure/week), so the true cost is higher than it appears. A 5th level spell researched over 5 weeks costs 10 treasure in research plus 5 treasure in living expenses — 15 treasure total before accounting for a character's share of party upkeep.

At the end of the minimum duration, roll d20 + WIS modifier vs target 15. Success = spell researched and added to spellbook. Failure = spend another week and try again (cost continues).

### Scribing Scrolls
Copy a known spell onto a scroll for single-use later.

**Cost:** 1 treasure per spell level.
**Duration:** 1 day per spell level (does not require a full downtime week).
**Requirements:** blank scroll (included in cost), spellbook access, quiet workspace.

A scroll costs half what research costs because it is consumed on use. Scrolls are useful insurance and delegation tools — a caster can hand a scroll to a non-caster for emergencies, or use one to cast a spell they haven't researched yet.

---

## Construction

Begin or make progress on a permanent structure or organization.

**Cost:** varies by project (see below).
**Duration:** 1 week per progress increment; large projects take months or years.

| Project | Cost per week | Notes |
|---------|--------------|-------|
| Hideout / safe house | 1 treasure | Small, concealed; 3–4 weeks to complete |
| Tower / outpost | 3 treasure | Defensible; 8–12 weeks |
| Fortress / keep | 5 treasure | Major undertaking; months of work; requires laborers |
| Business (shop, inn, etc.) | 1–2 treasure | Generates 1 treasure/month once established |
| Guild / organization | 2 treasure | Generates contacts, information, and loyalty |
| Cult / following | 2 treasure | Generates followers; requires a credible ideology |

Construction requires either the character's direct supervision or a trusted hireling managing the work. Unsupervised construction may encounter problems at the referee's discretion.

Completed structures provide ongoing benefits (safe rest, storage, income, followers) and serve as a base of operations.

---

## Market

Seek buyers, sellers, or traders for valuable goods and magic items.

**Cost:** 1 treasure (bribes, fees, introductions).
**Duration:** 1 week.

**Finding a buyer for magic items:**
Roll d6 + settlement size modifier (small settlement: −1, city: +1):
- 1–2: No buyer found this week
- 3–4: Buyer found; offers 50–75% of treasure value
- 5–6: Motivated buyer found; offers full treasure value
- 7+: Collector found; may offer above value or trade for something specific

**Finding a seller / specific item:**
Specify what you're looking for. Roll d6:
- 1–2: Nothing available
- 3–4: Something in the right category; random specific item
- 5–6: Close to what you wanted; referee determines
- 7+: Exactly what you wanted; at premium cost (150% treasure value)

**Trading magic for magic:**
Offer a magic item and specify what you want in return. The referee rolls on a random magic item table appropriate to the settlement's size and level. You can accept the trade or walk away; the original item is not spent until you agree.

---

## Employment

Find hirelings for the next expedition or attempt to recruit a retainer.

**Cost:** 1 treasure (posting notices, buying drinks, spreading word).
**Duration:** 1 week.

### Finding Hirelings
Roll 2d6 + CHA modifier:

| Roll | Result |
|------|--------|
| 2–4 | No takers — word has spread that you're unlucky or dangerous |
| 5–7 | 1d3 common hirelings available (porters, guards, torchbearers) |
| 8–10 | 2d3 common hirelings, or 1 skilled hireling |
| 11–12 | Multiple skilled hirelings available; choose up to 3 |
| 13+ | A specialist seeks you out; unusually capable |

### Recruiting a Retainer
A retainer is a long-term NPC companion — more capable than a hireling, with their own personality and agenda.

**Requirements:** CHA modifier of 0 or better; reputation as someone worth following.
**Process:** one recruitment attempt per downtime week. Roll 2d6 + CHA modifier vs target 9. Success = a retainer candidate approaches or agrees. Failure = not yet; try again next week.

Retainers begin with a loyalty score of 7. Loyalty increases with fair treatment, good pay, and shared success. Standard B/X loyalty and morale rules apply.

