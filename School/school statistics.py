# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:17:32 2018

@author: Administrator
"""
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

try:
    pd.set_option('display.mpl_style','default')
    df=pd.read_csv('cs application.csv',encoding='gbk')
#打印从csv导出的dataframe   
    print(df)
#统计各校申请人数
    school_counts=df[u'申请学校'].value_counts()
#将统计排序结果写入csv 并打印  
    school_counts.to_csv('cs application count .csv', sep=',', header=True, index=True)
    print(school_counts)
except Exception as e: 
    print(e)
sizes=[]
explode=[]
labels=[]
i=0
#设置字体
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']
#取申请人数前十名的学校绘制饼状图
for index in school_counts.index[0:10] :
    labels.append(index)
for data in school_counts.data[0:10]:
    sizes.append(data)
    explode.append(0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90) #startangle表示饼图的起始角
plt.axis('equal') 
plt.show()