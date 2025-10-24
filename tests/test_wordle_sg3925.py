

from wordle_sg3925 import validate_guess, check_guess, is_valid_word

def test_validate_guess():
    assert validate_guess('crane') is True
    assert not validate_guess('Crane')
    assert not validate_guess('cr4ne')
    assert not validate_guess('toolong')

def test_check_guess_basic():
    assert check_guess('crane', 'crane') == [
        ('c','green'), ('r','green'), ('a','green'), ('n','green'), ('e','green')
    ]
    assert check_guess('crane', 'blimp') == [
        ('b','gray'), ('l','gray'), ('i','gray'), ('m','gray'), ('p','gray')
    ]
