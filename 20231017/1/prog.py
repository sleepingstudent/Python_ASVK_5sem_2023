st = input().lower()
s = {st[i:i+2] for i in range(len(st) - 1) if st[i:i+2].isalpha()}
print(len(s))
