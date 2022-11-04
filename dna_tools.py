# DNA Toolkit file

from codecs import raw_unicode_escape_decode
from collections import Counter

from numpy import amin
from structures import *

# Validate a sequence to make sure it's composed of nucleotides
def validate_dna_seq(dna_seq):
    temp_seq = dna_seq.upper()
    for nucleotide in temp_seq:
        if nucleotide not in dna_nucleotides:
            return False
    return temp_seq

# Counter for nucleotide frequencies
def count_dna_nucleotide_frequency(seq):
    temp_freq_dict = {"A": 0, "T": 0, "C": 0, "G": 0}
    for nucleotide in seq:
        temp_freq_dict[nucleotide] += 1
    return temp_freq_dict

def count_rna_nucleotide_frequency(seq):
    temp_freq_dict = {"A": 0, "U": 0, "C": 0, "G": 0}
    for nucleotide in seq:
        temp_freq_dict[nucleotide] += 1
    return temp_freq_dict

# Transcribing DNA into RNA
def transcribe_dna_to_rna(seq):
    return seq.replace("T", "U")

def dna_complement(seq):
    return "".join([dna_to_dna_complement[nuc] for nuc in seq])
    
    # Faster pythonic approach
    # mapping = str.maketrans("ATCG", "TAGC")
    # return seq.translate(mapping)

# Generating a reverse complement for a dna sequence
def reverse_complement(seq):
    temp_seq = seq[::-1]
    rev_complement_seq = "".join([dna_to_dna_complement[nuc] for nuc in temp_seq])
    return rev_complement_seq

    # mapping = str.maketrans("ATCG", "TAGC")
    # return seq.translate(mapping)[::-1]

# Returns the GC-Content of a dna or rna sequence
def gc_content(seq):
    return ((seq.count("G") + seq.count("C")) / len(seq) * 100)

# GC Content in a DNA/RNA sub-sequence length k.
def gc_content_subsec(seq, k= 20):
    results = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        results.append(gc_content(subseq))
    return results

# Translate DNA into an amino acid sequence
def translate_sequence(seq, init_pos=0):
    return [DNA_Codons[seq[pos: pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

# Returns the frequency of each codon encoding a given amino acid in a DNA sequence
def codon_usage(seq, amino_acid):
    temp_list = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == amino_acid:
            temp_list.append(seq[i:i + 3])

    freq_dict = dict(Counter(temp_list))
    total_weight = sum(freq_dict.values())
    for seq in freq_dict:
        freq_dict[seq] = round(freq_dict[seq] / total_weight, 2)
    return freq_dict

# Generate the six reading frames of a particular sequence
def gen_reading_frames(seq):
    frames = []
    frames.append(translate_sequence(seq, init_pos=0))
    frames.append(translate_sequence(seq, init_pos=1))
    frames.append(translate_sequence(seq, init_pos=2))
    frames.append(translate_sequence(reverse_complement(seq), init_pos=0))
    frames.append(translate_sequence(reverse_complement(seq), init_pos=1))
    frames.append(translate_sequence(reverse_complement(seq), init_pos=2))
    return frames

# Returns the Hamming distance between 2 sequences
def hamming_distance(seq_a, seq_b):
    point_mutation_count = 0
    for i in range(len(seq_a)):
        if seq_a[i] != seq_b[i]:
            point_mutation_count += 1
    return point_mutation_count

# Converts a reading frame into a protein or list of proteins if it contains more than one protein
def proteins_from_reading_frame(reading_frame):
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

# Generate all RF, extract all proteins, returns a list of all proteins sorted or unsorted
def proteins_from_all_orfs(seq, start_reading_pos= 0, last_reading_pos= 0, ordered= False):
    if start_reading_pos < last_reading_pos:
        reading_frames = gen_reading_frames(seq[start_reading_pos : last_reading_pos])
    else:
        reading_frames = gen_reading_frames(seq)

    results = []
    for reading_frame in reading_frames:
        proteins = proteins_from_reading_frame(reading_frame)
        for protein in proteins:
            results.append(protein)

    if ordered:
        return sorted(results, key= len, reverse= True)
    return results
