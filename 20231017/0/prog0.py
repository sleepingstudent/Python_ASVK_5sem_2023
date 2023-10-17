import timeit

s = input()
num, timing = timeit.Timer(stmt = s).autorange()
per_run = timing/num
print(per_run *1000)
