#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Специфакация соединение к MySQL. 
Необходимо установить пакет MySQLdb.
"""

from ic.components import icwidget

# Константы
# Тип БД
MYSQL_DB_TYPE = 'MySQLDB'

# Спецификация БД
SPC_IC_MYSQL = {'type': MYSQL_DB_TYPE,
                'user': '',
                'dbname': '',
                'password': '',
                'host': '',
                'port': '3306',
                'options': '',
                'encoding': 'UTF-8',

                '__parent__': icwidget.SPC_IC_SIMPLE,
                }
