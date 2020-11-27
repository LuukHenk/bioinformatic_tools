# Rosalind bioinformatics in Python3 (and in Rust)

## Installing:
Clone repository using git:

```
$ mkdir ~/bioinformatic-tools
$ git clone https://github.com/LuukHenk/bioinformatic_tools.git ~/bioinformatic-tools
```

Each tool standard uses the `os`, `re` and `sys` libraries. The tools section below shows if tools need additional libraries installed.

## Tools:
All the tools can be found in the `./scripts/` folder and can be runned using python3. e.g.
```
$ python3 scripts/dna.py
```

The input file used by the tool can be found in the `./input/` folder. e.g. the file
`./scripts/dna.py` will use the `./input/rosalind_dna.txt`

The output files can be found in the `./output/` folder. e.g. the file `./scripts/dna.py` will
generate `./output/rosalind_dna.txt`

All current tools and their requirements are shown below:

### Nucleotide counter
Counts the nucleotides of dna strand <br />
Filename: `./script/dna.py` <br />
Additional libraries used: none

## References
- Used [Rosalind.info](http://rosalind.info/) for obtaining the ideas for the tools
- Got help from [Sidney Liebrand](https://github.com/SidOfc) about how to use rust
