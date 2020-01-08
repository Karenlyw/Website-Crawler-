# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:11:18 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:13:09 2018

@author: Administrator
"""
from bs4 import BeautifulSoup 
from urllib.request import urlopen
import csv
import re
overall=[]
reading=[]
listening=[]
speaking=[]
writing=[]
#基本url
base="http://bbs.gter.net/forum.php?mod=forumdisplay&fid=486&typeid=992&filter=typeid&typeid=992&page="
#遍历英国申请offer榜模块的65页
for i in range(1,66):
    url=base+str(i)
    html=urlopen(url).read()
    soup = BeautifulSoup(html, features='lxml')
    #找到所有有效帖子
    choice=soup.find_all("a",{"class":'xst'}) 
    #遍历每一个帖子
    for url in choice:
        url=url['href']
        html=urlopen(url).read()
        soup = BeautifulSoup(html, features='lxml')
        #找到所有个人情况表格        
        ptables=soup.find_all("table",{"summary":'个人情况',"class":"cgtl mbm"})
        #遍历所有个人情况表格
        for table in ptables:
            #找到所有表头单元格
            th_list=table.find_all('th')
            #找到所有内容单元格
            td_list=table.find_all('td')
            n=0
            #遍历所有表格内容找到雅思成绩信息
            for item in th_list:
                if item.get_text()=="IELTS:":
                    #如果当前表头为“IELTS：”，则将其对应的内容单元格的内容提取出来并去除首位空格
                    ielts=td_list[n].get_text().strip()
                    #将总分以及各项小分切割开
                    ielts=ielts.split('\r\n')
                    #对各项得分进行规范化
                    for m in range(0,len(ielts)):
                       ielts[m]=("".join(re.findall(r'[0-9].?[0-9]?',ielts[m]))).strip(',')
                    #更新各项得分列表
                    try:
                        overall.append(ielts[0])
                        reading.append(ielts[1])
                        listening.append(ielts[2])
                        speaking.append(ielts[3])
                        writing.append(ielts[4])
                    except :
                        pass                        
                n=n+1
#将学校信息写入csv
with open('IELTS.csv',"w",newline='') as f:
    writer=csv.writer(f)  
    writer.writerow(['Overall','Reading','Listening','Speaking','Writing'])  
    try:
        for j in range(0,len(overall)):  
            writer.writerow([overall[j],reading[j],listening[j],speaking[j],writing[j]])  
    except:
        pass
  