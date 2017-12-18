f = open('files/Day18.txt')
inp =list()
for line in f:
    line = line.strip('\n').split(' ')
    inp.append(line)


reg = dict()
reg = {'a':0,'i':0,'p':0,'b':0,'f':0,'z':0}
# print(registers)
#
# print(inp[0])
out_sound = 0
index = 0
while True:
    cmd = inp[index]
    if cmd[0] == 'snd':
        out_sound = reg[cmd[1]]
        index = index + 1

    if inp[index][0] == 'set':
        try:
            reg[cmd[1]] = int(cmd[2])
        except Exception:
            reg[cmd[1]] = reg[cmd[2]]
        index = index + 1

    if cmd[0] == 'add':
        try:
            reg[cmd[1]] += int(cmd[2])
        except Exception:
            reg[cmd[1]] += reg[cmd[2]]
        index = index + 1

    if cmd[0] == 'mul':
        try:
            reg[cmd[1]] = reg[cmd[1]]*int(cmd[2])
        except Exception:
            reg[cmd[1]] = reg[cmd[1]] * reg[cmd[2]]
        index = index + 1

    if cmd[0] == 'mod':
        try:
            reg[cmd[1]] = reg[cmd[1]] % int(cmd[2])
        except Exception:
            reg[cmd[1]] = reg[cmd[1]] % reg[cmd[2]]

        index = index + 1

    if cmd[0] == 'rcv':
        if out_sound != 0:
            print(out_sound)
            break
        index = index + 1
    if cmd[0] == 'jgz':
        if reg[cmd[1]] > 0:
            index = index + int(cmd[2])
        else: index = index + 1
    print(index)

print(inp[3])