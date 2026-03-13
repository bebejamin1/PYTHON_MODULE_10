#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 15:02:39 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/13 11:28:12 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from typing import Any, Dict, Tuple, List

from functools import wraps
import time


green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"


# =============================================================================
# ========================= FONCTIONS / CLASS =================================
# =============================================================================
"""
Le wrapper est l'emballage protecteur (ou le costume) de ton sortilège.

C'est une fonction intermédiaire qui entoure ton sort original pour lui ajouter
des pouvoirs supplémentaires sans modifier son code interne. Il permet
d'effectuer des actions juste avant le lancement (comme vérifier la puissance)
et juste après (comme calculer le temps d'exécution), tout en s'assurant que
le sort produit bien son effet final.
"""


# =============================== TIMER =======================================

def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args: Tuple[int, ...], **kwargs: Dict[str, int]) -> callable:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Casting {func.__name__}...")
        print(f"Spell completed in {end - start:.8f} seconds")
        return (result)

    return (wrapper)


@spell_timer
def fireball() -> str:
    return ("Fireball cast !")


# ============================= VALIDATOR =====================================

def power_validator(min_power: int) -> callable:

    def func_validator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> callable:

            if (len(args) > 1):
                if (args[2] >= min_power):
                    return (func(*args, **kwargs))
            elif (len(args) <= 1):
                if (args[0] >= min_power):
                    return (func(*args, **kwargs))
            return ("Insufficient power for this spell")

        return (wrapper)

    return (func_validator)


@power_validator(5)
def cast_fireball(power: int) -> str:
    return ("Fireball casted successfully")


# =============================== RETRY =======================================

def retry_spell(max_attempts: int) -> callable:

    def func_retry(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> callable:
            test: int = 1
            mana: int = args[0]
            while (test <= max_attempts):
                try:
                    mana += 1
                    return func(mana, **kwargs)
                except Exception as e:
                    print(f"{e} retrying... (attempt {test}/{max_attempts})")
                test += 1
            return (f"{red}[ERROR]{reset} Spell casting failed "
                    f"after {max_attempts} attempt")

        return (wrapper)

    return (func_retry)


@retry_spell(5)
def retry_lightning(power: int) -> str:
    if power < 8:
        raise Exception("Spell failed")
    return ("Lightning casted successfully")


# ============================= MageGuild =====================================
"""
Le staticmethod est le code de conduite universel de ta guilde.

C'est une règle ou un outil qui appartient à la guilde elle-même, mais qui ne
dépend d'aucun mage en particulier. Tu n'as pas besoin de désigner un mage
spécifique (pas de 'self') pour l'utiliser : c'est un savoir général que
tout le monde peut consulter directement depuis le manuel de la guilde.
"""


class MageGuild():

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for n in name:
            if (not n.isalpha() and not n.isspace() or len(name) <= 3):
                return (False)
        return (True)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        if (self.validate_mage_name(spell_name)):
            return (f"Successfuly cast {spell_name} with {power} power")
        return ("The name must be >= 3 characters long " + "\n"
                "and contain only letters and spaces.")


# =============================================================================
# =============================== MAIN ========================================
# =============================================================================


def main() -> None:
    print()
# *****************************************************************************
# *                           spell_timer()                                   *
# *                                                                           *

    print(f"{green}Testing spell timer...{reset}")
    fire: str = fireball()
    print(fire)

# *****************************************************************************
# *                         power_validator()                                 *
# *                                                                           *

    print("\n" + f"{green}Testing power validator...{reset}")
    mana: int = 8
    print(f"Casting fireball with {mana} mana: {cast_fireball(mana)}")
    mana: int = 2
    print(f"Casting fireball with {mana} mana: {cast_fireball(mana)}")

# *****************************************************************************
# *                          retry_spell()                                    *
# *                                                                           *

    print("\n" + f"{green}Testing retry spell...{reset}")
    print(f"Trying cast spell: {retry_lightning(5)}")

# *****************************************************************************
# *                           MageGuild()                                     *
# *                                                                           *

    names: List[str] = ["lighting", "123456789"]
    powers: List[int] = [15, 9]

    print("\n" + f"{green}Testing MageGuild...{reset}")
    mage: MageGuild = MageGuild()

    for name in names:
        print(mage.validate_mage_name(name))

    for name, power in zip(names, powers):
        print(mage.cast_spell(name, power))


if __name__ == "__main__":
    main()
