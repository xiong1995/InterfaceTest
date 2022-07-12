import requests

url = 'http://www.lemonban.com/'
response = requests.get(url=url)

# 获取返回响应的状态码
status_code = response.status_code
# 获取响应头
headers = response.headers
# 获取cookies
cookies = response.cookies
# 获取响应体
# 方法一：自动识别返回内容的编码，进行解码（有可能会出现错误或乱码）
response_text = response.text
# 方法二：指定编码对返回内容进行解码
response_content = response.content.decode('utf-8')

print(status_code, cookies, headers, response_text, response_content)
