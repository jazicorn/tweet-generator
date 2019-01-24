import sys
import random

print(sys.argv)

print('Number of arguments:', len(sys.argv), 'arguments.')

strlist = sys.argv[1:]

print('Argument List:', strlist)


print(random.sample(strlist, len(strlist)))
