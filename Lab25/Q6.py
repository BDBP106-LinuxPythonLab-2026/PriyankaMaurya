import csv
import io
import re

# Regex pattern for an exact email match
EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_csv_line(csv_line: str) -> bool:
    # Use csv.reader to handle quotes and commas properly
    reader = csv.reader(io.StringIO(csv_line.strip()))
    fields = next(reader, [])

    # Requirement 1: Must have MORE than 3 fields (> 3)
    if len(fields) <= 3:
        return False

    # Requirement 2: 3rd field (index 2) must match email pattern
    third_field = fields[2].strip()
    return bool(re.match(EMAIL_PATTERN, third_field))


# --- Test Lines ---
test_lines = [
    "1,Abhishek,265hsbd026@ibab.ac.in,Student,2026",  # Line 1: Abhishek
    "2,Priya,user.name@domain.com,",                 # Line 2
    "3,Amit,not_an_email,Developer,India",            # Line 3
    "4,Sara,support@ibab.ac.in",                     # Line 4
    '5,tanisq,"265hsbd025@ibab.ac.in",Active,2026',  # Line 5: Tanisq
]

for line in test_lines:
    result = validate_csv_line(line)
    print(f"Line: {line:<45} | Valid: {result}")