# -*- coding: gbk -*-
"""
Created on Sun Jan 11 12:03:57 2015
lightskyblue
@author: zhang
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  

outmap = collections.OrderedDict()  
day = 0
日期list=[]
个股Klist=[]
总手list=[]
金额list=[]
换手list=[]
均5list =[]
均10list=[]
均20list=[]
均30list=[]
均60list=[]
    
def mdl_view():
    outmap.clear()
    day = 0

    #读取基本K线数据
    with open("002154_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # 用tab分割字符串，并保存到列表
            outmap[strlist[0]] = [float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4]), \
                                  int(strlist[5]), int(strlist[6]), float(strlist[7]), float(strlist[8]), \
                                  float(strlist[9]), float(strlist[10]), float(strlist[11]), float(strlist[12])]
            day = day + 1
        #end of "for"
    #end of "with"


    ##打开K线文件，数据按key并入outmap
    ##研究标的的日期为key
    xstep = 0.5
    offset = (xstep - 0.1) / 2
    
    for (d,x) in outmap.items():
        if d.find("一") > 0:
            日期list.append(d[:8])
        else:
            日期list.append("")
        个股Klist.append([x[0],x[1],x[2],x[3]])
        总手list.append(x[4])
        金额list.append(x[5])
        换手list.append(x[6])
        均5list.append(x[7])
        均10list.append(x[8])
        均20list.append(x[9])
        均30list.append(x[10])
        均60list.append(x[11])
    #end of "for"
        
    x = np.arange(0, len(日期list)*xstep, xstep)
    xoffset= x + offset
    
    fig, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_xticklabels(日期list)
    plt.plot(xoffset, 均5list,  '.-', alpha = 0.6, color ='y')
    plt.plot(xoffset, 均10list, '-', alpha = 0.2, color ='yellowgreen')
    plt.plot(xoffset, 均20list, '-', alpha = 0.2, color ='lightskyblue')
    plt.plot(xoffset, 均30list, '-', alpha = 0.2, color ='c')
    plt.plot(xoffset, 均60list, '-', alpha = 0.2, color ='m')
    
    i = 0
    for each in 个股Klist:    
        开盘 = each[0]
        最高 = each[1]
        最低 = each[2]
        收盘 = each[3]
        if 收盘 > 开盘:
            ax.bar(x[i], 收盘-开盘, bottom = 开盘, width = .4, alpha = .9, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .4, facecolor ='r', edgecolor='r')
        elif 开盘 > 收盘:
            ax.bar(x[i], 开盘-收盘, bottom = 收盘, width = .4, alpha = .9, facecolor ='yellowgreen', edgecolor='yellowgreen')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .6, facecolor ='yellowgreen', edgecolor='yellowgreen')
        else: #开盘==收盘:
            ax.bar(x[i], 0.005, bottom = 开盘, width = .4, alpha = .9, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], 最高-最低, bottom = 最低, width = .015, alpha = .4, facecolor ='r', edgecolor='r') 
        #end of "if"
        i = i + 1
        
        


    ##打开其他K线文件（大盘，策略结果），数据按key并入outmap



    


mdl_view()
plt.show()
#plt.savefig('complex_bar_chart')

