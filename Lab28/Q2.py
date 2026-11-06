from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#1. Read lab genes.fasta with SeqIO.parse() into a list and print how many records it has.
records = list(SeqIO.parse("lab_genes.fasta", "fasta"))

print("Total Records:", len(records))

# 2. Print a table of ID, length, GC % (1 decimal place) and the protein translated up to
# the first stop codon.
print("\nID\tLength\tGC %\tProtein")

for record in records:
    gc = gc_fraction(record.seq) * 100
    protein = record.seq.translate(to_stop=True)

    print(record.id, len(record.seq), f"{gc:.1f}%", protein, sep="\t")

# 3. Write the genes with GC content of at least 50% to lab high gc.fasta, and print how
# many were written.
high_gc = []

for record in records:
    gc = gc_fraction(record.seq) * 100

    if gc >= 50:
        high_gc.append(record)

SeqIO.write(high_gc, "lab_high_gc.fasta", "fasta")

print("\nHigh GC sequences written:", len(high_gc))

# 4. Print the IDs sorted from highest to lowest GC content, using sorted() with a lambda.
sorted_records = sorted(
    records,
    key=lambda record: gc_fraction(record.seq),
    reverse=True
)

print("\nIDs sorted by GC content:")

for record in sorted_records:
    print(record.id)

print("==========================================")



