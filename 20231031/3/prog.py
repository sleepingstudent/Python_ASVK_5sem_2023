class Maze:
    def __init__(self, M):
        self.size = M
        self.field = list()
        for i in range(2 * M + 1):
            self.field.append(list())
            for j in range(2 * M + 1):
                if i % 2 != 1:
                    self.field[i].append("\u2588")
                    continue
                if j % 2 == 1:
                    self.field[i].append("\u00B7")
                else:
                    self.field[i].append("\u2588")

    def __getitem__(self, key):
        x_0, y_0, y_1 = key
        y_0, x_1 = y_0.start, y_0.stop
        novisited = [(x_0, y_0)]
        visited = []

        while len(novisited):
            tmp = novisited.pop()
            if tmp == (x_1, y_1):
                return True
            if tmp in visited:
                continue
            visited.append(tmp)
            if (tmp[0], tmp[1] - 1) not in novisited and self.field[2 * tmp[1]][2 * tmp[0] + 1] != '\u2588' and tmp[1]:
                novisited.append((tmp[0], tmp[1] - 1))
            if (tmp[0] + 1, tmp[1]) not in novisited and self.field[2 * tmp[1] + 1][2 * tmp[0] + 2] != '\u2588' and tmp[0] != self.size - 1:
                novisited.append((tmp[0] + 1, tmp[1]))
            if (tmp[0], tmp[1] + 1) not in novisited and self.field[2 * tmp[1] + 2][2 * tmp[0] + 1] != '\u2588' and tmp[1] != self.size - 1:
                novisited.append((tmp[0], tmp[1] + 1))
            if (tmp[0] - 1, tmp[1]) not in novisited and self.field[2 * tmp[1] + 1][2 * tmp[0]] != '\u2588' and tmp[0]:
                novisited.append((tmp[0] - 1, tmp[1]))
        return False

    def __setitem__(self, key, val):
        x_0, y_0, y_1 = key
        y_0, x_1 = y_0.start, y_0.stop
        min_xy = [min(x_0, x_1), min(y_0, y_1)]
        max_xy = [max(x_0, x_1), max(y_0, y_1)]
        if x_0 == x_1:
            for i in range(2 * (min_xy[1] + 1), 2 * (max_xy[1] + 1), 2):
                self.field[i][2 * x_0 + 1] = val 
        elif y_0 == y_1:
            for i in range(2 * (min_xy[0] + 1), 2 * (max_xy[0] + 1), 2):
                self.field[2 * y_0 + 1][i] = val

    def __str__(self):
        res = ""
        for i in range(len(self.field)):
            for j in self.field[i]:
                res = res + j
            if len(self.field) - 1 != i:
                res = res + '\n'
        return res

'''m = Maze(4)
print(m)
print(m[0,0 : 1,0],m[0,0 : 2,2],m[1,0 : 1,2])
m[0,0 : 0,3] = m[0,3 : 3,3] = m[3,3 : 3,0] = m[3,0 : 2,0] = m[2,0 : 2,2] = m[1,0 : 1,2] = "·"
print(m)
print(m[0,0 : 1,0],m[0,0 : 2,2],m[1,0 : 1,2])'''

import sys
exec(sys.stdin.read())