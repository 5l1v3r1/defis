#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Модуль базовых классов узлов-контроллеров SCADA системы.
"""

from ic.log import log


class icSCADANodeProto(object):
    """
    Базовый класс узла-контроллера SCADA системы.
    Организует общий интерфейс к объектам узлов-контроллеров SCADA системы.
    """
    def read_value(self, address):
        """
        Чтение значения по адресу.
        @param address: Адрес значения в узле.
        @return: Запрашиваемое значение или None в случае ошибки чтения.
        """
        log.error(u'Функция чтения данных по адресу не реализована в <%s>' % self.__class__.__name__)
        return None

    def write_value(self, address, value):
        """
        Запись значения по адресу.
        @param address: Адрес значения в узле.
        @param value: Записываемое значение.
        @return: True - запись прошла успешно/False - ошибка.
        """
        log.error(u'Функция записи данных по адресу не реализована в <%s>' % self.__class__.__name__)
        return None

    def read_values(self, addresses):
        """
        Чтение значений по адресам.
        @param addresses: Список адресов значений в узле.
        @return: Список запрашиваемых значений или None в случае ошибки чтения.
        """
        log.error(u'Функция чтения списка данных по адресу не реализована в <%s>' % self.__class__.__name__)
        return None
