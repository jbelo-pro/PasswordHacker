from itertools import product

for c in product(first_names, middle_names):
    print(c[0], c[1])

