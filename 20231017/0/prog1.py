import timeit
def ab(s):
    len(set(s) & alph_a), len(set(s) & alph_b)
    
s = input()
alph_a = set('aeiouy')
alph_b = set('abcdefghijklmnopqrstuvwxyz')
alph_b -= alph_a
num, tm = timeit.Timer('ab(s)', globals = globals()).autorange()
print(num, tm)
print(tm / num)
print(len(set(s) & alph_a), len(set(s) & alph_b))
