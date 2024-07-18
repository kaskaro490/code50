from twttr import shorten

def test_twttr(word, vowels):
    assert shorten("twitter") == "twttr"
