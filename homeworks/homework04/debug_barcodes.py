from Bio import SeqIO
from Bio.Seq import reverse_complement
import re

ha_rc = reverse_complement('CCGGATTTGCATATAATGATGCACCAT')
spacer = 'GCGGCCGCCT'

fastq_file = 'barcodes_R1.fastq'

print('Sample barcodes from HA reads:')
count = 0
for record in SeqIO.parse(fastq_file, 'fastq'):
    read_seq = str(record.seq)
    
    if ha_rc in read_seq and count < 5:
        spacer_pos = read_seq.find(spacer)
        barcode = read_seq[:spacer_pos]
        
        print(f'Read {count+1}: Barcode = "{barcode}" (len={len(barcode)})')
        print(f'  Is 16 chars: {len(barcode) == 16}')
        print(f'  Matches [ATGCN]{{16}}: {bool(re.match(r"^[ATGCN]{16}$", barcode))}')
        print()
        
        count += 1
