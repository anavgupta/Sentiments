import nltk


# to laod the word from a file in to a set
def load_words(word_file):
    words_set = set()
    with open(word_file, 'r') as f:
        for word in f:
            if word.startswith(';') or word == "":
                continue
            else:
                word = word.strip().lower()
                words_set.add(word)
    return words_set


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # inittating the attributes
        self.positives = load_words(positives)
        self.negatives = load_words(negatives)
        # print self.positives

    # to analyze a text and calculate a score
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        # Uses the NLTK Tweet Tokenizer
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        # print tokens
        # print [str(x.lower()) for x in tokens]

        # Categorize the text as positive, negative or neutral
        # For the words with incorrect spellings it will give neutral ratings
        score = 0
        for word in tokens:
            if word.lower() in self.negatives:
                score += -1
            elif word.lower() in self.positives:
                score += 1
            else:
                continue

        return score
