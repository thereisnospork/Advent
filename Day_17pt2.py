from timeit import default_timer as timer


steps = 356
index = 1
list_of = [0]
length = 1
start = timer()
for i in range(1,50000000):
    for n in range(steps):
        index = index + 1
        index = index % length
    #print(index)
    if not index:
        list_of.insert(index+1,i)
    index += 1
    length += 1


end = timer()
print(end-start)

print(list_of[0:10])
