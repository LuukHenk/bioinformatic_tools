#!/usr/bin/env python3
" Generation of a k-mer composition array "

import os
import re
import sys
from itertools import product

def generate_io_file_paths():
    "Generate the input- and output file paths"

    file_paths = {"input": "", "ouput": ""}

    path = os.path.abspath(__file__)
    filename = os.path.splitext(os.path.basename(path))[0]
    main_dir = os.path.abspath(os.path.join(path, "..", ".."))

    file_paths["input"] = "{}/input/rosalind_{}.txt".format(main_dir, filename)
    file_paths["output"] = "{}/output/rosalind_{}.txt".format(main_dir, filename)

    return file_paths

def load_file(filename):
    "Load a file"

    try:
        with open(filename, 'r') as myfile:
            inp = myfile.read()
        print("Opened '{}' ...\n-------\n".format(filename))
    except IOError:
        print("Unable to locate the input file '{}'".format(filename))
        sys.exit()

    return inp

def save_file(filename, output):
    "Save data to a file"

    with open(filename, 'w') as myfile:
        myfile.write(output)
        print("Saved output in '{}' ...\n-------\n".format(filename))


def main():
    " Main function for k-mer composition "

    # set variables
    fasta_naming_style = r"(Rosalind_\d\d\d\d)"
    kmer_size = 4

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_fasta_data = load_file(file_paths["input"])
    raw_fasta_data = re.sub(r"\s", "", raw_fasta_data).split(">")[1:]
    if len(raw_fasta_data) != 1:
        raise IndexError("""
            Input should only contain one FASTA string;
            More or less than one FASTA identifiers detected ('>')
        """)
    dna_string = re.sub(fasta_naming_style, "", raw_fasta_data[0])
    if not all(i in "ACGT" for i in dna_string):
        raise ValueError("DNA strand contains non-DNA characters")

    # Generate k-mer array
    kmer_count = {}
    product_list = list(product("ACGT", repeat=kmer_size))
    for kmer in product_list:
        kmer_count["".join(kmer)] = 0

    # Count k-mers values
    for position in range(0, len(dna_string) - kmer_size + 1):
        kmer = dna_string[position:position + kmer_size]
        kmer_count[kmer] = kmer_count[kmer] + 1

    # Format desired output
    kmer_count_output = re.sub(r", ", "\n", str(kmer_count)[1:-1])
    output_data = "{}-mers found in file:\n\n{}".format(kmer_size, kmer_count_output)
    save_file(file_paths["output"], output_data)

# Run main scrips
if __name__ == "__main__":
    main()
