#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: bbeaurai <bbeaurai@student.42lehavre.fr>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/12 15:02:39 by bbeaurai            #+#    #+#            #
#   Updated: 2026/03/12 16:03:39 by bbeaurai           ###   ########.fr      #
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


# Create a decorator factory that validates power levels
# Check if the first argument (power) is >= min_power
# If valid, execute the function normally
# If invalid, return "Insufficient power for this spell"
# Use functools.wraps properly
def power_validator(min_power: int) -> callable:
    
    def func_validator(func: callable) -> callable:

        @wraps(func)
        def wrapper(*args, **kwargs) -> callable:
            if (len(args) > 1):
                if (args[2] >= min_power):
                    return (func(*args, **kwargs))
            elif:
                if (args[0] >= min_power):
                    return (func(*args, **kwargs))
            return ("Insufficient power for this spell")
        return (wrapper)

    return (func_validator)


# Create a decorator that retries failed spells
# If function raises an exception, retry up to max_attempts times
# Print "Spell failed, retrying... (attempt n/max_attempts)"
# If all attempts fail, return "Spell casting failed after max_attempts attempts"
# If successful, return the result normally
def retry_spell(max_attempts: int) -> callable:
    pass


class MageGuild():

    # Name is valid if it’s at least 3 characters and contains only letters/spaces
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    # Should use the power_validator decorator with min_power=10
    # Return "Successfully cast spell_name with power power"
    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


@spell_timer
def fireball() -> str:
    return ("Fireball cast !")

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


if __name__ == "__main__":
    main()
