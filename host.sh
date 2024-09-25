#!/bin/bash

# 定义文件名变量
LOG_FILE="/var/log/auth.log"
DENY_FILE="/etc/hosts.deny"
TEMP_FILE="/etc/hosts.deny.tmp"

# 处理a.deny文件，添加#号到包含"sshd"的行
sed '/sshd/ s/^/#/' "$DENY_FILE" > "$TEMP_FILE"

# 使用awk命令处理日志文件并将输出追加到临时文件中
awk '
    /sshd.*banner exchange/ {
        if (NR > 1 && last_ip != "") {
            print "sshd: 47.92.151.211, " last_ip ", " $ip_field
        }
        for (i=1; i<=NF; i++) {
            if ($i ~ /[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/) {
                ip_field = i
                last_ip = $i
            }
        }
    }
' "$LOG_FILE" >> "$TEMP_FILE"

# 将临时文件内容覆盖回a.deny文件
mv "$TEMP_FILE" "$DENY_FILE"
