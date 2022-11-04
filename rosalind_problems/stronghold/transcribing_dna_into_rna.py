def transcribe_dna_to_rna(seq):
    return seq.replace("T", "U")

sample_seq = "TAAATCCGGTATAGCATAAAATTAGCCCTCACAAAGACACACGACTATGAAGCGGAGGCGCTTATCTCACTGCGGAGTTGGAAACTAGCCGCGTACGGCATCGTCTTTCATTCACGGGGTCGAGGGTTCTTGGCCAAATGACCCTAGCTTGCCAGAACTTTCTATAGTTACATGCGGCAGACATGCAGTTAGTATTACCTATTCTGTTCACTTGTAGCCAGTATCATCCGCCAGTTGCTAGCTGGTTTGCCTATGCTGAAATCCTAGAACCACCCCCTCCTTAGCTCCGGCTTATGCAATGCCGGAGGACTCGAATGCCGTAGAACTAGTAACCTTAGAAAATATATGCGCCGTAAAACCTCTACCGCAACCTGATTGGCTCGATAGCTATAGTGAGCCACCCAAGGAGACGCGAGAACCCAGATCCATGGGCAATACGTAGCCCCCAAGTCTCGTTCGTCCGATAGCGCGAGCCGACGAGATGCAACATGGGTGTACATCACACCGGTGGGGAGGGGAAATTCCATAACGGTCCGCGCCCACTGCAGATAGCTAAAAGACGAGGGGCGACGACTACGGATGAAGATCTAGGTGCTGCGTCCTCAAGAAGTGACCATTCTGCATCGGCGCGTCGCCCTTACCGTACAATAGAGACACAGATTAAATGCGCAACTTGTGGACACATGCGTACGATGATCAACAATCCTTTTCGAACGGTGCCTGATAACAGTTATAGCTCCCTTCTGCTGCGGATGAACATTGAATCAATAAACCTCTCCCAACGAATCCCGAAAAAAAATCCATTAGCGCGCGGCTTGTTAATACCACATGCTATCCTGGTTGAAAGCCTTATTATTTCAAGACTGAAATCCGTAACCACGCAGTCCCAAGCCAGCCTGGGGCACAAGGGAAT"

print(transcribe_dna_to_rna(sample_seq))