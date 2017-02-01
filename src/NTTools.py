def get_aa():
    return set("ARTNDCQEGHILKMFPSTWYV")

def get_codons():
    nt = "ATCG"
    codons = []
    stop_codons = set(["TAG", "TAA", "TGA"])
    for i in nt:
        for j in nt:
            for k in nt:

                codon = ''.join([i, j, k])
                if codon in stop_codons:
                    continue
                codons.append(codon)
    return codons


def translate_aa_to_nt(aa):
    translation_dict = {"A": ["GCT", "GCC", "GCA", "GCG"],
                        "R": ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"],
                        "N": ["AAT", "AAC"],
                        "D": ["GAT", "GAC"],
                        "C": ["TGT", "TGC"],
                        "Q": ["CAA", "CAG"],
                        "E": ["GAA", "GAG"],
                        "G": ["GGT", "GGC", "GGA", "GGG"],
                        "H": ["CAT", "CAC"],
                        "I": ["ATT", "ATC", "ATA"],
                        "L": ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"],
                        "K": ["AAA", "AAG"],
                        "M": ["ATG"],
                        "F": ["TTT", "TTC"],
                        "P": ["CCT", "CCC", "CCA", "CCG"],
                        "S": ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
                        "T": ["ACT", "ACC", "ACA", "ACG"],
                        "W": ["TGG"],
                        "Y": ["TAT", "TAC"],
                        "V": ["GTT", "GTC", "GTA", "GTG"]}
    return translation_dict[aa]


def translate_nt_to_aa(nt):
    translation_dict = {"CTT": "L",
                        "ATG": "M",
                        "AAG": "K",
                        "AAA": "K",
                        "ATC": "I",
                        "AAC": "N",
                        "ATA": "I",
                        "AGG": "R",
                        "CCT": "P",
                        "ACT": "T",
                        "AGC": "S",
                        "ACA": "T",
                        "AGA": "R",
                        "CAT": "H",
                        "AAT": "N",
                        "ATT": "I",
                        "CTG": "L",
                        "CTA": "L",
                        "CTC": "L",
                        "CAC": "H",
                        "ACG": "T",
                        "CAA": "Q",
                        "AGT": "S",
                        "CAG": "Q",
                        "CCG": "P",
                        "CCC": "P",
                        "TAT": "Y",
                        "GGT": "G",
                        "TGT": "C",
                        "CGA": "R",
                        "CCA": "P",
                        "TCT": "S",
                        "GAT": "D",
                        "CGG": "R",
                        "TTT": "F",
                        "TGC": "C",
                        "GGG": "G",
                        "GGA": "G",
                        "TGG": "W",
                        "GGC": "G",
                        "TAC": "Y",
                        "GAG": "E",
                        "TCG": "S",
                        "TTA": "L",
                        "GAC": "D",
                        "TCC": "S",
                        "GAA": "E",
                        "TCA": "S",
                        "GCA": "A",
                        "GTA": "V",
                        "GCC": "A",
                        "GTC": "V",
                        "GCG": "A",
                        "GTG": "V",
                        "TTC": "F",
                        "GTT": "V",
                        "GCT": "A",
                        "ACC": "T",
                        "TTG": "L",
                        "CGT": "R",
                        "CGC": "R"}
    return translation_dict[nt]
