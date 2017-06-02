#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Общесистемные функции.
"""

import platform


def getPlatform():
    """
    Определение платформы.
    """
    return platform.uname()[0].lower()


def isWindowsPlatform():
    return getPlatform() == 'windows'


def isLinuxPlatform():
    return getPlatform() == 'linux'
