import numpy as np

field = np.zeros([10000,10000], dtype=int)
x = 100
y = 100

field[x,y]=1
field[x+1,y] = 1
field[x+1,y+1] = 2
field[x,y+1] = 4
field[x-1,y+1] = 5

x = 99
y = 101
flattened = list()

def new_value(pos, field):
    x = pos[0]
    y = pos[1]
    return np.sum(field[x-1:x+2,y-1:y+2])

def adj_sqrs(pos, field):
    """returns number of filled agacent squres inc. self"""
    x = pos[0]
    y = pos[1]
    return np.count_nonzero(field[x-1:x+2,y-1:y+2])


dirs = 'DRUL' * 1000
dir_count = 0

for i in range(100):
    if dirs[dir_count]=='U':
        y += 1
    if dirs[dir_count]=='L':
        x += -1
    if dirs[dir_count]=='D':
        y += -1
    if dirs[dir_count]=='R':
        x += 1
    flattened.append(new_value([x,y],field))
    field[x,y] = new_value([x,y],field)
    # print(adj_sqrs([x,y],field))

    if adj_sqrs([x,y],field)==3:

        dir_count += 1



print(flattened)









#         print('TURNED'+ ' ' + dirs[dir_count]+ ' '+ str(dir_count))
#     print([x,y])
#
#
# print(new_value([x,y],field))
# print(field[x-10:x+10,y-10:y+10])
# print(dir_count)
#print(field)

# print(np.sum(field[x-1:102,0:2]))





#
# #UP DOWN LEFT RIGHT CHECK#
# ######Move UP%%%%%%
#     if field[x,y+1] == 0 and field[x,y-1] == 0 and field[x-1,y] !=0 and field[x+1,y]==0:
#         field[x,y+1]=1
#         y = y + 1
#
#         ######Move UP%%%%%%
#     if field[x,y+1] == 0 and field[x,y-1] == 0 and field[x-1,y] !=0 and field[x+1,y]==0:


# print(field)


# rules:
