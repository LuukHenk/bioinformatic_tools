#!/usr/bin/env python3
""" Counting DNA Nucleotides """

import os
import re
import sys

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

def lis(seq, seq_length, decrease=False):
    """
        Longest increasing subsequence (lis in short) using dynaming programming.
        Set descrease to true for longest decreasing sequence

    """

    # Make a counting list for increasing/decreasing values (starting value = 1)
    count = [1]*seq_length
    p = [-1]*seq_length

    # Count if values in range increasing/decrease
    i, j = 1, 0
    if decrease:
        while i < seq_length:
            if seq[i] < seq[j] and count[j] <= count[i]:
                count[i] = count[j] + 1
                p[i] = j

            j += 1

            if j == i:
                j = 0
                i += 1
    else:
        while i < seq_length:
            if seq[i] > seq[j] and count[j] <= count[i]:
                count[i] = count[j] + 1
                p[i] = j

            j += 1

            if j == i:
                j = 0
                i += 1

    idx = count.index(max(count))
    sub_seq = []
    while idx != -1:
        sub_seq.insert(0, seq[idx])
        idx = p[idx]

    return sub_seq

def main():
    " Main function for longest increasing/decreasing subsequence"

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_data = load_file(file_paths["input"])
    raw_data = re.sub(r"\n", "|", raw_data).split("|")[:-1]
    seq = list(map(int, raw_data[1].split(" ")))
    seq_length = int(raw_data[0])

    # Perform longest increasing/decreasing subsequence and convert to string
    out = re.sub(r",", "", str(lis(seq, seq_length)))[1:-1]
    out += "\n" + re.sub(r",", "", str(lis(seq, seq_length, decrease=True)))[1:-1]

    save_file(file_paths["output"], out)

# Run main scrips
if __name__ == "__main__":
    main()
