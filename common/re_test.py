import re

# 单个字符匹配

# s1 = '123242   14dfsfsdf$%#@&*^*'
# # \d:表示匹配一个数字，
# res = re.findall(r'\d', s1)
# print(res)
#
# # \D:表示匹配一个非数字
# res1 = re.findall(r'\D', s1)
# print(res1)
#
# # \s:表示匹配一个空白字符
# res2 = re.findall(r'\s', s1)
# print(res2)
#
# # \S:表示匹配一个非空白字符
# res3 = re.findall(r'\S', s1)
# print(res3)
#
# # \w:表示一个单词字符（数字，字母，下划线）
# res4 = re.findall(r'\w', s1)
# print(res4)
#
# # \W:表示一个非单词字符（除数字，字符，下划线之外的所有字符）
# res5 = re.findall(r'\W', s1)
# print(res5)
#
# # .:表示任意一个字符（通配符）
# res6 = re.findall(r'.', s1)
# print(res6)
#
# # []:列举匹配的单字符
# res7 = re.findall(r'[234a]', s1)
# print(res7)
# res8 = re.findall(r'[0-9a-zA-Z]', s1) # 匹配0到9，a到z，A到Z

# 多个字符匹配
# s2 = '12342#32131231#2dfSasfd#gdfgdf#gdgfd123123dAfgd#fgfdgdffs#df'
#
# # {n}：表示前一个字符出现n次
# res = re.findall(r'\d{4}', s2)
# res1 = re.findall(r'[a-zA-Z]{4}', s2)
# print(res, res1)
#
# # {n,}:表示前一个字符出现n次以上
# res2 = re.findall(r'[a-zA-Z]{5,}', s2)
# print(res2)
#
# # {n,m}:表示前一个字符出现n到m次
# res3 = re.findall(r'[a-zA-Z]{4,6}', s2)     # 贪婪模式，按最高次数匹配
# res4 = re.findall(r'[a-zA-Z]{4,6}?', s2)    # 非贪婪模式，按最低次数匹配
# print(res3, res4)
#
# # +：表示一次以上 *: 表示0次以上 ?: 表示关闭贪婪模式或者表示0次或1次
# res5 = re.findall(r'#.+?#', s2)
# print(res5)

# 表示边界
# s = "123456789abcdefghijklmnopqrst123uvwxy123"
#
# # 字符串边界 ^：表示字符串的开头(从起始位置开始匹配)， $:表示字符串的结尾（末尾开始匹配）
# # 单子边界 \b: 表示单词边界 \B:表示非单词边界
# res = re.findall(r'^123', s)
# res1 = re.findall(r'123$', s)
# print(res, res1)
#
# s1 = 'python python2 java c++'
# res2 = re.findall(r'\bpython', s1)
# print(res2)

# ():表示分组
# s = '{"id": "#id#"}'
# res = re.findall('#.*?#', s)
# res1 = re.findall('#(.*?)#', s)
# print(res, res1)

# |: 匹配左边或者右边的内容,表示多个匹配规则，满足一个就可以
# s = 'python java c'
# res = re.findall('python|java|c', s)
# print(res)

# findall：匹配字符串中所有符合规则的数据，并以列表的形式返回
# search: 匹配并返回第一个符合规则的匹配对象,group获取匹配的内容
# 正则替换
s = '{"id": "#id#"}'
res = re.findall('#(.*?)#', s)
print(res)

res1 = re.search('#(.*?)#', s)
print(res1.group(), res1.group(1))

