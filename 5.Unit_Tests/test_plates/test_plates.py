from plates import is_valid



def s):
    assert test_check_length("OUTATIME") == False
    assert test_check_length("H") == False

def test_check_start_letters(s):
    assert is_valid("CS50") == True

def test_check_characters(s):
    assert is_valid("CS50") == True
    assert is_valid("PI3.14") == False

def test_check_numbers(s):
    assert is_valid("CS05P") == False
