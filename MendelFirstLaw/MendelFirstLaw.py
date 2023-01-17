# 分析问题
# 要得到显性后代的可能性，那么相当于1-隐形后代的可能
# 所有个体中任意选2个，那么就是组合数N取2：N*(N-1)*0.5
# 依次计算杂合*杂合、杂合*隐形纯合中出现纯合的可能性”数量“
# 使用总数减去上述可能性”数量“再除以总数得到线性性状可能性

import sys

# 传入三种基因型数量
DominantHomoNum = int(sys.argv[1])
HeterozygoteNum = int(sys.argv[2])
RecessiveHomoNum = int(sys.argv[3])

SumNum = DominantHomoNum + RecessiveHomoNum + HeterozygoteNum

# 组合数，所有可能的交配情况
AllPos = SumNum * (SumNum - 1) * 0.5

# 显性性状的可能为：1-P（隐形性状）

# 隐性性状可能产生的组合：杂合*杂合、杂合*隐形纯和、隐形纯和*隐形纯和

# 杂合*杂合产生隐形性状可能性为0.25
Rece1 = HeterozygoteNum * (HeterozygoteNum - 1) * 0.5 * 0.25

# 杂合*隐形纯和产生隐形性状可能性为0.5
Rece2 = HeterozygoteNum * RecessiveHomoNum * 0.5

# 隐形纯和*隐形纯和产生隐形性状可能性为1
Rece3 = RecessiveHomoNum * (RecessiveHomoNum - 1) * 0.5 * 1

Possible = (AllPos - (Rece1 + Rece2 + Rece3)) / AllPos

print(AllPos)
print((Rece1 + Rece2 + Rece3))

print('%.5f' % Possible)

