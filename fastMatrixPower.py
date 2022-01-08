def mulMatrix(x, y):
    c = [[0 for i in range(len(x))] for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                c[i][j] += x[i][k] * y[k][j]
                # c[i][j] %= mod #如果有mod就用
    return c


def fastMatrixPower(matrix, power):
    res = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        res[i][i] = 1
    while power:
        if power & 1:
            res = mulMatrix(matrix, res)
        matrix = mulMatrix(matrix, matrix)
        power >>= 1
    return res


def fastPower(num, power, mod = 10**9+7):
    res = 1
    while power:
        if power & 1:
            res = (res * num) % mod

        num = (num * num) % mod
        power >>= 1
    return res

if __name__ == '__main__':
    b, m = 9,[[1,0,0],[0,1,0],[0,0,1]]
    print(fastMatrixPower(m,b))
    print(fastPower(2,9))