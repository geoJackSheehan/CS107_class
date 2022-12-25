#!/usr/bin/env python3
# File       : P3.py
# Description: DNA complement (solution)
# Copyright 2022 Harvard University. All Rights Reserved.

def dna_complement(seq):
    """Compute the DNA complement.

    Parameters
    ----------
    seq : str
        Input DNA sequence.

    Returns
    -------
    res : str or None
        Result complement DNA string in upper case letters.  None for invalid
        input.
    """

    mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}
    res = ""
    for s in seq:
        comp = mapping.get(s.upper(), None)
        if comp is None:
            return None
        res += comp
    return res


if __name__ == "__main__":
    # Demo:
    in1 = "ATCGGAatT"
    print(f"For input {in1} the output is {dna_complement(in1)}")
    in2 = "ABc"
    print(f"For input {in2} the output is {dna_complement(in2)}")
