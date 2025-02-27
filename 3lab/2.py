# рекурсивный метод
def x(i):
    if i == 1:
        return 1
    if i == 2:
        return -1/8
    else:
        return ((i-1)*x(i-1))/3 + (i-2)*x(i-2)/4
print(x(7))

# итеративный метод
def x(n):
    if n == 1:
        return 1
    if n == 2:
        return -1 / 8
    v = [0] * (n + 1)
    v[1] = 1
    v[2] = -1 / 8
    for i in range(3, n + 1):
        v[i] = ((i - 1) * v[i - 1]) / 3 + (i - 2) * v[i - 2] / 4
    return v[n]
print(x(7))