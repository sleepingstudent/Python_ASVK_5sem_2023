def lenght(dot_0, dot_1):
    x_1, y_1 = dot_0[0], dot_0[1]
    x_2, y_2 = dot_1[0], dot_1[1]
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5

def dot_inside_Triangle(dot, dots):
    a = (dots[0][0]-dot[0])*(dots[1][1]-dots[0][1])-(dots[1][0]-dots[0][0])*(dots[0][1]-dot[1])
    b = (dots[1][0]-dot[0])*(dots[2][1]-dots[1][1])-(dots[2][0]-dots[1][0])*(dots[1][1]-dot[1])
    c = (dots[2][0]-dot[0])*(dots[0][1]-dots[2][1])-(dots[0][0]-dots[2][0])*(dots[2][1]-dot[1])
    min_dots = [[min(dots[0][0], dots[1][0]), min(dots[0][1], dots[1][1])], [min(dots[2][0], dots[1][0]), min(dots[2][1], dots[1][1])], [min(dots[0][0], dots[2][0]), min(dots[0][1], dots[2][1])]]
    max_dots = [[max(dots[0][0], dots[1][0]), max(dots[0][1], dots[1][1])],[max(dots[2][0], dots[1][0]), max(dots[2][1], dots[1][1])],[max(dots[0][0], dots[2][0]), max(dots[0][1], dots[2][1])]]
    if a == 0 and dot[0] > min_dots[0][0] and dot[0] < max_dots[0][0] and dot[1] > min_dots[0][1] and dot[1] < max_dots[0][1]:
        return True
    elif b == 0 and dot[0] > min_dots[1][0] and dot[0] < max_dots[1][0] and dot[1] > min_dots[1][1] and dot[1] < max_dots[1][1]:
        return True
    elif c == 0 and dot[0] > min_dots[2][0] and dot[0] < max_dots[2][0] and dot[1] > min_dots[2][1] and dot[1] < max_dots[2][1]:
        return True
    elif (a > 0 and b > 0 and c > 0):
        return True
    elif (a < 0 and b < 0 and c < 0):
        return True
    else:
        return False

class Triangle:
    def __init__(self, d1, d2, d3):
        self.dots = [(d1[0], d1[1]), (d2[0], d2[1]), (d3[0], d3[1])]
        self.dist = [lenght(self.dots[0], self.dots[1]), lenght(self.dots[2], self.dots[1]), lenght(self.dots[0], self.dots[2])]

    def __abs__(self):
        if self.dist[0] < self.dist[1] + self.dist[2] and self.dist[1] < self.dist[0] + self.dist[2] and self.dist[2] < self.dist[0] + self.dist[1] and min(self.dist) > 0:
            return abs((self.dots[0][0] - self.dots[2][0]) * (self.dots[1][1] - self.dots[2][1]) - (self.dots[0][1] - self.dots[2][1]) * (self.dots[1][0] - self.dots[2][0])) / 2
        else:
            return 0

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __contains__(self, item):
        if item:
            if dot_inside_Triangle(item.dots[0], self.dots) and dot_inside_Triangle(item.dots[1], self.dots) and dot_inside_Triangle(
                    item.dots[2], self.dots):
                return True
            else:
                return False
        else:
            return True

    def __and__(self, other):
        if self and other:
            if dot_inside_Triangle(self.dots[0], other.dots) or dot_inside_Triangle(self.dots[1], other.dots) or dot_inside_Triangle(
                    self.dots[2], other.dots) or dot_inside_Triangle(other.dots[0], self.dots) or dot_inside_Triangle(other.dots[1], self.dots) or dot_inside_Triangle(other.dots[2], self.dots):
                return True
            else:
                return False
        else:
            return False

'''r = Triangle((4, 2), (1, 3), (2, 4))
s = Triangle((1, 1), (3, 1), (2, 2))
t = Triangle((0, 0), (2, 3), (4, 0))
o = Triangle((1, 1), (2, 2), (3, 3))
print(*(f"{n}({bool(x)}):{round(abs(x), 3)}" for n, x in zip("rsto", (r, s, t, o))))
print(f"{s < t=}, {o < t=}, {r < t=}, {r < s=}")
print(f"{s in t=}, {o in t=}, {r in t=}")
print(f"{r & t=}, {t & r=}, {s & r=}, {o & t=}")'''

import sys
exec(sys.stdin.read())