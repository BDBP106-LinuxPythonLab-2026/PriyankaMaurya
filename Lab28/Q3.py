#A DNA fragment of unknown orientation:
#mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")
#1. Translate all six reading frames: frames +1, +2 and +3 start at positions 0, 1 and 2
#of mystery; frames -1, -2 and -3 do the same on its reverse complement.
#2. Find the longest open reading frame: a stretch that starts with M and ends at a stop
#codon.
#Hint: trim each frame to a multiple of 3 bases before translating (s[:len(s) - len(s) % 3]),
#otherwise Biopython warns about a partial codon.


from Bio.Seq import Seq

# DNA sequence
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")

# 1. Translate all six reading frames

print("Six Reading Frames:")

frames = {}

# Forward strand (+1, +2, +3)
for i in range(3):
    frame = mystery[i:]
    frame = frame[:len(frame) - len(frame) % 3]

    protein = frame.translate()
    frames["+" + str(i + 1)] = protein

# Reverse complement strand (-1, -2, -3)
reverse_seq = mystery.reverse_complement()

for i in range(3):
    frame = reverse_seq[i:]
    frame = frame[:len(frame) - len(frame) % 3]

    protein = frame.translate()
    frames["-" + str(i + 1)] = protein

# Print all six translations
for name, protein in frames.items():
    print(name, ":", protein)


# 2. Find the longest Open Reading Frame (ORF)

longest_orf = ""
longest_frame = ""

for name, protein in frames.items():

    for i in range(len(protein)):

        if protein[i] == "M":

            # Find the next stop codon
            for j in range(i + 1, len(protein)):

                if protein[j] == "*":

                    orf = protein[i:j]

                    if len(orf) > len(longest_orf):
                        longest_orf = orf
                        longest_frame = name

                    break

print("\nLongest ORF:", longest_orf)
print("Reading Frame:", longest_frame)
print("ORF Length:", len(longest_orf), "amino acids")
print("Stop Codon: *")