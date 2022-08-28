"""
4、有两个长度一样列表a和b，它们里面的元素都是整形的数值，要求：通过交换两个列表的元素，使得sum(a) 和 sum(b)的差值最小
提示如下：
    1.将两序列合并为一个序列，并排序，为列表Source
    2.拿出最大元素Big，次大的元素Small
    3.在列表Source中找出最大值和最小值，将最大值和Small放在一起组成列表 c，将最小值和Big放在一起组成列表 d
    4.再在列表Source中找出最大值和最小值，重新计算sum(c)和sum(d)，将最大值放在重新计算后和最小的列表里面,最小值放在另一个列表里面
    5.重复第4步，直到分完
"""


def minimum(list1, list2):
    # 将两序列合并为一个序列,为列表source
    source = list1 + list2
    # 将source列表升序排序
    source.sort()
    # 将最大值和次大值分别存入列表c和d并在source中删除
    c = [source.pop()]
    d = [source.pop()]
    for i in range(len(list1) - 1):
        # 判断c和d列表内的所有元素的和
        # 和大的存最小值，和小的存最大值并将存入的元素删除
        if sum(c) > sum(d) or sum(c) == sum(d):
            c.append(source.pop(0))
            d.append(source.pop())
        else:
            c.append(source.pop())
            d.append(source.pop(0))
    return c, d, sum(c) - sum(d)


if __name__ == '__main__':
    a = [1]
    b = [5]
    a, b, c = minimum(a, b)
    print(a, b, c)
