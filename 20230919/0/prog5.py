while n := input():
    if type(eval(n)) == int and eval(n) % 2 == 0:
        print(n)
    if type(eval(n)) == int and eval(n) == 13:
        break
else:
    print("Congratuate!")
