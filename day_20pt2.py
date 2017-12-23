import numpy as np
input = np.genfromtxt('files\day20.txt', delimiter = ',', dtype='int')



# def remove_conficts(positions):
#     for rows in positions:
#         chk_row = row
#         print(count)

for i in range(100000):

    positions = input[:, 0:3]
    velocities = input[:, 3:6]
    accel = input[:, 6:9]


    velocities += accel
    positions += velocities

    _, indexes, counts = np.unique(positions, return_index = True,return_counts=True, axis = 0)
    counts = counts - 1
    counts = counts.astype(bool)
    counts = np.invert(counts)
    input =  input[indexes,:]
    input = input[counts,:]
    #print(input)


print(len(input[:,]))

