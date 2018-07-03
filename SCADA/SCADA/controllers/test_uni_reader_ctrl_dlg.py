#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Диалоговая форма тестирования контроллера UniReader.
"""

import wx

from . import test_uni_reader_ctrl_dlg_proto
from ic.engine import form_manager
from ic.log import log
from ic.dlg import ic_dlg

__version__ = (0, 0, 1, 1)


class icTestUniReaderCtrlDlg(test_uni_reader_ctrl_dlg_proto.icTestUniReaderControllerDlgProto,
                             form_manager.icFormManager):
    """
    Диалоговая форма тестирования контроллера UniReader.
    """
    def __init__(self, *args, **kwargs):
        """
        Конструктор.
        """
        test_uni_reader_ctrl_dlg_proto.icTestUniReaderControllerDlgProto.__init__(self, *args, **kwargs)

        self.tags = None

        self.controller = None

    def set_tags(self, tags=None):
        """
        Установить проверяемые теги.
        @param tags: Словарь тегов в формате:
            {'имя тега': 'адрес тега', ... }
        """
        if isinstance(tags, dict):
            self.tags = tags
        else:
            self.tags = dict()

    def set_controller(self, controller=None):
        """
        Установить контроллер.
        @param controller: Объект контроллера.
        """
        self.controller = controller
        if self.controller:
            # Сразу установить теги если контроллер определен
            self.set_tags(controller.getTags())

    def init_img(self):
        """
        Инициализация образов.
        """
        pass

    def init_ctrl(self):
        """
        Инициализация контролов.
        """
        self.setColumns_list_ctrl(self.tags_listCtrl, (dict(label=u'Тег', width=150),
                                                       dict(label=u'Адрес', width=400),
                                                       dict(label=u'Значение', width=400)))

    def init(self):
        """
        Общая функция инициализации окна.
        """
        self.init_img()
        self.init_ctrl()

    def set_tags(self, **tags):
        """
        Устанвить теги.
        @param tags: Словарь тегов в формате:
            {'имя тега': 'адрес тега', ... }
        @return: True/False.
        """
        # Сначала очистить список
        self.clear_ctrl_value(self.tags_listCtrl)

        if tags:
            tag_names = tags.keys()
            tag_names.sort()

            tag_values = self.read_tags(**tags)
            if tag_values is not None:
                rows = [(tag_name,
                         tags[tag_name],
                         tag_values[tag_name]) for tag_name in tag_names]
                self.setRows_list_ctrl(self.tags_listCtrl,
                                       rows=rows)

    def read_tags(self, **tags):
        """
        Прочитать теги из контроллера.
        @param tags: Словарь тегов в формате:
            {'имя тега': 'адрес тега', ... }
        @return: Словарь прочитанных значений:
            {'имя тега': 'значение тега', ... }
            Либо None в случае ошибки.
        """
        if self.controller is None:
            msg = u'Не определен объект контроллера для тестирования'
            log.warning(msg)
            ic_dlg.icWarningBox(u'ОШИБКА', msg)
            return None

        return self.controller.read_tags(**tags)

    def onOkButtonClick(self, event):
        """
        Обработчик кнопки <ОК>.
        """
        self.EndModal(wx.ID_OK)
        event.Skip()

    def onUpdateToolClicked(self, event):
        """
        Обработчик инструмента <Обновить>.
        """
        self.set_tags(**self.tags)
        event.Skip()

    def onAddToolClicked(self, event):
        """
        Обработчик инструмента <Добавить тег>
        """
        tag_name = self.tag_textCtrl.GetValue()
        tag_address = self.address_textCtrl.GetValue()

        if tag_name not in self.tags:
            self.tags[tag_name] = tag_address
            self.set_tags(**self.tags)
        else:
            msg = u'Тег <%s> уже есть в списке' % tag_name
            log.warning(msg)
            ic_dlg.icWarningBox(u'ОШИБКА', msg)

        event.Skip()

    def onDelToolClicked(self, event):
        """
        Обработчик инструмента <Удалить тег>
        """
        selected_idx = self.getItemSelectedIdx(self.tags_listCtrl)
        if selected_idx >= 0:
            tag_name = self.tags_listCtrl.GetItemText(selected_idx)
            log.debug(u'Удален тег <%s>' % tag_name)
            del self.tags[tag_name]
            self.set_tags(**self.tags)
        event.Skip()


def view_test_uni_reader_ctrl_dlg(parent=None, controller=None):
    """
    Функция отображения диалогового окна тестирования контроллера Uni Reader.
    @param parent: Родительское окно.
    @param controller: Объект контроллера.
    """
    if parent is None:
        app = wx.GetApp()
        parent = app.GetTopWindow()

    dlg = icTestUniReaderCtrlDlg(parent=parent)
    dlg.set_controller(controller)
    dlg.init()
    dlg.ShowModal()
