# Basic zip example with two lists
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# Creating a dictionary from two lists using zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Zip with different length iterables
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']  # Notice this is shorter
for num, letter in zip(list1, list2):
    print(num, letter)
# Output:
# 1 a
# 2 b
# 3 c
# (4 is ignored since list2 is shorter)

# Matrix transposition
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = list(zip(*matrix))
for row in transposed:
    print(row)
# Output:
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)

# Zipping and then unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # Output: (1, 2, 3)
print(letters)  # Output: ('a', 'b', 'c')