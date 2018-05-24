#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Общесистемные функции.
"""

import os
import sys
import locale
import platform

__version__ = (0, 0, 2, 1)


def getPlatform():
    """
    Определение платформы.
    """
    return platform.uname()[0].lower()


def isWindowsPlatform():
    return getPlatform() == 'windows'


def isLinuxPlatform():
    return getPlatform() == 'linux'


def getTerminalCodePage():
    """
    Кодировка коммандной оболочки по умолчанию.
    @return:
    """
    cmd_encoding = sys.stdout.encoding if isWindowsPlatform() else locale.getpreferredencoding()
    return cmd_encoding


def get_login():
    """
    Имя залогинненного пользователя.
    """
    username = os.environ.get('USERNAME', None)
    if username != 'root':
        return username
    else:
        return os.environ.get('SUDO_USER', None)


def getPythonMajorVersion():
    """
    Мажорная версия Python.
    """
    return sys.version_info.major


def getPythonMinorVersion():
    """
    Минорная версия Python.
    """
    return sys.version_info.minor


def isPython2():
    """
    Проверка на Python версии 2.
    @return: True - Python версии 2 / False - другая версия Python.
    """
    return sys.version_info.major == 2


def isPython3():
    """
    Проверка на Python версии 3.
    @return: True - Python версии 3 / False - другая версия Python.
    """
    return sys.version_info.major == 3
