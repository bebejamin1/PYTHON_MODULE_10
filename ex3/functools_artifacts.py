#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 13:09:34 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/13 11:24:49 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Dict, List, Any

from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul

green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"


# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================


# ============================== REDUCER ======================================
""" reduce(f, [x_1, x_2, x_3, x_4])
Reduce est le compresseur de ta bibliothèque
Il fusionne une liste d'éléments en une seule valeur finale en les combinant
deux par deux, de proche en proche, jusqu'à obtenir un résultat unique
"""


def spell_reducer(spells: List[int], operation: str) -> int:
    if (operation == "add"):
        return (reduce(add, spells))
    if (operation == "multiply"):
        return (reduce(mul, spells))
    if (operation == "max"):
        return (reduce(max, spells))
    if (operation == "min"):
        return (reduce(min, spells))
    else:
        return


# ============================== PARTIAL ======================================
"""
Partial est le préparateur de commandes de ta bibliothèque.

Il permet de créer une version "pré-remplie" d'un sort complexe en fixant
certains de ses paramètres à l'avance (comme la puissance ou l'élément).
Cela génère une nouvelle fonction plus simple qui ne demande plus que les
informations manquantes (comme la cible) pour être lancée.
"""


def partial_enchanter(base_enchantment: callable) -> Dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "light"),
           }


def base_enchantment(power: int, element: str, target: str) -> str:
    return (f"Enchantment {element} attacks {target} with a power of {power}")


# ============================= LRU_CACHE =====================================
"""
Lru_cache est le pupitre de lecture de ton archiviste.

Il retient en mémoire les résultats des calculs les plus récents pour éviter
de les refaire plusieurs fois. Si tu lui redemandes le même sort, il te
donne la réponse instantanément au lieu de retourner fouiller dans les
tréfonds de la bibliothèque, ce qui booste énormément la vitesse de ton code.
"""


@lru_cache()
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return (n)
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


# ============================ DISPATCHER =====================================
"""
Le dispatcher est l'aiguilleur de ta bibliothèque.

Il examine la nature de l'objet que tu lui confies (un nombre pour les dégâts,
un texte pour l'enchantement ou une liste pour le multi-cast) pour choisir
automatiquement le traitement approprié. C'est une porte d'entrée unique qui
redirige chaque type de donnée vers le sortilège qui lui correspond.
"""


def spell_dispatcher() -> callable:
    @singledispatch
    def dispatcher(s: Any) -> str:
        return (f"{s} Unknown argument, argument must be one of "
                "these different types (int, str, or list)")

    @dispatcher.register(int)
    def _(s: int) -> str:
        return (f"You have entered a number: {s}")

    @dispatcher.register(str)
    def _(s: str) -> str:
        return (f"You have entered a string of characters: {s}")

    @dispatcher.register(list)
    def _(s: List[str]) -> str:
        return (f"You have entered a list: {s}")

    return (dispatcher)


# =============================================================================
# =============================== MAIN ========================================
# =============================================================================

def main() -> None:
    print()
# *****************************************************************************
# *                          spell_reducer()                                  *
# *                                                                           *

    print(f"{green}Testing spell reducer...{reset}")
    operations: List[str] = ["add", "multiply", "max", "min"]
    spells: List[int] = [10, 50, 40]

    for operation in operations:
        print(operation, spell_reducer(spells, operation))

# *****************************************************************************
# *                        partial_enchanter()                                *
# *                                                                           *

    print("\n" + f"{green}Testing partial enchanter...{reset}")
    partial_test: Dict[str, callable] = partial_enchanter(base_enchantment)
    targets: List[str] = ["BLEU", "BLANC", "ROUGE"]

    for value, target in zip(partial_test.values(), targets):
        print(f"- {value(target)}")

# *****************************************************************************
# *                       memoized_fibonacci()                                *
# *                                                                           *

    print("\n" + f"{green}Testing memoized fibonacci...{reset}")
    f1: int = 10
    print(f"Fib({f1})", memoized_fibonacci(f1))
    f1: int = 15
    print(f"Fib({f1})", memoized_fibonacci(f1))

# *****************************************************************************
# *                        spell_dispatcher()                                 *
# *                                                                           *

    print("\n" + f"{green}Testing spell dispatcher...{reset}")
    types: List[Any] = [42, "Bonjour", ["Hello", "Bonjour"]]
    dis: callable = spell_dispatcher()

    for type in types:
        print(dis(type))


if __name__ == "__main__":
    main()
