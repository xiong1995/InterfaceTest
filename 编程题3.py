"""
写一个函数实现将包含100个元素的列表随机分成12分，每份至少有2个元素

1. 创建一个列表list2，保存随机分成的12份列表
2. 随机获取列表中的两个元素，循环获取12次
3. 将每次获取的两个元素添加到一个新的列表中并将新的列表添加到list2中(使用random.sample来获取两个元素)
4. 删除每次获取的两个元素
5. 将剩下的元素随机加入到list2中的每个列表中
"""

import random


def adivide(list1):
    # 创建一个新列表保存新生成的所有列表
    list2 = []
    for i in range(12):
        # 从100个元素中随机获取两个元素并以列表的形式添加到list2中
        # random.choices获取会有重复值，如果列表中的所有元素都不相等会报错
        # 所以使用random.sample来获取两个元素并返回列表添加到list2中
        list2.append(random.sample(list1, k=2))
        # 在list1中删除随机获取的两个元素
        list1.remove(list2[i][0])
        list1.remove(list2[i][1])
    # 将剩下的所有元素逐个随机添加到12个列表中
    for j in list1:
        list2[random.randint(0, 11)].append(j)
    return list2


if __name__ == '__main__':
    li = [i for i in range(100)]
    print(adivide(li))
