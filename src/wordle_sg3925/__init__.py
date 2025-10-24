# read version from installed package
from importlib.metadata import version
__version__ = version("wordle_sg3925")

from .wordle_sg3925 import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)

__all__ = [
    "validate_guess",
    "check_guess",
    "is_valid_word",
    "calculate_game_score",
]

