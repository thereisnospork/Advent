import numpy as np

input= list()
f = open('files\day8.txt')
for line in f:
    input.append(line.strip('\n').split(' '))


def execute(input):
    registers = dict()
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
        # print(happens)
        # print(sign * int(instruction[2]))
    # print(registers)
    # print(registers[np.max(registers)]) ###query answer, largest register's value
    return registers

def inc_dec(instruction):
    if instruction == 'inc':
        return 1
    else:
        return -1

def happens_or_not(bool_str, instruction_val, chk_value):
    results = {'==': np.equal, '>=':np.greater_equal, '<=' : np.less_equal, '>':np.greater, '<':np.less, '!=':np.not_equal}
    return results[bool_str](instruction_val, chk_value)


#####to get answer execute below


after = execute(input)
maximum = max(after, key=lambda i: after[i])
print(after)
print(after[maximum])  ## answer


#execute(input)
print(happens_or_not('==',1,1))