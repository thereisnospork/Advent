import re
import numpy as np

in_arr = np.genfromtxt('files\Day13.txt', delimiter=',', dtype='int')
in_arr = in_arr.transpose()
#print(in_arr)


def traversal (d_h, delay):
    depth = d_h[0]
    height = d_h[1]
    dict_of = dict(zip(depth,height))
    picos = 0 + delay
    step_max = np.max(depth) + 10
    cost = 0

    for i in range(step_max):
        try:
            if pos_scanner(picos, dict_of[i]):
               # cost += dict_of[i]*i
                return 9999
                #print('caught')
            #else:
                #print('not caught')
        except Exception:
            pass
            #print('no layer at this depth' + str(i))
        picos += 1
    return cost


def pos_scanner(timer, height):
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


def find_min_delay(d_h):
    delay = 0
    while(delay < 10000):
        delay = delay+1
        if traversal(d_h,delay) == 0:
            return delay
    return delay




a = find_min_delay(in_arr)
#b = pos_scanner(6,4)

assert (pos_scanner(6,4) == True)
assert(pos_scanner(2,2) == True)
assert(pos_scanner(2,3) == False)
assert(pos_scanner(99,2) == False)
assert(pos_scanner(12,4)==True)

print(a)
