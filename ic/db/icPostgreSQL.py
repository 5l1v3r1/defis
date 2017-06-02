#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Модуль функций установки связи с PostgreSQL.
"""

from ic.components import icwidget

# Константы
# Тип БД
POSTGRES_DB_TYPE = 'PostgreSQLDB'

# Спецификация БД
SPC_IC_POSTGRESQL = {'type': POSTGRES_DB_TYPE,
                     'user': '',
                     'dbname': '',
                     'password': '',
                     'host': 'localhost',
                     'port': '5432',
                     'options': '',
                     'encoding': 'UTF-8',

                     '__parent__': icwidget.SPC_IC_SIMPLE,
                     }
