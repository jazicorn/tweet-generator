import sys
import random

class dictionary_words():
    def __init__(self, word_list=None):
        pass

    def load_script():

        f = open('/usr/share/dict/words', 'r')
        content = f.read()
        f.close()

        lines = []

        lines.append(content)

        for dictionary_list in lines:
            # print(element)
            return dictionary_list


    def select_random():
        random_words = []
        random.choice(element)

    def create_string():
        pass

if __name__ == '__main__':
