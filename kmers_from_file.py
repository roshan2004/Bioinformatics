import sys
from collections import Counter
from itertools import product
b = True
while b:
    file = sys.argv[1]
    try:
        with open(file) as f:
            f.readline()
            ly = []
            for i in f.readlines():
                ly.append(i)
        b = False
    except:
        print('Enter the correct filename: ')
        
   
fasta_string = ''.join([i.strip() for i in ly])
k = int(input('Enter the value of k: '))



counts = Counter(fasta_string[i:i+k] for i in range(0,len(fasta_string)) if len(fasta_string[i:i+k])==k)

for k_mer in (''.join(t) for t in product('ACGT', repeat=k)):
    print(f"count of {k_mer} is {counts[k_mer]}")
