# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

# 读取fasta文件，并将序列放在字典中并返回
def Initfasta(file):
    seqDict = {}
    # 读取文件，将fasta序列写入字典
    with open(file) as fa:
        key = ''
        for line in fa:
            line = line.strip()
            if line.startswith(">"):
                key = line.replace(">", "")
                seqDict[key] = ''
            else:
                seqDict[key] += line.strip()
    return seqDict

# 根据序列的字典，循环处理，获得符合条件的id组合
def Deal(dictIn):
    combination = defaultdict(list)
    judged = []
    for item1 in dictIn:
        for item2 in dictIn:
            if item1 == item2:
                pass
            else:
                item1suffix = dictIn[item1][-3:]
                item2prefix = dictIn[item2][:3]
                if item1suffix == item2prefix:
                    combination[item1].append(item2)
    return combination

def Print(combt):
    for item in combt:
        if len(combt[item]) > 1:
            i = 0
            for id in combt[item]:
                #if(i<2):
                print(item + " " + id)
                i += 1
        else:
            print(item + " " + str(combt[item][0]).strip())

if __name__ == '__main__':
    Fasta = sys.argv[1]
    FastaDict = Initfasta(Fasta)
    Combination = Deal(FastaDict)
    Print(Combination)


# python OverlapGraphs.py test.fa
