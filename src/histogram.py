import sys
import os
os.system('clear')
import random

from termcolor import colored, cprint

def load_script():

    f = open('grimm-fairy-tales.txt', 'r')
    t = f.readlines()
    # content = ['cat', 'cat', 'dog', 'dog', 'animal', 'circus', 'greet']

    f.close()

    return t


def create_sample():
    """ Creates list of words from first [10] words of loadscript() """
    empty_list = []
    t = load_script()

    for i in t[1:10]:
        empty_list.append(i.strip())
        # filter() gets rid of empty strings in list
        sample_list = list(filter(None, empty_list))

    return sample_list


def create_list():
    final_list = []
    sample_list = create_sample()
    for row in sample_list[:100]:
        string = row.split()
        for word in string:
            final_list.append(word)
    
    return final_list


def welcome():

    welcome = colored("Welcome to Histogram Maker\nThe Brother's Grimm Fairy Tales Edition\n", 'magenta',attrs=['bold'])

    print(welcome)


def return_menu():

    print(
        "[1] Main Menu\n"
        "[2] Quit\n"
    )

    return_input()


def return_input():
    user_input = int_validation()
    
    os.system ('clear')
    if user_input == 1:
        main_menu()
    
    elif user_input == 2:
        goodbye()
    
    if len(user_input) > 1:
        print("Error Warning: Please choose 1 menu item at a time\n")
        return_menu()
    else:
        print("unknown error")
        main_menu()


def goodbye():

    script = "Are you sure you want to quit?\n\n[1] Yes\n[2] No\n\nMenu #"
    
    user_input = input(script)

    os.system ('clear')

    if user_input == str(1):
        sys.exit()
    elif user_input == str(2):
        print("Welcome Back!\n")
        main_menu()
    else:
        print("Unknown Error")
        return_menu()


def int_validation():

    user_input = input("Menu #: ")

    if len(user_input) > 1:
        print("Error Warning: Please choose 1 menu item at a time\n")
        return_menu()

    elif user_input.isalpha():
        if 'Q' in user_input.capitalize():
            goodbye()
        else:
            print("Error Warning: Numbers Only")
            print("Error Warning: Choose corresponding number of desired menu item\n")
            return_menu()
    else:
        try:
            val = int(user_input)

        except ValueError:
            print("Error Warning: Number Inputs Only")
            main_menu()
    
    return val
    
def main_menu(): 

    welcome()

    cprint("Choose Numbers 1 - 7", 'green')
    print(
    "\n[1] Histogram Definition\n"
    "[2] Histogram type: dictionary key-value pairs\n"
    "[3] Histogram type: list of lists\n"
    "[4] Histogram type: list of tuples\n"
    "[5] [Total] unique words in text\n"
    "[6] [Frequency] search for a single word in the text"
    )

    cprint("\n[7] Quit\n", 'red')

    main_input()


def main_input():

    user_input = int_validation()

    os.system ('clear')

    if user_input == 1:
        histogram_definition()

    elif user_input == 2:
        print("Histogram_dictionary:\n\n{} \n".format(histogram()))   

    elif user_input == 3:
        print("Histogram_list:\n\n{} \n".format(histogram_list()))

    elif user_input == 4:
        print("Histogram_tuple:\n\n{} \n".format(histogram_tuple()))
    
    elif user_input == 5:
        print("Unique words in Histogram_dictionary\nCount:{} \n".format(len(unique_words())))

    elif user_input == 6:
        frequency_menu()
    
    elif user_input == 7:
        goodbye()
            
    else:
        print("Error Warning: you can only numbers: 1-5 \n")

    return_menu()


def histogram_definition():

    print("What is a Histogram?\n")

    print("- Takes a source_text argument (can be either a filename or the contents of the file as a string)\n- Returns a data structure that stores each unique word with the number of times it appears in the source text\n")

def histogram():
    sample_list = create_list()
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


def histogram_list():
    sample_list = create_list()
    
    array_list = []

    for word in sample_list:
        add_word = False
        for row in array_list:

            if word == row[0]:
                row[1] += 1
                add_word = True

        if add_word == False:
            array_list.append([word,1])

    # print(array_list)
    return array_list
 

def histogram_tuple():
    hist_list = create_list()
    # print(hist_list)

    histogram_tuple = []

    for word in hist_list:
        found = False
        for inner_tuple in histogram_tuple:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                histogram_tuple.remove(inner_tuple)
                histogram_tuple.append((word,count))

        if not found:
            histogram_tuple.append((word,1))

    # print(histogram_tuple)
    return histogram_tuple


def unique_words():
    text_list = create_list()

    unique_words = []

    for word in text_list:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words


def frequency_menu():

    cprint("Find out how many times a given word is in the Brothers Grimm Fairy Tales\n", 'cyan')
    
    print(
        "[1] Choose Word\n"
        "[2] Main Menu\n"
        "[3] Quit\n"
    )

    frequency_input_validation()
    

def frequency_input_validation():

    user_input = input("\nMenu #: ")

    # intvalidation = user_input.isdigit()

    # strvalidation = user_input.isalpha()

    if user_input.isdigit():
        print("HI")

        if user_input == int(2):            
            # frequency_script()
            os.system ('clear')
            main_menu()

        elif user_input == 1:
            frequency_script()

        elif user_input == 3:
            os.system ('clear')
            goodbye()

        else:
            os.system ('clear')
            print("Error Try Again")
            frequency_menu()

    elif user_input.isalpha():
        frequency_script()

    else:
        os.system ('clear')
        print("Error Try Again")
        frequency_menu()
            

    return user_input


def try_again():
    print("Choose Another Word?\n\n[1] Yes\n[2] No\n")

    user_input = input("Menu #: ")

    if user_input == "1":
        os.system ('clear')
        frequency_menu()

    elif user_input == "2":
        os.system ('clear')
        goodbye()
        
    else:
        print("Error Try Again")
        os.system ('clear')
        frequency_menu()


def frequency_script():
    text_list = create_list()
    word_input = input("Word Choosen: ")

    how_many = []

    if word_input not in text_list:
        os.system ('clear')
        print("\nWord not in list. Try Again\n")
        frequency_menu()

    else: 

        for word in text_list:
            if word == word_input:
                how_many.append(word_input)

        results = "\nResults: '{}' appeared {} time(s) in the text\n".format(word_input, len(how_many))

        print(results)

        try_again()


def create_columns():
    # trying to create function that prints
    # list in multiple columns
    sample_list = create_list()

    count = 10

    list_set = []

    for word in sample_list:
        list_set.append(word)
        count -= 1
    
    print(list_set)


if __name__ == '__main__':
    
    if len(sys.argv) > 2:
        print ("Hello")

    elif sys.argv[1] == 'test':
        # features yet to be implemented
        create_columns()
    
    elif sys.argv[1] == 'menu':
        main_menu()

    else:
        histogram()