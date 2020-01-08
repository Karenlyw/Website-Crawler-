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
base="http://bbs.gter.net/forum.php?mod=forumdisplay&fid=957&typeid=1006&typeid=1006&filter=typeid&page="
applied_school=[]
#遍历offer榜模块的25页
for i in range(1,26):
    url=base+str(i)
    html=urlopen(url).read()
    soup = BeautifulSoup(html, features='lxml')
    #找到所有有效帖子
    choice=soup.find_all("a",{"class":'xst'})
    applied_school=[]
    #遍历每一个帖子
    for url in choice:
        url=url['href']
        html=urlopen(url).read()
        soup = BeautifulSoup(html, features='lxml')
        #找到所有offer表格        
        otables=soup.find_all("table",{"summary":re.compile("offer [0-9]+"),"class":"cgtl mbm"}) #找到所有offer信息表格
        #遍历所有offer表格
        for table in otables:
            td_list=table.find_all('td')
            oitems=table.find_all('th')
            i=0
            #遍历所有表格内容找到学校信息
            for item in oitems:
                if item.get_text()=="申请学校:":
                    school=td_list[i].get_text().strip()
                    school=re.sub('[\u4e00-\u9fa5]','',school)
                    applied_school.append(school)
                i=i+1
#将学校信息写入csv
with open('CS application.csv',"w",newline='') as f:
     try:  
         writer=csv.writer(f)  
         writer.writerow(['申请学校'])  
         for school in applied_school:  
             writer.writerow([school])  
     finally:  
         f.close() 