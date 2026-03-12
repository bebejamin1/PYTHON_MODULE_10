#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 15:02:39 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/12 17:41:07 by bbeaurai           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


from typing import Any

from functools import wraps
import time


green = "\033[32m\033[1m\033[1m"
red = "\033[31m\033[5m\033[1m"
redp = "\033[31m"
brown = "\033[0;33m"
blue = "\033[38;5;67m"
reset = "\033[0m"


# =============================================================================
# ============================= FONCTIONS =====================================
# =============================================================================


def spell_timer(func: callable) -> callable:

    @wraps(func)
    def wrapper(*args, **kwargs) -> callable:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"Casting {func.__name__}...")
        print(f"Spell completed in {end - start:.8f} seconds")
        return (result)

    return (wrapper)


def power_validator(min_power: int) -> callable:

    def func_validator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> callable:

            if (len(args) > 1):
                if (args[2] >= min_power):
                    return (func(*args, **kwargs))
            elif (len(args) <= 1):
                if (args[0] >= min_power):
                    return (func(*args, **kwargs))
            return ("Insufficient power for this spell")

        return (wrapper)

    return (func_validator)


def retry_spell(max_attempts: int) -> callable:

    def func_retry(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> callable:
            test = 1
            mana = args[0]
            while (test <= max_attempts):
                try:
                    mana += 1
                    return func(mana, **kwargs)
                except Exception as e:
                    print(f"{e} retrying... (attempt {test}/{max_attempts})")
                test += 1
            return f"Spell casting failed after {max_attempts} attempt"

        return (wrapper)

    return (func_retry)


class MageGuild():

    # Name is valid if it’s at least 3 characters and contains
    # only letters/spaces
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    # Should use the power_validator decorator with min_power=10
    # Return "Successfully cast spell_name with power power"
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


# =============================================================================
# ============================= UTILITIES =====================================
# =============================================================================


@spell_timer
def fireball() -> str:
    return ("Fireball cast !")


@power_validator(5)
def cast_fireball(power: int) -> str:
    return "Fireball casted successfully"


@retry_spell(5)
def retry_lightning(power: int) -> str:
    if power < 8:
        raise Exception("Spell failed")
    return "lightning casted successfully"


# =============================================================================
# =============================== MAIN ========================================
# =============================================================================


def main() -> None:
    print()
# *****************************************************************************
# *                           spell_timer()                                   *
# *                                                                           *
    print(f"{green}Testing spell timer...{reset}")
    fire = fireball()
    print(fire)

# *****************************************************************************
# *                         power_validator()                                 *
# *                                                                           *
    print("\n" + f"{green}Testing power validator...{reset}")
    mana = 8
    print(f"Casting fireball with {mana} mana: {cast_fireball(mana)}")
    mana = 2
    print(f"Casting fireball with {mana} mana: {cast_fireball(mana)}")

# *****************************************************************************
# *                          retry_spell()                                    *
# *                                                                           *
    print("\n" + f"{green}Testing retry spell...{reset}")
    print(f"Trying cast spell: {retry_lightning(5)}")

# *****************************************************************************
# *                           MageGuild()                                     *
# *                                                                           *
    print("\n" + f"{green}Testing MageGuild...{reset}")


if __name__ == "__main__":
    main()
