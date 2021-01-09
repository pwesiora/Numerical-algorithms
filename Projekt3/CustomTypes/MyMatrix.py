import random

from numpy import double


class Matrix(object):

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        mat = Matrix(m, n, init=False)
        mat.rows = rows

        return mat

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __setitemY__(self, idx, idy, item):
        self.rows[idx][idy] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def returnMatrix(self):
        return self.rows

    def returnItem(self, m, n):
        arr = self.rows[m]
        return arr[n]

    def retrunSizeX(self):
        return self.m

    def getTranspose(self):

        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat

    def getRank(self):
        return (self.m, self.n)

    def getRankM(self):
        return (self.m)

    def getRankN(self):
        return (self.n)

    def __mul__(self, mat):

        matm, matn = mat.getRank()

        mat_t = mat.getTranspose()
        mulmat = Matrix(self.m, matn)

        for x in range(self.m):
            for y in range(mat_t.m):
                mulmat[x][y] = sum([item[0] * item[1] for item in zip(self.rows[x], mat_t[y])])

        return mulmat

    def __abssub__(self, mat):

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [item[0] - item[1] for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        x = ret.__sum__()
        return x

    def __sum__(self):
        sum = 0
        for x in range(self.n):
            sum = abs(sum) + abs(self.rows[x][0])
        return abs(sum)

    def swapRows(self, x, y):
        tmp = self.rows[x]
        self.rows[x] = self.rows[y]
        self.rows[y] = tmp

    def swapCol(self, x, y):
        for i in range(0, self.m):
            tmp = self.returnItem(i, x)
            self.__setitemY__(i, x, self.returnItem(i, y))
            self.__setitemY__(i, y, tmp)

    def setColumn(self, array, i):
        for j in range(self.m):
            self.__setitemY__(j, i, array.returnItem(j, 0))

    def getColumn(self, k):
        return [row[k] for row in self]

    @classmethod
    def makeRandom(cls, m, n, type):

        obj = Matrix(m, n, init=False)

        for x in range(m):
            if type == 0:
                obj.rows.append([(random.uniform(0, 65536 - 1) / 65536) for i in range(obj.n)])
            elif type == 1:
                obj.rows.append([float(random.uniform(-65536, 65536 - 1) / 65536) for i in range(obj.n)])
            elif type == 2:
                obj.rows.append([double(random.uniform(-65536, 65536 - 1) / 65536) for i in range(obj.n)])
        return obj

    @classmethod
    def fromList(cls, listoflists):
        rows = listoflists[:]
        return cls._makeMatrix(rows)
