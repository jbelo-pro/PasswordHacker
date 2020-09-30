try:
    n = int(input())
    denominator = int(input())
    print(n // denominator)
except ZeroDivisionError as e:
    print("Division by zero is not supported")