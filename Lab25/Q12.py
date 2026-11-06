import re

dna = "ATCGCGYAATTCAC"

# Regex for non-standard/ambiguous bases
ambiguous_pattern = r"[^ATGC]"

# Find all ambiguous bases
ambiguous_bases = re.findall(ambiguous_pattern, dna)

if ambiguous_bases:
    print(f"Ambiguous bases found: {set(ambiguous_bases)}")

    # Extract and display all standard/non-ambiguous bases
    non_ambiguous_bases = re.findall(r"[ATGC]", dna)
    print("Non-ambiguous bases in sequence:", "".join(non_ambiguous_bases))
else:
    print("No ambiguous bases found in the DNA sequence.")