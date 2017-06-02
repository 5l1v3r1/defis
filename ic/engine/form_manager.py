#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Модуль класса - менеджера абстрактного WX окна.
"""

# Подключение библиотек
import sys
import os
import os.path
import wx
import wx.dataview

from ic.log import log
from ic.utils import ic_time
from ic import config
from ic.engine import ic_user
from ic.utils import resfunc
from ic.utils import wxfunc
from ic.utils import ic_str
from ic.utils import formdatamanager
from ic.bitmap import ic_bmp
from ic.utils import ic_file
from ic.utils import key_combins


__version__ = (0, 1, 3, 2)


class icFormManager(formdatamanager.icFormDataManager):
    """
    Менеджер WX окна.
    ВНИМАНИЕ! Для того чтобы пользоваться менеджером
    имена контролов должны совпадат с именами словаря заполнения.
    Т.е. если в словаре заполнения используются имена реквизитов
    объекта, то имена контролов их обрабатывающих должны быть такими
    же как имена реквизитов объекта.
    Основные методы:
        set_form_data|set_ctrl_data - расстановка значений в контролы диалогового окна.
        get_form_data|get_ctrl_data - получение значений из контролов диалогового окна.
        save_dlg|save_ctrl - сохранение позиций и размеров динамических контролов диалогового окна.
        load_dlg|load_ctrl - загрузка позиций и размеров динамических контролов диалогового окна.
    """

    def get_ctrl_value(self, ctrl):
        """
        Получить значение контрола не зависимо от типа.
        @param ctrl: Объект контрола.
        @return: Значение контрола.
        """
        value = None
        if issubclass(ctrl.__class__, wx.Window) and ctrl.IsEnabled():
            if hasattr(ctrl, 'getValue'):
                # Обработка пользовательских контролов
                # Обычно все пользовательские контролы имеют
                # метод получения данных <getValue>
                value = ctrl.getValue()
            elif issubclass(ctrl.__class__, wx.CheckBox):
                value = ctrl.IsChecked()
            elif issubclass(ctrl.__class__, wx.TextCtrl):
                value = ctrl.GetValue()
            elif issubclass(ctrl.__class__, wx.DatePickerCtrl):
                wx_dt = ctrl.GetValue()
                value = ic_time.wxdatetime2pydatetime(wx_dt)
            elif issubclass(ctrl.__class__, wx.DirPickerCtrl):
                value = ctrl.GetPath()
            elif issubclass(ctrl.__class__, wx.SpinCtrl):
                value = ctrl.GetValue()
            elif issubclass(ctrl.__class__, wx.dataview.DataViewListCtrl):
                value = self._get_wxDataViewListCtrl_data(ctrl)
            else:
                log.warning(u'icFormManager. Получение данных контрола <%s> не поддерживается' % ctrl.__class__.__name__)
        return value

    def set_ctrl_value(self, ctrl, value):
        """
        Установить значение контрола не зависимо от типа.
        @param ctrl: Объект контрола.
        @param value: Значение контрола.
        @return: True/False.
        """
        result = False
        if hasattr(ctrl, 'setValue'):
            # Обработка пользовательских контролов
            # Обычно все пользовательские контролы имеют
            # метод установки данных <setValue>
            ctrl.setVaue(value)
            result = True
        elif issubclass(ctrl.__class__, wx.CheckBox):
            ctrl.SetValue(value)
            result = True
        elif issubclass(ctrl.__class__, wx.StaticText):
            value = value if type(value) in (str, unicode) else ic_str.toUnicode(value, config.DEFAULT_ENCODING)
            ctrl.SetLabel(value)
            result = True
        elif issubclass(ctrl.__class__, wx.TextCtrl):
            value = value if type(value) in (str, unicode) else ic_str.toUnicode(value, config.DEFAULT_ENCODING)
            ctrl.SetValue(value)
            result = True
        elif issubclass(ctrl.__class__, wx.DatePickerCtrl):
            wx_dt = ic_time.pydatetime2wxdatetime(value)
            ctrl.SetValue(wx_dt)
            result = True
        elif issubclass(ctrl.__class__, wx.DirPickerCtrl):
            ctrl.SetPath(value)
            result = True
        elif issubclass(ctrl.__class__, wx.SpinCtrl):
            ctrl.SetValue(int(value))
            result = True
        elif issubclass(ctrl.__class__, wx.dataview.DataViewListCtrl):
            self._set_wxDataViewListCtrl_data(ctrl, value)
            result = True
        else:
            log.warning(u'icFormManager. Тип контрола <%s> не поддерживается для заполнения' % ctrl.__class__.__name__)
        return result

    def get_panel_data(self, panel, data_dict=None, *ctrl_names):
        """
        Получить выставленные значения в контролах объекта панели.
        @param data_dict: Словарь для заполнения.
            Если не определен то создается новый словарь.
        @param ctrl_names: Взять только контролы с именами...
            Если имена контролов не определены,
            то обрабатываются контролы,
            указанные в соответствиях (accord).
        """
        result = dict() if data_dict is None else data_dict
        if not ctrl_names:
            ctrl_names = self.__accord.values()

        for ctrlname in dir(panel):
            if ctrl_names and ctrlname not in ctrl_names:
                # Если нельзя автоматически добавлять новые
                # данные и этих данных нет в заполняемом словаре,
                # то пропустить обработку
                continue

            ctrl = getattr(panel, ctrlname)
            if issubclass(ctrl.__class__, wx.Window) and ctrl.IsEnabled():
                if issubclass(ctrl.__class__, wx.Panel):
                    data = self.get_panel_data(ctrl, data_dict, *ctrl_names)
                    result.update(data)
                else:
                    value = self.get_ctrl_value(ctrl)
                    result[ctrlname] = value
        return result

    def get_form_data(self, data_dict=None, *ctrl_names):
        """
        Получить выставленные значения в контролах.
        @param data_dict: Словарь для заполнения.
            Если не определен то создается новый словарь.
        @param ctrl_names: Взять только контролы с именами...
            Если имена контролов не определены,
            то обрабатываются контролы,
            указанные в соответствиях (accord).
        """
        return self.get_panel_data(self, data_dict, *ctrl_names)

    # Другое наименование метода
    get_ctrl_data = get_form_data

    def _get_wxDataViewListCtrl_data(self, ctrl):
        """
        Получить данные из контрола wxDataViewListCtrl.
        @param ctrl: Объект контрола.
        @return: Список словарей - строк контрола.
        """
        recordset = list()
        store = ctrl.GetStore()
        # Определить имена колонок контрола
        self_col_names = [name for name in dir(self) if
                          issubclass(getattr(self, name).__class__, wx.dataview.DataViewColumn)]
        # По именом определить объекты колонок определенные в диалоговой форме
        self_cols = [getattr(self, name) for name in self_col_names]

        for i_row in range(store.GetCount()):
            record = dict()
            for i_col in range(ctrl.GetColumnCount()):
                # Колонка контрола
                col = ctrl.GetColumn(i_col)
                # Если можно определить имя колонки, то берем имя
                # иначе берем в качестве имени индекс
                col_name = self_col_names[wxfunc.get_index_wx_object_in_list(col, self_cols)] if wxfunc.is_wx_object_in_list(col, self_cols) else i_col
                # Добавить значение колонки в запись
                record[col_name] = ctrl.GetValue(i_row, i_col)
            recordset.append(record)
            # log.debug(u'Record %s' % record)

        return recordset

    def _set_wxDataViewListCtrl_data(self, ctrl, records):
        """
        Установить данные в контрол wxDataViewListCtrl.
        @param ctrl: Объект контрола.
        @param records: Список словарей - записей.
            Имя колонки в записи может задаваться как именем,
            так и индексом.
        @return: True/False.
        """
        # Сначала очистить контрол от записей
        ctrl.DeleteAllItems()

        # Определить имена колонок контрола
        self_col_names = [name for name in dir(self) if
                          issubclass(getattr(self, name).__class__, wx.dataview.DataViewColumn)]
        # По именом определить объекты колонок определенные в диалоговой форме
        self_cols = [getattr(self, name) for name in self_col_names]

        for record in records:
            wx_rec = [u''] * ctrl.GetColumnCount()
            for colname, value in record.items():
                if type(colname) in (str, unicode):
                    # Колонка задается именем
                    if colname in self_col_names:
                        i_colname = self_col_names.index(colname)
                        idx = wxfunc.get_index_wx_object_in_list(self_cols[i_colname],
                                                                 ctrl.GetColumns())
                        wx_rec[idx] = ic_str.toUnicode(value)
                    else:
                        log.warning(u'Не найдено имя колонки <%s> при заполнении wxDataViewListCtrl контрола данными' % colname)
                elif isinstance(colname, int):
                    # Колонка задается индексом
                    wx_rec[colname] = ic_str.toUnicode(value)
                else:
                    log.warning(u'Не поддерживаемый тип имени колонки <%s> при заполнении wxDataViewListCtrl контрола данными' % colname)
            ctrl.AppendItem(wx_rec)

        return True

    def set_form_data(self, data_dict=None, *ctrl_names):
        """
        Установить значения в контролах.
        @param data_dict: Словарь для заполнения.
        @param ctrl_names: Взять только контролы с именами...
            Если имена контролов не определены,
            то обрабатываются контролы,
            указанные в соответствиях (accord).
        """
        return self.set_panel_data(self, data_dict, *ctrl_names)

    # Другое наименование метода
    set_ctrl_data = set_form_data

    def set_panel_data(self, panel, data_dict=None, *ctrl_names):
        """
        Установить значения в контролах.
        @param panel: Объект панели.
        @param data_dict: Словарь для заполнения.
        @param ctrl_names: Взять только контролы с именами...
            Если имена контролов не определены,
            то обрабатываются контролы,
            указанные в соответствиях (accord).
        """
        if data_dict is None:
            log.warning(u'Не определен словарь заполнения для контролов окна')
            return

        for name, value in data_dict.items():
            for ctrlname in dir(panel):
                if ctrl_names and ctrlname not in ctrl_names:
                    # Если нельзя автоматически добавлять новые
                    # данные и этих данных нет в заполняемом словаре,
                    # то пропустить обработку
                    continue

                if ctrlname == name:
                    ctrl = getattr(panel, ctrlname)
                    self.set_ctrl_value(ctrl, value)
                    break

    def _getCtrlData(self):
        """
        Получить данные контролов для сохранения.
        Не все данные могут сохраняться.
        @return: Словарь с данными для записи.
        """
        ctrl_data = dict()
        # Сначала сохранить размеры и положение самого окна
        ctrl_data['self'] = dict(pos=tuple(self.GetPosition()),
                                 size=tuple(self.GetSize()))

        for ctrlname in dir(self):
            ctrl = getattr(self, ctrlname)
            if issubclass(ctrl.__class__, wx.Window) and ctrl.IsEnabled():
                if issubclass(ctrl.__class__, wx.SplitterWindow):
                    ctrl_data[ctrlname] = dict(sash_pos=ctrl.GetSashPosition())
                else:
                    log.warning(u'icDialogManager. Тип контрола <%s> не поддерживается' % ctrl.__class__.__name__)

        return ctrl_data

    def save_dlg(self):
        """
        Сохранить позиции и размеры динамических контролов для
        последующего их востановления.
        Принцип такой: Пользователь может менять размеры окон,
        положение и размер сплиттеров и т.п.
        Этой функцией по закрытию происходит сохранение
        в локальную папку профиля.
        При открытии окна с помощью метода <load_dlg>
        происходит восстановление сохраненных параметров.
        @return: True/False.
        """
        # Определить имя файла для хранения данных
        res_filename = os.path.join(config.PROFILE_DIRNAME,
                                    ic_user.getPrjName(),
                                    self.__class__.__name__)
        data = self._getCtrlData()
        return resfunc.SaveResourcePickle(res_filename, data)

    # Другое наименование метода
    save_ctrl = save_dlg

    def _setCtrlData(self, ctrl_data):
        """
        Установить данные контролов после загрузки.
        @param ctrl_data: Данные контролов.
        @return: True/False.
        """
        # Сначала установить размеры и позиции
        # самого диалогового окна
        dlg_data = ctrl_data.get('self', dict())
        size = dlg_data.get('size', (-1, -1))
        self.SetSize(*size)
        pos = dlg_data.get('pos', (-1, -1))
        self.SetPosition(*pos)

        # Перебор других контролов
        for ctrlname, ctrl_value in [item for item in ctrl_data.items() if item[0] != 'self']:
            ctrl = getattr(self, ctrlname)
            if issubclass(ctrl.__class__, wx.Window) and ctrl.IsEnabled():
                if issubclass(ctrl.__class__, wx.SplitterWindow):
                    ctrl.SetSashPosition(ctrl_value.get('sash_pos', -1))
                else:
                    log.warning(u'icDialogManager. Тип контрола <%s> не поддерживается' % ctrl.__class__.__name__)
        return True

    def load_dlg(self):
        """
        Загрузить позиции и размеры динамических контролов окна.
        @return: True/False.
        """
        res_filename = os.path.join(config.PROFILE_DIRNAME,
                                    ic_user.getPrjName(),
                                    self.__class__.__name__)
        data = resfunc.LoadResourcePickle(res_filename)
        return self._setCtrlData(data)

    # Другое наименование метода
    load_ctrl = load_dlg

    def save_ext_data(self, name, **kwargs):
        """
        Запись дополнительных данных окна.
        @param name: Наименование файла для записи.
        @param kwargs: Словарь данных для записи.
        @return: True/False.
        """
        # Определить имя файла для хранения данных
        res_filename = os.path.join(ic_file.getPrjProfilePath(),
                                    name+'.ext')
        return resfunc.SaveResourcePickle(res_filename, kwargs)

    def load_ext_data(self, name):
        """
        Загрузка дополнительных данных окна.
        @param name: Наименование файла хранения данных.
        @return: Загруженные данные в виде словаря или 
            пустой словарь если данных нет.
        """
        res_filename = os.path.join(ic_file.getPrjProfilePath(),
                                    name+'.ext')
        data = resfunc.LoadResourcePickle(res_filename)
        if data is None:
            data = dict()
        return data

    def set_accord(self, **accord):
        """
        Установить словарь соответствий значений
        контролов и имен прикладного кода.
        @param accord: Cловарь соответствий значений
        контролов и имен прикладного кода.
            Формат:
            {'Имя используемое в прикладном коде': 'Имя контрола', ...}
        """
        self.__accord = accord

    def add_accord(self, **accord):
        """
        Добавить словарь соответствий значений
        контролов и имен прикладного кода.
        @param accord: Cловарь соответствий значений
        контролов и имен прикладного кода.
            Формат:
            {'Имя используемое в прикладном коде': 'Имя контрола', ...}
        """
        if accord:
            self.__accord.update(accord)

    def get_accord(self):
        """
        Получить словарь соответствий значений
        контролов и имен прикладного кода.
        @return: Cловарь соответствий значений
        контролов и имен прикладного кода.
            Формат:
            {'Имя используемое в прикладном коде': 'Имя контрола', ...}
        """
        return self.__accord

    def get_accord_ctrl_data(self):
        """
        Получить согласованные данные.
        @return: Словарь значений из контролов
            в формате соответствий.
            Формат:
            {'Имя используемое в прикладном коде': 'Значение контрола', ...}
        """
        ctrl_data = self.get_ctrl_data(*self.__accord.values())
        result_data = dict([(name, ctrl_data[self.__accord[name]]) for name in self.__accord.keys()])
        return result_data

    def set_accord_ctrl_data(self, **data):
        """
        Установить согласованные данные.
        @param data: Словарь значений в формате соответствий.
            Контролы заполняются в согласно соответствиям.
            Формат:
            {'Имя используемое в прикладном коде': 'Значение контрола', ...}
        """
        ctrl_data = dict([(self.__accord[name], data[name]) for name in data.keys()])
        self.set_ctrl_data(ctrl_data, *ctrl_data.keys())

    def find_panel_accord(self, panel):
        """
        Найти на панели контролы ввода на панели и определить 
        их как словарь соответствий.
        @param panel: Объект панели. 
        @return: Словарь соответствий контролов ввода.
        """
        panel_ctrl_names = dir(panel)
        accord = dict()
        for ctrl_name in panel_ctrl_names:
            ctrl = getattr(panel, ctrl_name)
            if issubclass(ctrl.__class__, wx.TextCtrl):
                accord[ctrl_name] = ctrl_name
            elif issubclass(ctrl.__class__, wx.SpinCtrl):
                accord[ctrl_name] = ctrl_name
            elif issubclass(ctrl.__class__, wx.CheckBox):
                accord[ctrl_name] = ctrl_name
            elif issubclass(ctrl.__class__, wx.DatePickerCtrl):
                accord[ctrl_name] = ctrl_name
            elif issubclass(ctrl.__class__, wx.DirPickerCtrl):
                accord[ctrl_name] = ctrl_name
            elif issubclass(ctrl.__class__, wx.dataview.DataViewListCtrl):
                accord[ctrl_name] = ctrl_name

        return accord

    def refresh_DataViewListCtrl(self, ctrl, data_list=None, columns=None):
        """
        Обновить список строк контрола типа wx.dataview.DataViewListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        """
        if data_list is None:
            data_list = list()

        if columns is not None:
            data_list = [[rec[col] for col in columns] for rec in data_list]

        # Удаляем все строки
        ctrl.DeleteAllItems()
        for row in data_list:
            ctrl.AppendItem(row)

    def refresh_ListCtrl(self, ctrl, data_list=None, columns=None):
        """
        Обновить список строк контрола типа wx.ListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        """
        if data_list is None:
            data_list = list()

        if columns is not None:
            data_list = [[rec[col] for col in columns] for rec in data_list]

        self.setRows_list_ctrl(ctrl, data_list)

    def refresh_list_ctrl(self, ctrl=None, data_list=None, columns=None):
        """
        Обновить список строк контрола.
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для обновления')
            return

        if isinstance(ctrl, wx.dataview.DataViewListCtrl):
            self.refresh_DataViewListCtrl(ctrl, data_list, columns)
        else:
            log.warning(u'Обновление списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)

    def moveUpRow_DataViewListCtrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                                   columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку выше в контроле типа wx.dataview.DataViewListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if idx != wx.NOT_FOUND and idx > 0:
            # Поменять номер строки если необходимо
            if n_col is not None:
                value = data_list[idx][n_col]
                data_list[idx][n_col] = data_list[idx - 1][n_col]
                data_list[idx - 1][n_col] = value
            # Поменять значения строк
            value = data_list[idx - 1]
            data_list[idx - 1] = data_list[idx]
            data_list[idx] = value

            if do_refresh:
                # Обновляем полностью контрол
                self.refresh_DataViewListCtrl(ctrl, data_list, columns=columns)
            else:
                # Обновляем конкретные строки
                for i_col, value in enumerate(data_list[idx-1]):
                    ctrl.SetTextValue(value if type(value) in (unicode, str) else str(value), idx-1, i_col)
                for i_col, value in enumerate(data_list[idx]):
                    ctrl.SetTextValue(value if type(value) in (unicode, str) else str(value), idx, i_col)
            ctrl.SelectRow(idx - 1)
            return True
        else:
            log.warning(u'Не выбрана перемещаемая строка списка')
        return False

    def moveUpRow_ListCtrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                           columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку выше в контроле типа wx.ListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if idx != wx.NOT_FOUND and idx > 0:
            # Поменять номер строки если необходимо
            if n_col is not None:
                value = data_list[idx][n_col]
                data_list[idx][n_col] = data_list[idx - 1][n_col]
                data_list[idx - 1][n_col] = value
            # Поменять значения строк
            value = data_list[idx - 1]
            data_list[idx - 1] = data_list[idx]
            data_list[idx] = value

            if do_refresh:
                # Обновляем полностью контрол
                self.refresh_ListCtrl(ctrl, data_list, columns=columns)
            else:
                # Обновляем конкретные строки
                for i_col, value in enumerate(data_list[idx-1]):
                    ctrl.SetStringItem(idx-1, i_col, value if type(value) in (unicode, str) else str(value))
                for i_col, value in enumerate(data_list[idx]):
                    ctrl.SetStringItem(idx, i_col, value if type(value) in (unicode, str) else str(value))
            ctrl.Select(idx - 1)
            return True
        else:
            log.warning(u'Не выбрана перемещаемая строка списка')
        return False

    def moveUpRow_list_ctrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                            columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку выше в контроле.
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для обновления')
            return False

        if isinstance(ctrl, wx.dataview.DataViewListCtrl):
            return self.moveUpRow_DataViewListCtrl(ctrl=ctrl, data_list=data_list,
                                                   idx=idx, columns=columns, n_col=n_col,
                                                   do_refresh=do_refresh)
        elif isinstance(ctrl, wx.ListCtrl):
            return self.moveUpRow_ListCtrl(ctrl=ctrl, data_list=data_list,
                                           idx=idx, columns=columns, n_col=n_col,
                                           do_refresh=do_refresh)
        else:
            log.warning(u'Перемещение строки списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def moveDownRow_DataViewListCtrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                                     columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку ниже в контроле типа wx.dataview.DataViewListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if idx != wx.NOT_FOUND and idx < (len(data_list) - 1):
            # Поменять номер строки если необходимо
            if n_col is not None:
                value = data_list[idx][n_col]
                data_list[idx][n_col] = data_list[idx + 1][n_col]
                data_list[idx + 1][n_col] = value
            # Поменять значения строк
            value = data_list[idx + 1]
            data_list[idx + 1] = data_list[idx]
            data_list[idx] = value

            if do_refresh:
                # Обновляем полностью контрол
                self.refresh_DataViewListCtrl(ctrl, data_list, columns=columns)
            else:
                # Обновляем конкретные строки
                for i_col, value in enumerate(data_list[idx]):
                    ctrl.SetTextValue(value if type(value) in (unicode, str) else str(value), idx, i_col)
                for i_col, value in enumerate(data_list[idx+1]):
                    ctrl.SetTextValue(value if type(value) in (unicode, str) else str(value), idx+1, i_col)
            ctrl.SelectRow(idx + 1)
            return True
        else:
            log.warning(u'Не выбрана строка списка для перемещения')
        return False

    def moveDownRow_ListCtrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                             columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку ниже в контроле типа wx.ListCtrl
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if idx != wx.NOT_FOUND and idx < (len(data_list) - 1):
            # Поменять номер строки если необходимо
            if n_col is not None:
                value = data_list[idx][n_col]
                data_list[idx][n_col] = data_list[idx + 1][n_col]
                data_list[idx + 1][n_col] = value
            # Поменять значения строк
            value = data_list[idx + 1]
            data_list[idx + 1] = data_list[idx]
            data_list[idx] = value

            if do_refresh:
                # Обновляем полностью контрол
                self.refresh_ListCtrl(ctrl, data_list, columns=columns)
            else:
                # Обновляем конкретные строки
                for i_col, value in enumerate(data_list[idx]):
                    ctrl.SetStringItem(idx, i_col, value if type(value) in (unicode, str) else str(value))
                for i_col, value in enumerate(data_list[idx+1]):
                    ctrl.SetStringItem(idx+1, i_col, value if type(value) in (unicode, str) else str(value))
            ctrl.Select(idx + 1)
            return True
        else:
            log.warning(u'Не выбрана строка списка для перемещения')
        return False

    def moveDownRow_list_ctrl(self, ctrl, data_list=None, idx=wx.NOT_FOUND,
                              columns=None, n_col=None, do_refresh=False):
        """
        Переместить строку ниже в контроле.
        @param ctrl: Объект контрола.
        @param data_list: Данные списка.
        @param idx: Индекс перемещаемой строки.
        @param columns: Список/кортеж колонок в случае если строки списка
            задаются словарями.
        @param n_col: Наименование/индекс колонки номера строки.
            Если не определено, то нет такой колонки.
        @param do_refresh: Произвести полное обновление контрола?
        @return: True - было сделано перемещение, False - перемещения не было.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для обновления')
            return False

        if isinstance(ctrl, wx.dataview.DataViewListCtrl):
            return self.moveDownRow_DataViewListCtrl(ctrl=ctrl, data_list=data_list,
                                                     idx=idx, columns=columns, n_col=n_col,
                                                     do_refresh=do_refresh)
        elif isinstance(ctrl, wx.ListCtrl):
            return self.moveDownRow_ListCtrl(ctrl=ctrl, data_list=data_list,
                                             idx=idx, columns=columns, n_col=n_col,
                                             do_refresh=do_refresh)
        else:
            log.warning(u'Перемещение строки списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def appendColumn_ListCtrl(self, ctrl, label=u'', width=-1):
        """
        Добавить колонку в wx.ListCtrl.
        @param ctrl: Объект контрола wx.ListCtrl.
        @param col_label: Надпись колонки.
        @param width: Ширина колонки.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        try:
            i = ctrl.GetColumnCount()
            if width <= 0:
                width = wx.LIST_AUTOSIZE
            ctrl.InsertColumn(i, label, width=width)
            return True
        except:
            log.fatal(u'Ошибка добавления колонки в контрол wx.ListCtrl')
        return False

    def appendColumn_list_ctrl(self, ctrl=None, label=u'', width=-1):
        """
        Добавить колонку в контрол списка.
        @param ctrl: Объект контрола.
        @param col_label: Надпись колонки.
        @param width: Ширина колонки.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для добавления колонки')
            return False

        if isinstance(ctrl, wx.ListCtrl):
            return self.appendColumn_ListCtrl(ctrl=ctrl, label=label, width=width)
        else:
            log.warning(u'Добавление колонки списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def setColumns_list_ctrl(self, ctrl=None, cols=()):
        """
        Установить колонки в контрол списка.
        @param ctrl: Объект контрола.
        @param cols: Список описаний колонок.
            колонка может описываться как списком
            ('Заголовок колонки', Ширина колонки)
            так и словарем:
            {'label': Заголовок колонки,
            'width': Ширина колонки}
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для добавления колонки')
            return False

        if isinstance(ctrl, wx.ListCtrl):
            result = True
            ctrl.ClearAll()
            for col in cols:
                if isinstance(col, dict):
                    result = result and self.appendColumn_ListCtrl(ctrl=ctrl, **col)
                elif isinstance(col, list) or isinstance(col, tuple):
                    result = result and self.appendColumn_ListCtrl(ctrl, *col)
            return result
        else:
            log.warning(u'Добавление колонок списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def appendRow_ListCtrl(self, ctrl, row=(),
                           evenBackgroundColour=None, oddBackgroundColour=None):
        """
        Добавить строку в контрол wx.ListCtrl.
        @param ctrl: Объект контрола wx.ListCtrl.
        @param row: Список строки по полям.
        @param evenBackgroundColour: Цвет фона четных строк.
        @param oddBackgroundColour: Цвет фона нечетных строк.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if type(row) not in (list, tuple):
            log.warning(u'Не корректный тип списка строки <%s> объекта wx.ListCtrl' % type(row))
            return False

        try:
            row_idx = -1
            # Ограничить список количеством колонок
            row = row[:ctrl.GetColumnCount()]
            for i, value in enumerate(row):
                if value is None:
                    value = u''
                elif type(value) in (int, float):
                    value = str(value)
                elif isinstance(value, str):
                    value = unicode(value, config.DEFAULT_ENCODING)
                elif isinstance(value, unicode):
                    pass
                else:
                    value = str(value)

                if i == 0:
                    row_idx = ctrl.InsertStringItem(sys.maxint, value)
                else:
                    ctrl.SetStringItem(row_idx, i, value)

            if row_idx != -1:
                if evenBackgroundColour and not (row_idx % 2):
                    # Добавляемая строка четная?
                    ctrl.SetItemBackgroundColour(row_idx, evenBackgroundColour)
                elif oddBackgroundColour and (row_idx % 2):
                    # Добавляемая строка не четная?
                    ctrl.SetItemBackgroundColour(row_idx, oddBackgroundColour)
            return True
        except:
            log.fatal(u'Ошибка добавления строки %s в контрол wx.ListCtrl' % str(row))
        return False

    def appendRow_list_ctrl(self, ctrl=None, row=(),
                            evenBackgroundColour=None, oddBackgroundColour=None):
        """
        Добавить строку в контрол списка.
        @param ctrl: Объект контрола.
        @param row: Список строки по полям.
        @param evenBackgroundColour: Цвет фона четных строк.
        @param oddBackgroundColour: Цвет фона нечетных строк.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для добавления строки')
            return False

        if isinstance(ctrl, wx.ListCtrl):
            return self.appendRow_ListCtrl(ctrl=ctrl, row=row,
                                           evenBackgroundColour=evenBackgroundColour,
                                           oddBackgroundColour=oddBackgroundColour)
        elif isinstance(ctrl, wx.dataview.DataViewListCtrl):
            ctrl.AppendItem(row)
            return True
        else:
            log.warning(u'Добавление колонок списка контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def setRow_list_ctrl(self, ctrl=None, row_idx=-1, row=(),
                         evenBackgroundColour=None, oddBackgroundColour=None,
                         doSavePos=False):
        """
        Установить строку контрола списка.
        @param ctrl: Объект контрола.
        @param row_idx: Индекс строки. Если -1, то строка не устанавливается.
        @param row: Cтрока.
            Строка представляет собой список/кортеж:
            (Значение 1, Значение 2, ..., Значение N),
        @param evenBackgroundColour: Цвет фона четных строк.
        @param oddBackgroundColour: Цвет фона нечетных строк.
        @param doSavePos: Сохранять позицию курсора?
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для установки строки')
            return False
        if row_idx == -1:
            log.warning(u'Не указан индекс устанавливаемой строки')
            return False
        if not isinstance(row, list) and not isinstance(row, tuple):
            log.warning(u'Не корректный тип данных строки <%s>' % row.__class__.__name__)
            return False

        if isinstance(ctrl, wx.ListCtrl):
            row_count = ctrl.GetItemCount()
            if 0 > row_idx > row_count:
                log.warning(u'Не корректный индекс <%d> контрола <%s>' % (row_idx, ctrl.__class__.__name__))
                return False
            cursor_pos = None
            if doSavePos:
                cursor_pos = ctrl.GetFirstSelected()

            for i, item in enumerate(row):
                item_str = ic_str.toUnicode(item, config.DEFAULT_ENCODING)
                ctrl.SetStringItem(row_idx, i, item_str)
                if evenBackgroundColour and not (row_idx % 2):
                    # Четная строка?
                    ctrl.SetItemBackgroundColour(row_idx, evenBackgroundColour)
                elif oddBackgroundColour and (row_idx % 2):
                    # Не четная строка?
                    ctrl.SetItemBackgroundColour(row_idx, oddBackgroundColour)
            if cursor_pos not in (None, -1) and cursor_pos < row_count:
                ctrl.Select(cursor_pos)
            return True
        else:
            log.warning(u'Установка строки контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def setRows_list_ctrl(self, ctrl=None, rows=(),
                          evenBackgroundColour=None, oddBackgroundColour=None,
                          doSavePos=False):
        """
        Установить строки в контрол списка.
        @param ctrl: Объект контрола.
        @param rows: Список строк.
            Строка представляет собой список:
            [
            (Значение 1, Значение 2, ..., Значение N), ...
            ]
        @param evenBackgroundColour: Цвет фона четных строк.
        @param oddBackgroundColour: Цвет фона нечетных строк.
        @param doSavePos: Сохранять позицию курсора?
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для добавления строк')
            return False

        if isinstance(ctrl, wx.ListCtrl):
            result = True
            cursor_pos = None
            if doSavePos:
                cursor_pos = ctrl.GetFirstSelected()
            ctrl.DeleteAllItems()
            for row in rows:
                if isinstance(row, list) or isinstance(row, tuple):
                    result = result and self.appendRow_ListCtrl(ctrl=ctrl, row=row,
                                                                evenBackgroundColour=evenBackgroundColour,
                                                                oddBackgroundColour=oddBackgroundColour)
            if cursor_pos not in (None, -1) and cursor_pos < len(rows):
                ctrl.Select(cursor_pos)
            return result
        elif isinstance(ctrl, wx.dataview.DataViewListCtrl):
            result = True
            cursor_pos = None
            if doSavePos:
                cursor_pos = ctrl.GetSelection()
            ctrl.DeleteAllItems()
            for row in rows:
                if isinstance(row, list) or isinstance(row, tuple):
                    try:
                        ctrl.AppendItem(row)
                        result = result and True
                    except:
                        log.fatal(u'Ошибка доавления строки %s в контрол <%s>' % (str(row), ctrl.__class__.__name__))
                        result = False
            if cursor_pos not in (None, -1) and cursor_pos < len(rows):
                ctrl.SelectRow(cursor_pos)
            return result
        else:
            log.warning(u'Добавление колонок контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def setRowForegroundColour_list_ctrl(self, ctrl=None, i_row=0, colour=None):
        """
        Установить цвет текста строки в контроле списка.
        @param ctrl: Объект контрола.
        @param i_row: Индекс строки.
        @param colour: Цвет текста строки.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для установления цвета строки')
            return False
        if colour is None:
            colour = wx.SYS_COLOUR_CAPTIONTEXT

        if isinstance(ctrl, wx.ListCtrl):
            try:
                ctrl.SetItemTextColour(i_row, colour)
            except:
                log.warning(u'Не корректный индекс строки <%s>' % i_row)
                return False
            return True
        else:
            log.warning(u'Установление цвета строки контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def setRowBackgroundColour_list_ctrl(self, ctrl=None, i_row=0, colour=None):
        """
        Установить цвет фона строки в контроле списка.
        @param ctrl: Объект контрола.
        @param i_row: Индекс строки.
        @param colour: Цвет фона строки.
        @return: True - все прошло нормально / False - какая-то ошибка.
        """
        if ctrl is None:
            log.warning(u'Не определен контрол для установления цвета строки')
            return False
        if colour is None:
            colour = wx.SYS_COLOUR_INACTIVECAPTION

        if isinstance(ctrl, wx.ListCtrl):
            try:
                ctrl.SetItemBackgroundColour(i_row, colour)
            except:
                log.warning(u'Не корректный индекс строки <%s>' % i_row)
                return False
            return True
        else:
            log.warning(u'Установление цвета строки контрола типа <%s> не поддерживается' % ctrl.__class__.__name__)
        return False

    def enableTools_toolbar(self, toolbar, **kwargs):
        """
        Установить вкл./выкл. инструментов панели инструментов wx.ToolBar.
        @param toolbar: Объект контрола wx.ToolBar. 
        @param kwargs: Словарь формата:
            {
                Имя инструмента1: True/False,
                ...
            }
            Имя инструмента - имя контрола в проекте wx.FormBuilder.
            Объект инструмента ищется среди атрибутов формы по типу wx.ToolBarToolBase.
        @return: True - все ок, False - какая то ошибка 
        """
        result = True

        if not isinstance(toolbar, wx.ToolBar):
            log.warning(u'Объект %s не типа wx.ToolBar' % str(toolbar))
            return False

        for tool_name, enable in kwargs.items():
            tool = getattr(self, tool_name) if hasattr(self, tool_name) else None
            if tool and isinstance(tool, wx.ToolBarToolBase):
                toolbar.EnableTool(tool.GetId(), enable)
                result = result and True
            else:
                log.warning(u'Инструмент <%s> не найден или не соответствует типу' % tool_name)
                result = result and False

        return result

    def getItemSelectedIdx(self, obj):
        """
        Получить индекс выбранного элемента контрола.
        Т.к. индекс выбранного элемента может возвращать объекты разных
        типов (контролы и события) то:
        Эта функция нужна чтобы не заботиться о названии функции 
        для каждого контрола/события.
        @param obj: Объект контрола или события.  
        @return: Индекс выбранного элемента или -1 если ничего не выбрано.
        """
        if isinstance(obj, wx.ListEvent):
            return obj.m_itemIndex
        elif isinstance(obj, wx.ListCtrl):
            return obj.GetFirstSelected()
        elif isinstance(obj, wx.dataview.DataViewListCtrl):
            return obj.GetSelectedRow()

        log.warning(u'Объект типа <%s> не поддерживается как определитель выбранного элемента контрола' % obj.__class__.__name__)
        return -1

    def selectItem_list_ctrl(self, ctrl=None, item_idx=-1):
        """
        Выбрать элемент контрола списка по индексу.
        @param ctrl: Объект контрола.  
        @return: True - выбор прошел успешно.
        """
        if ctrl is None:
            log.warning(u'Не указан контрол списка для выбора элемента')
            return False

        if isinstance(ctrl, wx.ListCtrl):
            if (0 > item_idx) or (item_idx >= ctrl.GetItemCount()):
                log.warning(u'Не корректный индекс <%d> контрола списка <%s>' % (item_idx, ctrl.__class__.__name__))
                return False
            ctrl.Select(item_idx)
            return True
        elif isinstance(ctrl, wx.dataview.DataViewListCtrl):
            try:
                ctrl.SelectRow(item_idx)
            except:
                log.fatal(u'Ошибка индекса <%d> контрола списка <%s>' % (item_idx, ctrl.__class__.__name__))
                return False
            return True
        else:
            log.warning(u'Объект типа <%s> не поддерживается для выбора элемента контрола' % ctrl.__class__.__name__)
        return False

    def getItemCount(self, obj):
        """
        Получить количество элементов контрола.
        Т.к.  количество элементов контрола может возвращать объекты разных
        типов, то:
        Эта функция нужна чтобы не заботиться о названии функции 
        для каждого контрола.
        @param obj: Объект контрола списка элементов.  
        @return: Количество элементов контрола списка.
        """
        if isinstance(obj, wx.ListCtrl):
            return obj.GetItemCount()
        elif isinstance(obj, wx.dataview.DataViewListCtrl):
            log.warning(u'ВНИМАНИЕ! В этой версии wxPython не реализована функция получения количества элементов для контрола <%s>' % obj.__class__.__name__)
            return 0

        log.warning(u'Объект типа <%s> не поддерживается как определитель количества элементов контрола' % obj.__class__.__name__)
        return 0

    def getLastItemIdx(self, obj):
        """
        Индекс последнего элемента списка.
        @param obj: Объект контрола списка элементов.  
        @return: Индекс последнего элемента контрола списка или -1 если 
            в списке нет элементов.
        """
        item_count = self.getItemCount(obj)
        return item_count - 1

    def setLibImages_ToolBar(self, tool_bar=None, **tools):
        """
        Установить библиотечне картинки в качестве картинок инструментов в wxToolBar.        
        @param tool_bar: Объект wx.ToolBar. 
        @param tools: Словарь соответствий имен инструментов с именами файлов образов библиотеки.
            Например:
                edit_tool = 'document--pencil.png' 
        @return: True/False.
        """
        if not tools:
            # Если словарь соответствий пуст, то ничего не делаем
            return False

        for tool_name, lib_img_filename in tools.items():
            if hasattr(self, tool_name):
                # <wx.Tool>
                tool = getattr(self, tool_name)
                tool_id = tool.GetId()
                bmp = ic_bmp.createLibraryBitmap(lib_img_filename)

                if bmp:
                    if tool_bar is None:
                        tool_bar = tool.GetToolBar()
                    # ВНИМАНИЕ! Для смены образа инструмента не надо использовать
                    # метод инструмента <tool.SetNormalBitmap(bmp)> т.к. НЕ РАБОТАЕТ!
                    # Для этого вызываем метод панели инструметнтов
                    # <toolbar.SetToolNormalBitmap(tool_id, bmp)>
                    tool_bar.SetToolNormalBitmap(tool_id, bmp)
                else:
                    log.warning(u'Не найдена библиотечная картинка <%s>' % lib_img_filename)
            else:
                log.warning(u'Не найден инструмент <%s> панели инструментов' % tool_name)

        if tool_bar:
            tool_bar.Realize()
        else:
            log.warning(u'Не определена панель инструментов wxToolBar')

    def checkAllItems_list_ctrl(self, ctrl, check=True):
        """
        Установить галки всех элементов контрола списка.
        @param check: Вкл./выкл.
        @return: True/False. 
        """
        if isinstance(ctrl, wx.ListCtrl):
            for i in range(ctrl.GetItemCount()):
                ctrl.CheckItem(i, check=check)
            return True

        log.warning(u'Объект типа <%s> не поддерживается вкл./выкл. элментов контрола' % ctrl.__class__.__name__)
        return False

    def getCheckedItems_list_ctrl(self, ctrl):
        """
        Получить список индексов помеченных/отмеченных элементов контрола списка. 
        @param ctrl: Объект контрола списка элементов.  
        @return: Список индексов помеченных элементов контрола списка.
            Либо None в случае ошибки.
        """
        if isinstance(ctrl, wx.ListCtrl):
            result = list()
            for i in range(ctrl.GetItemCount()):
                if ctrl.IsChecked(i):
                    result.append(i)
            return result

        log.warning(u'Объект типа <%s> не поддерживается вкл./выкл. элментов контрола' % ctrl.__class__.__name__)
        return None

    def setAcceleratorTable_win(self, win=None, **key_combine_connections):
        """
        Установить акселераторную таблицу для окна.
        @param win: Объект окна для которого устанавливается акселераторная 
            таблица. Если не определен, то берется self. 
        @param key_combine_connections: Словарь связей комбинаций клавиш 
            с контролами обработки/управления.
            Формат:
                {
                    'комбинация клавиш': идентификатор инструмента/пункта меню,
                    ...
                }
            Например:
                {
                    'CTRL_F1': self.tool1.GetId(), ...
                }
            Пример комбинаций клавиш см. ic/utils/key_combins.py            
        @return: True/False
        """
        if win is None:
            win = self

        used_key_combins = [(key_combine_name,
                             key_combins.get_key_combine(key_combine_name)) for key_combine_name in key_combine_connections.keys()]
        used_key_connections = [(combine_key['mode'],
                                 combine_key['key'],
                                 key_combine_connections[name]) for name, combine_key in used_key_combins]
        win._accelerator_table = wx.AcceleratorTable(used_key_connections)
        win.SetAcceleratorTable(win._accelerator_table)

    def getAcceleratorTable_win(self, win=None):
        """
        Получить акселераторную таблицу окна.
        @param win: Объект окна для которого устанавливается акселераторная 
            таблица. Если не определен, то берется self. 
        @return: Объект акселераторной таблицы если он есть или None если его нет. 
        """
        if win is None:
            win = self

        if hasattr(win, '_accelerator_table'):
            return win._accelerator_table
        else:
            log.warning(u'В объекте <%s> не обнаружена акселераторная таблица' % win.__class__.__name__)
        return None
