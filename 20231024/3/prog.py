from itertools import product #combinations_with_replacement, permutations
print(*sorted(filter(lambda x: (x.count('TOR') == 2), [''.join(i) for i in product('TOR', repeat=int(input()))])))

'''print(*sorted(filter(lambda x: (x.find('TOR') != x.rfind('TOR')) and (x.find('TOR') != -1), 
                     {''.join(k) for j in [''.join(i) for i in combinations_with_replacement('TOR', int(input()))] for k in permutations(j)})))'''
