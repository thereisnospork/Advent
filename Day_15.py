import numpy as np

###Part 1###

gen_a_f = 16807
gen_b_f = 48271
divisor = 2147483647
gen_a_last = 618
gen_b_last = 814
count = 0

for n in range(5000000):
    gen_a_last = gen_a_last * gen_a_f % divisor
    while gen_a_last % 4 != 0:
        gen_a_last = gen_a_last * gen_a_f % divisor

    gen_b_last = gen_b_last * gen_b_f % divisor
    while gen_b_last % 8 != 0:
        gen_b_last = gen_b_last * gen_b_f % divisor


    if bin(gen_a_last)[-16:] == bin(gen_b_last)[-16:]:
        count += 1
        print(n)


print(count)






print(bin(1431495498)[-8:])