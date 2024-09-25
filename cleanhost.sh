#!/bin/bash

# 定义hosts.deny文件路径
HOSTS_DENY="/etc/hosts.deny"
# 定义输出文件路径
OUTPUT_FILE="/etc/hosts.deny"

# 检查hosts.deny文件是否存在
if [ ! -f "$HOSTS_DENY" ]; then
  echo "Error: '$HOSTS_DENY' file does not exist."
  exit 1
fi

# 创建一个临时文件来存储不带#号的行
TEMP_FILE=$(mktemp)

# 读取hosts.deny文件，删除带有#号的行，并将结果保存到临时文件
grep -v '^#' "$HOSTS_DENY" > "$TEMP_FILE"

# 读取hosts.deny文件，获取带有#号的行，并将结果追加到临时文件
#grep '^#' "$HOSTS_DENY" >> "$TEMP_FILE"

# 将临时文件的内容移动到输出文件
mv "$TEMP_FILE" "$OUTPUT_FILE"

# 输出结果
#echo "Cleaned 'hosts.deny' file saved as '$OUTPUT_FILE'"

