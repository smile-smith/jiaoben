import requests

# URL是表单提交的目标地址
url = 'https://www.serv00.com/ip_unban/'

# 表单数据，根据你的HTML，我们假设需要提交server字段
data = {
    'server': '7'  # 选择一个服务器，例如's9.serv00.com'
}

# 请求头，可能需要包含CSRF令牌
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36 Edg/129.0.0.0',
    'csrftoken': 'O9ye1Ow6nBPUeWUtPXxidSyLOKeDpkPI',  # 从HTML中提取的CSRF令牌
    'Referer': 'https://www.serv00.com/contact/'  # 参考链接，有时服务器会检查
}

# 发送POST请求
response = requests.post(url, data=data, headers=headers)

# 打印响应内容
print(response.text)

