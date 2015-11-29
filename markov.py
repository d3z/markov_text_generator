import re
import random


def clean_text(input):
    text = re.sub(r"\n", " ", input)
    return text


def triplets(words):
    for index in range(len(words) - 2):
        yield (words[index], words[index+1], words[index+2])


def parse(text):
    corpus = {}
    words = clean_text(text).split(" ")
    for (w1, w2, w3) in triplets(words):
        key = (w1, w2)
        corpus[key] = corpus.get(key, []) + [w3]
    return corpus


def get_starting_state(corpus):
    return random.choice([state for state in corpus.keys() if re.match("^[A-Z].*", state[0])])


def get_next_state(state, corpus):
    next_state = (state[1], random.choice(corpus[state]))
    return next_state


def generate(corpus, sentences=5):
    sentences_seen = 0
    result = ""
    state = get_starting_state(corpus)
    while sentences_seen < sentences:
        if state[0].endswith("."):
            sentences_seen += 1
        result += state[0] + " "
        try:
            state = get_next_state(state, corpus)
        except(KeyError):
            return result + state[1]
    return result
