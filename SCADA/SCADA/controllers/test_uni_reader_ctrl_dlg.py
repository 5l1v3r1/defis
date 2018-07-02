#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Диалоговая форма тестирования контроллера UniReader.
"""

import wx

from . import test_uni_reader_ctrl_dlg_proto

__version__ = (0, 0, 0, 1)


class icTestUniReaderCtrlDlg(test_uni_reader_ctrl_dlg_proto.icTestUniReaderControllerDlgProto):
    """
    Диалоговая форма тестирования контроллера UniReader.
    """
    def __init__(self, *args, **kwargs):
        """
        Конструктор.
        """
        test_uni_reader_ctrl_dlg_proto.icTestUniReaderControllerDlgProto.__init__(self, *args, **kwargs)

    def onOkButtonClick(self, event):
        """
        Обработчик кнопки <ОК>.
        """
        self.EndModal(wx.ID_OK)
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
    dlg.ShowModal()
