import re

# 正则表达式，用于匹配包含"banner exchange"的行并提取IP地址
banner_exchange_pattern = re.compile(r'.*banner exchange: Connection from (\d+\.\d+\.\d+\.\d+).*')

# 读取auth.log文件并筛选出IP地址
banner_exchange_ips = set()
with open('/var/log/auth.log', 'r') as file:
    for line in file:
        match = banner_exchange_pattern.match(line)
        if match:
            banner_exchange_ips.add(match.group(1))

# 将IP地址分组，每组5个
banner_exchange_ips_list = list(banner_exchange_ips)
ip_groups = [banner_exchange_ips_list[i:i + 5] for i in range(0, len(banner_exchange_ips_list), 5)]

# 准备写入hosts.deny的内容
hosts_deny_content = []
for ip_group in ip_groups:
    line = "sshd: " + ", ".join(ip_group) + "\n"
    hosts_deny_content.append(line)

# 读取现有的hosts.deny文件内容
try:
    with open('/etc/hosts.deny', 'r') as file:
        existing_content = file.readlines()
except FileNotFoundError:
    existing_content = []

# 在包含"sshd"的行前添加注释符号'#'
new_existing_content = []
for line in existing_content:
    if "sshd" in line:
        new_existing_content.append("#" + line)
    else:
        new_existing_content.append(line)

# 写回hosts.deny文件，先写入原来的内容，再追加新的IP地址
with open('/etc/hosts.deny', 'w') as file:
    file.writelines(new_existing_content)
    file.writelines(hosts_deny_content)

# 打印禁止的ip
#print("Updated hosts.deny with the following IP groups:")
#for line in hosts_deny_content:
#    print(line.strip())

