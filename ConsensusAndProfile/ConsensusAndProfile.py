# -*- coding: utf-8 -*-
import sys
import pandas as pd

def Deal(file):
    seqDict = {}
    collen = ''
    rowlen = ''
    # 读取文件，将fasta序列写入字典
    with open(file) as fa:
        key = ''
        for line in fa:
            line.strip()
            if line.startswith(">"):
                key = line.replace(">", "")
                seqDict[key] = ''
            else:
                seqDict[key] += line.strip()
        collen = len(seqDict[key])
        rowlen = len(seqDict)
    # 遍历字典，将所有碱基分割开，写入dataframe
    # # 初始化一个dataframe，值为NaN
    seqDf = pd.DataFrame(index=range(rowlen), columns=range(collen))
    count = pd.DataFrame(index=['A', 'C', 'G', 'T'], columns=range(collen))
    i = 0
    for key1 in seqDict:
        seqSplit = list(seqDict[key1].strip())
        # print(seqSplit)
        # 将list按行写入dataframe
        seqDf.loc[i] = seqSplit
        i += 1
    for i in range(collen):
        if seqDf[i].str.contains('A').any():
            countA = seqDf[i].value_counts()['A']
        else:
            countA = 0
        if seqDf[i].str.contains('C').any():
            countC = seqDf[i].value_counts()['C']
        else:
            countC = 0
        if seqDf[i].str.contains('G').any():
            countG = seqDf[i].value_counts()['G']
        else:
            countG = 0
        if seqDf[i].str.contains('T').any():
            countT = seqDf[i].value_counts()['T']
        else:
            countT = 0
        count.loc['A', i] = countA
        count.loc['C', i] = countC
        count.loc['G', i] = countG
        count.loc['T', i] = countT

    seqfinal = ''
    for i in range(collen):
        # 修改object类型为int类型，使用idxmax()方法调用每一列最大值的行索引
        seqfinal = seqfinal + count[i].astype('int').idxmax()
    print(seqfinal)
    count = count.T
    for i in ['A', 'C', 'G', 'T']:
        trans = count[i].values.tolist()
        print(str(i) + ": " + " ".join(str(x) for x in trans))


if __name__ == '__main__':
    Fasta = sys.argv[1]
    Deal(Fasta)


# 运行命令
# python ConsensusAndProfile.py rosalind_cons.txt



