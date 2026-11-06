from utils import math_utils
from utils import string_utils

# Numbers
a = 34
b = 45

print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))
print("Multiplication:", math_utils.multiply(a, b))
print("Division:", math_utils.divide(a, b))
print("Remainder:", math_utils.remainder(a, b))


# Strings
s1 = "BDBH"
s2 = "101"

print("\nUppercase:", string_utils.to_upper(s1))
print("Lowercase:", string_utils.to_lower(s1))
print("Concatenation:", string_utils.concatenate(s1, s2))