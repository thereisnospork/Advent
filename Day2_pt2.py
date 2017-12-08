import numpy as np
import collections

data = np.genfromtxt('files\day2.csv', delimiter=',', dtype=int)
#print(data[1])
out = []

for index, row in enumerate(data):
    for item in row:

        foo = item % row
        if np.count_nonzero(foo) == 14: #len = 16, so 2 zeros)
            out.append(item)
            break

print(out)
sum_out = 0

for index, each in enumerate(out):
    foo = each / data[index]
    foo = foo[foo%1 == 0]
    sum_out += max(foo)
    print(foo)

print(sum_out)














# for column in np.transpose(data):
#     mod = column % data
#     divided = column / data
#     print(divided)
#     div_int = column // data
#     mod_bool = mod.astype(bool)
#     mod_bool_inv = np.logical_not(mod_bool)
#     asdf = mod_bool_inv * data
#    # print(asdf)
#     list_of_divisor_arrays.append(divided)
#



#for divisors in list_of_divisor_arrays:


#print(list_of_divisor_arrays[-1])
# print(checksum)