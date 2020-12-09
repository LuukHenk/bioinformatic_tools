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

def longest_increasing_subsequence_method_one(seq, seq_length):
    longest_increasing_seq = [seq_length]
    # longest_increasing_seq_len = len(longest_increasing_seq)

    for seq_position in range(seq_length-1):
        for starting_match in range(seq_position + 1, seq_length):
            current_sequence = [seq[seq_position]]

            # if current_sequence[0] == seq_length \
            # or seq_length - starting_match < longest_increasing_seq_len:
            #     break

            for match_position in range(starting_match, seq_length):
                match = seq[match_position]

                if match > current_sequence[-1]:
                    current_sequence.append(match)

                # if match == seq_length:
                #     break

            # Dit verplaatsen paar per sequence positie in plaats van match positie
            if len(current_sequence) > len(longest_increasing_seq):
                longest_increasing_seq = current_sequence
                # print(current_sequence)
                # longest_increasing_seq_len = len(longest_increasing_seq)

    return longest_increasing_seq

def longest_increasing_subsequence_method_two(seq, seq_length):
    longest_sequences = []
    for seq_position in range(seq_length-1):
        print(seq_position)
        for starting_match in range(seq_position + 1, seq_length):
            current_sequence = [seq[seq_position]]

            for match_position in range(starting_match, seq_length):
                match = seq[match_position]

                if match > current_sequence[-1]:
                    current_sequence.append(match)

            longest_sequences.append(current_sequence)


    return(max(longest_sequences, key=len))

def main():
    " Main function for nucleotide counting"

    # Generate file paths
    file_paths = generate_io_file_paths()

    # Load and format DNA string
    raw_data = load_file(file_paths["input"])
    raw_data = re.sub(r"\n", "|", raw_data).split("|")[:-1]
    seq = list(map(int, raw_data[1].split(" ")))
    seq_length = int(raw_data[0])

# Run main scrips
if __name__ == "__main__":
    main()
