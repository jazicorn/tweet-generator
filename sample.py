import sys
import random
import math
# import histogram

# input_list = histogram.histogram()
# print(histogram)

input_list = ['cat', 'cat', 'dog', 'dog', 'animal', 'circus', 'greet']

# input_list = sys.argv[1:]


def histogram():
    # print(input_list)
    sample_list = input_list
    dictionary = {}

    for word in sample_list:
        if word not in dictionary: 
            dictionary.update({word:1})
        else:
            the_value = dictionary[word]
            the_value += 1
            dictionary.update({word:the_value})

    # print(dictionary)
    return dictionary

def word_list():
    word_list = []
    dictionary = histogram()
    for key, value in dictionary.items():
        word_list.append(key)

    # for word in input_list:
    #     word_list.append(word)

    return word_list

def random_word():
    from_word_list = word_list()
    rand_index = random_index()
    dictionary = histogram()

    print("testing: random int: {}".format(rand_index))

    for word in from_word_list:
        print("word: {}".format(word))
        print("index of word: {}".format(from_word_list.index(word)))

    count = 0
    for key, value in dictionary.items():
        count += value

    random_word = from_word_list[rand_index]

    return random_word

def random_index():
    input_list = word_list()
    # print("len of wordlist: {}".format(len(input_list)))
    rand_index = random.randint(0, len(input_list) -1)
    print(rand_index)
    return rand_index

def percent():
    # Grabbing random word
    dictionary = histogram()
    word = random_word()
    print("Random Word: {}".format(word))

    # total amoun of words in wordlist
    total = len(word_list()) - 1
    print("Total: {}".format(total))

    # determining index number of random number
    rand_index = random_index()
    print("Random Index: {}".format(rand_index))

    # determining percent the word is in wordlist
    percent = rand_index/total
    percent_round = percent     
    print("Percent: {}\n".format(percent_round))

    #returning the percent to be used by other functions
    return percent_round

def choices():
    total = len(word_list())
    word = random_word()
    word_percent = percent()

    randomize = random.random()

    dict= []

    sum = 0

    for key in dict:
        sum += dict[key] / total

        if sum > randomize:
            print(key)

        else:
            print(sum)



# sample.py function we covered in class
def sample_in_class():
    sentence = "one fish two fish red fish blue fish"
    sentence_array = sentence.split()
    dict = histogram(sentence_array)

    total_count = len(sentence_array)
    cumulative_probability = 0

    randomized = random.random()
    for key in dict:
        cumulative_probability += dict[key] / total_count
        if cumulative_probability > randomized:
            return key



# percent()

dictionary = histogram()

value_list = list(dictionary.values())

sum = sum(value_list)
# or you can do:
# sum(i for i in a)
# sm = sum(a[0:len(a)]

#    for key, value in dictionary.items():
#         count += value

base = 0

percent_list = []

for number in value_list:

    percent = number/sum

    base += percent
    print("Index: {} percent is: {}".format(number, base))

    percent_list.append(base)

random_float = random.random()


for number in percent_list:
    if random_float < number:
        print("This random number {} was smaller than this list float: {}".format(random_float, number))
          
print("Random_float: {}".format(random_float))

# print(percent_list)


def test(seq)
count = 1000

while counter > 0:
    

