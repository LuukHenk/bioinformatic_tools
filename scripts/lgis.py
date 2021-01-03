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

# Method from internet
# def lgis(seq):
#     incr_list = [[seq[0]]]
#     for i in range(1, len(seq)):
#         incr_list.append(
#             max([incr_list[j] for j in range(i) if incr_list[j][-1] < seq[i]] or [[]], key=len)
#             + [seq[i]]
#         )
#     return max(incr_list, key=len)

def main():
    " Main function for longest increasing/decreasing subsequence"

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_data = load_file(file_paths["input"])
    raw_data = re.sub(r"\n", "|", raw_data).split("|")[:-1]
    seq = list(map(int, raw_data[1].split(" ")))
    seq_length = int(raw_data[0])

    # save_file(file_paths["output"], out)

# Run main scrips
if __name__ == "__main__":
    main()
