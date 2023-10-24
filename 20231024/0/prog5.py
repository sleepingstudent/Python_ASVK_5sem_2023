from itertools import dropwhile, filterfalse, count, repeat, product
"""
s1 = 'ABCDEFGH'
s2 = '12345678'
ite = list(product(s1,s2))
for i in ite:
    print(''.join(i))
"""
print(list(f"{c[0]}{c[1]}" for c in product("abcdefgh", range(1,9))))
