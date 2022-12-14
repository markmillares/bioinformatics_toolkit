dna_to_dna_complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

def reverse_complement(seq):
    temp_seq = seq[::-1]
    rev_complement_seq = "".join([dna_to_dna_complement[nuc] for nuc in temp_seq])
    return rev_complement_seq

seq = "CCACGCGTGCGTATGGTCAAGCAGCCTGCGACACATCACTGCAGTCACGAAGTTAAATACAAGCAGTTTTAGGTATGGTTGCATGGGACTGCAGTGGGTTAATGCTGAGTGGCATCCACCCTTTGCAAATAATCAACTGTACTCTCTCATGCACACTTTAGCGCTATAGTTAACGGAAGATAAATCCGTCACTCCGGTGGCCCCAGTTTTGGCAGCAAAAGACATTAAGTCACCCGATGCCCAATCGTGTTGCGAGCAGGTTCTTGAGGCGCCTAGATCCGTTTTCGGCAAGCCTGACAGGCTCTCACTGAACCCCGAGAGGAGGTATTTGGCAAGACAGCTCTATCCCAAGACTCCGAAACGAAATGGCAAGCTCGCTTAATCTTAGACCTACTTGGCGGCCTTTTTGGCGCAAAAGTTCTATCCTCCGTCTGTATGGGACGAAGCTCGGGCGTCATAAATGAGAGTACATAGATTTCATAAAGGCCAGCCACTTCCACATGAATCTTTTCGCTTGATTTACAGTTCTAATAAATGGTCTATGGGAGTTAACACTTTGTTCTCCCCCTGCGTTAGGGGTTTAAAGTACCATGGCTTGATTAACATGTGGATCCTAACTGGCAATATACATGGCGATAGGAGACAGGGTGGCCAGGAGTTCCAGTGACACGCCCCCTCGGAGTCGAATTCGATCAGAGAGAATCTCTACATGGTGCCAGGGGTGAGGCGTTATGCTTCGCGCACGGAAATTTCTTCTCTATATTCATATCAAATGCGGCATAGACCAATATCTAGACTTTACTTCTCTGCGAAAGTGAAAGCTTGTGGACCTGCTCTGCCGGGAAGTTGGGACGCTCTAGACTAAACGACCGCTGAGGGGCAATCACGT"

print(reverse_complement(seq))