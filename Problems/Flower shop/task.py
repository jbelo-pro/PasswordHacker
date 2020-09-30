from itertools import combinations

# flower_names = ['rose', 'tulip', 'sunflower']

for r in range(1, 4):
    for c in combinations(flower_names, r):
        print(c)
