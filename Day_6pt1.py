import numpy as np

input = np.genfromtxt('files\day6.txt', delimiter = ',', dtype = 'int')
#input = [0,2,7,0]
rounds = 0
outputs = [[]]
input = list(input)

while len(outputs) < 100000: #True: #len(outputs) < 10:  #True
    redist = np.where(input == np.amax(input))
    # print(max(input))
    # print(np.where(input == np.amax(input)))
    # print(input)
    redist = int(redist[0][0])
    index = redist+1 # position 1 right of highest
    count = input[redist] #number of highest to be redist
    input[redist] = 0
    rounds = rounds + 1

    while count > 0:
        a = index % len(input)
        b = input[a] + 1
        input[a] = b#input[a] + 1
        #print(index%len(input))
        index += 1
        count = count - 1
        #print(count)


    #print(outputs)

    # print(input)
    if str(input) in outputs:
        print(rounds)
        print(outputs.index(str(input)))
        break

   # print(rounds)
    outputs.append(str(input))

#  print(outputs[0])
print(rounds)

