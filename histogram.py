def load_script():

    f = open('grimm-fairy-tales.txt', 'r')
    t = f.readlines()
    # content = ['cat', 'cat', 'dog', 'dog', 'animal', 'circus', 'greet']

    f.close()

    return t


def create_sample():
    empty_list = []
    t = load_script()

    for i in t[1:100]:
        empty_list.append(i.strip())
        sample_list = list(filter(None, empty_list))
    return sample_list
    
def create_list():
    final_list = []
    sample_list = create_sample()
    for row in sample_list:
        string = row.split()
        for word in string:
            final_list.append(word)
    
    return final_list

def histogram_dictionary():
    sample_list = create_list()
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
    sample_list = create_list()
    
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
    return array_list
        

def histogram_tuple():
    hist_list = histogram_list()
    print(hist_list)

    histogram_tuple = []

    for word in hist_list:
        histogram_tuple.append(tuple(word))

    print(histogram_tuple)


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
    histogram_dictionary()
    histogram_list()
    histogram_tuple()
