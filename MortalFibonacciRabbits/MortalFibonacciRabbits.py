# 问题分析：兔子有寿命，新生兔子1个月成熟，第三个月生下一对兔子
# 首先初始化一个列表list，用于存储每个月的兔子数，值的依次顺序为生存N个月的兔子数
# 可以发现，第1个月时，首月1对兔子，后面全是0，因此
# 第1个月为：[1,0,0,0,0,0,...]
# 第2个月为：[0,1,0,0,0,0,...]
# 第3个月为：[1,0,1,0,0,0,...]
# 第4个月为：[1,1,0,1,0,0,...]
# 第5个月为：[2,1,1,0,1,0,...]
# 总结规律：新生兔子（即list[0]）数量为后面所有值的和，更新月份时，列表数字“往右移一格”

import sys

MonthN, SurvivalM = int(sys.argv[1]), int(sys.argv[2])

if SurvivalM == 1:
    print("The survival time is 1 month, the rabbit has not reproduced and is extinct!")
    exit()

# 初始化数组
l = []
for i in range(0, SurvivalM):
    l.append(0)

def MortalFibRabbits(li, n):
    if n == 1:
        li[0] = 1
        return(li, 1)
    else:
        tmp = MortalFibRabbits(li, n-1)
        li = tmp[0]
        li[-1] = sum(li[1:])
        li = li[-1:] + li[:-1]
        # print(li)
        return(li, tmp[1])

x = MortalFibRabbits(l, MonthN)

print(sum(x[0]))
