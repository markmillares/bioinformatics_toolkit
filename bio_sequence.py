from bio_structures import DNA_Codons, dna_nucleotides
from collections import Counter
import random

class BioSeq():
    """DNA sequence class. Accepts string. Default value: ATCG, DNA, No label."""
    def __init__(self, sequence, seq_type="DNA", label="No Label"):
        self.seq = sequence.upper()
        self.label = label
        self.seq_type = seq_type
        self.length = len(sequence)
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be a correct {self.seq_type} sequence."

    def __validate(self):
        """Check sequence to make sure it is a valid DNA string."""
        return set(dna_nucleotides).issuperset(self.seq)

    @classmethod
    def generate_random_seq(cls, length=50):
        """Creates a random sequence for testing"""
        seq = "".join([random.choice(dna_nucleotides) for nucleotide in range(length)])
        return cls(sequence= seq, seq_type="DNA", label="Random Generated Sequence")

    def get_seq_type(self):
        """Returns sequence type."""  
        return self.seq_type

    def get_seq_info(self):
        """Returns full sequence information."""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[length]: {self.length}"

    def nucleotide_frequency(self):
        """Returns the frequency for each nucleotide in the sequence"""
        return dict(Counter(self.seq))

    def transcribe_to_rna(self):
        """DNA to RNA form, T replaced with U"""
        if self.seq_type == "DNA":
            return self.seq.replace("T", "U")
        else:
            return "Sequence type is already RNA."

    def dna_complement(self):
        """Returns the DNA pair strand for a given DNA sequence"""
        mapping_table = str.maketrans("ATCG", "TAGC")
        return self.seq.translate(mapping_table)

    def dna_reverse_complement(self):
        """Generates a reverse complement for a DNA sequence"""
        mapping_table = str.maketrans("ATCG", "TAGC")
        return self.seq.translate(mapping_table)[::-1]

    def gc_content(self):
        """GC-content of a sequence"""
        return ((self.seq.count("G") + self.seq.count("C")) / len(self.seq) * 100)

    def gc_content_subsec(self, k= 20):
        results = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i + k]
            results.append((subseq.count("G") + subseq.count("C")) / len(subseq) * 100)
        return results

    def translate_sequence(self, init_pos=0):
        """Translates DNA sequence into amino acid"""
        return [DNA_Codons[self.seq[pos: pos + 3]] for pos in range(init_pos, len(self.seq) - 2, 3)]

    def codon_usage(self, amino_acid):
        """Returns the frequency of each codon encoding a given amino acid in a DNA sequence"""
        temp_list = []
        for i in range(0, len(self.seq) - 2, 3):
            if DNA_Codons[self.seq[i:i + 3]] == amino_acid:
                temp_list.append(self.seq[i:i + 3])

        freq_dict = dict(Counter(temp_list))
        total_weight = sum(freq_dict.values())
        for codon in freq_dict:
            freq_dict[codon] = round(freq_dict[codon] / total_weight, 2)
        return freq_dict

    def reading_frames(self):
        """Generate the six reading frames of a particular sequence"""
        frames = []
        frames.append(self.translate_sequence(init_pos=0))
        frames.append(self.translate_sequence(init_pos=1))
        frames.append(self.translate_sequence(init_pos=2))

        temp_seq = BioSeq(self.dna_reverse_complement(), seq_type= self.seq_type, label= self.label)

        frames.append(temp_seq.translate_sequence(init_pos=0))
        frames.append(temp_seq.translate_sequence(init_pos=1))
        frames.append(temp_seq.translate_sequence(init_pos=2))
        del temp_seq
        return frames
    
    @staticmethod
    def proteins_from_reading_frame(reading_frame):
        """Converts a reading frame into a protein or list of proteins if it contains more than one protein"""
        current_protein = []
        proteins = []

        for amino_acid in reading_frame:
            if amino_acid == "_":
                if current_protein:
                    for protein in current_protein:
                        proteins.append(protein)
                    current_protein = []
            else:
                if amino_acid == "M":
                    current_protein.append("")
                for i in range(len(current_protein)):
                    current_protein[i] += amino_acid
        return proteins

    def proteins_from_all_orfs(self, start_reading_pos= 0, last_reading_pos= 0, ordered= False):
        """Generate all RF, extract all proteins, returns a list of all proteins sorted or unsorted"""
        if start_reading_pos < last_reading_pos:
            temp_seq = BioSeq(self.seq[start_reading_pos : last_reading_pos], self.seq_type, self.label)
            reading_frames = temp_seq.reading_frames()
        else:
            reading_frames = self.reading_frames()

        results = []
        for reading_frame in reading_frames:
            proteins = self.proteins_from_reading_frame(reading_frame)
            for protein in proteins:
                results.append(protein)

        if ordered:
            return sorted(results, key= len, reverse= True)
        return results