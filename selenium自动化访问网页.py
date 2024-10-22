import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# 自定义User-Agent
custom_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# 创建Firefox选项
options = Options()
options.add_argument('--headless')  # 无头模式，不会打开浏览器界面
options.set_preference("general.useragent.override", custom_user_agent)

# 关闭geckodriver日志
os.environ['MOZ_LOG'] = '-timestamp -emoji -rcc'
os.environ['MOZ_LOG_FILE'] = '/dev/null'

# 创建一个新的Firefox浏览器实例
browser = webdriver.Firefox(options=options)

# 要访问的网页
url = 'http://example.com/'

try:
    # 访问网页
    browser.get(url)
    
    # 等待10秒
    time.sleep(10)
    
    # 获取网页源代码
    source_code = browser.page_source
    
    # 打印源代码（为了简洁，这里只显示前500个字符）
#    print(source_code[:500])
    
    # 获取并打印cookie
#    cookies = browser.get_cookies()
#    print("Cookies:")
#    for cookie in cookies:
#        print(cookie)
    
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # 关闭浏览器
    browser.quit()

# 杀掉所有Firefox进程（Windows系统）
if os.name == 'nt':
    os.system("taskkill /F /IM firefox.exe")
elif os.name == 'posix':
    # 杀掉所有Firefox进程（Linux系统）
    subprocess.run(["pkill", "-f", "firefox"])