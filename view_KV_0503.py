# -*- coding: gbk -*-
'''
'%d'%int(height)

'''

path_rule_rst = "����������\\"
path_avg_data = "��ֵ��������\\"

file = "002154_avg.txt"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections  
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

viewfileoutmap = collections.OrderedDict()  
day = 0
����list=[]
#����Klist=[]
����list=[]
���list=[]
����list=[]
��5list =[]
��10list=[]
��20list=[]
��30list=[]
��60list=[]

def read_rule1rst():

    #��ȡrule�������
    #������Ϊkey������map
    with open(path_rule_rst + "002154_rule1.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            if(strlist[0] in viewfileoutmap):
                viewfileoutmap[strlist[0]]['�������'] = {strlist[1]: strlist[2]}
        #end of "for"
    #end of "with"
#end of "def"

def read_rule2rst():

    #��ȡrule�������
    #������Ϊkey������map
    with open(path_rule_rst + "002154_rule2.txt", 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            if(strlist[0] in viewfileoutmap):
                viewfileoutmap[strlist[0]]['�������'] = {strlist[1]: strlist[2]}
        #end of "for"
    #end of "with"
#end of "def"


xstep = 0.5
offset = (xstep - 0.1) / 2
    
def mdl_view():
    viewfileoutmap.clear()
    day = 0

    #��ȡ����K������
    #keyΪ����
    with open(path_avg_data + file, 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            viewfileoutmap[strlist[0]] = {'��K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                  'V':[int(strlist[5]), int(strlist[6]), float(strlist[7])], \
                                  '��':[float(strlist[8]), float(strlist[9]), float(strlist[10]), float(strlist[11]), \
                                       float(strlist[12])]}
            day = day + 1
        #end of "for"
    #end of "with"


    ##��K���ļ������ݰ�key����viewfileoutmap
    ##�о���ĵ�����Ϊkey
    read_rule1rst()
    read_rule2rst()
    
    
    for (d,x) in viewfileoutmap.items():
        if d.find("һ") > 0:
            ����list.append(d[:8])
        else:
            ����list.append("")
        #����Klist.append(x["��K"])
        ����list.append(x["V"][0])
        ���list.append(x["V"][1])
        ����list.append(x["V"][2])
        ��5list.append(x["��"][0])
        ��10list.append(x["��"][1])
        ��20list.append(x["��"][2])
        ��30list.append(x["��"][3])
        ��60list.append(x["��"][4])
    #end of "for"
        
    xpos = np.arange(0, len(����list)*xstep, xstep)
    xoffset= xpos + offset
    
    fig, ax = plt.subplots()   
    # ����ͼ�ĵױ߾�
    plt.subplots_adjust(bottom = 0.15)
    #plt.subplots_adjust(right = 0.5)
    #plt.subplots_adjust(left = 0.05)
    #plt.subplots_adjust(top = 10)
    #plt.grid() #��������
    ax.set_xticks(xpos)
    ax.set_xticklabels(����list, rotation=90, fontsize=10)
    plt.plot(xoffset, ��5list,  '.-', alpha = 0.7, color ='y')
    plt.plot(xoffset, ��10list, '-', alpha = 0.5, color ='yellowgreen')
    plt.plot(xoffset, ��20list, '-', alpha = 0.5, color ='lightskyblue')
    plt.plot(xoffset, ��30list, '-', alpha = 0.5, color ='c')
    plt.plot(xoffset, ��60list, '-', alpha = 0.5, color ='m')
    
    i = 0
    for (d, x) in viewfileoutmap.items():
        ���� = d
        ���� = x['��K'][0]
        ��� = x['��K'][1]
        ��� = x['��K'][2]
        ���� = x['��K'][3]
        
        if ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r')
        elif ���� > ����:
            ax.bar(xpos[i], ����-����, bottom = ����, width = .4, alpha = .3, facecolor ='green', edgecolor='green')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .3, facecolor ='green', edgecolor='green')
        else: #����==����:
            ax.bar(xpos[i], 0.005, bottom = ����, width = .4, alpha = .5, facecolor ='r', edgecolor='r')
            ax.bar(xoffset[i], ���-���, bottom = ���, width = .015, alpha = .5, facecolor ='r', edgecolor='r') 
        #end of "if"

        if  '�������' in x:
            for (d2, x2) in x['�������'].items():
                print(����, d2, x2)
                #������
                squal_x = [xpos[i], xpos[i], xpos[i] + xstep*10, xpos[i] + xstep*10, xpos[i]]
                squal_y = [����, ����*1.2, ����*1.2, ����, ����]
                ruleID = x2[1][-1:]
                plt.plot(squal_x, squal_y, '-', alpha = 0.8, color = 'r')
                #д����
                ax.text(xpos[i], ����*1.2, d2+' '+x2, alpha = 0.8, color = 'r')
            #end of "for"
        #end of "if"


            
        i = i + 1

#end of "def"        

#main()
mdl_view()
plt.show()
#plt.savefig('complex_bar_chart')

