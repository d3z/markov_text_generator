import re
import random


def clean_text(input):
    text = re.sub(r"\n", " ", input)
    return text


def states(words, state_size):
    for index in range(len(words) - state_size):
        state = []
        for x in range(state_size):
            state.append(words[index + x])
        yield (tuple(state), words[index + state_size])


def parse(text, state_size=2):
    corpus = {}
    words = clean_text(text).split(" ")
    for state in states(words, state_size):
        (key, value) = state
        corpus[key] = corpus.get(key, []) + [value]
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
