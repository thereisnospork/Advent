import numpy as np
import re

input = np.genfromtxt('files/day4_input', dtype=str)

# input = ['abc','bca']

def sum_ascii(word):
    output = 0
    for char in word:
        output += ord(char)*ord(char)*ord(char)
    return str(output)




count = len(input)
for line in input:
    words = line.split(',')
    ascii_words = list(map(sum_ascii, words))
    for word in ascii_words:
        if(ascii_words.count(word)) > 1:
            count = count - 1
            break


print(count)