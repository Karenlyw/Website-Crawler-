# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:25:56 2018

@author: Administrator
"""
import pandas as pd
import matplotlib.pyplot as plt
try:
    pd.set_option('display.mpl_style','default')
    df=pd.read_csv('IELTS.csv',encoding='gbk',dtype='float')
    #打印从csv导出的dataframe(浮点型)   
    print(df)
    #分别统计各项得分的分布
    overall_counts=df[u'Overall'].value_counts()
    reading_counts=df[u'Reading'].value_counts()
    listening_counts=df[u'Listening'].value_counts()
    speaking_counts=df[u'Speaking'].value_counts()
    writing_counts=df[u'Writing'].value_counts()
    #将统计结果打印  
    print('Overall:\n',overall_counts)
    print('Reading:\n',reading_counts)
    print('Listening:\n',listening_counts)
    print('Speaking:\n',speaking_counts)
    print('Writing:\n',writing_counts)
    #绘制总分的分布直方图
    plt.bar(overall_counts.index,overall_counts.values,width=0.35,align='center',color='#EE6666')
    plt.title('IELTS Distribution(Overall)')
    plt.show()
    #绘制Reading与Listening的分布直方图（中国考生优势科目）
    fig1, ax1 = plt.subplots()
    width = 0.15
    opacity = 0.4
    rects1 = ax1.bar(reading_counts.index, reading_counts.values, width,alpha=opacity, color='b',label='Reading')
    rects2 = ax1.bar(listening_counts.index + width,listening_counts.values ,width,alpha=opacity, color='r',label='Listening')
    ax1.set_title('IELTS Distribution(Reading&Listening)')
    ax1.set_xticks(writing_counts.index )
    ax1.legend()
    fig1.tight_layout()
    plt.show()
    #绘制Speaking与Writing的分布直方图（中国考生劣势科目）
    fig2, ax2 = plt.subplots()
    width = 0.15
    opacity = 0.4
    rects1 = ax2.bar(speaking_counts.index, speaking_counts.values, width,alpha=opacity, color='b',label='Speaking')
    rects2 = ax2.bar(writing_counts.index + width,writing_counts.values ,width,alpha=opacity, color='r',label='Writing')
    ax2.set_title('IELTS Distribution(Speaking&Writing)')
    ax2.set_xticks(speaking_counts.index )
    ax2.legend()
    fig2.tight_layout()
    plt.show()     
except Exception as e: 
    print(e)