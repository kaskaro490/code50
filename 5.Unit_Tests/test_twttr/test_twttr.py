from twttr import shorten

def test_twttr():
    #vowels = ["a","e","i","o","u","A","E","I","O","U"]
    #words = ["twitter","autism","rocket","social","explicit","video","search","browser","minautor","maze"]
    assert shorten("twitter", vowels) == "twttr"
