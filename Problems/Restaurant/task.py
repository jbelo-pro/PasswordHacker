from itertools import product

# main_courses = ['beef stew', 'fried fish']
# price_main_courses = [28, 23]

# desserts = ['ice-cream', 'cake']
# price_desserts = [2, 4]

# drinks = ['cola', 'wine']
# price_drinks = [3, 10]

for c in product(zip(main_courses, price_main_courses),
                 zip(desserts, price_desserts),
                 zip(drinks, price_drinks)):
    t = c[0][1] + c[1][1] + c[2][1]
    if t <= 30:
        print(c[0][0], c[1][0], c[2][0], t)

