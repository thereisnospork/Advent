import numpy as np

f=open('files/day7.txt')


input=list()
for line in f:
    a = line.strip('\n')
    b = a.split(' ')
    input.append(b)

#print(input)
    #dict weights and set of programs
weights = dict()

set_of = set()
for line in input:
    line[1] = line[1].strip('(').strip(')')
    line[1] = int(line[1])
    weights[line[0]] = line[1]
    set_of.add(line[0])


#strip out all programs listed as being supported from set of programs
for line in input:
    if len(line) > 2:
        supported_strs = line[3:]
       # print(line[3:])
        for prog in supported_strs:
            prog = prog.strip(',')
            #print(prog)
            set_of.remove(prog)

for line in input:
    if len(line) < 3:
        top_strs = line[0]
        if top_strs in set_of:
            set_of.remove(top_strs)
#strip out all programs not supporitng anyhting (the top)
print(set_of)

