import re
import numpy as np

in_arr = np.genfromtxt('files\Day13.txt', delimiter=',', dtype='int')
in_arr = in_arr.transpose()
print(in_arr)


def traversal (d_h):
    depth = d_h[0]
    height = d_h[1]
    dict_of = dict(zip(depth,height))
    picos = 0
    pico_max = np.max(depth) + 1
    cost = 0

    for i in range(pico_max):
        try:
            if pos_scanner(picos, dict_of[i]):
                cost += dict_of[i]*i
                print('caught')
            #else:
                #print('not caught')
        except Exception:
            print('no layer at this depth' + str(i))
        picos += 1
    return cost


def pos_scanner(timer, height):
    i = 0
    pos = 0
    up_down = 1
    for n in range(timer):
        pos = pos + up_down
        if pos == height -1:
            up_down = -1
        if pos == 0:
            up_down = 1
    if pos == 0:
        return True
    else:
        return False




a = traversal(in_arr)
#b = pos_scanner(6,4)

assert (pos_scanner(6,4) == True)

print(a)
