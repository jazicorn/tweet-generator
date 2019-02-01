def load_script():

    f = open('words.txt', 'r')
    # content = f.read().split()
    content = ['cat', 'cat', 'dog', 'dog', 'animal', 'circus', 'greet']
    f.close()

    return content


def create_list():
    empty_list = []
    content = load_script()
    for word in content[:100]:
        empty_list.append(word)
    # print(sample_list)
    sample_list = tuple(empty_list)
    return sample_list


def histogram_dictionary():
    sample_list = load_script()
    dictionary = {}

    for word in sample_list:
        if word not in dictionary: 
            dictionary.update({word:1})
        else:
            the_value = dictionary[word]
            the_value += 1
            dictionary.update({word:the_value})

    print(dictionary)

def histogram_list():
    sample_list = load_script()
    
    array_list = []

    add_word = False

    for word in sample_list:
        add_word = False
        for row in array_list:

            if word == row[0]:
                row[1] += 1
                add_word = True

        if add_word == False:
            array_list.append([word,1])

    print(array_list)
        

    


def histogram_tuple():
    pass


def histogram():
    '''
    takes a source_text argument (can be either a filename or the contents of the file as a string)
    and return a histogram data structure that stores each unique word
    along with the number of times the word appears in the source text
    '''
    pass


def unique_words():
    '''
    takes a histogram argument and 
    returns the total count of unique words in th histogram
    '''
    pass

def frequency():
    '''
    takes a word and histogram argument and 
    returns the number of times that word appears in a text.
    '''
    pass

if __name__ == '__main__':
    # histogram_list()
    histogram_dictionary()
    histogram_list()