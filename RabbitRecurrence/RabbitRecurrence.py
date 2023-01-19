# 分析问题
# 当第1个月时，繁殖年龄兔子0对，新生兔子1对；（第1个if）
# 当第2个月时，繁殖年龄兔子1对，新生兔子0对；（第2个if）
# 当第3个月时，繁殖年龄兔子为上一个月新生兔子对数，新生兔子为上一个月繁殖年龄兔子数*3

import sys

# 函数输入月份和每对繁殖年龄兔子生育兔子数
def RabbitReccurence(a, b):
    if a == 1:
        return (0, 1)
    if a == 2:
        return (1, 0)
    elif a > 2:
        (c, d) = RabbitReccurence(a-1, b)
        return(c + d, c * int(sys.argv[2]))

# 前面导入sys模块后，使用sys.argv[num]调用参数，索引从1开始
x, y = RabbitReccurence(int(sys.argv[1]), int(sys.argv[2]))

print(x + y)

