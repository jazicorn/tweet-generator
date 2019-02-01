import sys
import random



def load_script():

    f = open('/usr/share/dict/words', 'r')
    content = f.read().splitlines()
    f.close()
    return content

def command_line_input():

    return sys.argv[1:]

def random_generator():

    content = load_script()
    arg_input = command_line_input()
    arg_int = int(' '.join(arg_input))
    return random.choices(content, k=arg_int)

def create_sentence():
    results = ' '.join(random_generator())
    print(results)
    return results


if __name__ == '__main__':
    create_sentence()
