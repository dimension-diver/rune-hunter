---
title: Enemy Design
parent: Enemy Rules
nav_order: 1
---

# Enemy Design

Monsters use **HD** and **size** as their two primary axes. HD determines ATK, DEF, save, and HP pool. Size determines the HP die and damage die.

All rolls are player-facing. Monsters never roll. When a monster attacks, the targeted player rolls d20 + DEF vs 10 + monster ATK. When a monster splits attacks, all targeted players roll simultaneously.

---

## Core Statistics

**ATK = HD.** A 5 HD monster attacks at +5. Monsters implicitly account for magic gear, venom, special training, and raw ferocity that PCs accumulate through explicit treasure. The HD already assumes peak capability.

**DEF = 10 + floor(HD / 2).** Adjust for shields or exceptional agility.

**Save = 19 - floor(HD / 2).** Minimum 2.

**HP:** roll the size die once per HD. Use average values for ease of reference.

**AR:** 0-3 for mundane creatures; 4+ for magical ones.

---

## Size

| Size | HD die | Damage die | Base AR |
|------|--------|------------|---------|
| Small | d4 | d4 | 0 |
| Medium | d6 | d6 | 0 |
| Large | d8 | d8 | 1 |
| Huge | d10 | d10 | 1 |
| Colossal | d12 | d12 | 2 |

---

## Attack Count by Size and Tier

| Size | Attacks |
|------|---------|
| Small | 1 attack; second at HD 4 |
| Medium | 1 attack; second at HD 4 |
| Large | 1 attack; second at HD 3; third at HD 5 |
| Huge | 1 attack; second at HD 3; third at HD 5 |
| Colossal | 2 attacks; third at HD 4 |

---

## Special Abilities

**Free (no budget cost):**
Pack tactics, keen senses, morale bonus, poison on hit, any flavor trait that creates fiction without changing the math.

**Minor:**
- +1 AR (max 3 mundane, 4+ for magical creatures)
- Step up damage die
- Additional attack per round
- Veteran (+1 ATK beyond HD baseline)

**Significant:**
- Regeneration (recovers HP each round; stopped by fire/acid/magic)
- Frightful presence (save or -1 ATK/DEF while in range)
- Grab/grapple (on hit, target held; action to escape)

**Major:**
- Area attack / breath weapon (all in zone save for half; bypasses AR)
- Powerful spell-like ability (1/day)
- Multiple phases
- Legendary resistance (once per encounter, turn a failed save into a success)

---

## Special Ability Damage Scaling

Area attacks and breath weapons scale with HD. Maximum damage dice = ceil(HD / 2):

| HD | Max damage dice |
|----|----------------|
| 1-2 | 1 die |
| 3-4 | 2 dice |
| 5-6 | 3 dice |
| 7-8 | 4 dice |
| 9-10 | 5 dice |

Use the monster's size die. A 5 HD Colossal can stomp for 3d12 (save for half).

---

## Split Attack

Monsters divide their ATK bonus across multiple targets the same way Hunters do: minimum +1 per attack, each attack targets a different creature. The referee declares the split before players roll defense.

---

## Stat Block Format

```
MONSTER NAME
HD: X   Size: X   HP: X   ATK: +X   DEF: X   AR: X   Save: X+
Attacks: X   Damage: die
Special: [abilities]
Morale: X   Treasure: X
Notes: [behavior, habitat, tactics]
```

---

## Design Notes

- Not every monster needs special abilities. Simple monsters are fine. Save complexity for encounters that matter.
- AR creates tactical texture. High AR monsters require magic weapons or clever tactics.
- Treasure baseline: HD / 2. Adjust for fiction.
- Special abilities make fights memorable. Regeneration, frightful presence, grab, and breath weapons all change how players approach the encounter.
