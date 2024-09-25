# 示例 Python 脚本

# 打开文件并读取所有行
with open('/etc/hosts.deny', 'r') as file:
    lines = file.readlines()

# 创建一个新的行列表，排除带有#号的行
filtered_lines = [line for line in lines if '#' not in line]

# 将修改后的内容写回文件
with open('/etc/hosts.deny', 'w') as file:
    file.writelines(filtered_lines)

