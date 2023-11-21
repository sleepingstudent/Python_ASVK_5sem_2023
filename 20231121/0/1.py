import pathlib
with open("cal", "rwb") as f:
    '''id_end = f.seek(0, 2)
    f.seek(0)'''
    txt = f.read()
    s = []
    cnt = 0
    while b:=f.read(1):
        s.append(b)
        cnt += 1
    f.clean()
    for i in range(cnt // 2, cnt):
        f.write(s[i])
    for i in range(cnt//2):
        f.write(s[i])