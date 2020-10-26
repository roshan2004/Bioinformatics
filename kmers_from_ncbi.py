import sys
from collections import Counter
from itertools import product
from Bio import Entrez
Entrez.email = sys.argv[1]

file = input('Enter the ncbi accession number: ')
k = int(input('Enter the value of k: '))

handle = Entrez.efetch(db = 'nucleotide', id = file,rettype="fasta", retmode="text")
record = handle.read()
fasta_string = ''.join(record.split('\n')[1:])


counts = Counter(''.join(t) for t in zip(*[iter(fasta_string)]*k))

for k_mer in (''.join(t) for t in product('ACGT', repeat=k)):
    print(f"count of {k_mer} is {counts[k_mer]}")
