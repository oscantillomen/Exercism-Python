import string
ALPHABET = set(string.ascii_lowercase)

def is_pangram(sentence):
    return ALPHABET <= set(sentence.lower())