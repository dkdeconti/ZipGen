#!/usr/bin/python

import NTTools
import sys


class Blosum():
    def __init__(self, filename):
        self.handle = open(filename, 'rU')


    def close(self):
        self.handle.close()


    def parse_header(self, col):
        value_indices = {}
        for i, v in enumerate(col):
            value_indices[i] = v
        return value_indices


    def to_dict(self):
        column_header = True
        scoring = {}
        if self.handle.closed:
            sys.stderr.write("File was closed\n")
            return None
        for line in self.handle:
            if line[0] == '#':
                continue # skip header
            arow = line.strip('\n').split()
            if column_header:
                col_header_indices = self.parse_header(arow)
                column_header = False
                continue
            k = arow[0]
            scoring[k] = {}
            for i, v in enumerate(arow[1:]):
                kv = col_header_indices[i]
                scoring[k][kv] = int(v)
        return scoring


def convert_aa_to_nt_scores(scores):
    aa = NTTools.get_aa()
    nt_scores = {}
    for i in aa:
        k = NTTools.translate_aa_to_nt(i)
        kv = {}
        for j in aa:
            v = NTTools.translate_aa_to_nt(j)
            kv.update(zip(v, [scores[i][j]]*len(v)))
        nt_scores.update(zip(k, [kv]*len(k)))
    return nt_scores
