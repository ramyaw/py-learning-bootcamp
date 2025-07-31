name = "John"
print(f" - {name}")

name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

name = "Alice"
# Old % formatting
print("Hello, %s" % name)
# str.format() method
print("Hello, {}".format(name))
# f-string (modern, cleaner)
print(f"Hello, {name}")

# Formatting numbers
price = 19.9999
print(f"Price: ${price:.2f}")

price = 5.0
print(f"Price: ${price:.2f}")

# Expressions
a = 5
b = 3
print(f"Sum: {a + b}")  # Sum: 8




# Strings
name = "Alice"
print(f"Name: {name}")  # Name: Alice

# Integers
age = 25
print(f"Age: {age}")  # Age: 25

# Floats
height = 1.75
print(f"Height: {height}")  # Height: 1.75

# Booleans
is_student = True
print(f"Is student? {is_student}")  # Is student? True

# Lists
fruits = ["apple", "banana"]
print(f"Fruits: {fruits}")  # Fruits: ['apple', 'banana']

# Dictionaries
person = {"name": "Bob", "age": 30}
print(f"Person: {person}")  # Person: {'name': 'Bob', 'age': 30}

# None
value = None
print(f"Value: {value}")  # Value: None

# Expressions
a = 10
b = 5
print(f"Sum: {a + b}")  # Sum: 15
print(f"Is a > b? {a > b}")  # Is a > b? True

# Methods
text = "hello"
print(f"Uppercase: {text.upper()}")  # Uppercase: HELLO


# Float formatting
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")  # Pi to 2 decimal places: 3.14

# Integer formatting with padding
number = 42
print(f"Number with padding: {number:04d}")  # Number with padding: 042

# Percentage formatting
ratio = 0.8543
print(f"Percentage: {ratio:.1%}")  # Percentage: 85.4%
print(f"Percentage: {ratio:.2%}")

# Scientific notation
large_num = 1000000
print(f"Scientific: {large_num:e}")  # Scientific: 1.000000e+06
print(f"Scientific: {large_num:.2e}")


# Width specification
text = "hi"
print(f"{text:>10}")     # '        hi' (right align, width 10)
print(f"{text:<10}")     # 'hi        ' (left align, width 10)
print(f"{text:^10}")     # '    hi    ' (center align, width 10)

# Binary, Octal, Hex Formatting
num = 42
print(f"{num:b}")        # 101010 (binary)
print(f"{num:o}")        # 52 (octal)
print(f"{num:x}")        # 2a (hex)
print(f"{num:X}")        # 2A (hex uppercase)


# The format specification after the colon follows this general pattern:
#   {expression:[alignment][sign][#][0][width][grouping][.precision][type]}
# Where each part is optional and:
# - `alignment`: `<` (left), `>` (right), `^` (center)
# - `width`: minimum field width
# - `precision`: decimal places for floats
# - `type`: formatting type (f, d, %, e, etc.)
# This formatting system gives you precise control over how values are displayed in your strings.
number = 123.456
print(f"{number:>10.2f}")  # '    123.46' (right-aligned, width 10, 2 decimal places)

