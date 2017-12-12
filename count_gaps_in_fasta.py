#!/usr/bin/env python3

# The script reads a fasta file and reports the number of gaps and their percentage out of each sequence
####################################################################
# Written by Moran Neuhof, 2017

# The script reads a fasta file and reports the number of gaps and their percentage out of each sequence

from Bio import SeqIO
from sys import argv, exit

def count_gaps(record):
	"""Receives a sequence record and returns the id, gaps and the percentage of non-gaps out of the sequence"""
	
	# gaps can be denoted as '-'' or as 'N', we would like to include both:
	gaps = record.seq.count('-') + record.seq.count('N')
	non_gaps = len(record.seq) - gaps
	percent_gaps = (gaps / float(len(record.seq))) * 100
	percent_non_gaps = 100 - percent_gaps
	return f"{record.id},{gaps},{non_gaps},{percent_gaps:.4},{percent_non_gaps:.4}"


# USAGE:
if len(argv) != 2:
	print("Error: Please provide one fasta file to parse and filter.")
	print(f'Usage: {argv[0]} <fasta file>')
	exit(1)

infile = argv[1]

# read the infile once:
records = list(SeqIO.parse(infile, "fasta"))  # reaing using the BioPython SeqIO package
num_all_records = len(records)
last_kept_record_num = 0  # initialized for comparison

outfile = infile + ".gap_number.csv"

with open(outfile, 'w') as outputfile:
	print("sequence,gaps,non-gaps,percent gaps,percent non gaps", file=outputfile)
	for line in (count_gaps(record) for record in records):
		print(line, file=outputfile)

print(f"Results saved to {outfile}")
print("Done.")
