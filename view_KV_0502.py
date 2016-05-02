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
����list=[]
����Klist=[]
����list=[]
���list=[]
����list=[]
��5list =[]
��10list=[]
��20list=[]
��30list=[]
��60list=[]
    
def mdl_view():
    outmap.clear()
    day = 0

    #��ȡ����K������
    with open("002154_avg.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            outmap[strlist[0]] = [float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4]), \
                                  int(strlist[5]), int(strlist[6]), float(strlist[7]), float(strlist[8]), \
                                  float(strlist[9]), float(strlist[10]), float(strlist[11]), float(strlist[12])]
            day = day + 1
        #end of "for"
    #end of "with"


    ##��K���ļ������ݰ�key����outmap
    ##�о���ĵ�����Ϊkey
    xstep = 0.5
    offset = (xstep - 0.1) / 2
    
    for (d,x) in outmap.items():
        if d.find("һ") > 0:
            ����list.append(d[:8])
        else:
            ����list.append("")
        ����Klist.append([x[0],x[1],x[2],x[3]])
        ����list.append(x[4])
        ���list.append(x[5])
        ����list.append(x[6])
        ��5list.append(x[7])
        ��10list.append(x[8])
        ��20list.append(x[9])
        ��30list.append(x[10])
        ��60list.append(x[11])
    #end of "for"
        
    x = np.arange(0, len(����list)*xstep, xstep)
    xoffset= x + offset
    
    fig, ax = plt.subplots()
    ax.set_xticks(x)
    ax.set_xticklabels(����list)
    plt.plot(xoffset, ��5list,  '.-', alpha = 0.6, color ='y')
    plt.plot(xoffset, ��10list, '-', alpha = 0.2, color ='yellowgreen')
    plt.plot(xoffset, ��20list, '-', alpha = 0.2, color ='lightskyblue')
    plt.plot(xoffset, ��30list, '-', alpha = 0.2, color ='c')
    plt.plot(xoffset, ��60list, '-', alpha = 0.2, color ='m')
    
    i = 0
    for each in ����Klist:    
        ���� = each[0]
        ��� = each[1]
        ��� = each[2]
        ���� = each[3]
        if ���� > ����:
            ax.bar(x[i], ����-����, bottom = ����, width = .4, alpha = .9, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .4, facecolor ='r', edgecolor='r')
        elif ���� > ����:
            ax.bar(x[i], ����-����, bottom = ����, width = .4, alpha = .9, facecolor ='yellowgreen', edgecolor='yellowgreen')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .6, facecolor ='yellowgreen', edgecolor='yellowgreen')
        else: #����==����:
            ax.bar(x[i], 0.005, bottom = ����, width = .4, alpha = .9, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .4, facecolor ='r', edgecolor='r') 
        #end of "if"
        i = i + 1
        
        


    ##������K���ļ������̣����Խ���������ݰ�key����outmap



    


mdl_view()
plt.show()
#plt.savefig('complex_bar_chart')

