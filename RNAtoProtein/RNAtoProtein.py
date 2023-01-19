# 问题：将给定的RNA序列转换成蛋白序列
# （默认前三个字符为密码子区间不乱码，且最后三个字符为终止密码子）

import sys

CODON = sys.argv[1]
RNASEQ = sys.argv[2]

codon = {}
with open(CODON, "r") as cd:
    CodonAminoAcid = []
    for line in cd:
        CodonAminoAcid = line.strip().split('\t')
        codon[CodonAminoAcid[0]] = CodonAminoAcid[1]

# print(codon['UAA'])

Protein = []
with open(RNASEQ, "r") as rs:
    lines = rs.readline().strip()
    print(lines)
    RnaStringLen = len(lines)
    i = 0
    while i < RnaStringLen:
        if(codon[lines[i:(i+3)]] != 'Stop'):
            Protein.append(codon[lines[i:(i+3)]])
        else:
            break
        i += 3

print(''.join(Protein))

