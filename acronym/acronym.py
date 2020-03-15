import re


def abbreviate(words):
    cleanString = re.sub(r'[_-]', ' ', words)
    word_list = re.split(r"\s", cleanString)
    filtered_list = list(filter(lambda word: word, word_list))
    acronym = "".join(list(map(lambda word: word[0], filtered_list)))
    return(acronym.upper())
