import re

dna = "ATCGCGAATTCAC"
pattern = r"GAATTC"

# re.search returns a match object if the pattern exists in the sequence
match = re.search(pattern, dna)

if match:
    print(f"EcoRI site found at index positions {match.start()} to {match.end() - 1}.")
else:
    print("No EcoRI restriction site found.")