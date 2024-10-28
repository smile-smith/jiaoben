#!/bin/bash

# 检查是否传递了参数
if [ -z "$1" ]; then
  echo "Usage: $0 <IP-ADDRESS>"
  exit 1
fi

# 使用curl获取IP信息
curl "https://ipinfo.io/widget/demo/$1"

