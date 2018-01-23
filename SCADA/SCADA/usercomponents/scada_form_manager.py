#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Менеджер форм/панелей SCADA системы.
"""

import wx
from ic.engine import form_manager

from ic.log import log

__version__ = (0, 0, 2, 5)

# Период сканирования формы/панели SCADA системы по умолчанию
DEFAULT_SCAN_TICK = -1

ADDRESS_DELIMETER = u'.'

ENGINE_ADDRESS_IDX = 0
OBJ_ADDRESS_IDX = 1


class icSCADAFormManager(form_manager.icFormManager):
    """
    Менеджер форм/панелей SCADA системы.
    """

    def __init__(self, *args, **kwargs):
        """
        Конструктор.
        """
        form_manager.icFormManager.__init__(self, *args, **kwargs)

        # Список движков сканирования SCADA системы
        self.scada_engines = list()

        # Период сканирования для обновления формы/панели
        self.scan_tick = DEFAULT_SCAN_TICK

        self.timer = None

        # Признак автозапуска и автоостанова всех движков при создании/закрытии окна
        self.auto_run = False

        try:
            self.Bind(wx.EVT_TIMER, self.onTimerTick)
        except:
            log.fatal(u'Ошибка связи обработчика события таймера')

    def get_panel_obj_addresses(self, panel, data_dict=None, *ctrl_names):
        """
        Получить адреса объектов указанных в data_name свойстве контролов панели.
        Адреса объектов указываются как <Имя_движка.Имя_объекта_в_движке>.
        @param data_dict: Словарь для заполнения.
            Если не определен то создается новый словарь.
        @param ctrl_names: Взять только контролы с именами...
            Если имена контролов не определены,
            то обрабатываются контролы,
            указанные в соответствиях (accord).
        @return: Заполненный словарь соответствий {Имя контрола: Адрес тега}
        """
        result = dict() if data_dict is None else data_dict
        if not ctrl_names:
            ctrl_names = self.getAllChildrenNames()
            # log.debug(u'Обрабатываемые контролы формы <%s>: %s' % (self.name, ctrl_names))

        for ctrlname in dir(panel):
            if ctrl_names and ctrlname not in ctrl_names:
                # Если нельзя автоматически добавлять новые
                # данные и этих данных нет в заполняемом словаре,
                # то пропустить обработку
                continue

            ctrl = getattr(panel, ctrlname)
            if issubclass(ctrl.__class__, wx.Window) and ctrl.IsEnabled():
                if issubclass(ctrl.__class__, wx.Panel):
                    data = self.get_panel_obj_addresses(ctrl, data_dict, *ctrl_names)
                    result.update(data)
                else:
                    if hasattr(ctrl, 'data_name'):
                        address = getattr(ctrl, 'data_name')
                        if self.is_address(address):
                            # Сразу разделить адрес на имя движка и имя объекта
                            result[ctrlname] = tuple(address.split(ADDRESS_DELIMETER))
                        else:
                            log.error(u'Ошибка адресации <%s> в контроле <%s>. Адреса указываются как <Имя_движка.Имя_объекта_в_движке>' % (address, ctrlname))
        return result

    def is_address(self, value):
        """
        Проверка является ли строковое значение адресом SCADA объекта.
        @param value: Проверяемое значение.
        @return: True - это адрес объекта / False - нет.
        """
        return (ADDRESS_DELIMETER in value) and (value.count(ADDRESS_DELIMETER) == 1)

    def startEngines(self):
        """
        Запуск движков.
        @return: True-все движки успешно запущены / False - ошибка запуска.
        """
        return all([engine.start() for engine in self.scada_engines])

    def stopEngines(self):
        """
        Останов движков.
        @return: True-все движки успешно остановлены / False - ошибка останова.
        """
        return all([engine.stop() for engine in self.scada_engines])

    def addSCADAEngine(self, scada_engine):
        """
        Добавить движок в список.
        @param scada_engine: Объект движка.
        @return: True/False.
        """
        if scada_engine is None:
            log.warning(u'Не определен объект движка сканирования SCADA системы')
            return False

        if isinstance(self.scada_engines, list):
            if scada_engine not in self.scada_engines:
                self.scada_engines.append(scada_engine)
                return False
            else:
                log.warning(u'Движок <%s> у же присутствует в списке обработки' % scada_engine)
        else:
            log.warning(u'Ошибка типа списка движков сканирования SCADA системы <%s>' % self.scada_engines.__class__.__name__)
        return False

    def startTimer(self):
        """
        Запуск таймера обновления данных.
        @return: True/False.
        """
        if self.scan_tick > 0:
            self.timer = wx.Timer(self)
            self.timer.Start(self.scan_tick)
            return True
        else:
            self.timer = None
            log.warning(u'Не указан период сканирования панели SCADA системы')
        return False

    def stopTimer(self):
        """
        Останов таймера обновления данных.
        @return: True/False.
        """
        if self.timer:
            self.timer.Stop()
            self.timer = None
            return True
        return False

    def onTimerTick(self, event):
        """
        Обработчик одного тика таймера.
        """
        if self.timer is not None:
            # Если таймер запущен, то обновлять форму
            self.updateValues()

    def findSCADAEngine(self, engine_name):
        """
        Поиск движка скада системы в списке по имени.
        @param engine_name: Имя движка.
        @return: Объект движка или None, ели объект движка не найден.
        """
        for engine in self.scada_engines:
            if engine.name == engine_name:
                return engine
        engine_names = [engine.name for engine in self.scada_engines]
        log.warning(u'Движок SCADA не найден среди обрабатываемых %s' % engine_names)
        return None

    def updateValues(self):
        """
        Обновить значения контролов.
        """
        try:
            obj_addresses = self.get_panel_obj_addresses(panel=self)

            for ctrlname, address in obj_addresses.items():
                engine_name, obj_name = address
                engine = self.findSCADAEngine(engine_name)
                if engine:
                    obj = engine.FindObjectByName(obj_name)
                    if obj:
                        value = obj.getCurValue()
                        ctrl = getattr(self, ctrlname)
                        ctrl.setValue(value)
                    else:
                        log.warning(u'Объект <%s> не найден в движке <%s>' % (obj_name, engine_name))
        except:
            log.fatal(u'Ошибка обновления значений контролов формы SCADA системы')


