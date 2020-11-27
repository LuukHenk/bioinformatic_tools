#!/usr/bin/env python3
""" Counting DNA Nucleotides """

import sys
import os
import re

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
    " Main function for nucleotide counting"

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_dna_string = load_file(file_paths["input"])
    dna_string = re.sub(r"\s", "", raw_dna_string)
    if not all(i in "ACGT" for i in dna_string):
        raise ValueError("DNA strand contains non-DNA characters")

    nucleotide_counts = "Nucleotides counted\nA: {}, C: {}, G: {}, T: {}".format(
        dna_string.count("A"), dna_string.count("C"), dna_string.count("G"), dna_string.count("T")
    )

    save_file(file_paths["output"], nucleotide_counts)

# Run main scrips
if __name__ == "__main__":
    main()
