import struct
import sys
import random
#" ".join(map(hex, list(struct.pack("bhl", 5, 0x432, 0x234234))))
'''with open(sys.argv[1], "wb") as f:
    for i in range(10):
        data = (random.random(), bytearray((random.randrange(255),random.randrange(255),random.randrange(255))), random.randrange(200000))
        f.write(struct.pack("<f3si", *data))'''
#b = bytearray((random.randrange(255),random.randrange(255),random.randrange(255)))
b = random.randbytes(3)
n = random.randrange(200000)
f = random.random()
for fmt, name in [("<f3si", sys.argv[1]), ("!f3si", sys.argv[2])]:
    with open(name, "wb") as ff:
        for i in range(10):
            #data = (random.random(), bytearray((random.randrange(255),random.randrange(255),random.randrange(255))), random.randrange(200000))
            ff.write(struct.pack(fmt, f, b, n))
    