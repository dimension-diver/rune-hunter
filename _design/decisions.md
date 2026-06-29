# Rune Hunter — Design Decisions

Key mechanical decisions and the reasoning behind them. Reference this before relitigating settled questions.

---

## Combat System

**ATK = class progression.** Hunters top at +7, Delvers at +5, Casters at +3 over 10 levels. Monster ATK = HD. This means a 10HD monster is equivalent to a L10 Hunter with a +3 magic weapon -- monsters implicitly account for magic gear without needing to be equipped.

**DEF = 10 + floor(level/2) for everyone.** Experience-based, not combat-skill-based. A L10 Caster is harder to hit than a L1 Caster not because they fight better but because they've survived long enough to know how not to get hit. Monsters use the same formula with HD.

**AR (Armor Rating) as flat damage reduction.** Light armor AR1, heavy armor AR2, magic AR3+. Replaces the two-gate armor save system. DR was initially rejected for causing death-by-a-thousand-cuts fights, but crit degradation (nat 20 reduces AR by 1 for the fight) solves that by preventing high-AR monsters from becoming pure stalling exercises. PC armor degraded in combat requires downtime repair -- armor as resource.

**Player-facing defense rolls.** When a monster attacks, the targeted player rolls d20 + DEF vs 10 + monster ATK. This keeps all dice in player hands and makes split attacks exciting -- all targeted players roll simultaneously.

**Split Attack (Hunter only).** Divide ATK bonus across multiple targets, minimum +1 each, different targets only. Magic weapon bonus adds to the budget. This is Hunter's signature feature.

**Sneak Attack (Delver).** +4 ATK and damage multiplier (x2/x3/x4/x5 at levels 1/4/7/10) when attacking with positional advantage. Applies to melee and ranged. Referee judges the fiction.

**Saves: 15 - floor(level/2) for PCs, 19 - floor(HD/2) for monsters.** Improves every two levels. Monsters improve slower than PCs intentionally -- high level casters should be able to land hold monster on a 10HD creature (save 14, ~35% success) without it being trivial.

**Nat 20 on attack:** bypass AR, reduce target AR by 1 for the fight.
**Nat 20 on defense:** avoid hit and make a free counterattack this round.
**Nat 1 on defense:** monster crits you.

---

## Monster Framework

**Monster ATK = HD** (not ceil(HD/2)). Monsters account for magic weapons, venom, and natural ferocity implicitly. A 10HD monster at +10 is peer-equivalent to a L10 Hunter with a +3 sword. Referee doesn't need to equip monsters.

**Monster DEF = 10 + floor(HD/2).** Same formula as PCs. Listed as a pre-calculated number on stat blocks; adjust for shields or exceptional AGI.

**Size sets HP die and damage die.** Small d4, Medium d6, Large d8, Huge d10, Colossal d12. Special ability damage = floor(HD/2) rounded up dice of the size die -- same logic as spell tiers. A 5HD Colossal monster can stomp for 3d12, save for half.

---

## Classes

Three core classes. Optional classes (Noble, Striker, Ranger, Seeker, Esper, Dabbler) function as one of the three with specific differences noted. See classes document.

**Hunter HD d8, Delver HD d6, Caster HD d4.** Striker is an optional Hunter-derived class with d8 HD. Dabbler is an optional Caster-derived class with d6 HD and light armor.

---

## Magic System

**Spell slots (UA progression).** Replaced MP system. Slots recover after rest.

**Runecasting** includes: prepare and cast spells from a runebook, identify/appraise/craft magic items (Runecrafting), read scrolls. Casters and Seekers can scribe scrolls and copy runebooks. Others can only use scrolls.

**Runebooks** take 1 inventory slot each, contain 3 spells (any combination of tiers/runes). Casters receive 2 runebooks from their teacher at start. Crafting a custom runebook (compiling 3 spells from different sources) is a downtime activity.

**Scrolls** are tier-fixed at scribing. 3 scrolls per inventory slot. Anyone with Spell Scrolls access can use them. Scribing scrolls or runebooks requires Runecasting.

**10 common runes:** Fire, Wind, Water, Earth, Thunder, Nature, Beast, Dark, Light, Soul. Each has 5 spells (T1-T5). Rare/advanced runes (Rime, Void, Rage, Gate, etc.) are found in play. Runes = spirits for Espers -- same mechanical object, different fiction.

**WIS governs Runecasting (Mage tradition). CHA governs Spirit Summoning (Esper tradition).** Runic Lore (WIS 15+) and Spirit Lore (CHA 15+) each grant one extra T1 slot per day.

---

## Advancement

No XP. Advance through expedition rewards and accomplishments. ATK, DEF, and saves advance automatically with level. HP: roll full HD pool each level, take if higher than current HP, minimum +1, RES modifier per die.

Level bands (1-2, 3-4, 5-6, 7-8, 9-10) require accomplishments to cross. Advancing is always optional -- the Conan principle.

---

## Key Aesthetic Decisions

**Offense ahead of defense.** Monster ATK = HD grows faster than PC DEF (half level). High HD monsters are genuinely threatening without special rules. A 15HD monster hitting a L10 Hunter at 80% is correct -- use spells, tactics, and preparation.

**Magic items are not assumed.** The monster framework doesn't require magic gear. Finding a +2 sword is a meaningful upgrade, not a baseline expectation.

**Encounter design over balance.** OSR philosophy: encounters aren't balanced, they're situations. A Cockatrice in a level 1 dungeon is something to run from or engage cleverly, not a calibrated challenge.
