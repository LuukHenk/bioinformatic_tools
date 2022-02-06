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

def lgis(seq, n):
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if seq[i] > seq[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    print(lis)
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    print(maximum)




def main():
    " Main function for longest increasing/decreasing subsequence"

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_data = load_file(file_paths["input"])
    raw_data = re.sub(r"\n", "|", raw_data).split("|")[:-1]
    seq = list(map(int, raw_data[1].split(" ")))
    seq_length = int(raw_data[0])
    print("len: {}".format(seq_length))
    print("seq: {}".format(seq))
    lgis(seq, seq_length)

    # save_file(file_paths["output"], out)

# Run main scrips
if __name__ == "__main__":
    main()
