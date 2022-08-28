"""
1、加密是日常生活中经常用到的保护信息内容的方法，
比如非常简单的凯撒密码，利用字母移位来加密字母，
比如让字母移动1位，比如a变成b，b变成c，最后z变成a，
将内容整体移动一位来加密内容，现在要求实现这样的一个加密类，
有一个加密的方法，也有一个解密到的方法，请实现这样的一个类。ord() chr()

加密：
    1.创建变量保存加密后的数据
    2.遍历字符串，取出每个字符串
    3.判断每个字符是否为字母
        是：通过ord()转换为十进制数字并且加1，将加1的十进制数字通过chr()方法转换为字母再拼接到新的字符串
            如果字母是Z或者z，需要做特殊处理，直接改为A或者a
        否：不做改变，直接拼接到新字符串

解密：
    1.创建变量保存解密后的数据
    2.遍历字符串，取出每个字符串
    3.判断每个字符是否为字母
        是：通过ord()转换为十进制数字并且减1，将减1的十进制数字通过chr()方法转换为字母再拼接到新的字符串
            如果字母是A或者a，需要做特殊处理，直接改为Z或者z
        否：不做改变，直接拼接到新字符串
"""


class Des:
    def encryption(self, str1):
        """
        加密
        :param str1: 加密前的字符串
        :return: str
        """
        str2 = ''
        # 遍历字符串
        for i in str1:
            # 判断是否为字母
            if i.isalpha():
                # 判断是否为z,是则直接转换为a
                if i == 'z':
                    str2 += 'a'
                # 判断是否为Z,是则直接转换为A
                elif i == 'Z':
                    str2 += 'A'
                # 其他字母需转换为十进制数字且加1，再转换为字母
                else:
                    str2 += chr(ord(i) + 1)
            else:
                # 非字母直接拼接到新字符串
                str2 += i
        return str2

    def decrypt(self, str1):
        """
        解密
        :param str1: 解密前的字符串
        :return: str
        """
        str2 = ''
        # 遍历字符串
        for i in str1:
            # 判断是否为字母
            if i.isalpha():
                # 判断是否为a,是则直接转换为z
                if i == 'a':
                    str2 += 'z'
                # 判断是否为A,是则直接转换为Z
                elif i == 'A':
                    str2 += 'Z'
                # 其他字母需转换为十进制数字且加1，再转换为字母
                else:
                    str2 += chr(ord(i) - 1)
            else:
                # 非字母直接拼接到新字符串
                str2 += i
        return str2


if __name__ == '__main__':
    des = Des()
    str1 = '12ggersg&(^%$&^868GKGUGFAZza'
    enc = des.encryption(str1)
    dec = des.decrypt(enc)
    print(str1 == dec)
