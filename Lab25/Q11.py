import re

dna = "ATCGCGAATTCAC"

# [ATGC] matches any single standard DNA base inside GCNGC
bisi_pattern = r"GC[ATGC]GC"

match = re.search(bisi_pattern, dna)

if match:
    print(f"BisI site found: '{match.group()}' at index {match.start()}:{match.end()}")
else:
    print("No BisI restriction site found.")