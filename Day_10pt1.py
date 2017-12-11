import numpy as np

#print(in_deque)

instructions = [230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167]
in_test = [0,1,2,3,4]
in_arr = np.zeros(256)

for index1, etc in enumerate(in_arr):
    in_arr[index1] = index1
print(in_arr)
## in_arr[1:10] = in_arr[10:1:-1] #invert list by slice (demo)  or np.flip

def hash_circle(num_arr, instr, cp = 0, skip_size = 0, len_init = 256):

    for length in instr:
        start_index = cp #% arr_length ###for rotating
        end_index =(cp + length) #% arr_length ### + 1 for inclusive in slice

        #stack_num_arr = num_arr

        #if end_index > len(num_arr):
        stack_num_arr = np.hstack((num_arr,num_arr))

        flip = np.flip(stack_num_arr[start_index : end_index], axis = 0)
        print([start_index, end_index])
        for index, value in enumerate(flip):
            num_arr[(start_index + index) % len(num_arr)] = value
           # print(num_arr)


        cp += (skip_size + length)
        cp = cp %len(num_arr)
        skip_size += 1

    return num_arr

a = hash_circle(in_arr,instructions)


print(a)
print(a[0]*a[1])



# if end_index > len(num_arr):
#     num_arr = np.hstack((num_arr,num_arr))
#     flag = True
# if flag:
#     num_arr = np.delete(num_arr,np.s_[0:len_init])
#     print('trimmed')
#     cp = cp - len_init
#     flag = False
