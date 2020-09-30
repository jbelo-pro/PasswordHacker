n = int(input())


def squares(n):
    for x in range(1, n + 1):
        yield x ** 2


for k in squares(n):
    print(k)