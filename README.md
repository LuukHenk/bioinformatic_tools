# Bioinformatics in Rust

## Author:
- Luuk Perdaems

## Status
Version: 0.0.1 (Alpha)

## Installing:
Clone repository using git:
```
$ mkdir ~/bioinformatic-tools
$ git clone https://github.com/LuukHenk/bioinformatic_tools.git ~/bioinformatic-tools
```
Choose the tool you want to use. e.g. the DNA counter:
```
$ cd bioinformatic-tools
$ ./dna_nucleotide_counter/target/release/dna
```
Give a file path which contains DNA nucleotides, and DNA nucleotides only. e.g. `./dna_nucleotide_counter/sample_dataset.txt`.

## The setup:
### DNA counter
The counter will output the amount of nucleotides counted (A, C, G, and T) in a specific file.

## Changelog:
### Version 0.0.1 (4 March 2020)
- Added DNA counter tool (unstable)

## To do:
### General
- Simplification of the tool loading

### DNA counter tool
- Add more ways to find the end of the file (currently only detected by an enter)
- Add a way to handle unknown characters
- Add RNA counter
- Add user input for the maximum bytes used
- Add multithreading

## References
- Got help from [Sidney Liebrand](https://github.com/SidOfc) about how to use rust
- Used [Rosalind.info](http://rosalind.info/) for obtaining the ideas
