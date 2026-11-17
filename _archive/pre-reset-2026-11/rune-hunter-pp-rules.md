# Rune Hunter: A Pits & Perils Hack
### House Rules Reference (Draft v3)

*A Pits & Perils hack using Rune Hunter's setting, races, and classes. Retains as much original P&P mechanical content as possible (treasure tables, monster stats, saving dice, spell descriptions) while retiming ability progression for a faster, less grindy, more front-loaded power curve — closer to the attrition model of Wizardry and its JRPG successors than to modern injury-softened OSR design.*

---

## Table of Contents

1. Combat
2. Classes
3. Kith & Chimera (Clans)
4. Treasure & Economy
5. Advancement
6. Downtime
7. Boss & Encounter Design
8. HP, Death, and Attrition Philosophy
9. Open Questions / Not Yet Resolved

---

## 1. Combat

### 1.1 Attack Tables

| Table | Miss | 1 hit | 2 hits | 3 hits |
|---|---|---|---|---|
| Non-combatant | 2-7 | 8-9 | 10-12 | — |
| Combatant | 2-7 | 8-9 | 10-11 | 12 |
| Fighter/Hunter (combatant +1) | 2-6 | 7-8 | 9-10 | 11+ |

- **Natural 2 always misses**, regardless of modifiers.
- **Natural 12** still triggers RAW's unmodified-roll effects (vorpal blades, hammer of thunder, soul stealer, Smash/Thrust bonus damage) independent of table math.

### 1.2 Combatant / Non-Combatant Assignment

- **Combatant:** Hunter, Ranger, Striker
- **Non-combatant:** Delver, Caster, Seeker, Shaman
- **Monsters:** default combatant; referee may override per individual creature or NPC.

### 1.2a Saving Dice & Non-Combat Actions Threshold

RAW unifies these into one mechanic: both Saving Dice and Non-Combat Actions use 7+ on 2d6, same modifier table (nearly impossible -5, less-than-ideal -3, well-suited +1, ideal +3). Moved both together to **8+**, matching the retimed combat threshold (Section 1.1) — deliberately kept as one unified shift rather than splitting the two apart, to preserve RAW's original unification rather than introduce a new asymmetry.

Reasoning: 7+ is 58.3% (21/36), 8+ is 41.7% (15/36) — a flat +1 modifier bridges the two exactly. This makes the *unmodified* baseline slightly disadvantaged by design, with a single +1 (from an ability, a class feature, favorable conditions) flipping it to slightly advantaged. Confirmed this doesn't undermine Delver's stealth identity: RAW's actual Thief feature was never just the leveled +1/3-levels bonus — Thieves automatically have Dexterity regardless of rolled/chosen ability (see Section 2.2), meaning guaranteed standard-rate access to stealth tasks from 1st level is the real advantage, and that holds regardless of what the baseline number is.

### 1.3 Weapon & Magic Modifiers

- **Magic weapon bonus** applies to the attack roll (2d6), shifting which tier a hit lands in — stacks additively with class-based roll bonuses.
- **Two-handed weapon** (great axe, great sword, flail, morning star, long/short bow, crossbow, sling) adds a flat +1 to final hit count, no shield use.
- **Off-label weapon use** (e.g., swinging a bow like a club): keeps normal handling requirements, but only deals one-handed damage — never the two-handed +1.
- **Bayoneted rifle** (Rune Hunter flavor): two-handed for handling (no shield), Thrust-eligible in melee, but one-handed damage in melee mode. Full bow-equivalent stats at range, Volley-eligible (treated as a bow, not a crossbow).
- **Firearms generally:** mechanically identical to bows (two-handed, +1 damage, Volley-eligible if not crossbow-equivalent). No extra damage for "anime logic" flavor.

### 1.4 Combat Moves

RAW's Fear! Fire! Foes! combat-move system, retimed to 3/6/9 (1 move at 3rd, 2 at 6th, 3 at 9th) for all combatant-table classes with move access. One move active per round.

| Maneuver | Requirements | Special Effect |
|---|---|---|
| Bash | Shield | Knock back a foe |
| Block | Shield | Deflect an attack |
| Cover | Shield | Ignore missile fire (immobile, no fighting) |
| Dodge | 20' space | Deflect, no shield needed |
| Parry | Melee weapon | Deflect or disarm |
| Smash | Axe/hammer | Bonus damage on natural 12 |
| Sweep | Two-handed melee | Divide damage among multiple foes in range |
| Thrust | Blade/spear | Bonus damage on natural 12 |
| Volley | Long/short bow | Divide damage among multiple foes in range |

**Sweep/Volley caveat:** these divide a *single roll's* hit total across targets rather than adding attacks. Against fragile (1 HP/level) enemies this is excellent — spreading a hit total kills more targets outright. Against durable enemies (2+ HP/level), dividing chip damage across many foes is *worse* than focusing one down, since every merely-wounded enemy still acts next round. Sweep/Volley are conditionally good, not universally good — value depends on enemy fragility.

### 1.5 Armor

Unchanged from RAW — armor is a flat, additive bonus to total hits (leather +1, chainmail +2, plate +3, shield +1, stacking), never a modifier to the attack roll. It doesn't interact with the combatant/non-combatant table retiming at all, since that retiming only changed how many hits land on a given roll, not how many hits a character can absorb. No house rule needed.

- **Magic weapon bonus vs. magic armor bonus are different axes, easily conflated:** magic weapon bonus shifts the *attacker's* 2d6 roll (Section 1.3); magic armor bonus just makes the *wearer's* armor act as if rated higher (e.g., +2 magic chainmail = chainmail +4 worth of hits). Confirmed against RAW's magic armor table (leather +2 through plate +6) — always a bigger flat number, never a to-hit modifier.
- **Explicitly not adopted:** Infernal Realms' variant (unconsciousness delay = armor value, then death) and Divine Spark's variant (rally to armor-value hits at 0 HP, gear ruined). Both are injury-softening layers of exactly the kind Section 8 rejects on principle — 0 HP means dead, full stop, and armor's job stays purely additive capacity, not a second life bar.

---

## 2. Classes

### 2.1 Hunter (Fighter chassis)

| Trait | Value |
|---|---|
| HP | 10 + 2/level |
| Table | Combatant |
| Attack bonus | +1 (all attacks) |
| Combat moves | 3/6/9, full list |
| 9th-level feature | RAW Fighter's unmodified ability: 2 melee attacks/round, against a single opponent or divided between targets — **no different-target restriction**; this is RAW's baseline Fighter feature, not a house addition |
| Armor/weapons | Any (RAW Fighter) |

### 2.2 Delver (Thief chassis)

| Trait | Value |
|---|---|
| HP | 8 + 1/level |
| Table | Non-combatant |
| Stealth bonus | +1 every 3 levels (RAW Thief, max +3 at 9th) |
| Automatic Dexterity | **Missed on the first pass, caught later:** RAW's Thief "gets dexterity in addition to whatever else the player rolls" — confirmed via core rulebook text (p. 8, p. 23). Delver (and Seeker, which shares Delver's stealth) always counts as having Dexterity for non-combat actions, regardless of rolled/chosen ability. If a Delver/Seeker's own personal ability is *also* Dexterity, RAW grants an additional +1 to all stealth dice — ported directly. This is the real early-game advantage (guaranteed standard-rate access to stealth tasks before the +1/3-levels bonus kicks in at 3rd), not just the later numeric bonus — Ryan's reframe once the 8+ threshold shift made the old 7+ default look like a bigger loss than it is. |
| Backstab | x2/x3/x4 of non-combatant max (4/6/8 flat hits) at levels 3/6/9; +2 to hit; flat damage, no die roll |
| Armor/weapons | Leather; any one-handed weapon (relaxed from dagger-only) |
| Combat moves | None (non-combatant) |

### 2.3 Caster (Magician chassis)

| Trait | Value |
|---|---|
| HP | 6 + 1/level |
| Table | Non-combatant |
| Spellcasting | Full RAW Magician progression — MP starts at 2, +2 every odd level (2/4/6/8/10 at 1st/3rd/5th/7th/9th); learns 1 new spell every level after 1st |
| Item crafting | Gated 3 (potions/scrolls) → 6 (rings/staves/wands) → 9 (armor/weapons/mixed magic), using RAW cost/time tiers |
| Item access | Full — uses and crafts all magic items |
| Armor/weapons | None; dagger/staff, relaxed to any one-handed weapon |

### 2.4 Seeker (alternate Delver — limited caster)

| Trait | Value |
|---|---|
| Chassis | Delver's (HP, table, stealth, weapons) minus backstab |
| Spellcasting | Draws from Caster's full Magician spell list (comprehensive doc Section 8) — not a bespoke fixed list; Seeker isn't a RAW Cleric-equivalent, so it doesn't get a small fixed set from 1st level |
| Spell acquisition | Elf-rate — new spell(s) at 3rd/6th/9th; MP follows Cleric's FP table (1/2/3/4/5 at 1st/3rd/5th/7th/9th) |
| Healing access | **Resolved.** Pulling from the full Magician list means Cure/Heal are available like any other spell — no separate carve-out needed |
| Item access | Scrolls, wands, and other magic items "that make sense" |

### 2.5 Shaman (alternate Caster — nature/ranger hybrid)

| Trait | Value |
|---|---|
| HP | 8 + 1/level (tied with Delver) |
| Table | Non-combatant |
| Armor/weapons | None; staff only |
| Spellcasting | Draws from Caster's full Magician spell list — not a bespoke fixed list. Same MP formula as Caster (2 base, +2 every odd level) and same full-caster acquisition rate (1 new spell every level) |
| Wildlife ability | Free, at-will saving-dice check to pacify/repel wild creatures (replaces tracking skill) |
| Item crafting | None |
| Item access | Full use, no crafting |

### 2.6 Ranger (restricted Fighter/combatant hybrid)

| Trait | Value |
|---|---|
| HP | 8 + 2/level |
| Table | Combatant, no roll bonus |
| Armor/weapons | No heavy armor/shields; no two-handed melee weapons (ranged two-handers fine) |
| Tracking/survival | +1 every 3 levels |
| Sneak attack (ranged only) | x2/x3/x4 of combatant max → 6/9/12 flat hits at 3/6/9 |
| Combat moves | 3/6/9, full list |

### 2.7 Striker (Monk-derived hybrid)

| Trait | Value |
|---|---|
| HP | 8 + 2/level (Cleric/Hermit/Monk line) |
| Table | Combatant |
| Armor/weapons | None; bare hands or quarterstaff |
| FP | Cleric's table (1/2/3/4/5 at 1/3/5/7/9) |
| Spell acquisition | Elf-rate — new spell(s) at 3rd/6th/9th, drawn from Caster's full Magician spell list, **not** RAW Cleric's small-fixed-set-from-1st-level model (confirmed via RAW: clerics just know Cure/Heal outright, no per-level growth; Elves instead gain 1 new spell per 3 levels from a broader list — Striker follows the Elf model, per Ryan's direction) |
| Combat moves | 3/6/9, restricted to Dodge/Block/Parry/Smash/Sweep (Sweep needs quarterstaff), one active per round |
| Ambidexterity | Bare hands +1 dmg; quarterstaff +2 dmg (RAW monk bonus) — **quarterstaff cannot deliver spell-on-hit**, only bare hands can |
| Spell-on-hit | Bare hands only; on a successful hit, choose normal damage or spend 1 FP for the declared spell's effect (touch/self range only); natural 12 does both, spell free |
| Spells declared | Pre-initiative (as with all caster types in this hack) |

**Magic flavor (two schools, flavor only):** all four caster-adjacent classes share the same mechanical spell list (Caster's full Magician list) and are distinguished only by acquisition rate/MP table and in-fiction framing. Caster and Seeker draw on **runic magic** (scholarly, learned, invoking hidden laws rather than summoning). Shaman and Striker draw on **spirit magic** (channeling or briefly hosting primal/elemental forces). This is purely a narrative distinction — resolved as flavor-only per Ryan's direction, not a mechanical fork.

---

## 3. Kith & Chimera (Clans)

Races are fully decoupled from class. Any race may pair with any of the seven classes above.

**Universal rule:** any race with claws or fangs fights unarmed as a natural one-handed weapon, no penalty.

**Design principle (revised):** each Chimera clan gets one mechanical trait plus a genuine fictional drawback, modeled directly on Retrospace's variant/optional species (Appendix II) rather than its core five. The mechanical trait is specifically the part of the clan's nature that impacts adventures — combat, saves, detection, resource economy (poison resistance, claw damage, initiative, HP recovery). Everything else — swimming, breathing underwater, general "of course an aquatic species can do this" competence — is a fictional permission: it means the character simply never triggers the relevant rule (drowning, suffocation) rather than needing a roll or a budgeted mechanical benefit. The earlier "treated as having ability X" pattern (old Ronso/Ygguana) was dropped entirely — it was redundant with Chimera already choosing their ability freely at chargen (Section 2), so it added no real cost or distinction.

**Kith ability roll (finalized):** Strength and Constitution are the two deliberately rare results, matching Kith's "agile, clever, not physically brutish" concept (the Hylian/Elder Scrolls-elf archetype that originally motivated this). Tested against a 3-rare alternative (adding Intelligence or Dexterity to the rare tier) using an evenness metric — the 2-rare table scored 0.77, the 3-rare versions scored only 0.62, so fewer rare slots actually produces a *more* diverse spread overall, not less, since 2d6's middle-heavy curve needs more "common" buckets to avoid clustering. Also confirmed via actual simulated rolls (3 parties of 4), not just theoretical probability.

| 2d6 | Ability | % |
|---|---|---|
| 2-3 | Strength | 8.3% |
| 4 | Constitution | 8.3% |
| 5-6 | Wisdom | 25.0% |
| 7 | Dexterity | 16.7% |
| 8-9 | Charisma | 25.0% |
| 10-11 | Intelligence | 13.9% |
| 12 | Any two | 2.8% |

| Race | Trait | Drawback |
|---|---|---|
| Kith | No fixed trait — rolls for ability instead of choosing (Section 2) | — |
| Ctarl | Party gains +1 initiative (Section 1.4-adjacent, see new Initiative rule) whenever a Ctarl is present — replaces RAW's "one or more elves in the party +1" slot, since Elf isn't a class/clan here and Ctarl is the closer thematic fit; corrected from an earlier "+1 personal initiative" phrasing that didn't actually fit the side-based (not individual) initiative mechanic once that got built out; may roll saving dice for no fall damage where a cat-like landing is plausible (referee's call), otherwise standard half-damage-on-save applies (Tajaris-derived) | Water aversion |
| Kobold | +1 saving dice, +2 vs. mechanical traps (RAW Dwarf trait, narrowed to just the save bonus) | Uncomfortable in open, sunlit surface terrain |
| Goblin | Detects movement in total darkness within 30' by echolocation | Loud noise negates it (built-in counter) |
| Zora | Telepathic communication and ambient emotion-sensing with any mind within 30' underwater, collapsing to touch-range on land (Stari-derived). Water-breathing and swimming are fictional permission only — never triggers drowning rules, no mechanical budget spent on it | Severely limited range on land is the drawback in itself |
| Rito | Flies at full speed | Requires 4 free pack slots — single, self-contained cost |
| Kreen | Regenerates a lost limb within 1d6 days (flavor, no injury system to attach to mechanically); heals +1 HP per day even without resting (Xenlu's exact pairing — flavor half + mechanical half) | Alien, unsettling appearance |
| Ygguana | Immune to poison and disease from mundane sources or low-level creatures (1st-3rd level) — RAW's Adder Stone's exact scope, granted racially. Strong swimming and extended breath-holding are fictional permission only, not a budgeted trait | Cold-blooded: sluggish in cold environments |
| Wolf People | Detects hidden creatures by scent within 30' in darkness/fog; cannot be surprised by anything with a scent | Strong/overpowering smells nearby disrupt or distract them |
| Ronso | Fights with both claws as natural weapons for +1 damage, dividing damage among multiple targets in melee range (Kazin-derived — Retrospace's own claws-analog of RAW's Ambidexterity rule) | No shield, and no more than leather armor, while fighting this way (matches RAW's generic Ambidexterity rule in full — if it applies to dual daggers, it applies to dual claws) |

*Ctarl's rare shifter variant still needs a concrete mechanic — see Section 9.*

---

## 4. Treasure & Economy

### 4.1 Tiers

Categorical Treasure Tiers replace GP — not summable, no quantity of a lower tier ever equals one of a higher tier. Each Type roll produces **one asset at that tier**, never a quantity of lower-tier assets bundled together.

| Tier | Represents |
|---|---|
| I | Modest sum, one solid mundane item, or several small ones |
| II | A serious purchase — heavy armor, two-handed weapon, firearm, fine instruments |
| III | Minor magic — potion, scroll, minor magic item |
| IV | Real magic or a major asset — magic weapon/armor, staff, ring, small building |

- Base yield = the Type number itself, flat (Type I hoard = 1 Treasure, Type IV = 4).
- Magic-item chance unchanged from RAW (2/3/4-in-6 for Type II/III/IV).
- Monster bestiary tags (A/I, B/II, B/III, B/IV) map directly — no conversion needed.

### 4.2 Slots

10-slot inventory (2 hand, 2 body, 6 pack):

- One-handed weapon/shield/light-medium armor: 1 slot.
- Two-handed weapon/plate armor: 2 slots (bulky).
- Small items (potions, scrolls, darts, mundane gear like rope/bedroll): bundle 3 per slot.
- Magic items: 1 slot regardless of value.
- Mundane Treasure: ~1 slot per point (coin/bulky goods), or ~1 slot per 2-3 points if gems/jewelry/art — same asset, different physical form determines the cost, not the value.
- **Petty items** (keepsakes, personal documents, quest-relevant trinkets with no mechanical function) never consume a slot — distinct from bundling, which still applies to practical gear.
- **Universal starting kit** (every character, regardless of class): rations (1 week, 1 slot), torches (3 uses, 1 slot), a Tier I coin purse (1 slot) for incidentals. Rope, bedroll, and similar are optional extras, not baseline — bundle freely per the rule above.

### 4.3 Rushed vs. Full Looting

A live/guarded hoard (dragon still present, threat not yet removed) can only be searched under time pressure:

- Grab-and-go: guaranteed 1 Tier I asset, no roll, standard random-encounter check applies each turn spent.
- Digging for more: roll each turn spent searching (exact table TBD, likely 2d6 with better results at the extremes); **Tier IV is never available under time pressure** — only full, unhurried looting (threat removed) can yield it.

### 4.4 GP Conversion Reference

| Tier | Roll for exact GP value |
|---|---|
| I | 1d6 |
| II | 1d6 × 10 |
| III | 1d6 × 100 |
| IV | 1d6 × 1,000 |

Non-magic economy mapped to tiers by order of magnitude:
- **Tier I:** basic gear, an inn stay, a specialist's weekly wage, minor bribes, a starting character's pocket money
- **Tier II:** armor/weapon/mount purchase, monthly hireling retainer
- **Tier III:** potions/scrolls, a modest stronghold (grove, shrine)
- **Tier IV:** staves/wands/rings, enchanted armor/weapons, Resurrection, a castle

---

## 5. Advancement

- XP-for-gold and monster-kill-XP tables are dropped entirely.
- A character advances one level upon completing a fictional milestone appropriate to their class/story (guild rank, training an apprentice, a class-appropriate trial), inspired by Rune Hunter's Accomplishment system but granting one level per milestone rather than jumping a whole level-band.
- RAW's numeric tables (HP/SP/FP, combat-move/backstab/crafting unlocks) still govern what a given level grants — only the *route* to a level changed, not what's waiting there.
- **Resolved:** advancement "opt-out" is a non-issue under this model. Since the *only* path to a level is its specific milestone, a player who doesn't pursue that milestone simply doesn't reach that level — no separate opt-out rule is needed.
- **A milestone's completion is narrated as a downtime beat**, not a separate transaction on top of one — the guild ceremony, the lesson from a teacher, the training montage between adventures. See Section 6.
- **PCs cap at 10th level.** Per Ryan's direction, there's no 15th-level "Becoming a Legend" tier for player characters — the Becoming a Legend capstone section is removed from the comprehensive doc (formerly Section 13c). Every class's numeric progression (HP/MP/FP, combat moves, spell acquisition) already tops out at or before 9th level per its own table, so nothing else needs retiming to support the cap.

---

## 6. Downtime

Rune Hunter's own downtime system (Rest, Carousing, Training, Spell Research, Crafting, Networking, Hireling recruitment, per-character Upkeep) provides the activity menu and weekly cadence. Its costs are ported over in spirit, not in exact numbers, since its treasure economy and this hack's are built differently.

### 6.1 Why Costs Changed Shape

Rune Hunter's Treasure is a flat, summable scalar (1, 2, 3, 5, 10, 20+). This hack's Treasure Tiers (Section 4.1) are explicitly **not summable** — each roll produces one discrete asset at a tier, never a quantity of lower-tier assets bundling into a higher one. Downtime costs are therefore denominated directly in Tier assets, never summed, per Ryan's direction.

Rune Hunter's injury/condition system and armor-degrades-on-crit rule (its own Wounds & Recovery page) also don't port over — this hack has no injury layer beneath HP (Section 8), so "Injury treatment" as a line item is dropped entirely rather than given something to attach to.

### 6.2 The Tier Ladder (general rule)

One rule generates all downtime costs below, rather than a table of special cases:

| Path | Cost | Why |
|---|---|---|
| Buy or loot the finished asset | Asset's own Tier (Section 4.1) | Full market value |
| Commission a durable copy from an NPC crafter | Asset's own Tier | You get something storable/resellable — full price |
| Self-craft (PC pays materials only) | Asset's Tier − 1 | RAW's own crafting rule is "item value **plus materials**" — a PC supplies their own labor, skipping the "plus" |
| Hire a one-time, non-storable effect (a single spell cast) | Asset's Tier − 1 | No durable object changes hands — same discount logic as self-crafting |

Checked against RAW's actual numbers: potions/scrolls are a Tier III asset (4.1), and RAW's materials-only cost for them (50 GP) sits in the Tier II band of the GP-conversion table — confirming self-craft = Tier III − 1 = Tier II independently of this rule being stated. Rings/staves/wands are a Tier IV asset (4.1), and RAW's 2,500 GP materials cost sits in the Tier IV band, so a high-level Caster self-crafting one at Tier III (IV − 1) is consistent with the same pattern, not a special exception.

### 6.3 Weekly Activities

| Activity | Cost | Time | Notes |
|---|---|---|---|
| Upkeep (per character) | Tier I | per week | Baseline cost of being in town |
| Rest & recover | Tier I | per week | Covers lodging only — does **not** change RAW's 1 HP/day healing rate |
| Carousing / rumors / research (non-spell) | Tier I | 1 week | One activity, not three — "spend money to get leads, hints, contacts." Payout is diegetic (a lead, a contact, a rumor), not a mechanical stat bump — Rune Hunter's LUC-restoration doesn't port over since LUC doesn't exist in this system |
| Hireling recruitment | Tier I | 1 week | Roll for available hirelings |
| Spell Research (Seeker/Shaman/Caster) | Tier II | 1 week | See 6.4 — bespoke-extra, not a gate on the guaranteed floor |
| Training (Hunter/Ranger/Striker) | Tier II | 1 week | See 6.4 — bespoke-extra, not a gate on the guaranteed floor |
| Hire a single-use spell effect (e.g., a cast Cure/Heal) | Tier II | Instant | Asset Tier III − 1, per 6.2 |
| Self-craft potions/scrolls | Tier II | 1 week | Asset Tier III − 1, per 6.2 |
| Commission potions/scrolls from an NPC | Tier III | 1-2 weeks | Full asset Tier, per 6.2 |
| Self-craft rings/staves/wands (high-level Caster) | Tier III | Weeks-months, multi-roll — see 6.5 | Asset Tier IV − 1, per 6.2 |
| Commission major magic from an NPC | Tier IV, if available at all | Referee's call | Full asset Tier; RAW already gates most of this behind a PC Caster's own crafting (2.3) rather than an open service market — many settlements may simply have no one to hire for this |
| Mundane armor/weapon repair | Tier I | 1 week | Asset Tier II − 1, per 6.2 |

### 6.4 Training and Spell Research Never Gate the Guaranteed Floor

Every class keeps its RAW-native acquisition rate as a guaranteed floor, untouched by downtime economy:

| Class type | Guaranteed floor | Source |
|---|---|---|
| Full caster (Caster, Shaman) | New spell every level; MP pool follows RAW Magician's exact table (2 base, +2 every odd level: 2/4/6/8/10 at 1st/3rd/5th/7th/9th) | RAW Magician, unchanged — Shaman uses the identical formula, just applied to its own fixed spell list |
| Restricted caster (Seeker, Striker) | New spell(s) at 3rd/6th/9th; MP pool follows Cleric's FP table (1/2/3/4/5 at 1st/3rd/5th/7th/9th) | RAW Elf's 1-per-3-levels rate — already lands on the same cadence as the maneuver milestones |
| Combatant with maneuvers (Hunter, Ranger, Striker) | New maneuver at 3rd/6th/9th | Already locked in (Section 1.4) |

Training and Spell Research are the same downtime mechanism aimed at two different guaranteed floors, and both are strictly additive — a character who never spends downtime on either still gets everything the floor above promises, right on schedule. Their only job is to let a player acquire something *beyond* the floor: a bespoke technique not in RAW's maneuver list, or a spell outside the character's normal progression. Since Seeker, Shaman, and Striker all now draw from Caster's shared Magician list (Section 2), Spell Research for them mainly matters for reaching something unusual outside that list, or for Seeker/Striker to pick up a spell ahead of their 3rd/6th/9th schedule — a minor, occasional role, not the list-building job it used to have.

**Rejected alternative:** gating all spell/maneuver acquisition behind downtime spend (removing the RAW-native floor entirely) was considered and set aside — it would make a character's actual combat/spell repertoire hostage to treasure on hand rather than levels reached, cutting directly against the stated goal of a front-loaded, level-driven power curve.

### 6.5 Multi-Week Crafting: Completion Chance

RAW already has the shape needed for "pay once, then roll until it's done" — the core rulebook's potion-brewing rule (pay for materials and an alchemist's time, then the referee rolls 2d6 weekly for failure/success, with side outcomes like a lab accident or a bonus double-strength potion) is the same mechanic Rune Hunter's crafting-completion-chance idea is reaching for. Extend that table (or a simplified pass/fail version of it) to staff/wand/ring crafting rather than build new dice math, and modify the weekly roll using RAW's existing non-combat action modifiers (+1 to +3 for favorable conditions, per the Referee Companion) to reflect workshop quality — a caster with a tower and apprentices rolls better odds than a lone hermit.

**Placeholder table (Ryan to fill in), built on RAW's own potion-brewing format:**

| 2d6 | Result |
|---|---|
| 2 | |
| 3-7 | |
| 8 | |
| 9-10 | |
| 11 | |
| 12 | |

RAW's own potion table for reference: 2 = lab accident/side effects (F), 3-7 = no potion brewed (F), 8 = half-strength (S), 9-10 = normal (S), 11 = double-strength (S), 12 = new potion, referee's option (S). Workshop-quality modifiers (tower + apprentices vs. lone hermit) still TBD — apply RAW's existing +1 to +3 non-combat action modifier band once the base table above is filled in.

---

## 7. Boss & Encounter Design

Findings from testing actual party builds against RAW monsters at various level gaps.

### 6.1 RAW Gives No CR System

RAW is explicit: *"NUMBER is just a guide. The referee should balance the number encountered against the level and/or strength of the party."* There is no monster-level-to-party-level parity assumption. A solo monster at party-equal level is trivial (dies in ~3 rounds, barely threatens anyone) — RAW's own precedent (dragons to 12th level, liches 11th-15th, named demon lords above 10th) confirms bosses are meant to sit several levels above the party, not at parity.

### 6.2 The Level-Gap Heuristic

Testing across multiple tiers (level 1 party vs. level 3-4 threat; level 3 party vs. level 6 Manticore; level 9 party vs. level 10 Ancient Dragon) consistently found: **a genuine solo boss wants to sit roughly 3-4 levels above the party and have either multiple attacks or a signature ability functioning like one.** A single-attack monster at any level gap tends to be trivial; attack count/signature ability matters more than the raw level number.

### 6.3 Telegraphed Signature Abilities

Boss-tier monsters with a big AoE opener (Dragon's breath, Manticore's spike volley) should be handled as follows:

- **Declared at the start of the round**, before initiative — a visible telegraph, same convention used for all spellcasters in this hack.
- **Resolved per RAW's own text for that specific ability**, no added formation/exposure layer on top. Manticore spikes, per RAW, are automatic hits with no save, dividing 2d6 among all targets within the 30' range — that's the whole rule, nothing further to call out. Dragon breath follows the hack's own young/mature/ancient damage scale (Section 8/15 of the comprehensive doc), save for half where noted. **The earlier formation-based exposure/Dodge-Cover contest house rule is dropped** — it was solving a problem RAW's own text doesn't actually raise.
- **A natural 12 on Smash interrupts** the ability that round (the boss's concentration/windup is broken).
- Frequency caps by tier, matching the existing young/mature/ancient damage-die progression: **1 use for young-tier, 2 for mature-tier, 3 for ancient-tier**, usable no more than every other round.

### 6.4 True Bosses Need an Answer to Magic

Sustained direct-cast spellcasting (a Caster spamming Bolt) is the single biggest threat to boss pacing — far more than melee output. RAW already has the answer for its own top-tier threats (Nephilim, Lich, Seraphim all carry spell resistance or auto-counter against weaker magic) — this pattern should extend to **any** monster meant to function as a genuine boss, not just named legendary NPCs.

### 6.5 Test at Realistic Resources, Not Full

RAW's 1 HP/day healing rate confirms HP is a whole-dungeon resource, not a per-fight one — a party reaching a boss has typically been ground down by everything before it (confirmed by tallying an actual module: Cellars of Castle Keep's path to its final boss totals ~143 HP of intervening monsters). **Boss math should default to testing at roughly half HP and half spell points**, not full — full-resource testing only shows the best-case ceiling, not the intended experience. A telegraphed AoE that's a manageable risk at full HP can become a near-certain kill at realistic mid-dungeon attrition.

### 6.6 Hordes: Use Real Monsters, Not Invented Levels

RAW doesn't design monster "families" across a level range (there is no "level 5 orc") — difficulty variation within a horde comes from RAW's own explicit levers: HP per creature (1-3/level, referee's choice), armor (a chainmail orc goes from 3 HP to 5), and weapon choice (two-handed weapons add real per-hit damage). Testing an "elite" horde (6 orcs, chainmail, 5 HP each = 30 total) against a level 9 party confirms these levers work as a meaningful middle difficulty between disposable 1-HP fodder and a genuine boss, without needing any new monster entries.

---

## 8. HP, Death, and Attrition Philosophy

- **HP represents stamina, health, and wounds all at once** — there is no separate injury/condition layer at 0 HP. A character reduced to 0 is dead or grievously incapacitated, full stop.
- This is a deliberate departure from crunchier OSR design (which often adds injury tables specifically to soften small, static HP pools). P&P doesn't have that problem: HP pools are generous and grow every level *specifically so* 0 HP can mean death without individual fights feeling arbitrarily punishing.
- **The real per-dungeon resource is SP/FP, potions, scrolls, and item charges** — not HP directly. HP is the top-level gauge; those consumables are the tools that let a party manage it without spending the one currency that actually restores it (real in-game rest days).
- This is the same shape as a classic JRPG dungeon crawl (Wizardry, early Dragon Quest): MP/HP tick down together, running low on resources is what forces a retreat decision, and hitting 0 HP is a real death, not a soft failure state.
- **Death is expensive, not permanent**, which completes the JRPG parallel: Healing potions/staves, Undo (high-level Caster), and the Clone Vats (below) are the confirmed PC-side mechanisms.
- **Resurrection mechanism (resolved):** the Clone Vats — a Phantasy Star II-derived concept, confirmed via Ryan's reference image (a "Clone Pits" table from a third-party OSR supplement, not P&P RAW — adapted, not copied). Reshaped from the source's 3d6 scale to this hack's native 2d6, and from six-stat drawbacks to this hack's single-ability system. Full table now lives in the comprehensive doc (Section 11). Kept the source's overall shape: a dominant "no problems" middle band, symmetric rare extremes (amnesia vs. major mutation), and a drawback tier more common on the low end than the payoff tier on the high end.
- **Reincarnation** — confirmed as a non-issue. Not part of the Clone Vats process; no separate mechanism needed. Treated as a rare story event, referee's call, same as Ryan's direction for both before the Clone Vats concept was pinned down.
- **Minor/major mutation tables** (rolled 11/12 on the Clone Vats table) are deliberately left as referee's-call placeholders — inventing two full mutation tables wasn't part of what got asked for this pass, and it's better flagged as a real gap than filled with unreviewed content. Candidate for a future session if it comes up in actual play.

---

## 9. Open Questions / Not Yet Resolved

1. **Ronso** — *resolved.* Treated as having Strength.
2. **Ygguana** — *resolved.* Constitution (breathe underwater, +1 HP recovery/day, poison/disease save, hold breath, swim rough water).
3. **Kreen** — *resolved.* Xenlus-style regeneration, replacing the earlier "cannot be surprised."
4. ~~Ctarl shifter variant~~ — *dropped.* Gravy, not necessary for the base game; scratched off per Ryan's direction. (The Werewolf/"lost Ctarl" monster entry in the Bestiary stays as-is — that's an NPC/monster stat block, not the player-facing mechanic this item was tracking.)
5. **Advancement opt-out** — *resolved, non-issue.* See Section 5.
6. ~~Rushed-search table~~ — dropped from active list per Ryan's direction; exact dice TBD only if it comes up again.
7. ~~Eighth class~~ — dropped from active list; roster stands at seven (Beastmaster/Dwarf-chassis/Noble noted as future options if revisited).
8. ~~Seeker's spell list~~ — *resolved.* Seeker draws from Caster's full Magician list at Elf-rate (3rd/6th/9th), same as Striker — not a bespoke fixed list. Healing access resolved as a consequence: Cure/Heal are just part of the shared list.
9. ~~Shaman's and Striker's spell lists~~ — *resolved.* Both also draw from Caster's full Magician list — Shaman at full-caster rate (new spell every level), Striker at Elf-rate. The runic/spirit-magic split (Section 2) is confirmed as flavor-only, not a mechanical fork.
10. ~~Rushed-search table exact odds~~ — *confirmed dropped, no table needed right now* (same item as #6).
11. ~~Manticore spike volley~~ — *resolved.* Keeping RAW as written: automatic hits, no save, 2d6 divided among all targets in range. The formation-based exposure/Dodge-Cover house rule (Section 6.3) is removed as unnecessary.
12. ~~Kith/Chimera race traits beyond the nine listed~~ — *resolved, non-issue.* Confirmed via the actual repo (`player-rules/kith-chimera.md`): the site's "there are more" line is an open invitation to homebrew anything with mechanical weight, not a hidden roster of named clans this hack hasn't ported. All nine named Chimera genos on the site (Ctarl, Kobold, Goblin, Zora, Rito, Kreen, Ronso, Ygguana, Wolf People) are already fully statted here. Nothing's missing.
13. **Multi-week crafting completion odds** (Section 6.5) — a fillable placeholder table (RAW's potion-brewing format) has been added; Ryan to fill in actual 2d6 bands and workshop-quality modifiers.
14. **Bespoke maneuver/spell content for Training and Spell Research** (Section 6.4) — the mechanism is settled, but the actual list of non-RAW techniques/spells a player could research hasn't been designed yet.
15. ~~Resurrection and Reincarnation~~ — *resolved.* Resurrection's mechanism is the Clone Vats (2d6 table, Section 11 of the comprehensive doc), adapted from a third-party OSR "Clone Pits" table Ryan referenced, not P&P RAW. Reincarnation stays unaddressed — not part of the Clone Vats process, treated as a rare story event if it ever comes up. Minor/major mutation sub-tables (rolled 11/12 on the Clone Vats table) are left as referee's-call placeholders, not yet designed.
16. **Stronghold assignments by class** — *left as-is, gravy, not a priority.* Seeker's Archive and Ranger's Lodge remain judgment calls without direct RAW precedent, per Ryan's direction to leave this section alone for now.
17. ~~Becoming a Legend capstones~~ — *dropped.* The entire Becoming a Legend section (comprehensive doc, formerly 13c) is removed; Ryan is capping PC advancement at 10th level, so no 15th-level capstone tier is needed. See Section 5's advancement note.
18. **Bestiary complete (first pass), then corrected.** *Left as-is per Ryan's direction — Beholder and Balhannoth still need real design work beyond a template reskin, and Ryan will adjust these himself.* ~85 entries across all four tiers in the comprehensive doc's Section 15, matching RAW's core bestiary size and distribution. A correction pass fixed several real problems Ryan caught: two entries were named after their real-world source rather than given an in-world name (the elite raider was still literally called "Bugbear," renamed **Enforcer**; a ranged automaton was named after the game it was pulled from, renamed **Ancient Sentry**) — worth remembering as a category of error, not just these two instances. Grell's mechanic was corrected after verifying the actual source (tentacle-barbs inject paralytic venom + separate beak bite, not a "sting"). Flumph had a stat line but no real description at all, and what little existed was wrong (real Flumphs have an acid-tentacle attack and a stench spray, not "harmless") — fixed. Hook Horror was discussed in conversation but never actually added to the file — added properly this time. Established a concrete dragon-breath damage scale (young 1d6, mature 2d6, ancient 3d6, RAW's own numbers) to replace several vague "scaled to a dragon's breath" references. Also added missing damage dice throughout (Ankheg's acid, Gas Spore's cloud, Ochu/Otyugh's crush) and stripped remaining meta-commentary from descriptions (a second round of the same drift the Section 13-15 cleanup pass was supposed to catch — worth checking new bestiary content for this pattern going forward, since it recurred). Two entries still need more design work than a template reskin gave them: **Beholder** (multiple simultaneous ray effects, genuinely its own build) and **Balhannoth** (illusion-lure-and-grapple kit has no close RAW analog). Seeker's stronghold was renamed from "Hideout" to **Archive** — Ryan's catch that Seeker is caster-flavored (fixed spell list, Cleric's FP cadence), not primarily a rogue, so a knowledge/secrecy building fits better than a thief's den; still invented without direct RAW precedent. Ranger's stronghold (Lodge) has the same caveat. Striker's Temple, by contrast, turned out to be a **direct RAW match**, not an invention — Fear! Fire! Foes!'s Monk class has its own stronghold (Temple, 750 GP, 15 acolytes), confirmed via source text; the comprehensive doc previously said "treat as Hunter's castle numbers, reflavored," which was simply wrong — corrected to Monk's actual numbers.
19. **Random encounter frequency changed from RAW's default.** RAW checks once per hour (every 6 turns) at 1-in-6 odds — computed out, that's an *expected* rate of about one encounter every 6 hours, which Ryan flagged as too sparse to serve as "the engine of the dungeon." The mismatch: RAW's sparse default reflects its own goal of minimizing bookkeeping, but this hack's HP philosophy (Section 8/11) explicitly models Wizardry/JRPG-style attrition, which needs real encounter volume to function. Switched to the classic OSR standard instead — every 2 turns, same 1-in-6 odds — which produces roughly 2-4 expected encounters over a typical 4-6 hour session rather than under 1. This is a deliberate departure from RAW's own rate, not a retiming of it. Also confirmed RAW's actual encounter tables are exactly the flat "creature type + number" filler Ryan suspected (e.g. "Bat (2-12)," "Kobold (6-12)") — worth building this hack's own weighted/curated encounter tables at some point rather than just pointing at the Bestiary's low tier indefinitely.

---
