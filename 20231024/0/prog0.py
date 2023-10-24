def walk2d():
    x = 0
    y = 0
    dx, dy = yield (x, y)
    while dx and dy:
        x += dx
        y += dy
        dx, dy = yield (x, y)

ite = walk2d()
next(ite)
while (s := input()):
    dx, dy = eval(s)
    print(ite.send((dx, dy)))


