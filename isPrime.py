def is_prime(n):
    """该函数返回是否质数"""
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


def hcf(x, y):
    """该函数返回两个数的最大公因数"""
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def lcm(x, y):
    """该函数返回两个数的最小公倍数"""
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


if __name__ == '__main__':
    a = 42
    print(a, '是否质数', is_prime(a))
    b = 5
    c = 6
    print(b, c, '最大公因数', hcf(b, c))
    print(b, c, '最小公倍数', lcm(b, c))
