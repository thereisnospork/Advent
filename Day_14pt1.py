import numpy as np
import itertools
import re
from Day_10pt2 import knot_hash


def hash_to_bin(hash):
    line = list()
    for hex_digit in hash:
        bin_digit_long = bin(int(hex_digit, 16))
        bin_digit_short = re.sub('0b','',bin_digit_long)
        while (len(bin_digit_short) <4):
            bin_digit_short = '0' + bin_digit_short

        for char in bin_digit_short:
            line.append(char)
    return(line)

def find_neighors(grid, x_y, neighbors):
    x = x_y[0]
    y = x_y[1]
    # print(type(neighbors))
    # print((x,y))
    if not grid[x,y]:  #make sure spot is valid
        # print(type(neighbors))
        return neighbors

    if x +1 < 128 and grid[x + 1,y] and (x+1,y) not in neighbors :
        neighbors.add((x + 1, y))
        find_neighors(grid, (x + 1, y), neighbors)

    if x-1 >= 0 and grid[x - 1 ,y] and (x-1,y) not in neighbors:
        neighbors.add((x - 1, y))
        find_neighors(grid, (x - 1, y), neighbors)

    if y+1 < 128 and grid[x,y + 1] and (x,y+1) not in neighbors:
        neighbors.add((x, y + 1))
        find_neighors(grid, (x, y + 1), neighbors)

    if y-1 >= 0 and grid[x,y - 1]and (x,y-1) not in neighbors:
        neighbors.add((x, y - 1))
        find_neighors(grid, (x, y - 1), neighbors)

    neighbors.add((x,y))  ##necessary to have in 2 lines
    return neighbors



inp = 'jzgqcdpd'
# inp = 'flqrgnkx'
grid = np.zeros([128,128], dtype='int')

for index in range(128):
    hash = knot_hash(inp+'-'+str(index))
    hash_bin = hash_to_bin(hash)
    grid[index] = hash_bin

sets_of_neighbors = set()
neighbors_1 = set()

for i in range(len(grid[0])):
    for n in range(len(grid[1])):
        neighbors_1 = set()
        neighbors_1 = find_neighors(grid,[i,n],neighbors_1)
        # print('end of this recursion')
        #temp = frozenset(neighbors_1)
        sets_of_neighbors.add(frozenset(neighbors_1))
       # print(frozenset(neighbors_1))

print(len(sets_of_neighbors)-1)
print
# print(len(sets_of_neighbors))


#
print(grid)

# print(grid.shape)
# print(np.count_nonzero(grid))
#
# x_y = [1,2]
# print(grid[1,2])





hash_inp = knot_hash('jzgqcdpd')







# stop = len(hash),