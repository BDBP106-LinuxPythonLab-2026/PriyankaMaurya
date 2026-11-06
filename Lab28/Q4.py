# A cloning construct (49 bp) contains a BamHI site, a short coding sequence and an
# EcoRI site:
# plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")
# 1. Create a SeqRecord with id and name PLAB001, set annotations[”molecule type”] =
# ”DNA”, and add three features: a misc feature for the BamHI site at 0-6, a CDS at 8-41
# with qualifiers gene = labA and translation = MASKGEELFT, and a misc feature for
# the EcoRI site at 41-47 (Python-style positions).
# 2. Write it to lab construct.gb in GenBank format; open the file in a text editor and
# find the FEATURES table.
# 3. Read it back with SeqIO.read() and list every feature with its type, its 1-based start
# and end, and its gene or note.
# 4. Extract the CDS, translate it, and check that the result matches the stored translation
# qualifier.



from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO

# DNA sequence
plasmid_seq = Seq("GGATCCTTATGGCTAGCAAAGGAGAAGAACTTTTCACTTAAGAATTCCC")

# 1. Create SeqRecord
record = SeqRecord(
    plasmid_seq,
    id="PLAB001",
    name="PLAB001",
    description="Cloning construct"
)

record.annotations["molecule_type"] = "DNA"

# Add three features
bamhi = SeqFeature(
    FeatureLocation(0, 6),
    type="misc_feature",
    qualifiers={"note": "BamHI site"}
)

cds = SeqFeature(
    FeatureLocation(8, 41),
    type="CDS",
    qualifiers={
        "gene": "labA",
        "translation": "MASKGEELFT"
    }
)

ecori = SeqFeature(
    FeatureLocation(41, 47),
    type="misc_feature",
    qualifiers={"note": "EcoRI site"}
)

record.features = [bamhi, cds, ecori]

# 2. Write to GenBank file
SeqIO.write(record, "lab_construct.gb", "genbank")

print("GenBank file created successfully!")

# 3. Read GenBank file
new_record = SeqIO.read("lab_construct.gb", "genbank")

print("\nFeatures in GenBank file:")
print("Type\t\tStart\tEnd\tGene/Note")

for feature in new_record.features:
    start = int(feature.location.start) + 1
    end = int(feature.location.end)

    gene_or_note = (
        feature.qualifiers.get("gene", [""])[0]
        or feature.qualifiers.get("note", [""])[0]
    )

    print(feature.type, start, end, gene_or_note, sep="\t")

# 4. Extract CDS and translate
for feature in new_record.features:

    if feature.type == "CDS":

        cds_seq = feature.extract(new_record.seq)
        protein = cds_seq.translate(to_stop=True)

        stored_translation = feature.qualifiers["translation"][0]

        print("\nCDS Sequence:", cds_seq)
        print("Translated Protein:", protein)
        print("Stored Translation:", stored_translation)

        if str(protein) == stored_translation:
            print("Translation matches: YES")
        else:
            print("Translation matches: NO")