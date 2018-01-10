#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Общесистемные функции.
"""

import sys
import locale
import platform

__version__ = (0, 0, 0, 2)


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
