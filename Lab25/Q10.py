import re


def check_avaii_site(dna_sequence: str) -> bool:
    # Pattern matches GGACC or GGTCC using a character class [AT]
    avaii_pattern = r"GG[AT]CC"

    matches = list(re.finditer(avaii_pattern, dna_sequence))
    if matches:
        print(f"AvaII site detected! Found {len(matches)} match(es):")
        for m in matches:
            print(f"  - Sequence '{m.group()}' at position {m.start()}:{m.end()}")
        return True
    else:
        print("No AvaII restriction site found.")
        return False


# Example usage
dna1 = "CCGCTGGACCTGCTA"  # Contains GGACC
dna2 = "ATCGGTCCTAAA"  # Contains GGTCC
dna3 = "ATCGCGTTCCAC"  # Invalid sequence

check_avaii_site(dna1)
print("-" * 40)
check_avaii_site(dna2)
print("-" * 40)
check_avaii_site(dna3)