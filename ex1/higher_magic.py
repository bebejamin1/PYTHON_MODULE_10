#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 14:51:55 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/13 11:18:05 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import List, Any


green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"

spells = ["Alter Invisibility", "Field of Frost", "test"]

# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================
"""
En Python, les fonctions sont traitées comme n'importe quelle autre donnée.

Elles peuvent être affectées à des variables, passées en tant qu'arguments
à d'autres fonctions, renvoyées par des fonctions et stockées dans des
structures de données. Cette flexibilité technique permet l'utilisation
de patterns de programmation fonctionnelle comme les fonctions d'ordre
supérieur, les closures et les décorateurs.
"""


# ============================= COMBINER ======================================

def spell_combiner(spell1: callable, spell2: callable) -> callable:

    def combine(name: str) -> tuple:
        return (spell1(name), spell2(name))

    return (combine)


def fireball(name: str) -> str:
    return (f"Fireball hits {name}")


def heals(name: str) -> str:
    return (f"Heals {name}")


# ============================ AMPLIFIER ======================================

def power_amplifier(waterball: callable, multiplier: int) -> callable:

    def multiplies(power: int) -> tuple:
        return (power, waterball(power) * multiplier)

    return (multiplies)


def waterball(power: int) -> int:
    return (power)


# ============================= CASTER ========================================

def conditional_caster(condition: callable, spell: callable) -> callable:

    def caste(name: str) -> Any:
        return (spell(name) if condition(name) is True
                else f"Spell \"{name}\" fizzled")

    return (caste)


def condition(spell: str) -> bool:
    return (True if spell in spells else False)


def spell_valid(spell: str) -> str:
    return (f"The name \"{spell}\" is valid")


# ============================= SEQUENCE ======================================

def spell_sequence(spells: List[callable]) -> callable:

    def sequence(name: str) -> List[str]:
        return [spell(name) for spell in spells]

    return (sequence)


def attack(name: str) -> str:
    return (f"Attacks {name}")


# =============================================================================
# =============================== MAIN ========================================
# =============================================================================


def main() -> None:
    print()

# *****************************************************************************
# *                          spell_combiner()                                 *
# *                                                                           *
    print(f"{green}Testing spell combiner...{reset}")
    combined: callable = spell_combiner(fireball, heals)
    print("Combined spell result:", *combined("Dragon"))

# *****************************************************************************
# *                         power_amplifier()                                 *
# *                                                                           *

    print("\n" + f"{green}Testing power amplifier...{reset}")
    mega_waterball: callable = power_amplifier(waterball, 3)
    print(f"Original: {mega_waterball(10)[0]}, "
          f"Amplified: {mega_waterball(10)[1]}")

# *****************************************************************************
# *                        conditional_caster()                               *
# *                                                                           *

    print("\n" + f"{green}Testing conditional caster...{reset}")
    caster: callable = conditional_caster(condition, spell_valid)
    print(caster("Field of Frost"))

# *****************************************************************************
# *                          spell_sequence()                                 *
# *                                                                           *

    print("\n" + f"{green}Testing spell sequence...{reset}")
    sequences: callable = spell_sequence([fireball, heals, attack])
    for sequence in sequences("dragon"):
        print(sequence)


if __name__ == "__main__":
    main()
