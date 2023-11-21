import pickle
#pickle.dumps("QWERTY")

class SerCls:
    pass

ser = SerCls()
ser.lst = [1,2,3]
ser.dct = {'a':1, 'b':2}
ser.num = 10
ser.st = "qwerty"
s = pickle.dumps(ser) #protocol=0)
print(s)
del ser

ser2 = pickle.loads(s)
