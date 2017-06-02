#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Интерфейс классов данных системы.
"""


class icDataClassInterface:
    """
    Интерфейс классов данных системы.
    """
    def __init__(self, TabRes_=None):
        """
        Конструктор.
        @param TabRes_: Ресурс таблицы.
        """
        self.res = TabRes_
        #   Указатель на класс провайдера
        self._class = None

    def getResource(self):
        """
        Ресурс.
        """
        return self.res
            
    def getConnection(self):
        """
        Возвращает объект соединения с базой данных, который поддерживает DB API 2.0. Внутренний
        счетчик пользователей увеличивается на 1. После использования объекта надо вызвать функцию
        releaseConnection - счетчик пользователей уменьшится на 1.
        """
        pass
        
    def releaseConnection(self):
        """
        Уменьшает счетчик пользователей соединения на 1. Когда кольчеств пользователей <= 0. Соединение может
        быть безопасно уничтожено.
        """
        pass
        
    def getProvider(self):
        """
        Возвращает указатель на класс данных, который реально работает с базой данных
        (Например класс, наследованный от SQLObject).
        """
        return self._class
        
    def getClassName(self):
        """
        Возвращает имя класса данных.
        """
        pass
        
    def delete(self, id):
        """
        Удаления объекта класса данных.
        
        @type id: C{int}
        @param id: Идентификатор объекта.
        """
        pass
        
    def add(self, *args, **kwargs):
        """
        Добавить объект.
        """
        pass
        
    def update(self, *args, **kwargs):
        """
        Изменить объект.
        """
        pass
        
    def get(self, id):
        """
        Получить объект.
        """
        pass

    def select(self, *args, **kwargs):
        """
        Выбрать список объектов из класса данных.
        @return: Возвражает объект SelectResults.
        """
        pass
        
    def queryAll(self, *args, **kwargs):
        """
        Выполнить запрос класса данных.
        @return: Возвращает список кортежей.
        """
        pass
        
    def queryRecs(self, SQLQuery_):
        """
        Выполнить запрос класса данных.
        @param SQLQuery_: Строка запроса.
        @return: Возвражает список объектов icSQLRecord.
        """
        pass
        
    def txtClassToDB(self, text):
        """
        Функция конвертации имен полей из предствления класса в представление базы данных.
        """
        pass

    def txtDBToClass(self, text):
        """
        Функция конвертации имен полей из предствления класса в представление базы данных.
        """
        pass
        
    def convQueryToSQL(self, text):
        """
        Конвертация запроса в терминах класса в SQL запрос.
        """
        pass

    def Lock(self):
        """
        Блокирует таблицу.
        """
        pass
        
    def unLock(self):
        """
        Разблокирует таблицу.
        """
        pass
        
    def LockObject(self, id):
        """
        Блокировка изменения объекта.
        """
        pass
        
    def unLockObject(self, id):
        """
        Разблокирует объект.
        """
        pass
        
    def IsLock(self):
        """
        Возвращает признак блокировки класса данных.
        """
        pass
        
    def IsLockObject(self, id):
        """
        Возвращает признак блокировки объекта класса данных.
        """
        pass

    def clear(self):
        """
        Очистить таблицу.
        """
        pass
