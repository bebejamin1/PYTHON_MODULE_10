#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 10:59:57 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/12 12:07:36 by bbeaurai           ###   ########.fr      #
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


def mage_counter() -> callable:
    count = 0

    def counter() -> str:
        nonlocal count
        count += 1
        return (f"Call {count}: {count}")

    return (counter)


def spell_accumulator(initial_power: int) -> callable:
    power = 0
    count = 0

    def accumulator() -> str:
        nonlocal power, count
        power += initial_power
        count += 1
        return (f"- Accumulator {count}: {power}")

    return (accumulator)


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(name: str) -> str:
        nonlocal enchantment_type
        return (f"{enchantment_type} {name}")

    return (enchantment)


def memory_vault() -> Dict[str, callable]:
    memory = {}

    def store(key: Any, value: Any) -> None:
        nonlocal memory
        memory[key] = value

    def recall(key: Any) -> Any:
        nonlocal memory
        value = memory.get(key)
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
    counter = mage_counter()
    for c in range(3):
        print(counter())

# *****************************************************************************
# *                         spell_accumulator()                               *
# *                                                                           *
    print("\n" + f"{green}Testing spell accumulator...{reset}")
    accumulator = spell_accumulator(8)
    for c in range(3):
        print(accumulator())

# *****************************************************************************
# *                        enchantment_factory()                              *
# *                                                                           *
    print("\n" + f"{green}Testing enchantment factory...{reset}")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

# *****************************************************************************
# *                           memory_vault()                                  *
# *                                                                           *
    print("\n" + f"{green}Testing memory vault...{reset}")
    data = {12: "Bonjour", "bonjour": 42}
    m = memory_vault()
    for key, value in data.items():
        m["store"](key, value)

    for key in data.keys():
        print(m["recall"](key))


if __name__ == "__main__":
    main()
