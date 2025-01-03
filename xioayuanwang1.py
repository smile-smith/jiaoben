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
  'password' : '72483ea510176f135a8c68d64be0f7ce245ed04bd36b412bebaf8422cf68f983af4b453348c69f73c09768b94d100be6a5d607fc85c649506095949314c31de40353672dd2902d33608b6015ffdf2c1415ad116dad231c8aba1128584b6d57679ea41e3d7bc299f980241080b22b432ea7612b94d987ac60ad737cc3cfb41e08',
  'passwordEncrypt' : 'true',
  'vaildcode' : '',
  'service' : '',
  'queryString' : '',
  'operatorPwd' : '',
  'operatorUserId' : '',
  'callback' : ''
}

params1 = {
  'wlanuserip' : '873ce49576559538d7e5051b66152210',
  'wlanacname' : 'fd38d7521de3b050841711ac27012e2e',
  'ssid' : '',
  'nasip' : 'c6aba79ca43fd623277acd514d2d1726',
  'snmpagentip' : '',
  'mac' : '717742c64d10fd03be9d0823cc6f4da1',
  't' : '',
  'url' : '795c649bdeb10f4d4d6c1ee3155a5a2a35a0a569f8ecf3bb',
  'apmac' : '',
  'nasid' : 'fd38d7521de3b050841711ac27012e2e',
  'vid' : '1fc7ea4712f9d8b1',
  'port' : '3495334aedfa5fea',
  'nasportid' : '040f54214d5f54d2f8bb6249163eb184090e32c0ddee0d3569a06211ac6e40ed5f1e3370e974446f8a655b70dca55deb'
}

params2 = {
  'userIndex' : '',
  'callback' : ''
}

# 定义变量
a = requests.post(url2,data=data1)
a.encoding = 'UTF-8'

# 定义存储用户ID的文件
counter_file = 'user_id_counter.txt'

# 定义用户ID的开始和结束值
start_user_id = '02000'
end_user_id = '03999'

# 读取当前用户ID，如果文件不存在则设置为开始ID
if os.path.exists(counter_file):
    with open(counter_file, 'r', encoding='utf-8') as file:
        current_user_id = file.read().strip()
else:
    current_user_id = start_user_id
    with open(counter_file, 'w', encoding='utf-8') as file:
        file.write(current_user_id)

# 自增当前用户ID
current_user_id = int(current_user_id)
current_user_id += 1

# 检查用户ID是否超过结束值
if current_user_id > int(end_user_id):
    print("用户ID已达到最大值。")
    exit()

# 将新的用户ID格式化为5位字符串
new_user_id = f'{current_user_id:05d}'

# 更新存储的用户ID
with open(counter_file, 'w', encoding='utf-8') as file:
    file.write(new_user_id)

# 使用新的用户ID更新data1字典
data1['userId'] = new_user_id

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

# 获取userIndex
a = requests.post(url4,params=params2)
a.encoding = 'GDK'
print(a.text)
print(a)
print(a.content)

#保持连接
random_seconds = random.randint(7, 30)
time.sleep(random_seconds)
print(f"已经等待了 {random_seconds} 秒。继续执行下一步...")
#退出登录
a = requests.post(url6,params=params2)
a.encoding = 'UTF-8'
print(a.text)
