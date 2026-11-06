import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

# Split at one or more consecutive non-ATGC characters
pattern = r"[^ATGC]+"

# re.split creates a list of sub-strings separated by ambiguous bases
valid_segments = [segment for segment in re.split(pattern, dna) if segment]

print("Output:", valid_segments)