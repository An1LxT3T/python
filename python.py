# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:18:24 2021

@author: Administrator
"""
#方法的使用在最下方的if __name__ == '__main__'语句中
import requests
from lxml import etree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def 获取网址代码():
    url="https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=1"
    content=requests.get(url)
    return content.text
def 内部网址获取():
    url=[0]*5
    for i in range(5):
        url[i]='https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={0}'.format(i)
    return url
    
def 页面分析():
    b=0
    list=[[0]*4]*100
    for i in range(5):
        url="https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={0}".format(i+1)
        content=requests.get(url)
        html =etree.HTML(content.text)
        datas_title= html.xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/ul/li')
        for data in datas_title:
            data_title=data.xpath('div[2]/h4/a/text()')
            data_name=data.xpath('div[2]/p[1]/a[1]/text()')
            data_leixing=data.xpath('div[2]/p[1]/a[2]/text()')
            data_jianjie=data.xpath('div[2]/p[2]/text()')
            list[b]=[data_title,data_name,data_leixing,data_jianjie]
            b=b+1
    return list
def 数据可视化():
    list2=页面分析()
    轻小说数量=0
    悬疑数量=0
    玄幻数量=0
    都市数量=0
    仙侠数量=0
    科幻数量=0
    历史数量=0
    武侠数量=0
    游戏数量=0
    奇幻数量=0
    其他=0
    for i in range(100):
        if list2[i][2]==['轻小说']:
            轻小说数量=轻小说数量+1
        elif list2[i][2]==['悬疑']:
            悬疑数量=悬疑数量+1
        elif list2[i][2]==['玄幻']:
            玄幻数量=玄幻数量+1
        elif list2[i][2]==['都市']:
            都市数量=都市数量+1
        elif list2[i][2]==['仙侠']: 
            仙侠数量=仙侠数量+1
        elif list2[i][2]==['科幻']: 
            科幻数量=科幻数量+1
        elif list2[i][2]==['历史']: 
            历史数量=历史数量+1
        elif list2[i][2]==['武侠']: 
            武侠数量=武侠数量+1
        elif list2[i][2]==['游戏']:
            游戏数量=游戏数量+1
        elif list2[i][2]==['奇幻']:
            奇幻数量=奇幻数量+1
        else:
            其他=其他+1
    list3=[["轻小说",轻小说数量],["悬疑",悬疑数量],["玄幻",玄幻数量],["都市",都市数量],["仙侠",仙侠数量],["科幻",科幻数量],["历史",历史数量],["武侠",武侠数量],["游戏",游戏数量],["奇幻",奇幻数量],["其他",其他]]
    
    height=[0]*11
    x_pos=[0]*11
    #条形图
    for i in range(len(list3)):
        height[i]=list3[i][1]
        x_pos[i]=list3[i][0]
    plt.bar(x_pos,height)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.show()
    #折线图
    plt.plot(x_pos, # x轴数据
         height, # y轴数据
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 折线图中添加圆点
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='brown', # 点的填充色
         )
    plt.title("各种类型小说的观看程度折线图显示")
    plt.show()
    #饼图
    plt.pie(x=height,labels=x_pos,autopct='%0.0f%%')
    plt.title("")
    plt.show("各种类型小说的观看比例的饼图显示")
    return "显示完成"
if __name__ == '__main__':
    print(获取网址代码())
    print(内部网址获取())
    print(页面分析())
    print(数据可视化())
         