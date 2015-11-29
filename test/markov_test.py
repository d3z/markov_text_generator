import unittest
from markov import parse, generate


class MarkovTests(unittest.TestCase):
    def test_parse(self):
        corpus = parse("This is some text.")
        self.assertDictEqual({("This", "is"): ["some"], ("is", "some"): ["text."]}, corpus)

    def test_generate(self):
        corpus = parse("This is some text.")
        generated = generate(corpus)
        self.assertEqual("This is some text.", generated)

    def test_generate_number_of_sentences(self):
        corpus = parse("This is some text. This is some more text. And some more. Have some more text.")
        for x in range(1, 5):
            generated = generate(corpus, x)
            number_of_sentences = generated.count(".")
            self.assertEqual(x, number_of_sentences)
