from twttr import shorten

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("AEIOU") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("Python Programming") == "Pythn Prgrmmng"
