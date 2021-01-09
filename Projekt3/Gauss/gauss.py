import copy


def gauss(a, b, version):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = a.retrunSizeX()
    p = len(b[0])
    # det = 1
    for i in range(n - 1):
        k = i

        if version == 0:
            # No choice
            for j in range(i + 1, n):
                if abs(a[j][i]) != 0:
                    k = j
                    break

        elif version == 1:
            # With partial choice
            for j in range(i + 1, n):
                if abs(a[j][i]) > abs(a[k][i]):
                    k = j
		#NOT IMPLEMENTED
        #elif version == 2:
        #    # With full choice
        #    for j in range(i + 1, n):
        #        for l in range(i + 1, n):
        #            if abs(a[j][l]) > abs(a[k][i]):
        #                k = j
        if k != i:
            a.swapRows(i, k)
            b.swapRows(i, k)
            # det = -det

        for j in range(i + 1, n):
            t = a[j][i] / a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t * a[i][k]
            for k in range(p):
                b[j][k] -= t * b[i][k]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t * b[j][k]
        t = 1 / a[i][i]
        # det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return b
