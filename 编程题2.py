"""
2、给定一个列表和一个值，列表中数字两两相加如果
有等于这个值的，就返回这两个值的索引，否则返回[-1, -1],比如：
(1). 给定列表[1, 5, 7, 20], 给定值12，返回[1,2]
(2). 给定列表[1, 2, 6, 8 ], 给定值2，返回[-1, -1]

1. 第一次遍历所有数字
2. 第二次遍历第一次遍历后的数字且与第一次遍历的数字相加
3. 判断两次相加的结果是否等于给定值,有则返回下标
4. 遍历完仍没有等于给定值的和返回[-1, -1]
"""


# 只返回一个和为给定值的下标
def sum1(list1, num1):
    # 取出除最后一个的所有数字
    for i in range(len(list1) - 1):
        # 取出上一个循环取出的数字之后的所有数字并单独与之相加
        for j in range(i + 1, len(list1)):
            # 判断和是否为给定的值，是则返回下标
            if num1 == list1[i] + list1[j]:
                return [i, j]
    return [-1, -1]


# 返回全部和为给定值的下标
def sum2(list1, num1):
    list2 = []
    for i in range(len(list1) - 1):
        for j in range(i + 1, len(list1)):
            if num1 == list1[i] + list1[j]:
                list2.append([i, j])
    if list2:
        return list2
    else:
        return [-1, -1]


if __name__ == '__main__':
    list1 = [5, 20, 5, 7]
    num1 = 12
    print(sum1(list1, num1))
    print(sum2(list1, num1))
