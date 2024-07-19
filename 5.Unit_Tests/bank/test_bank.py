from bank import value

def test_value():
    # Test for exact match with different cases
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

    # Test for starting with 'h' but not 'hello'
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("HI") == 20

    # Test for other cases
    assert value("shalom") == 100
    assert value("Shalom") == 100
    assert value("SHALOM") == 100
