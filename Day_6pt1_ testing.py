import numpy as np

#input = np.genfromtxt('files\day6.txt', delimiter = ',', dtype = 'int')
input = [0,2,7,0]
rounds = 0
outputs = [[]]
input = list(input)
input_start = input
print(input)
print(input_start)
while len(outputs) < 10000: #True: #len(outputs) < 10:  #True
    redist = np.where(input == np.amax(input))
    redist = int(redist[0][0])
    index = redist+1 # position 1 right of highest
    count = input[redist] #number of highest to be redist
    input[redist] = 0
    rounds = rounds + 1

    # while count > 0:
    #     a = index % len(input)
    #     b = input[a] + 1
    #     input[a] = b#input[a] + 1
    #     #print(index%len(input))
    #     index += 1
    #     count = count - 1
    outputs.append(input)

#  print(outputs[0])
print
print(outputs)
print(len(outputs))
print(input_start)
print(input)

