import numpy as np
import re

f = open('files\day9.txt')
for line in f: ##only one line
    inp = line

#inp = str("{{<!!>},{<!!>},{<!!>},{<!!>}}")
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


a = remove_exc(inp)
b = remove_garbage(a)
print(b)

c = processing(inp)
print(c)