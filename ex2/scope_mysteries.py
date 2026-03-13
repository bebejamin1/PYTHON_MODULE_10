#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 10:59:57 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/13 11:20:08 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, Any


green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"

# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================
"""
Le mot-clé nonlocal permet de modifier une variable définie dans la portée
de la fonction parente.

Il est indispensable pour créer des fermetures (closures) capables de
maintenir et de mettre à jour un état interne (comme un compteur ou un
accumulateur) sans avoir recours aux variables globales. Il lie
explicitement un nom de variable à l'espace de noms immédiatement supérieur
qui n'est pas global.
"""


# ============================== COUNTER ======================================

def mage_counter() -> callable:
    count: int = 0

    def counter() -> str:
        nonlocal count
        count += 1
        return (f"Call {count}: {count}")

    return (counter)


# ============================ ACCUMULATOR ====================================

def spell_accumulator(initial_power: int) -> callable:
    power: int = 0
    count: int = 0

    def accumulator() -> str:
        nonlocal power, count
        power += initial_power
        count += 1
        return (f"- Accumulator {count}: {power}")

    return (accumulator)


# ============================= ENCHANTMENT ===================================

def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(name: str) -> str:
        nonlocal enchantment_type
        enchantment_type = enchantment_type
        return (f"{enchantment_type} {name}")

    return (enchantment)


# =============================== MEMORY ======================================

def memory_vault() -> Dict[str, callable]:
    memory: Dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        nonlocal memory
        memory = memory
        memory[key] = value

    def recall(key: Any) -> Any:
        nonlocal memory
        memory = memory
        value: Any = memory.get(key)
        if (value is None):
            return ("Memory not found")
        return (value)

    return {"recall": recall, "store": store}


# =============================================================================
# =============================== MAIN ========================================
# =============================================================================

def main() -> None:
    print()
# *****************************************************************************
# *                           mage_counter()                                  *
# *                                                                           *

    print(f"{green}Testing mage counter...{reset}")
    counter: callable = mage_counter()
    for c in range(3):
        print(counter())

# *****************************************************************************
# *                         spell_accumulator()                               *
# *                                                                           *

    print("\n" + f"{green}Testing spell accumulator...{reset}")
    accumulator: callable = spell_accumulator(8)
    for c in range(3):
        print(accumulator())

# *****************************************************************************
# *                        enchantment_factory()                              *
# *                                                                           *

    print("\n" + f"{green}Testing enchantment factory...{reset}")
    flaming: callable = enchantment_factory("Flaming")
    frozen: callable = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

# *****************************************************************************
# *                           memory_vault()                                  *
# *                                                                           *

    print("\n" + f"{green}Testing memory vault...{reset}")
    data: Dict[Any, Any] = {12: "Bonjour", "bonjour": 42}
    m: Dict[str, callable] = memory_vault()

    for key, value in data.items():
        m["store"](key, value)

    for key in data.keys():
        print(m["recall"](key))


if __name__ == "__main__":
    main()
