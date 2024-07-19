from plates import is_valid


def test_is_valid(s):
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == True
    assert is_valid("OUTATIME") == True
    assert is_valid("CS50") == True

def test_check_length(s):

    assert is_valid("OUTATIME") == True

def test_check_start_letters(s):
    assert is_valid("CS50") == True

def test_check_characters(s):
    assert is_valid("CS50") == True

def test_check_numbers(s):
    assert is_valid("CS05P") == False
