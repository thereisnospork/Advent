f = open('files/day19.txt')
import re

inp = list()
for line in f:
    inp.append(line)

count = 0
direction ='down'
down = True
right = False
left = False
up = False

out_letters = list()

def new_direction(x,y,inp, direction):
    if inp[y][x+1] == '-' and direction != 'left':
        return 'right'
    if inp[y][x-1] == '-' and direction != 'right':
        return 'left'
    try:
        if inp[y-1][x] == '|' and direction != 'down':
            return 'up'
    except Exception:
        print('!!!!!!!')
        pass
    if inp[y+1][x] == '|' and direction != 'up':
        return 'down'
    return 'end'

def is_letter(char_1):
    letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')

    if char_1 in letters:
        return True

y = 0
x = 0

for index, letter in enumerate(inp[x]):
    if letter == '|':
        x = index




while direction != 'end':
    while direction == 'down':
        if is_letter(inp[y+1][x]):
            out_letters.append(inp[y+1][x])
            y = y + 1
        if inp[y+1][x]=='|' or inp[y+1][x] == '-':
            y = y + 1
        if inp[y+1][x]=='+':
            y = y+1
            direction = new_direction(x,y, inp, direction)

    while direction == 'up':
        if is_letter(inp[y-1][x]):
            out_letters.append(inp[y-1][x])
            y = y - 1
        if inp[y-1][x]=='|' or inp[y-1][x] == '-':
            y = y - 1
        if inp[y - 1][x] == '+':
            y = y - 1
            direction = new_direction(x, y, inp, direction)


    while direction == 'right':
        if is_letter(inp[y][x+1]):
            out_letters.append(inp[y][x+1])
            x = x + 1
        if inp[y][x+1]=='|' or inp[y][x+1] == '-':
            x = x + 1
        if inp[y][x+1]=='+':
            x = x+1
            direction = new_direction(x,y, inp, direction)

    while direction == 'left':
        if is_letter(inp[y][x-1]):
            out_letters.append(inp[y][x-1])
            x = x - 1
        if inp[y][x-1]=='|' or inp[y][x-1] == '-':
            x = x - 1
        if inp[y][x-1]=='+':
            x = x-1
            direction = new_direction(x,y, inp, direction)

    print(count)

