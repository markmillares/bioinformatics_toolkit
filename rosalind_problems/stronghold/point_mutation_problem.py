import os
path = os.path.dirname(__file__)


def hamming_distance(seq_a, seq_b):
    point_mutation_count = 0
    for i in range(len(seq_a)):
        if seq_a[i] != seq_b[i]:
            point_mutation_count += 1
    return point_mutation_count

with open(path + "/rosalind_hamm.txt", "r") as f:
    sequences = f.readlines()

seq_a = sequences[0]
seq_b = sequences[1]
    

print(hamming_distance(seq_a, seq_b))