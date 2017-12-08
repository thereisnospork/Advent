import numpy as np

f=open('files/day7.txt')


input=list()
for line in f:
    a = line.strip('\n')
    b = a.split(' ')
    input.append(b)

#print(input)
    #dict weights and set of programs
weights = dict()
above = dict()
above_DNT = dict()
set_of = set()
top = list()

for line in input:
    line[1] = line[1].strip('(').strip(')')
    line[1] = int(line[1])
    weights[line[0]] = line[1]
    set_of.add(line[0])re




#strip out all programs listed as being supported from set of programs

for line in input:
    if len(line) > 2:
        for item in line[3:]:
            above[line[0]] = line[3:]
    else:
        above[line[0]] = list()
        top.append(line[0])

for line in input:  #2nd above for reference later
    if len(line) > 2:
        for item in line[3:]:
            above_DNT[line[0]] = line[3:]
    else:
        above_DNT[line[0]] = list()

# print(above)
# print(top)

## SUM weights above
#


def total_weight(weights):
    total_weight = 0
    for weight in weights:
        total_weight += weights[weight]
        return(total_weight)

def list_of_below(prog):
    out = list()
    for each2 in above:
        # print(above[each])
        # print(prog in above[each])
        if prog in above[each2]:
            out.append(each2)
    return out


# output_weight = dict()
# output_weight[each] = weights[each] #weight of self


def weight_step(top = top, weights = weights):  #NEEDS qualifier to make sure all weights above have been added
    """recursively adds mass layer by layer from the top down"""

    layer_below = list()
    layers_below = list()
    for each in top:
        below_list = list_of_below(each)
        if len(below_list) > 0:
            for prog in below_list:
                weights[prog] += weights[each]
                above[prog].remove(each)
                if(len(above[prog])) == 0: #prevents adding to layer below unless there are no more layers above!
                    layer_below.append(prog)
                    layer_below = list(set(layer_below)) ###remove dups



    print(layer_below)
    layers_below.append(layer_below)


    if len(layer_below) > 0:
        weight_step(layer_below, weights)
    return layers_below

# print(weights['aapssr'])
asdf = weight_step()
# print(weights)
# print(asdf)

def balance(bottom = 'aapssr', weights=weights):  ### have manually asertained my odd-node is Heavy
    '''returns text for out of balance node'''
    layer_weights = list()
    for node in above_DNT[bottom]:
        layer_weights.append(weights[node])
        print(weights[node])
    maximum = max(layer_weights)
    avg = np.mean(layer_weights)
    #print(maximum)
    #print(new_bottom)
    if maximum ==avg:
        print(bottom)
        print(type(bottom))
        return bottom
    new_bottom = next(node for node, value in weights.items() if value == maximum)
    balance(new_bottom)

balance()





# print(weights)
# print(weights[str()])

# print(asdf['aapssr'])
# print(list_of_below('hgtyjhv'))

# for each in above_DNT['aapssr']:
#     print(weights[each])






# def add_weights_immediately_below(below_sym, weights = weights, above = above, total_weight = total_weight):
#
#     while(weights['aapssr']) < total_weight:
#
#         for prog_above_below_sym in above[below_sym]:
#             weights[below_sym] += weights[prog_above_below_sym]
#             print(weights['aapssr'])
#             add_weights_immediately_below(prog_above_below_sym)
#

    # return weights


# asdf = add_weights_immediately_below('aapssr', weights)
# print(asdf)


#
# #
# # for line in input:
# #     if len(line) < 3:
# #         top_strs = line[0]
# #         if top_strs in set_of:
# #             set_of.remove(top_strs)
# # #strip out all programs not supporitng anyhting (the top)
# # print(set_of)
# #

# def tree(base, above):
#     for prog in above[base]:
#         print(prog)
#         above[base] = above[base].append(prog)