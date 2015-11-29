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
    while sentences_seen <= sentences:
        if state[0].endswith("."):
            sentences_seen += 1
        result += state[0] + " "
        state = get_next_state(state, corpus)
    return result


input = """
If I speak in the tongues of men or of angels, but do not have love, I am only a resounding gong or a clanging cymbal.
If I have the gift of prophecy and can fathom all mysteries and all knowledge, and if I have a faith that can move mountains,
but do not have love, I am nothing. If I give all I possess to the poor and give over my body to hardship that I may boast, but do not have love,
I gain nothing.
Love is patient, love is kind. It does not envy, it does not boast, it is not proud. It does not dishonor others, it is
not self-seeking, it is not easily angered, it keeps no record of wrongs. Love does not delight in evil but rejoices with the truth.
It always protects, always trusts, always hopes, always perseveres.
Love never fails. But where there are prophecies, they will cease; where there are tongues, they will be stilled; where there is
knowledge, it will pass away. For we know in part and we prophesy in part, but when completeness comes, what is in part disappears.
When I was a child, I talked like a child, I thought like a child, I reasoned like a child. When I became a man, I put the ways of childhood behind me.
For now we see only a reflection as in a mirror; then we shall see face to face. Now I know in part; then I shall know fully, even as I am fully known.
And now these three remain: faith, hope and love. But the greatest of these is love.
Lucius Tarquinius, for his excessive pride surnamed Superbus, after he had caused his own father-in-law Servius Tullius to be cruelly murdered, and,
contrary to the Roman laws and customs, not requiring or staying for the people's suffrages, had possessed himself of the kingdom, went, accompanied
with his sons and other noblemen of Rome, to besiege Ardea. During which siege the principal men of the army meeting one evening at the tent of Sextus
Tarquinius, the king's son, in their discourses after supper every one commended the virtues of his own wife: among whom Collatinus extolled the
incomparable chastity of his wife Lucretia. In that pleasant humour they posted to Rome; and intending, by their secret and sudden arrival, to make
trial of that which every one had before avouched, only Collatinus finds his wife, though it were late in the night, spinning amongst her maids: the
other ladies were all found dancing and revelling, or in several disports. Whereupon the noblemen yielded Collatinus the victory, and his wife the fame.
At that time Sextus Tarquinius being inflamed with Lucrece' beauty, yet smothering his passions for the present, departed with the rest back to the camp;
from whence he shortly after privily withdrew himself, and was, according to his estate, royally entertained and lodged by Lucrece at Collatium.
The same night he treacherously stealeth into her chamber, violently ravished her, and early in the morning speedeth away. Lucrece, in this lamentable
plight, hastily dispatcheth messengers, one to Rome for her father, another to the camp for Collatine. They came, the one accompanied with Junius Brutus,
the other with Publius Valerius; and finding Lucrece attired in mourning habit, demanded the cause of her sorrow. She, first taking an oath of them for
her revenge, revealed the actor, and whole manner of his dealing, and withal suddenly stabbed herself. Which done, with one consent they all vowed to root
out the whole hated family of the Tarquins; and bearing the dead body to Rome, Brutus acquainted the people with the doer and manner of the vile deed, with
a bitter invective against the tyranny of the king: wherewith the people were so moved, that with one consent and a general acclamation the Tarquins were
all exiled, and the state government changed from kings to consuls.
"""

print(generate(parse(input)))
