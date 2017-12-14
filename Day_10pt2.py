import numpy as np
# from timeit import default_timer as timer
# start = timer()
#print(in_deque)
#
# raw_inst = "230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167"
# in_test = [0,1,2,3,4]


# in_arr = np.zeros(256, dtype='int')
#
# for index1, etc in enumerate(in_arr):
#     in_arr[index1] = index1
#print(in_arr)
## in_arr[1:10] = in_arr[10:1:-1] #invert list by slice (demo)  or np.flip

def hash_circle(num_arr, instr, cp = 0, skip_size = 0):
    for length in instr:
        start_index = cp #% arr_length ###for rotating
        end_index =(cp + length) #% arr_length ### + 1 for inclusive in slice
        stack_num_arr = np.hstack((num_arr,num_arr))

        flip = np.flip(stack_num_arr[start_index : end_index], axis = 0)
        for index, value in enumerate(flip):
            num_arr[(start_index + index) % len(num_arr)] = value

        cp += (skip_size + length)
        cp = cp %len(num_arr)
        skip_size += 1

    return (num_arr, cp, skip_size)

### run hash_circle recursively/repetively

def str_to_inst(arb_input):
    out = list()
    for letter in arb_input:
        out.append(ord(letter))
    for each in [17, 31, 73, 47, 23]: #special input from problem
        out.append(each)
    return out


def hash_circle_rpted(list_of, instructions, n = 64):
    """runs hash_circle n-times, input = hash circle output list [0]
    num_arrary [1] = cp,
    [2] = skip_size """

    for _ in range(n):
        list_of = hash_circle(list_of[0],
                              instructions,
                              cp = list_of[1],
                              skip_size =list_of[2])
    return list_of[0]

def dense_hash (sparse_hash, n= 16):
    """takes sparse hash, n slice length returns decimal output
     as list based on bitwise XOR of each slice"""
    start_index = 0
    end_index = n
    dec_output = list()
    for _ in range(len(sparse_hash) // n):
        slice = sparse_hash[start_index:end_index]
        dec_output.append(bitwise_XOR_of_slice(slice))

        start_index += n
        end_index += n
    return dec_output

def bitwise_XOR_of_slice(slice):
    out = slice[0]
    for index, _ in enumerate(slice[1:]):
        out = out ^ slice[index+1]
    return out

def ints_to_hex(ints):
    out = ''
    for num in ints:
        hexed = hex(num)
        out = out + hexed[-2:]
    #print(len(out))
    out = out.replace('x','0')  ###deal with single digit hex values
    return out

def knot_hash(raw_input):
    """ties together the steps to do knot hash on input, returning hex representation"""

    in_arr = np.zeros(256, dtype='int')
    for index1, etc in enumerate(in_arr):
        in_arr[index1] = index1

    instructions = str_to_inst(raw_input)
    #print(raw_input)
    #print(instructions)
    sparse_hashed = hash_circle_rpted([in_arr, 0, 0], instructions, n=64)
    dense_hashed = dense_hash(sparse_hashed)
    hex_hashed = ints_to_hex(dense_hashed)
    return hex_hashed

##########EXECUTE##########
#
# a = knot_hash("230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167")
# #a = knot_hash('1,2,3')
# print(a)
# print(len(a))

# b = knot_hash(raw_input='raw_inst')
# print(b)



#ascii instructions from raw input as def'd before
# instructions = str_to_inst(raw_inst)

# sparse_hashed = hash_circle_rpted([in_arr,0,0], instructions, n=60)
# b = dense_hash(sparse_hashed)
# print(b)
#
#
#
# end = timer()
#
# test_sparse_slice = [65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]
# #
# assert(bitwise_XOR_of_slice(test_sparse_slice)==64)
assert(knot_hash('AoC 2017')=='33efeb34ea91902bb2f59c9920caa6cd')
assert(knot_hash('')=='a2582a3a0e66e6e86e3812dcb672a272')


#print(sparse_hashed)



# if end_index > len(num_arr):
#     num_arr = np.hstack((num_arr,num_arr))
#     flag = True
# if flag:
#     num_arr = np.delete(num_arr,np.s_[0:len_init])
#     print('trimmed')
#     cp = cp - len_init
#     flag = False

#
#
# print(str(end-start)+' seconds elapsed')