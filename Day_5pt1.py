import numpy as np



f = open('files\day_5.txt')
input = list()
for item in f:
    item = item.strip('\n')
    input.append(int(item))

#input = [0,3,0,1,-3]

steps = 0
index = 0
new_index = 0
while index < len(input):
    #print(input[index])
    new_index = index + input[index]
    input[index] += 1
    index = new_index
    steps = steps+1


print(steps)
