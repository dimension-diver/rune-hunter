# Rune Delver. Player's Guide

---

## How Rolls Work

Three resolution systems, each for its own domain:

- **Combat:** d20 + STR or DEX vs 10 + monster SKILL. Player-facing. Players roll to attack and to defend. Monsters are static numbers.
- **Saving throws:** d20 + relevant stat vs 15. Failed saves deal conditions, not HP damage.
- **Tasks:** d6, X-in-6 where X is half the relevant stat rounded up. Traits add +1.

All rolls are **player-facing**. Players roll for themselves, their hirelings, retainers, familiars, and summoned creatures. Monsters never roll.

---

## Character Creation

### 1. Assign or Roll Stats
All three stats start at 1. You have 3 points to spend increasing them, with a maximum of 3 in any stat at character creation.

**Assign:** spend the 3 points freely across **STR, DEX, WIL**.

**Roll (default):** roll d6 three times. Each result adds 1 point to a stat:

| d6 | Stat |
|----|------|
| 1–2 | +1 STR |
| 3–4 | +1 DEX |
| 5–6 | +1 WIL |

If all three rolls hit the same stat (which would exceed the starting maximum of 3), assign the third point freely to any stat.

Stats range from 1 to 8 over the course of a career. Each stat has a derived value **X** equal to half the stat rounded up, used for task rolls and some trait effects.

### 2. Starting HP
**4 + STR.** A character with STR 1 starts with 5 HP. STR 2 starts with 6 HP. STR 3 starts with 7 HP.

### 3. Choose Two Traits
All characters start with two traits. Roll d66 on the trait table or pick freely.

**Trait 1** is typically innate or experiential: species heritage, unusual origin, something you were born with or that shaped you before you started delving.

**Trait 2** is typically background or origin: where you came from, what you did before, who you ran with.

Chimeric characters spend one trait on their heritage. Kith spend neither and have two fully open trait slots.

### 4. Choose One Tech
All characters start with one tech: a learned combat ability, magical tradition, or specialist capability. Techs are precise and prescribed; they do exactly what they say.

**Rune Magic** and **Spirit Magic** both unlock spell slots based on WIL and access to runes. Characters without one of these techs have no spell slots regardless of WIL. Rune Magic draws on academic study of ancient formulae. Spirit Magic draws on negotiation with elemental and natural spirits. Both use the same spell slot table; they differ in which runes are accessible and how new ones are learned.

Techs are otherwise acquired through play: training with a master, finding a manual, receiving a gift from a spirit. See Techs.

### 4. Starting Equipment
*[Starting equipment packages, placeholder]*

---

## Stats

Three stats cover everything a character does.

**STR** covers melee attacks and defense, HP, feats of physical force, and endurance. X used for tasks involving strength, athletics, and physical labor.

**DEX** covers ranged attacks and defense, stealth, speed, and precision. X used for tasks involving agility, sleight of hand, and fine motor control. DEX is reduced by medium and heavy armor.

**WIL** covers magic (if the Rune Caster trait is taken), saves vs mental effects, social rolls, and knowledge. X used for tasks involving persuasion, lore, and willpower.

Stats increase by 1 at each level up. The maximum stat for a PC is 8.

---

## Combat

### Round Sequence
1. **Declare spells:** characters casting a rune this round announce it before initiative. The spell resolves at the end of the round. Any damage taken before resolution loses the spell and the MP. Artificers are exempt: gadgets activate as a normal action with no prior declaration.
2. **Roll initiative:** each side rolls d6. Winning side acts first. Ties resolve simultaneously.
3. **Missiles:** ranged attacks in initiative order.
4. **Movement:** characters move in initiative order.
5. **Melee:** melee attacks in initiative order.
6. **Spells:** declared spells resolve in initiative order.

### Actions
Each round a character may:
- **Move 1 zone and take an action:** attack, use an item, cast a spell, attempt a task, aid another
- **Move 2 zones and take no action**

### Attacking
**Melee:** d20 + STR vs 10 + monster SKILL

**Ranged:** d20 + DEX vs 10 + monster SKILL

Players may use STR or DEX for melee defense: bracing uses STR, ducking uses DEX.

**Static defense:** instead of rolling, treat defense as a fixed 10 + STR or DEX. Cannot be used to flee melee.

| Result | Effect |
|--------|--------|
| Hit | Roll weapon damage, armor save applies |
| Miss | No effect |
| Natural 20 on attack | Critical hit, always penetrates armor |
| Natural 20 on defense | Free counterattack this round |
| Natural 1 on defense | Monster crits you |

### Damage and Armor Save
Roll weapon die + damage modifier and compare to target's armor rating (AR):
- Total **equal to or under** AR: 0 damage
- Total **strictly greater than** AR: full damage

### Critical Hits
Natural 20 on attack, bypasses armor:
1. Deal max die + damage modifier
2. Roll weapon die again, add modifier
3. Both results bypass armor

### Weapons
| Option | Effect |
|--------|--------|
| One-handed | Standard damage die |
| Two-handed | Step up damage die (d4→d6, d6→d8) |
| Dual wield | +1 ATK; use damage die of either weapon |
| Shield | +1 DEF when DEX is not applying to defense due to armor |

### Ranged Combat
Defenders cannot counterattack ranged attackers. Ranged weapons cannot be used in melee and cannot safely target enemies engaged in melee.

**Ammunition:** tracked with 3 bubbles. After each fight involving ranged attacks, roll d6: on 4–6 mark one bubble. When all 3 bubbles are marked, one shot remains. Resupply clears all bubbles. Rare or specialist ammo marks a bubble on 3+.

### Stealth Attacks
Attacking from stealth or an undetected position: maximum weapon damage, bypasses AR. Stealth is lost after the attack.

Certain traits (Thief, Assassin, Sniper) add +Xd6 to stealth attack damage, also bypassing AR.

### Mounted Combat
A mount grants +1 ATK and DEF in melee. A mounted charge, moving at least 1 zone before attacking, grants +2 ATK on the attack.

### Defeat
At 0 HP a character is **defeated:** not automatically dead. The referee determines consequences: capture, unconsciousness, grievous injury.

### Fleeing Melee
A character who flees a melee zone gives opponents a free attack before leaving.

---

## Armor

| Armor | AR | Slots | Treasure | Notes |
|-------|----|-------|----------|-------|
| Light (leather, hide) | 1 | 1 body | 1 | — |
| Medium (mail, brigandine) | 2 | 1 body | 2 | No stealth; DEX does not apply to defense |
| Heavy (plate, relic suit) | 3 | 2 body | 3 | No stealth, no swimming; DEX does not apply to defense |
| Magic armor | 4+ | varies | 5+ | — |
| Shield | — | 1 hand | 1 | +1 DEF when DEX does not apply |

Medium and heavy armor negate DEX on defense rolls. The shield bonus applies instead when carried with medium or heavy armor.

---

## Saving Throws

**Target: 15.** Roll d20 + relevant stat. Meet or beat to succeed.

| Threat | Stat |
|--------|------|
| Poison, disease, physical harm | STR |
| Breath weapons, area effects | DEX |
| Beguilement, fear, illusions | WIL |
| Magical compulsion | WIL |

Failed saves deal **conditions** rather than HP damage. The dungeon leaves a mark that costs time and treasure to address.

Traits may add +1 or +2 to specific saves.

---

## Task Resolution

Roll d6 equal to or under **X** (half relevant stat rounded up) to succeed.

| Stat | X | Base chance |
|------|---|-------------|
| 1–2  | 1 | 1-in-6 |
| 3–4  | 2 | 2-in-6 |
| 5–6  | 3 | 3-in-6 |
| 7–8  | 4 | 4-in-6 |

A relevant trait adds +1. Multiple applicable traits can stack to a maximum of 5-in-6. 6-in-6 is not possible: something always has a chance to go wrong.

---

## Traits

Traits are the primary source of character differentiation. They cover species heritage, background, job capabilities, martial techniques, and magical traditions. Every trait has a clear described use and can be interpreted at the edges by the referee.

**Stacking:** trait bonuses of the same type do not stack. Take the higher value. Bonuses from stats and items stack normally with trait bonuses.

**Stat requirements:** some traits require a minimum stat. Requirements reflect real capability: a master's technique cannot be learned without the physical or mental foundation to support it.

Traits are starting points, not complete definitions. A Criminal who conceives of themselves as a former soldier turned deserter can establish that over play. The trait stays true going forward once defined. Players can also create custom traits with referee approval by describing what they are and what they imply.

Roll d66 or pick from the table. The tens digit groups loosely by category.

| d66 | Trait | Description |
|-----|-------|-------------|
| 11 | Mighty | Your physical power is exceptional. You can attempt feats of force others could not try. |
| 12 | Quick Reflexes | You react faster than most. Surprises rarely catch you flat-footed. |
| 13 | Clever | Your mind is sharp and retentive. Languages, patterns, and old knowledge come easily. |
| 14 | Hardy | Your body resists sickness and poison with unusual stubbornness. |
| 15 | Silver-tongued | People find you naturally persuasive. Strangers give you more benefit of the doubt than they probably should. |
| 16 | Alert | You notice things. It is difficult to sneak up on you or hide something in plain sight. |
| 21 | Slippery | You cannot be easily grabbed, pinned, or restrained. You always find the gap. |
| 22 | Rubber Bones | You squeeze through tight spaces and escape restraints easily. Falls rarely hurt you as much as they should. |
| 23 | Good Nose | Your sense of smell is uncannily sharp. You notice things others miss entirely. |
| 24 | Light-footed | You move quietly and keep your balance instinctively, even on treacherous ground. |
| 25 | Sure-handed | Your grip and precision are exceptional. You rarely fumble or drop things under pressure. |
| 26 | Weathered | Exposure to extremes of cold, heat, and hardship has left its mark. Your body has adapted. |
| 31 | Soldier | You served. Military discipline, tactics, and chain of command are second nature. |
| 32 | Archivist | You spent years in formal study. Libraries, inscriptions, and old records are familiar ground. |
| 33 | Criminal | You ran with a crew at some point. The tools and habits of that life stuck with you. |
| 34 | Sailor | You know the sea. Ships, tides, knots, and port town culture are all familiar territory. |
| 35 | Tracker | You grew up in or spent significant time in rough country. You read terrain, find food, and stay alive with little. |
| 36 | Shaman | You were initiated into a spiritual tradition. Its rites, spirits, and obligations are familiar to you. |
| 41 | Machinist | You work with old-world technology. Mechanisms, power cells, and relic devices are familiar ground. |
| 42 | Performer | Stages, courts, and taverns are your natural habitat. The particular freedoms and suspicions that follow entertainers are old friends. |
| 43 | Well-traveled | You have been many places. New locations rarely catch you off guard and you carry a sense of their customs and dangers. |
| 44 | Apothecary | You know how to prepare medicinal and alchemical items in the field given the right materials. |
| 45 | Inquisitor | You have a sense for when someone is lying. You may not know the truth but you usually know when you are not hearing it. |
| 46 | Houseborn | You were raised inside a noble household or political structure. Its hierarchies, obligations, and intrigues are second nature. |
| 51 | Ctarl | You carry the blood of the great cats. Keen senses, a predator's instincts, and claws that deal d4 damage. |
| 52 | Rito | Hollow bones and vestigial wings let you glide from any height without taking fall damage. Medium or heavy armor grounds you entirely. |
| 53 | Ronso | Large, powerful, and cold-resistant. You carry 12 inventory slots instead of 10 and hit with exceptional force on a charge. |
| 54 | Ygguana | You are attuned to the Ygg-link. Old-world machines, terminals, and inscriptions sometimes respond to you as if they recognize you. |
| 55 | Kobold | Small, quick, and difficult to pin down. You move through tight spaces and crowded fights with an ease larger creatures find unsettling. |
| 56 | Chimera | You carry traits from more than one lineage. Describe your chimeric qualities with the referee and work out what they imply together. |
| 61 | Lucky | Things have a way of breaking in your direction when it counts. Not always. But enough. |
| 62 | Nature-friend | Animals and plants respond to you differently. Wild creatures are rarely immediately hostile. |
| 63 | Attuned | You sense magic, spirits, and old-world signals that others cannot. The referee tells you when something is present, not what it is. |
| 64 | Construct | You are a golem, automaton, or re-awakened machine. You do not need food or sleep but require power cells. Poison and disease do not affect you. |
| 65 | Ancient | You are descended directly from the builders, or possibly are one, re-awoken. The old world is not entirely foreign to you. |
| 66 | Magic Resistant | Spells and psychic effects slide off you. This is occasionally a problem. |

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
| Curse / hex | Temple or ritual | 1–3 treasure/slot |
| Magical binding | Specific ritual or component | Narrative |

| Severity | Slots | Examples |
|----------|-------|---------|
| Minor | 1 | Sprained ankle, mild fever, minor hex |
| Major | 2 | Broken bone, serious disease, powerful curse |

---

## Magic

Magic is locked behind a trait: **Rune Caster**, **Shaman**, or **Artificer**. Without one of these traits, WIL governs saves, social rolls, and tasks but generates no MP and grants no spell access.

### Spell Slots
Spell slots are determined by WIL score. X (half WIL rounded up) equals the highest spell level accessible.

| WIL | 1st | 2nd | 3rd | 4th |
|-----|-----|-----|-----|-----|
| 1   | 1   |     |     |     |
| 2   | 2   |     |     |     |
| 3   | 3   | 1   |     |     |
| 4   | 4   | 2   |     |     |
| 5   | 4   | 2   | 1   |     |
| 6   | 4   | 3   | 2   |     |
| 7   | 4   | 3   | 2   | 1   |
| 8   | 4   | 3   | 3   | 2   |

5th level spells exist but are beyond normal PC reach. Spell slots recover fully after rest.

### Casting
Declare a rune at the start of the round before initiative. It resolves at the end of the round. Any damage taken before resolution loses the spell and the slot.

Resisted spells: roll d20 + WIL vs 10 + monster SKILL. Unresisted spells (healing, buffs, utility) simply work.

### Spells Known
Capped by WIL score. A character with WIL 4 can know at most 4 runes.

### Rune Invocations
Each rune has expressions at different spell levels. Higher level slots unlock qualitatively new capabilities, not just bigger numbers.

*Example: BOLT at 1st level strikes one target. At 3rd level it arcs to multiple targets. At 5th level it becomes a zone discharge.*

Learning a new invocation of a known rune is the primary advancement path for casters and is acquired through fiction: inscriptions, teachers, spirits. See Downtime: Rune Research.

### Spell Damage
Damaging spells deal d6 per spell level spent and bypass AR entirely.

*[Full rune list and invocations, placeholder. See rune reference.]*

---

## Advancement

Characters advance by level, from 1 to 10. No experience points are tracked.

**Level up:** when the referee determines the party has earned a level, each character:
1. Increases one stat by 1
2. Rerolls all HD (d6 per level) and adds STR to the total. If the result exceeds current HP, that becomes the new HP. If equal or lower, HP increases by 1.

Choosing STR on a level up improves both the reroll distribution and the HP floor immediately.

**Tiers:** levels group into tiers that describe the scale at which the character operates in the world.

| Tier | Levels | Title |
|------|--------|-------|
| 1 | 1–2 | Adventurer |
| 2 | 3–4 | Hero |
| 3 | 5–6 | Lord |
| 4 | 7–8 | Legend |
| 5 | 9–10 | Mythic |

Tier is descriptive. It affects how the world regards the character and sets the scale of appropriate threats and sites. It is not a separate advancement gate.

---

## Equipment

*[Full equipment list, placeholder. Weapon and armor tables are compatible with Rune Hunter and Rune Master with no conversion needed.]*
