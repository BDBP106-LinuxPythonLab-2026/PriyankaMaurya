import re
pattern = r"^(?:[0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$"

def check_number(text):
    if re.match(pattern, text):
        return "Valid (0 to 255)"
    else:
        return "Invalid"


test_inputs = ["0", "5", "99", "150", "255", "256", "05", "000"]

for val in test_inputs:
    print(f"{val} -> {check_number(val)}")