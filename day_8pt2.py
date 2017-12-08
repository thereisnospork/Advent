import numpy as np

input= list()
f = open('files\day8.txt')
for line in f:
    input.append(line.strip('\n').split(' '))


def execute(input):
    """returns maximum register value achieved"""
    registers = dict()
    overall_max = 0
    for line in input:
        registers[line[0]] = 0 #initial condition for registers

    for instruction in input:
        equality_sym = instruction[5]
        register_val_init = registers[instruction[4]]
        check_against = int(instruction[-1])

        happens = happens_or_not(equality_sym, register_val_init, check_against)

        #print(happens)
        if happens:
            sign = inc_dec(instruction[1])
            registers[instruction[0]] += sign * int(instruction[2])
            ###maximum tracking###
            if max_in_dict(registers) > overall_max:
                overall_max = max_in_dict(registers)
    return overall_max

def inc_dec(instruction):
    if instruction == 'inc':
        return 1
    else:
        return -1

def happens_or_not(bool_str, instruction_val, chk_value):
    results = {'==': np.equal, '>=':np.greater_equal, '<=' : np.less_equal, '>':np.greater, '<':np.less, '!=':np.not_equal}
    return results[bool_str](instruction_val, chk_value)


#####to get answer execute below

def max_in_dict(registers):
    maximum = max(registers, key=lambda i: registers[i])
    return registers[maximum]

after = execute(input)
print(after)


#########A better solution, not mine, better import ######

from collections import defaultdict

# lines = open('input.txt').read().splitlines()
# regs = defaultdict(int)
# mxv = 0
# for line in lines:
#     reg, inst, num, iff, regc, op, num2 = line.split()
#     if eval("regs[regc] " + op + num2):
#         if inst == 'inc':
#             regs[reg] += int(num)
#             mxv = max(mxv, regs[reg])
#         else:
#             regs[reg] -= int(num)
#
# print max(regs.values()) # PART 1
# print mxv # PART 2