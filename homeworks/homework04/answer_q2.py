# Question 2: How many HA sequences did not have a valid barcode? 
# Also answer the same question for NA.

from Bio import SeqIO
from Bio.Seq import reverse_complement
import re

# Define the known end sequences for HA and NA genes
ha_end = "CCGGATTTGCATATAATGATGCACCAT"
na_end = "CACGATAGATAAATAATAGTGCACCAT"

# Reverse complements for identifying reads
ha_rc = reverse_complement(ha_end)
na_rc = reverse_complement(na_end)

# Spacer sequence that separates barcode from gene end
spacer = "GCGGCCGCCT"

# Counters for HA and NA
ha_total = 0
ha_valid_barcodes = 0
na_total = 0
na_valid_barcodes = 0

# Parse the FASTQ file
fastq_file = "barcodes_R1.fastq"

for record in SeqIO.parse(fastq_file, "fastq"):
    read_seq = str(record.seq)
    
    # Check if read matches HA
    if ha_rc in read_seq:
        ha_total += 1
        
        # Find where the spacer sequence begins
        spacer_pos = read_seq.find(spacer)
        if spacer_pos != -1:
            # The barcode is the sequence before the spacer
            barcode = read_seq[:spacer_pos]
            
            # Check if barcode is valid: exactly 16 nucleotides with only ATGCN
            if len(barcode) == 16 and re.match(r"^[ATGCN]{16}$", barcode):
                ha_valid_barcodes += 1
    
    # Check if read matches NA
    elif na_rc in read_seq:
        na_total += 1
        
        # Find where the spacer sequence begins
        spacer_pos = read_seq.find(spacer)
        if spacer_pos != -1:
            # The barcode is the sequence before the spacer
            barcode = read_seq[:spacer_pos]
            
            # Check if barcode is valid: exactly 16 nucleotides with only ATGCN
            if len(barcode) == 16 and re.match(r"^[ATGCN]{16}$", barcode):
                na_valid_barcodes += 1

# Calculate sequences without valid barcodes
ha_without_valid_barcode = ha_total - ha_valid_barcodes
na_without_valid_barcode = na_total - na_valid_barcodes

# Display results
print("HA sequences without valid barcode:", ha_without_valid_barcode)
print("NA sequences without valid barcode:", na_without_valid_barcode)
