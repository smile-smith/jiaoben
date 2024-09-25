#!/bin/bash

# 指定文件名和要删除的模式
filename="/var/log/auth.log"
#filename="/var/log/syslog"
pattern="pam_unix(cron:session)"
#pattern="cron"

# 使用sed命令删除包含特定模式的行
sed -i "/$pattern/d" "$filename"

