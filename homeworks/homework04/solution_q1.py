"""
Question 1: How many reads map to HA, and how many reads map to NA?

This script analyzes a FASTQ file to count reads that correspond to 
influenza HA (hemagglutinin) and NA (neuraminidase) genes.

The analysis works by looking for the reverse-complement sequences of 
the gene-specific end sequences in each read.

References:
- BioPython documentation: https://biopython.org/
- Course lectures 8 and 9 on FASTQ file analysis
"""

from Bio import SeqIO
from Bio.Seq import reverse_complement

# Define the known end sequences for HA and NA genes
# These are the 3' end sequences of the original HA and NA genes
ha_end = "CCGGATTTGCATATAATGATGCACCAT"
na_end = "CACGATAGATAAATAATAGTGCACCAT"

# Since the reads come from the reverse end of the molecules, we need to look
# for the reverse complement of these sequences in our reads
ha_rc = reverse_complement(ha_end)
na_rc = reverse_complement(na_end)

print("Expected reverse complement sequences in reads:")
print(f"HA reverse complement: {ha_rc}")
print(f"NA reverse complement: {na_rc}")

# Initialize counters for HA and NA reads
ha_count = 0
na_count = 0

# Parse the FASTQ file and count reads matching each gene
fastq_file = "barcodes_R1.fastq"

for record in SeqIO.parse(fastq_file, "fastq"):
    read_seq = str(record.seq)
    
    # Check if this read contains the HA-specific sequence
    if ha_rc in read_seq:
        ha_count += 1
    # Check if this read contains the NA-specific sequence
    elif na_rc in read_seq:
        na_count += 1

# Display results
print("\n" + "="*50)
print("ANSWER TO QUESTION 1:")
print("="*50)
print(f"Number of reads mapping to HA: {ha_count}")
print(f"Number of reads mapping to NA: {na_count}")
print(f"Total mapped reads: {ha_count + na_count}")
print("="*50)
