#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# Name:       report_cfg.py
# Purpose:    Классы описания конфигурации разбора.
#
# Author:     <Оконешников А.В.>
#
# Created:     11.07.2007
# RCS-ID:
# Copyright:   (c) 2007 Infocentre
# Licence:     $licence:<your licence>$
# -----------------------------------------------------------------------------
from . import ic_mode
if ic_mode.isDebugMode():
    print('import',__file__)

import re, sys,os
import logging
import time

date_re = re.compile('([0-3]\d)\.([0-1]\d)\.(\d{4})$')
date_re1 = re.compile('([0-3]\d)-([0-1]\d)-(\d{4})$')
date_re2 = re.compile('([0-3]\d)/([0-1]\d)/(\d{4})$')

null_re = re.compile('[-]+$')
money_re = re.compile('((\d{3},)+)?\d{3}((\.(\d){2})|)$')

def convertNumber(balstr, bZero=True):
    """ Функция преобразования из Balans-ого формата чисел в Excel-ный:
    1. числа преобразуются как xxx,xxx,xxx.xx -> xxxxxxxxx.xx
    2. даты остаются без изменения
    3. '----' заменяются на 0
    4.
    @param balstr: Преобразуемая строка.
    @param bZero: Признак того, что '---' преобразуются в 0.
    """
    # Преобразуем '----' в 0
    if null_re.match(balstr) and bZero:
        return 0

    # Проверим является ли строка датой
    if date_re.match(balstr) or date_re1.match(balstr) or date_re2.match(balstr):
        return ' ' + balstr
    
    # '01234' -> '01234'
    if balstr.startswith('0') and not balstr.startswith('0.'):
        return balstr

    # числа преобразуются как xxx,xxx,xxx.xx -> xxxxxxxxx.xx
##    if money_re.match(balstr) or money_re2.match(balstr):
##        return balstr.replace(',','')
    try:
        try:
            return int(balstr.replace(',',''))
        except:
            pass
        
        return float(balstr.replace(',',''))
    except:
        pass
    
    return balstr

def get_col_name_lst():
    """ Возвращает список имен колонок."""
    sAlf1 = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sAlf2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lst = []
    for s1 in sAlf1:
        for s2 in sAlf2:
            lst.append((s1+s2).strip())
            if len(lst)==256:
                return lst
    return lst

def get_row_col(addr):
    """ Преобразут Excel адрес к картежу (ряд, колонка)."""
    lst = get_col_name_lst()
    beg = 26
    end = -1
    step = 26
    
    if addr[1] in '1234567890':
        beg = 0
        end = 26
        step = 0

    if end < 0:
        lst = lst[beg:]
    else:
        lst = lst[beg:end]
        
    #print '-- beg, end', beg, end, lst
    for col, nm in enumerate(lst):
        if addr.startswith(nm):
            return (int(addr.split(nm)[-1]), col+1+step)
    
def Msg(msg, id=0):
    """ Окно сообщения."""
    if sys.platform == 'win32':
        try:
            import win32api
            win32api.MessageBox(id, msg.encode('cp1251'))
        except:
            logging.error('Msg:import error win32api')
            
        logging.info(msg)
    else:
        logging.info(msg)
    
    tolog(msg)

def tolog(msg,log_file_name='econvert2.log'):
    if type(msg) == type(u''):
        msg = msg.encode('utf-8')
    #Здесь я сделал автоматическое определение папки HOME
    home_dir=''    
    if sys.platform[:3].lower()=='win':
        if 'HOMEDRIVE' in os.environ and 'HOMEPATH' in os.environ:
            home_dir=os.environ['HOMEDRIVE']+os.environ['HOMEPATH']
        else:
            if 'TEMP' in os.environ:
                home_dir=os.environ['TEMP']
            else:
                home_dir='C:'
        home_dir=home_dir.replace('\\','/')
    else:
        home_dir=os.environ['HOME']
    
    try:
        f = open(home_dir+'/'+log_file_name,'a+')
        t = time.strftime('[%Y-%m-%d %H:%M:%S] ', time.localtime())
        f.write(t + msg+'\n')
        f.close()
    except:
        print(msg)