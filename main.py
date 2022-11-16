from dna_tools import *
from structures import *
import random
from bio_sequence import BioSeq

# Generating random sequence
# random_seq = "".join([random.choice(dna_nucleotides) for nucleotide in range(50)])

# validated_seq = validate_dna_seq(random_seq)

# print(f"\nSequence: {validated_seq}\n")
# print(f"[1] + Sequence Length: {len(validated_seq)}")
# print(f"[2] + DNA Nucleotide Frequency: {count_dna_nucleotide_frequency(validated_seq)}")
# print(f"[3] + DNA Transcribed to RNA: {transcribe_dna_to_rna(validated_seq)}\n")
# print(f"[4] + DNA Sequence + Complement + Reverse Complement:")
# print(f"5' {validated_seq} 3'")
# print(f"   {''.join(['|' for x in range(50)])}")
# print(f"3' {dna_complement(validated_seq)} 5' [Complement]")
# print(f"5' {reverse_complement(validated_seq)} 3' [Reverse Complement]")
# print(f"\n[5] + GC Content: {round(gc_content(validated_seq), 1)}%")
# print(f"[6] + GC Content in Subsection k=5: {gc_content_subsec(validated_seq, k=5)}")
# print(f"\n[7] + Amino Acid Sequence from DNA:{translate_sequence(validated_seq)}")
# print(f"[8] + Codon Frequency (L): {codon_usage(validated_seq, 'L')}")
# print(f"[9] + Reading Frames:")
# for frame in gen_reading_frames(validated_seq):
#     print(frame)

# print(f"\n[10] + All proteins in 5 open reading frames:")
# for protein in proteins_from_all_orfs(BC005255_1, ordered= True):
#     print(protein)


# test_dna = BioSeq("ATCGGGAAAATTTCCCC")

# print(test_dna.get_seq_info())
# print(test_dna.get_seq_type())

test_dna_2 = BioSeq.generate_random_seq()
print(test_dna_2.get_seq_info())