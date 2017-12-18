import re
from timeit import default_timer as timer

f = open('files\day16input.txt')
for line in f:
    inp = line.rstrip().split(',')


start_str = 'abcdefghijklmnop'





def spin(inp_str,i_1):
    i_1 = int(i_1)
    substr = inp_str[-i_1:]
    inp_str = inp_str.rstrip(substr)  ### removes chars in substring, but fine for this purpose
    inp_str = substr + inp_str
    return inp_str

def xchang(inp_str, i_1,i_2):
    i_1 = int(i_1)
    i_2 = int(i_2)
    char_1 = inp_str[i_1]
    char_2 = inp_str[i_2]
    inp_str = list(inp_str)
    inp_str[i_1] = char_2
    inp_str[i_2] = char_1
    inp_str = ''.join(inp_str)
    return inp_str

def partner(inp_str, char_1, char_2):
    i_1 = inp_str.find(char_1)
    i_2 = inp_str.find(char_2)
    return xchang(inp_str, i_1,i_2)





dict_of_cmd = {'s':spin, 'x': xchang,'p':partner}

# foo = partner(start_str,'a','b')
# print(foo)
start = timer()
set_of = set()
for i in range(1000000000%48): ## 48 is time to start value
    for each in inp:
        operation = each[0]
        index_2 = False
        each = each[1:]
        each_split = each.split('/')
        index_1 = each_split[0]
        try:
            index_2 = each_split[1]
        except Exception:
            pass

        if index_2:
            start_str = dict_of_cmd[operation](start_str, index_1,index_2)
        else:
            start_str = dict_of_cmd[operation](start_str, index_1)
    if start_str in set_of:
        print(len(set_of))
    set_of.add(start_str)


end = timer()
print(start_str)

print(end-start)