n = int(input())


def even():
    initial = 0
    while True:
        yield initial
        initial += 2


g = even()
for i in range(n):
    print(next(g))
