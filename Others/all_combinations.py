import itertools

numbers = [1, 2, 3, 4, 5, 6]
for x in numbers:
    for group in itertools.permutations(numbers, x):
        print(group)