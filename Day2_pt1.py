import numpy as np

data = np.genfromtxt('files\day2.csv', delimiter=',')
print(data[1])
checksum = 0
for index, row in enumerate(data):
    checksum += max(row) - min(row)

print(checksum)