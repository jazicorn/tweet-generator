import sys
import random
import histogram

input_list = histogram.histogram()

# input_list = ['cat', 'cat', 'dog', 'dog', 'animal', 'circus', 'greet']

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


def word_sample():
    his = histogram()
    total = 0

    for key in his:
        total += his[key]

    randomized = random.randrange(total)
    line_total = 0

    for key in his:
        line_total += his[key]

        if randomized < line_total:
            return key
            # print(key)


def prob_sample():
    new_dic = {}
    counter = 1000

    while counter > 0:
        random_word = word_sample() 

        if random_word in new_dic:
            new_dic[random_word] += 1

        else:
            new_dic[random_word] = 1
        counter -= 1

    return new_dic
    # print(new_dic)

if __name__ == '__main__':
    print('\nStachastic Sampling: {}'.format(prob_sample()))

