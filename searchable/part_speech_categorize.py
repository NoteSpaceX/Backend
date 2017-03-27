import nltk
from nltk.compat import raw_input


class Categorize:
    # stores each word in a line in a list
    def text_dictionary(self):
        dict = {}
        # sentences = nltk.sent_tokenize(self)
        tokens = nltk.word_tokenize(self)
        tagged = nltk.pos_tag(tokens)

        for item in tagged:
            key = item[1]
            if key not in dict:
                dict[key] = [item[0]]
            else:
                dict[key].append(item[0])
        return dict

    def list_to_string(self):
        result = ""
        for item in self:
            result += item + " "
        return result

def main():
    print("Enter a file name: ")
    file_name = raw_input()
    text_file = open(file_name, 'r')
    text = text_file.read()

    dict = Categorize.text_dictionary(text)
    print(dict)

    print("Select a key")
    print(dict.keys())

    key = raw_input()

    if key not in dict:
        print("invalid input")
    else:
        print("These are the words that match this part of speech: " + Categorize.list_to_string(dict[key]))


if __name__ == "__main__":
    main()


