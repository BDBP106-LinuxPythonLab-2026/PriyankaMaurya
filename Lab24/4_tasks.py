# Custom Exception Classes

class InvalidDNASequenceError(Exception):
    pass


class InvalidDNACharacterError(Exception):
    pass


class DNASequence:

    def __init__(self, seq, sequence=None):

        if sequence is None:
            self.id = "seq"
            self.seq = seq
        else:
            self.id = seq
            self.seq = sequence

        if not isinstance(self.seq, str):
            raise InvalidDNASequenceError(
                "DNA sequence must be a string"
            )

        self.cleaned_seq = ''.join(self.seq.split()).upper()

        if any(base not in 'ATGC' for base in self.cleaned_seq):
            raise InvalidDNACharacterError(
                "Invalid DNA character found"
            )

        self.sequence = self.cleaned_seq
        self.length_seq = len(self.cleaned_seq)
        self.counts = {}
        self.gc = 0

    def __str__(self):
        return (
            f'Input sequence: {self.seq}\n'
            f'Cleaned sequence: {self.cleaned_seq}'
        )

    def length(self):
        return self.length_seq

    def count_bases(self):
        self.counts = {
            base: self.cleaned_seq.count(base)
            for base in 'ATGC'
        }

        print('Base counts:', self.counts)
        return self.counts

    def gc_content(self):

        if self.length_seq == 0:
            self.gc = 0
        else:
            self.gc = (
                (self.cleaned_seq.count('G') +
                 self.cleaned_seq.count('C'))
                / self.length_seq
            ) * 100

        return self.gc

    # 1. Complement Method
    def complement(self):

        complement_seq = ''

        for base in self.cleaned_seq:

            if base == 'A':
                complement_seq += 'T'
            elif base == 'T':
                complement_seq += 'A'
            elif base == 'G':
                complement_seq += 'C'
            elif base == 'C':
                complement_seq += 'G'

        return DNASequence(
            self.id + "_comp",
            complement_seq
        )

    # 2. Reverse Complement Method
    def reverse_complement(self):

        comp = self.complement()

        return DNASequence(
            self.id + "_revcomp",
            comp.cleaned_seq[::-1]
        )

    # 3. Transcription Method
    def transcribe(self):

        return self.cleaned_seq.replace('T', 'U')

    # 4. Find Site Method
    def find_site(self, site):

        if not isinstance(site, str):
            raise InvalidDNASequenceError(
                "DNA site must be a string"
            )

        site = ''.join(site.split()).upper()

        if not site:
            raise InvalidDNASequenceError(
                "DNA site cannot be empty"
            )

        if any(base not in 'ATGC' for base in site):
            raise InvalidDNACharacterError(
                "Invalid DNA character in site"
            )

        positions = []
        start = 0

        # Find all occurrences, including overlapping ones
        while True:

            position = self.cleaned_seq.find(site, start)

            if position == -1:
                break

            # Positions start from 1
            positions.append(position + 1)

            start = position + 1

        return positions

    # Check for stop codons
    def check_stop_codon(self):

        rna_seq = self.transcribe()
        stop_codons = ['UAA', 'UAG', 'UGA']

        for codon in stop_codons:

            if codon in rna_seq:
                return codon

        return None

    # Check for start codon
    def check_start_codon(self):

        rna_seq = self.transcribe()

        if 'AUG' in rna_seq:
            return 'AUG'

        return None


# Main Program

input_seq = 'AatgccTT AAGGCC TT'

dna_seq = DNASequence(input_seq)

print(dna_seq)

print('Length:', dna_seq.length())

dna_seq.count_bases()

print('GC content:', dna_seq.gc_content(), '%')

print('Complementary sequence:',
      dna_seq.complement().cleaned_seq)

print('Reverse complement:',
      dna_seq.reverse_complement().cleaned_seq)

print('Transcribed RNA sequence:',
      dna_seq.transcribe())

print('Stop codon present:',
      dna_seq.check_stop_codon())

print('Start codon present:',
      dna_seq.check_start_codon())


# Find a specific DNA site
site = input('Enter DNA site to find: ')

print('Site positions:', dna_seq.find_site(site))


# Lab 24 Test Code

s2 = DNASequence("seq2", "ATGGAATTCTAG")

print("\n----- LAB 24 TEST OUTPUT -----")

print("Original:         ", s2.cleaned_seq)

print("Complement:       ",
      s2.complement().cleaned_seq)

print("Reverse complement:",
      s2.reverse_complement().cleaned_seq)

print("mRNA:             ",s2.transcribe())

print("GAATTC at:",s2.find_site("GAATTC"))

print("TTT at:",s2.find_site("TTT"))