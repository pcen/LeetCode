def test():
    print(reverse(-123456))

def reverse(x):
    n = 0
    if x < 0:
        s = -1
    else:
        s = 1
    x *= s
    while x != 0:
        n = (10 * n) + x % 10
        x = x // 10
    return s * n * int(abs(n) <= 0x7fffffff)

test()