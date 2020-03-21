#！/usr/bin/env python
# -*- coding: utf-8 -*-
# 命令行 cmd 
# pip install requests
import requests
import re
# 下载一个网页
url = 'http://www.12365auto.com/'
# 模拟浏览器发送http请求
response = requests.get(url)
#编码方式
response.encoding = 'utf-8'
html = response.text
fb = open('1.txt','w', encoding='utf-8')
fb.write(html)
