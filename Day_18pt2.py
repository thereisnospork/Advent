f = open('files/Day18.txt')
inp =list()
for line in f:
    line = line.strip('\n').split(' ')
    inp.append(tuple(line))

inp = tuple(inp)

reg_0 = {'a':0,'i':0,'p':0,'b':0,'f':0,'z':0}
reg_1 = {'a':0,'i':0,'p':1,'b':0,'f':0,'z':0}

def value(char_int, dict_):
    try:
        a = int(char_int)
        return a
    except Exception:
        a = dict_[char_int]
        return a



out_sound = 0
index_0 = 0
index_1 = 0

snd_0 = False
snd_1 = False
rcv_0 = False
rcv_1 = False
snd_count = 0
snd_list_0 = list()
snd_list_1 = list()


while True:
    while not rcv_0:
        cmd_0 = inp[index_0]
    
        if cmd_0[0] == 'snd':
            try:
                snd_list_0.append(int(cmd_0[1]))
            except Exception:
                snd_list_0.append(reg_0[cmd_0[1]])  #add to list of stuff to send to prog 2
            index_0 = index_0 + 1
    
        if cmd_0[0] == 'set':
            try:
                reg_0[cmd_0[1]] = int(cmd_0[2])
            except Exception:
                reg_0[cmd_0[1]] = reg_0[cmd_0[2]]
            index_0 = index_0 + 1
    
        if cmd_0[0] == 'add':
            try:
                reg_0[cmd_0[1]] += int(cmd_0[2])
            except Exception:
                reg_0[cmd_0[1]] += reg_0[cmd_0[2]]
            index_0 = index_0 + 1
    
        if cmd_0[0] == 'mul':
            try:
                reg_0[cmd_0[1]] = reg_0[cmd_0[1]]*int(cmd_0[2])
            except Exception:
                reg_0[cmd_0[1]] = reg_0[cmd_0[1]] * reg_0[cmd_0[2]]
            index_0 = index_0 + 1
    
        if cmd_0[0] == 'mod':
            try:
                reg_0[cmd_0[1]] = reg_0[cmd_0[1]] % int(cmd_0[2])
            except Exception:
                reg_0[cmd_0[1]] = reg_0[cmd_0[1]] % reg_0[cmd_0[2]]
    
            index_0 = index_0 + 1
    
        if cmd_0[0] == 'rcv':
            rcv_0 = True
            print('RCV_0')

        if cmd_0[0] == 'jgz':
            if value(cmd_0[1],reg_0) > 0:
                index_0 = index_0 + value(cmd_0[2],reg_0)
            else:
                index_0 = index_0 + 1

    while not rcv_1:
        cmd_1 = inp[index_1]
    
        if cmd_1[0] == 'snd':
            try:
                snd_list_1.append(int(cmd_1[1]))
            except Exception:
                snd_list_1.append(reg_1[cmd_1[1]])  #add to list of stuff to send to prog 2
            snd_count+= 1
            index_1 = index_1 + 1
    
        if cmd_1[0] == 'set':
            try:
                reg_1[cmd_1[1]] = int(cmd_1[2])
            except Exception:
                reg_1[cmd_1[1]] = reg_1[cmd_1[2]]
            index_1 = index_1 + 1
    
        if cmd_1[0] == 'add':
            try:
                reg_1[cmd_1[1]] += int(cmd_1[2])
            except Exception:
                reg_1[cmd_1[1]] += reg_1[cmd_1[2]]
            index_1 = index_1 + 1
    
        if cmd_1[0] == 'mul':
            try:
                reg_1[cmd_1[1]] = reg_1[cmd_1[1]]*int(cmd_1[2])
            except Exception:
                reg_1[cmd_1[1]] = reg_1[cmd_1[1]] * reg_1[cmd_1[2]]
            index_1 = index_1 + 1
    
        if cmd_1[0] == 'mod':
            try:
                reg_1[cmd_1[1]] = reg_1[cmd_1[1]] % int(cmd_1[2])
            except Exception:
                reg_1[cmd_1[1]] = reg_1[cmd_1[1]] % reg_1[cmd_1[2]]
    
            index_1 = index_1 + 1
    
        if cmd_1[0] == 'rcv':
            rcv_1 = True

        if cmd_1[0] == 'jgz':
            if value(cmd_1[1],reg_1) > 0:
                index_1 = index_1 + value(cmd_1[2],reg_1)
            else:
                index_1 = index_1 + 1

    
    #reconcile stop
    
    if rcv_0 and len(snd_list_1) > 0:
        reg_0[cmd_0[1]] = snd_list_1.pop(0)
        index_0 += 1
        print('RCVED from prog 1 to prog 0')
        rcv_0 = False

    if rcv_1 and len(snd_list_0) > 0:
        reg_1[cmd_1[1]] = snd_list_0.pop(0)
        index_1 += 1
        rcv_1 = False

    if rcv_1 and rcv_0:
        print(rcv_0)
        print(rcv_1)
        print(snd_count)
        break
