#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Функции обработки дат.
"""

import datetime

import ic

__version__ = (0, 0, 1, 1)


def get_first_day_of_month(year, month):
    """
    Первый день месяца.
    @param year: Год.
    @param month: Месяц.
    @return: Первый дата месяца.
    """
    if not isinstance(year, int):
        year = int(year)
    if not isinstance(month, int):
        month = int(month)

    year = max(datetime.MINYEAR, min(datetime.MAXYEAR, year))
    month = max(1, min(12, month))

    return datetime.date(day=1, month=month, year=year)


def get_last_day_of_month(year, month):
    """
    Последний день месяца.
    @param year: Год.
    @param month: Месяц.
    @return: Последняя дата месяца.
    """
    if not isinstance(year, int):
        year = int(year)
    if not isinstance(month, int):
        month = int(month)

    year = max(datetime.MINYEAR, min(datetime.MAXYEAR, year))
    month = max(1, min(12, month))

    start_month = datetime.date(day=1, month=month, year=year)
    date_on_next_month = start_month + datetime.timedelta(31)
    start_next_month = datetime.datetime(year=date_on_next_month.year, month=date_on_next_month.month, day=1)
    last_day_month = start_next_month - datetime.timedelta(days=1)
    return last_day_month


def next_month(src_date):
    """
    Следующий месяц от заданного числа.
    @param src_date: Исходная дата
    @return: Новую расчетную дату.
    """
    return src_date + datetime.timedelta(days=(src_date.max.day - src_date.day) + 1)


def prev_month(src_date):
    """
    Предыдущий месяц от заданного числа.
    @param src_date: Исходная дата
    @return: Новую расчетную дату.
    """
    result = src_date - datetime.timedelta(days=src_date.day)
    result.replace(day=1)
    return result


# --- Текущий год прикладной системы ---
SYS_YEAR = None


def getYEAR():
    """
    Год прикладной системы.
    """
    year = globals()['SYS_YEAR']
    if year is None:
        setYEAR(datetime.date.today().year)
    return year


def setYEAR(year):
    """
    Год прикладной системы.
    """
    globals()['SYS_YEAR'] = year


def saveYEAR(year=None):
    """
    Сохранить год прикладной системы в INI файле проекта.
    """
    if year is None:
        year = getYEAR()
    else:
        setYEAR(year)
    ic.settings.THIS.SETTING.sys_year.set(year)
    return year


def loadYEAR():
    """
    Загрузить год прикладной системы из INI файла проекта.
    """
    year = ic.settings.THIS.SETTING.sys_year.get()
    setYEAR(year)
    return year
