#! /usr/bin/python

import MutAlign
import Scoring
import sys

def main(sa):
    a = "ATGCGAATGCGA"
    b =   "TGCGAATGCGAT"
    a = [a[i:i+3] for i in range(len(a))]
    b = [b[i:i+3] for i in range(len(b))]
    filename = sa[0]
    blosum = Scoring.Blosum(filename)
    blosum_scores = blosum.to_dict()
    blosum.close()
    print(a, b)
    scores = Scoring.convert_aa_to_nt_scores(blosum_scores)
    #a_build, b_build = MutAlign.MutAlignDFS.align(a, b, scores, False)
    a_build, b_build = MutAlign.MutAlignGreedy().greedy_mut(a, b, False)
    print(a_build, b_build)


if __name__ == "__main__":
    main(sys.argv[1:])
