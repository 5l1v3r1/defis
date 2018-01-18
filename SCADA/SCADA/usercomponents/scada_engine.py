#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Компонент движка SCADA системы.
"""

from ic.components import icwidget
from ic.components import icResourceParser as prs

from ic.utils import util
from ic.PropertyEditor import icDefInf

from ic.log import log

from ic.bitmap import ic_bmp

from . import scada_tag
from . import scada_event
from . import scada_alarm

# --- Спецификация ---
SPC_IC_SCADA_ENGINE = {
                       '__parent__': icwidget.SPC_IC_SIMPLE,
                      }


#   Тип компонента
ic_class_type = icDefInf._icUserType

#   Имя класса
ic_class_name = 'icSCADAEngine'

#   Спецификация на ресурсное описание класса
ic_class_spc = {'type': 'SCADAEngine',
                'name': 'default',
                'child': [],
                'activate': True,
                '_uuid': None,

                '__events__': {},
                '__lists__': {},
                '__attr_types__': {icDefInf.EDT_TEXTFIELD: ['description', '_uuid'],
                                   },
                '__parent__': SPC_IC_SCADA_ENGINE,
                }

#   Имя иконки класса, которые располагаются в директории
#   ic/components/user/images
ic_class_pic = ic_bmp.createLibraryBitmap('control_panel.png')
ic_class_pic2 = ic_bmp.createLibraryBitmap('control_panel.png')

#   Путь до файла документации
ic_class_doc = ''
ic_class_spc['__doc__'] = ic_class_doc

#   Список компонентов, которые могут содержаться в компоненте
ic_can_contain = ['SCADATag', 'SCADAEvent', 'SCADAAlarm']

#   Список компонентов, которые не могут содержаться в компоненте, если не определен
#   список ic_can_contain
ic_can_not_contain = None

#   Версия компонента
__version__ = (0, 0, 0, 1)


class icSCADAEngine(icwidget.icSimple):
    """
    Компонент движка SCADA системы.

    @type component_spc: C{dictionary}
    @cvar component_spc: Спецификация компонента.

        - B{type='defaultType'}:
        - B{name='default'}:

    """

    component_spc = ic_class_spc

    def __init__(self, parent, id=-1, component=None, logType=0, evalSpace=None,
                 bCounter=False, progressDlg=None):
        """
        Конструктор базового класса пользовательских компонентов.

        @type parent: C{wx.Window}
        @param parent: Указатель на родительское окно.
        @type id: C{int}
        @param id: Идентификатор окна.
        @type component: C{dictionary}
        @param component: Словарь описания компонента.
        @type logType: C{int}
        @param logType: Тип лога (0 - консоль, 1- файл, 2- окно лога).
        @param evalSpace: Пространство имен, необходимых для вычисления внешних выражений.
        @type evalSpace: C{dictionary}
        @type bCounter: C{bool}
        @param bCounter: Признак отображения в ProgressBar-е. Иногда это не нужно -
            для создания объектов полученных по ссылки. Т. к. они не учтены при подсчете
            общего количества объектов.
        @type progressDlg: C{wx.ProgressDialog}
        @param progressDlg: Указатель на идикатор создания формы.
        """
        component = util.icSpcDefStruct(self.component_spc, component, True)
        icwidget.icSimple.__init__(self, parent, id, component, logType, evalSpace)

        #   По спецификации создаем соответствующие атрибуты (кроме служебных атрибутов)
        lst_keys = [x for x in component.keys() if not x.startswith('__')]

        for key in lst_keys:
            setattr(self, key, component[key])

        #   Создаем дочерние компоненты
        self.childCreator(bCounter, progressDlg)

    def childCreator(self, bCounter=False, progressDlg=None):
        """
        Функция создает объекты, которые содержаться в данном компоненте.
        """
        return prs.icResourceParser(self, self.child, None, evalSpace=self.evalSpace,
                                    bCounter=bCounter, progressDlg=progressDlg)

    def getChildrenTags(self):
        """
        Дочерние теги.
        """
        # Нужно отфильтровать дочерние объекты
        return [child for child in self.component_lst if isinstance(child, scada_tag.icSCADATag)]

    def getChildrenEvents(self):
        """
        Дочерние объекты событий.
        """
        # Нужно отфильтровать дочерние объекты
        return [child for child in self.component_lst if isinstance(child, scada_event.icSCADAEvent)]

    def getChildrenAlarms(self):
        """
        Дочерние объекты аварийных событий.
        """
        # Нужно отфильтровать дочерние объекты
        return [child for child in self.component_lst if isinstance(child, scada_alarm.icSCADAAlarm)]
