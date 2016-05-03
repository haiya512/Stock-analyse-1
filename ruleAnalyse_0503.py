# -*- coding: gbk -*-

path_rule_rst = '����������'
#sys.path.append(path_rule_rst)
path_avg_data = '��ֵ��������'
#sys.path.append(path_avg_data)

file = "002154_avg.txt"

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import collections
import sys


Outmap = collections.OrderedDict()  
rules = []

Anlyinmap = collections.OrderedDict()  
Anlyoutmap = collections.OrderedDict()  


'''��ȡ����K������'''
def mdl_read():
    Outmap.clear()
    Anlyinmap.clear()

    ##��K���ļ������ݰ�key����Outmap
    ##�о���ĵ�����Ϊkey
    with open(path_avg_data + '\\' + file, 'r') as f:
        head = f.readline()
        for line in f.readlines():
            strlist = line.split('\t')  # ��tab�ָ��ַ����������浽�б�
            Outmap[strlist[0]] = {'��K':[float(strlist[1]), float(strlist[2]), float(strlist[3]), float(strlist[4])], \
                                  'V':[int(strlist[5]), int(strlist[6]), float(strlist[7])], \
                                  '��':[float(strlist[8]), float(strlist[9]), float(strlist[10]), float(strlist[11]), \
                                       float(strlist[12])]}
        #end of "for"
    #end of "with"

    '''��ȡ���������������ݣ������K����Ϣ�棩��������key����outmap'''

    '''outmap��key����i++���'''
    i = 0
    for (d,x) in Outmap.items():
        Anlyinmap[i] = x
        Anlyinmap[i]['date'] = d
        i = i + 1
    #end of "for"
#end of "def"


'''��ȡrules'''
def mdl_ruleget():
    #������Ϊ���� �ַ��������Ӧ�ĺ���������
    
    if 1==1:
        rules.append({'һ��������', 'rule1'})
    if 1==2:
        rules.append({'�Ϳ�����', 'rule2'})
#end of "def"


def rule_2():
    ��pre = 0
    �� = 0
    �� = 0
    
    �Ϳ��� = 0.01
    ������ = 0.08
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        if d <= 1:
            continue
        else:
            ��pre = min(��, ��)
            �� = x['��K'][0]
            �� = x['��K'][1]
            �� = x['��K'][2]
            �� = x['��K'][3]
            if  (��pre - ��) > ��*�Ϳ��� and (�� - ��) > ��*������:
                Anlyoutmap[x['date']] = {'rule2', '�Ϳ�����'}
    #end of "for"

    head = "��������\t����ID\t��������\n"
    with open(path_rule_rst + '\\' + file[:6] + "_rule2.txt", 'w') as out:
        out.write(head)
        for (d,x) in Anlyoutmap.items():
            tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
#end of "def"

    
def rule_1():
    Anlyoutmap.clear()
    for (d,x) in Anlyinmap.items():
        �� = x['��K'][0]
        �� = x['��K'][1]
        �� = x['��K'][2]
        �� = x['��K'][3]
        ��5  = x['��'][0]
        ��10 = x['��'][1]
        ��20 = x['��'][2]
        ��30 = x['��'][3]
        ��60 = x['��'][4]
        if ��>=��5 and ��>=��10 and ��>=��20 and ��>=��30 and ��>=��60 and \
           ��<=��5 and ��<=��10 and ��<=��20 and ��<=��30 and ��<=��60:
            Anlyoutmap[x['date']] = {'rule1', 'һ��������'} 
    #end of "for"

    head = "��������\t����ID\t��������\n"
    with open(path_rule_rst + '\\' + file[:6] + "_rule1.txt", 'w') as out:
        out.write(head)
        for (d,x) in Anlyoutmap.items():
            tmpstr = d + "\t" + "\t".join(str(i) for i in x) + "\n"
            out.write(tmpstr)
        #end of "for"
    #end of "with"
#end of "def"


'''�������ݷ���'''
def mdl_ruleanlys():
    rule_1()
    rule_2()
#end of "def"


#main()
mdl_read()
mdl_ruleget()
mdl_ruleanlys()

