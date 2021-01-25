a, b, c, x, y = 1, 2, 4, 8, 16


def mystery(x, y):
    global a
    a = 65
    x, y = x * x, y * y
    b = 16
    b = b * 2
    c = 4323
    print(a, b, c, x, y)


mystery(10, 12)
print(a, b, c, x, y)
