import re

# Simple pattern:
# 000-199  -->  [01]\d\d
# 200-249  -->  2[0-4]\d
# 250-255  -->  25[0-5]
pattern = r"^([01]\d\d|2[0-4]\d|25[0-5])$"

def check_number(text):
    if re.match(pattern, text):
        return "Valid (between 000 and 255)"
    else:
        return "Invalid"

test_inputs = ["000", "150", "255", "256", "300", "999", "12"]

for val in test_inputs:
    print(f"{val} -> {check_number(val)}")