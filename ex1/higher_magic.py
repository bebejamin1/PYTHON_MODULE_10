#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 14:51:55 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/11 15:28:07 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import List


green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"

# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================


# Return a new function that calls both spells with the same arguments
# The combined spell should return a tuple of both results
# Example: combined = spell_combiner(fireball, heal)
def spell_combiner(spell1: callable, spell2: callable) -> callable:

    def combine(name: str) -> tuple:
        return (spell1(name), spell2(name))

    return (combine)


# Return a new function that multiplies the base spell’s result by multiplier
# Assume base spell returns a number (damage, healing, etc.)
# Example: mega_fireball = power_amplifier(fireball, 3)
def power_amplifier(base_spell: callable, multiplier: int) -> callable:

    def multiplies(power: int) -> tuple:
        return (power, base_spell(power) * multiplier)

    return (multiplies)


# Return a function that only casts the spell if condition returns True
# If condition fails, return "Spell fizzled"
# Both condition and spell receive the same arguments
def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


# Return a function that casts all spells in order
# Each spell receives the same arguments
# Return a list of all spell results
def spell_sequence(spells: List[callable]) -> callable:
    pass

# =============================================================================
# ============================== UTILITY ======================================
# =============================================================================


def fireball(name: str) -> str:
    return (f"Fireball hits {name}")


def heals(name: str) -> str:
    return (f"Heals {name}")


def amp(power: int) -> int:
    return (power)


def main() -> None:
    print()

# *****************************************************************************
# *                          spell_combiner()                                 *
# *                                                                           *
    print(f"{green}Testing spell combiner...{reset}")
    combined = spell_combiner(fireball, heals)
    print("Combined spell result:", *combined("Dragon"))

# *****************************************************************************
# *                         power_amplifier()                                 *
# *                                                                           *

    print(f"{green}Testing power amplifier...{reset}")
    ampli = power_amplifier(amp, 3)
    print(f"Original: {ampli(10)[0]}, Amplified: {ampli(10)[1]}")


if __name__ == "__main__":
    main()
