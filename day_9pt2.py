import numpy as np
import re

f = open('files\day9.txt')
for line in f: ##only one line
    inp = line

#inp = str("<{oii!a,<{i<a>")
###remove !!!'s

def remove_exc(inp):
    inp = re.sub('!.', '', inp)
    return inp

def remove_garbage(inp):
    inp = re.sub('<.*?>', '', inp)
    return inp

def processing(inp):
    inp = remove_exc(inp)
    inp = remove_garbage(inp)
    inp = summation(inp)
    return inp


def summation(inp):
    score = 0
    depth = 1

    for letter in inp:
        if letter == '{':
            score += depth
            depth += 1
        if letter == '}':
            depth += -1
    return score


def count_garbage(inp):
    inp = remove_exc(inp)
    len_st = len(inp)
    num_matches = len(re.findall('<.*?>',inp))
    inp = remove_garbage(inp)
    garbage_chars = (len_st - len(inp)) - 2 * num_matches
    return garbage_chars




c = count_garbage(inp)
print(c)
