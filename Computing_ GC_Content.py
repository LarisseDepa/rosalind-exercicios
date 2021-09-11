# referencias
# https://www.youtube.com/watch?v=LddJx5n8vqA
# https://github.com/vappiah/Python-Bioinformatics-Hacks/blob/main/Notebooks/GC_content.ipynb

from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd


filepath = '/Users/BAHIANA/Desktop/rosalind/rosalind_gc.txt'
seq_objects = SeqIO.parse(filepath, 'fasta')
sequences = [seq for seq in seq_objects]
number_of_sequences = len(sequences)
print(number_of_sequences)

for seq in sequences:
    seq_id = seq.id
    sequence = seq.seq
    gc_content = GC(sequence)
    print(seq_id, gc_content)
