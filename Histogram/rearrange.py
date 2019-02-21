import sys
import random

# wordSplit = strList.split('');
# new_array = []
# new_array.push(wrordSplit[random.randint])
# wordSplit.pop(wordSplit[random.randint])
# new_array.join
# print(new_array)

# print(sys.argv)

# print('Number of arguments:', len(sys.argv), 'arguments.')

# strList = sys.argv[1:]
# strReverse = strList[::-1]
print('Random Order List:', random.sample(sys.argv[1:], len(sys.argv[1:])))
# reverseRandomOrder = random.sample(strReverse, len(strReverse))

# def strReverse(strList):
#     for word in strList:
#         print(word)
# print('Argument List:', strList)
# print('Reversed List:', strReverse)
# print('Random Order List:', randomOrder)
# print('Reversed Random Order List:', reverseRandomOrder)

# strReverse(strList)

# non-library way to use it
# Conner Solution https://github.com/Connor-Cahill/tweet-generator
# def rearrange_sen(sent):
#     str_arr = sent.split(" ")
#     for i in range(len(str_arr)):
#         rand_int = randpm.ranint(0, len(str_arr) - 1):
#         str_arr[rand_int], str[i] = str_arr[i], str_arr[rand_int]
#     return ' '.join(str_arr)
