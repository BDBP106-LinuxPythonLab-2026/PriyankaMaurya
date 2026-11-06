
#Q1. The thrL gene of E. coli encodes a short leader peptide:
# thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
# Print its length, its GC content as a percentage (2 decimal places), its translation with
# and without to stop=True, the number of times ACC occurs, its last codon, and the first
# 12 bases of its reverse complement.

from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

thrL = Seq("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")
print("Length:", len(thrL))
print("GC Content:", round(gc_fraction(thrL) * 100, 2), "%")
print("Translation:", thrL.translate())
print("Translation with stop:", thrL.translate(to_stop=True))
print("ACC Count:", thrL.count("ACC"))
print("Last Codon:", thrL[-3:])
print("First 12 bases of Reverse Complement:", thrL.reverse_complement()[:12])


print("==========================================")

