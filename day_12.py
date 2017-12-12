import re

f=open('files/day12.txt')

input=list()
for line in f:
    a = line.strip('\n')
    c = a.split(' ')
    c.pop(1)
    input.append(c)

links = dict()
for line in input:
    linked = set()
    for item in line[1:]:
        item = item.strip(',')
        linked.add(int(item))
#        print(linked)
    links[int(line[0])]=linked

# print(links)

###end initialization

def propogate(dict_of_links):
    for head in dict_of_links:
        links = dict_of_links[head]
        linked = set()
        for prog in links:
            linked.add(prog)
        for item in linked:
            dict_of_links[item] = dict_of_links[item].union(linked)
    return dict_of_links

        # for linked in prog:
        #     set_of_links[linked].add(prog)

q = propogate(links)

# pt2 down here
set_of_sets = set()
for i in q:
    set_of_sets.add(frozenset(q[i]))

print(len(set_of_sets))