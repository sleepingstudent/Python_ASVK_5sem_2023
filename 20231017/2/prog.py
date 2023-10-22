from math import *
d = dict()
cntr_str = 0
while (st := input()) and st[:5] != 'quit ':
    cntr_str += 1
    if st[0] == ':':
        s = st[1:].split()
        d[s[0]] = [s[-1], s[1:-1]]
    else:
        
        idx = st.find(' ')
        if idx == -1:
            s = [st]
        elif len(d[st[:idx]][1]) == 1:
            s = [st[:idx], eval(st[idx:])]
        else:
            s = st.split()
            for i in range(1, len(s)):
                s[i] = eval(s[i])
        print(eval(d[s[0]][0], globals() | dict(zip(d[s[0]][1], s[1:]))))
cntr_str += 1
print(eval(st[5:]).format(len(d) + 1, cntr_str))
