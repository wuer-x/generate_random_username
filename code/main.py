# coding:utf8
import random

def main(count=3, name_type='camel'):
    with open('../data/word_source','r') as f:
        word_source = f.readlines()

    word_source_list = word_source[0].split(',')
    name_list = []
    rst = ''
    random_index = get_random_numbers(count, len(word_source_list) - 1)
    
    for i in range(len(random_index)):
        name_list.append(word_source_list[i])

    if name_type.lower() == 'camel':
        return ''.join(name_list)
    elif name_type.lower() == '_':
        return '_'.join(name_list)

    return rst

# count: how many random numbers needed
# max_value: numbers range 0 to max_value
def get_random_numbers(count, max_value):
    rst = []
    for i in range(count):
        rst.append(int(random.random() * max_value))
    return rst


if __name__ == '__main__':
    print main()
