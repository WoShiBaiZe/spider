#！/usr/bin/env python
# -*- coding: utf-8 -*-
# 命令行 cmd 
# pip install requests
import requests
import re
headers ={
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
# 下载一个网页
url = 'https://www.jingcaiyuedu.com/book/15401.html'
# 模拟浏览器发送http请求
response = requests.get(url,headers=headers)
print(response.request.headers)
#编码方式
response.encoding = 'utf-8'
# 目标小说主页的网页源码
html = response.text
# 小说的名字
title = re.findall(r'<meta prperty="og:title" content="(.*?)"/>', html)[0]
# 新建一个文件，保存小说内容
fb = open('%s.txt' % title, 'w', encoding='utf-8')
# 获取每一章的信息(章节，url)
dl = re.findall(r'<dl id="list">.*?</dl>',html,re.s)
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)
# 循环每一个章节，分别下载
for chapter_info in chapter_info_list:
	# chapter_title = chapter_info[1]
	# chapter_url = chapter_info[0]
	chapter_url,chapter_title = chapter_info
	chapter_url = "http://www.jingcaiyuedu.com%s" % chapter_url
	# 下载章节内容
	chapter_repsonse = requests.get(chapter_url)
	chapter_repsonse.encoding = 'utf-8'
	chapter_html = chapter_repsonse.text
	# 提取章节内容
	chapter_content = re.findall(r'<script>a1\(\);</script>(.*?)<script>a2\(\);</script>',chapter_html)
	# 清洗数据
	chapter_content = chapter_content.replace(' ','')
	chapter_content = chapter_content.replace('&nbsp;','')
	chapter_content = chapter_content.replace('<br/>','')

	# 持久化
	fb.write(chapter_title)
	fb.write(chapter_content)
	fb.write('\n')
	print(chapter_url)