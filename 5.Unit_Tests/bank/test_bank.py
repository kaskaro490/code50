from bank import value

def test_value():
    assert value("hello").lower() == 0
    assert value("hi").lower() == 20
    assert value("shalom").lower() == 100

