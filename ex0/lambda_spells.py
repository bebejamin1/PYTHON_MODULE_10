#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/11 10:03:44 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/12 10:08:25 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import List

green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"

# The goal is to master anonymous functions and functional programming patterns

# =============================================================================
# ================================ DATA =======================================
# =============================================================================

artifacts = [
    {"name": "Fire Staff", "power": 92, "type": "fire"},
    {"name": "Crystal Orb", "power": 85, "type": "crystal"}
            ]

mages = [
    {"name": "Gold Ark", "power": 26, "element": "fire"},
    {"name": "Urn of Doom", "power": 15, "element": "wind"},
    {"name": "Feather of Enigmas", "power": 9, "element": "water"},
    {"name": "Statuette of the Gods", "power": 2, "element": "tree"},
        ]

spells = ["fireball", "heal", "shield"]


# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================


def artifact_sorter(artifacts: List[dict]) -> List[dict]:
    return (list(sorted(artifacts, key=lambda x: x['power'], reverse=True)))


def power_filter(mages: List[dict], min_power: int) -> List[dict]:
    return (list(filter(lambda x: x['power'] >= min_power, mages)))


def spell_transformer(spells: List[str]) -> List[str]:
    return (list(map(lambda x: "* " + x + " *", spells)))


def mage_stats(mages: List[dict]) -> dict:
    return {
        "max": max(mages, key=lambda x: x['power'])['power'],
        "min": min(mages, key=lambda x: x['power'])['power'],
        "avg": sum([power['power'] for power in mages]) / round(len(mages), 2)
           }


def main() -> None:
    try:
        print()
# *****************************************************************************
# *                         artifact_sorter()                                 *
# *                                                                           *

        print(f"{green}Testing artifact sorter...{reset}")

        art_list = []
        for artifact in artifact_sorter(artifacts):
            art_list.append(f"{artifact['name']} ({artifact['power']} power)")
        print(*art_list, sep=" comes before ")

# *****************************************************************************
# *                          power_filter()                                   *
# *                                                                           *

        print("\n" + f"{green}Testing power filter...{reset}")

        min_power = 9
        print("All mages who have more power "
              f"than the minimum power ({min_power})")
        for mage in power_filter(mages, min_power):
            print(f"{mage['name']} with {mage['power']}")

# *****************************************************************************
# *                        spell_transformer()                                *
# *                                                                           *

        print("\n" + f"{green}Testing spell map...{reset}")

        spell = spell_transformer(spells)
        print(*spell)

# *****************************************************************************
# *                           mage_stats()                                    *
# *                                                                           *

        print("\n" + f"{green}Testing mage stats...{reset}")

        stats = mage_stats(mages)
        for ope, result in stats.items():
            print(f"{ope} = {result}")

    except NameError as e:
        print(f"{red}[ERROR]{reset} {e}")


if __name__ == "__main__":
    main()
