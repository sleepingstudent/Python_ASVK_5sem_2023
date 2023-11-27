import sys

first = sys.stdin.buffer.read(1)
st = sys.stdin.buffer.readline()
lenght = len(st)
if st[-1] == 10:
    st = st[:lenght - 1]
lenght -= 1
num = first[0]
ans = list()
for i in range(num):
    ans.append(st[int(i * lenght / num): int((i + 1) * lenght / num)])
ans = [first] + sorted(ans) + [b'\n']
sys.stdout.buffer.write(b''.join(ans))