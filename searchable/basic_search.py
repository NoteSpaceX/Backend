import nltk
from nltk.book import *
from nltk.corpus.reader import CategorizedCorpusReader


# finds out other word appear in similar context
def similar_context(text, word):
    dict = {}
    dict[word] = text.similar(word)
    # dict = {word: text.similar(word)}
    list(dict)
    for key, val in sorted(dict.items()):
        print(key + ":", val)


def gender_features(word):
    return {'last_letter': word[-1]}

# occurrence of a given word with some context

def main():

    similar_context(text1, "monstrous")

    print(gender_features("Shrek"))

if __name__ == "__main__":
    main()