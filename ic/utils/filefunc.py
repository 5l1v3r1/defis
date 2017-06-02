#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Функции работы с файлами.
"""

import os
import os.path
from . import util

__version__ = (0, 0, 2, 1)


def createTxtFile(FileName_,Txt_=None):
    """
    Создать текстовый файл.
    @param FileName_: Имя создаваемого файла.
    @param Txt_: Текст по умолчанию записываемый в файл.
    @return: True/False.
    """
    Txt_ = util.encodeText(Txt_)
    f = None
    try:
        if os.path.exists(FileName_):
            os.remove(FileName_)
        f = open(FileName_, 'w')
        if Txt_:
            f.write(Txt_)
        f.close()
        return True
    except:
        if f:
            f.close()
            f = None
        raise
    return False


def is_same_file_length(filename1, filename2):
    """
    Проверка что файл1 и файл2 совпадают.
    Проверка производиться по размеру файлу.
    @return: True/False.
    """
    if os.path.exists(filename1) and os.path.exists(filename2):
        file_size1 = os.path.getsize(filename1)
        file_size2 = os.path.getsize(filename2)
        return file_size1 == file_size2
    return False
