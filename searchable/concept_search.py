import nltk
from nltk.corpus import wordnet as wn


def synonyms(word):
    word_list = []
    for i, j in enumerate(wn.synsets(word)):
        words = j.lemma_names()
        for item in words:
            if item not in word_list:
                word_list.append(item)
    return word_list


dict = {}


def find_word(word, text):
    word_list = synonyms(word)
    for item in word_list:
        if not item == word:
            if item in text and word not in dict:
                dict[word] = [item]
            elif word in dict and item in text:
                dict[word].append(item)


def word_to_concepts(text):
    text = text.split()
    for item in text:
        find_word(item, text)
    return dict

print(word_to_concepts("Hey there little small modest friend hello hi pal companion"))