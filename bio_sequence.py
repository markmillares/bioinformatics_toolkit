from bio_structures import *
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

    def count_nucleotide_frequency(self):
        """Returns the frequency for each nucleotide in the sequence"""
        return dict(Counter(self.seq))
