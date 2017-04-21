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
    
    # iterate through the list of synonyms
    for item in word_list:
        sublist = []
        
        # make sure not getting the same word
        if not item == word:
            # make a list and add item, page number, column number to it
            sublist.append(item)
            sublist.append(Drafts.Navigate.Navigate.get_line(item, "sample.txt"))
            sublist.append(Drafts.Navigate.Navigate.get_specific_column_number(item, "sample.txt"))
            
            # turn the list into tuple
            item_tuple = tuple(sublist)
            if item in text and word not in dict:
                dict[word] = [item_tuple]
            elif word in dict and item in text and item_tuple not in dict[word]:
                dict[word].append(item_tuple)


def word_to_concepts(text):
    
    text = text.split()
    for item in text:
        find_word(item, text)
    return dict


# print(word_to_concepts("sample.txt"))
