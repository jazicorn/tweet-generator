import sys
import random



def load_script():

    f = open('/usr/share/dict/words', 'r')
    content = f.read().splitlines()
    f.close()

    return content

def random_generator():
    content = load_script()
    return random.sample(content, 7)

def create_string():
    content_list = random_generator()
    print(' '.join(content_list))


if __name__ == '__main__':
    create_string()
    # sentence.select_random()