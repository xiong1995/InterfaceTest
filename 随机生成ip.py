import random

ip_list = []
while True:
    ip = ''
    for i in range(4):
        # 在范围1-255内随机生成一个正整数
        ran_ip = random.randint(1, 255)
        if i == 3:
            ip = ip + str(ran_ip)
        else:
            ip = ip + str(ran_ip) + '.'
    if ip not in ip_list:
        ip_list.append(ip)
    else:
        continue
    # 判断生成的ip数量是否大于需要的数量
    if len(ip_list) == 1000:
        break
with open('ip.txt', 'a+') as f:
    for i in ip_list:
        f.write(i + '\n')
