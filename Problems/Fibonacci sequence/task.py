def fibonacci(n):
    first = 0
    second = 0
    c = 0
    while c < n:
        yield first + second
        c += 1
        if c < 3:
            second = 1
        else:
            first, second = second, first + second
