#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Компонент движка SCADA системы.

Основной функцией SCADA движка является сканирование контроллеров
и обновление значений тегов, которые содержатся в движке.
Также происходит проверка и выполнение событий и аварий.
"""

import time
import thread

from ic.components import icwidget
from ic.components import icResourceParser as prs

from ic.utils import util
from ic.PropertyEditor import icDefInf

from ic.log import log

from ic.bitmap import ic_bmp

# from . import scada_tag
from . import int_tag
from . import float_tag
from . import bool_tag
from . import str_tag
from . import datetime_tag

from . import scada_event
from . import scada_alarm

# --- Спецификация ---
SPC_IC_SCADA_ENGINE = {'__parent__': icwidget.SPC_IC_SIMPLE,
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
ic_class_pic = ic_bmp.createLibraryBitmap('recycle.png')
ic_class_pic2 = ic_bmp.createLibraryBitmap('recycle.png')

#   Путь до файла документации
ic_class_doc = ''
ic_class_spc['__doc__'] = ic_class_doc

#   Список компонентов, которые могут содержаться в компоненте
ic_can_contain = ['IntSCADATag', 'FloatSCADATag', 'BoolSCADATag', 'StrSCADATag', 'DateTimeSCADATag',
                  'SCADAEvent', 'SCADAAlarm']

#   Список компонентов, которые не могут содержаться в компоненте, если не определен
#   список ic_can_contain
ic_can_not_contain = None

#   Версия компонента
__version__ = (0, 0, 1, 1)


# Классы тегов
TAG_CLASSES = (int_tag.icIntSCADATag, float_tag.icFloatSCADATag, bool_tag.icBoolSCADATag,
               str_tag.icStrSCADATag, datetime_tag.icDateTimeSCADATag)


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

        # Словарь классов сканирования для обработки в цикле
        # {паспорт класс сканирования: объект класса сканирования,...}
        self._scan_classes = dict()
        # Словарь cканируемых тегов для обработки в цикле
        # {паспорт класс сканирования: [объект сканируемого тега,...],..}
        self._scan_tags = dict()
        # Словарь обрабатываемых событий для обработки в цикле
        # {паспорт класс сканирования: [объект события,...],...}
        self._scan_events = dict()
        # Словарь обрабатываемых аварий для обработки в цикле
        # {паспорт класс сканирования: [объект аварии,...],...}
        self._scan_alarms = dict()

        # Признак запущенного цикла обработки
        self.is_running = False
        # Флаг-команда выхода из цикла обработки
        self.exit_run =True

        # Закешированные списки внутренних объектов
        self._tags_cache = None
        self._events_cache = None
        self._alarms_cache = None

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
        if self._tags_cache is None:
            # Нужно отфильтровать дочерние объекты
            self._tags_cache = [child for child in self.component_lst
                                if any([isinstance(child, tag_class) for tag_class in TAG_CLASSES])]
        return self._tags_cache

    def getChildrenEvents(self):
        """
        Дочерние объекты событий.
        """
        if self._events_cache is None:
            # Нужно отфильтровать дочерние объекты
            self._events_cache = [child for child in self.component_lst if isinstance(child, scada_event.icSCADAEvent)]
        return self._events_cache

    def getChildrenAlarms(self):
        """
        Дочерние объекты аварийных событий.
        """
        if self._alarms_cache is None:
            # Нужно отфильтровать дочерние объекты
            self._alarms_cache = [child for child in self.component_lst if isinstance(child, scada_alarm.icSCADAAlarm)]
        return self._alarms_cache

    def findTag(self, tag_name):
        """
        Найти объект тега по имени.
        @param tag_name: Имя тега.
        @return: Объект тега или None в случае ошибки.
        """
        tags = self.getChildrenTags()
        for tag in tags:
            if tag.name == tag_name:
                return tag
        return None

    def _init_scan_objects(self, obj_list, scan_obj_dict=None):
        """
        Инициализация сканируемых объектов.
        @param obj_list: Список объектов сканирования.
        @param scan_obj_dict: Словарь сканирумых объектов.
        @return: Заполненный словарь сканируемых объектов.
        """
        if scan_obj_dict is None:
            scan_obj_dict = dict()

        for obj in obj_list:
            scan_class_psp = obj.getScanClassPsp()
            if scan_class_psp not in self._scan_classes:
                self._scan_classes[scan_class_psp] = obj.getScanClass()
            if scan_class_psp not in scan_obj_dict:
                scan_obj_dict[scan_class_psp] = list()
            scan_obj_dict[scan_class_psp].append(obj)
        return scan_obj_dict

    def init_scan_objects(self):
        """
        Инициализация сканируемых объектов.
        @return: True/False.
        """
        self._scan_classes = dict()

        # Теги
        self._scan_tags = self._init_scan_objects(self.getChildrenTags())
        # События
        self._scan_events = self._init_scan_objects(self.getChildrenEvents())
        # Аварии
        self._scan_alarms = self._init_scan_objects(self.getChildrenAlarms())

    def start(self):
        """
        Запуск основного цикла обработки тегов.
        @return: True/False.
        """
        self.init_scan_objects()

        self.exit_run = False
        thread.start_new(self.run, ())
        return True

    def stop(self):
        """
        Остановка основного цикла обработки тегов.
        @return: True/False.
        """
        self.exit_run = True
        return True

    def isRunning(self):
        """
        Признак запущенного цикла обработки.
        @return: True/False.
        """
        return self.is_running

    def run(self):
        """
        Функция основного цикла обработки.
        """
        self.is_running = True
        while not self.exit_run:
            start_tick = time.time()

            scan_classes_psp = self.get_active_scan_classes_psp(start_tick)

            # Подготовка тегов для чтения
            read_tags = self.get_refreshable_tags(*scan_classes_psp)
            # Чтение тегов
            self.read_tags(*read_tags)

            # События
            self.do_events(*scan_classes_psp)

            # Аварии
            self.do_alarms(*scan_classes_psp)

        self.is_running = False

    def get_active_scan_classes_psp(self, ctrl_tick):
        """
        Список паспортов классов сканирования, которые необходимо обновить.
        @param ctrl_tick: Контрольное значение времени,
            для определения необходимости обработки.
        @return: Список паспортов классов сканирования.
        """
        return [scan_class_psp for scan_class_psp, scan_class in self._scan_classes.items() if scan_class.isOverTick(ctrl_tick)]

    def get_refreshable_tags(self, *scan_classes_psp):
        """
        Список всех тегов, которые пора прочитать/обновить значения.
        @param scan_classes_psp: Список паспортов классов сканирования,
            которые необходимо обновить.
        @return: Список тегов, которые необходимо обновить/прочитать из источника данных.
        """
        read_tags = list()
        for scan_class_psp in scan_classes_psp:
            tags = self._scan_tags.get(scan_class_psp, list())
            read_tags += tags
        return read_tags

    def read_tags(self, *tags):
        """
        Запустить процедуру чтение тегов.
        @param tags: Список читаемх тегов.
        @return: True/False.
        """
        if not tags:
            log.warning(u'Не определен список тегов для чтения')
            return False

        # Подготовка списка узлов
        tag_nodes = [tag.getNode() for tag in tags]
        nodes = list()
        for tag_node in tag_nodes:
            if tag_node not in nodes:
                nodes.append(tag_node)

        # Подготовка списка тегов
        node_tags = [list() for node in nodes]
        for tag in tags:
            tag_node = tag.getNode()
            i_node = nodes.index(tag_node)
            node_tags[i_node].append(tag)

        # Запустить процедуру чтения данных
        for i, node in enumerate(nodes):
            node.readTags(node_tags[i])

        return True

    def do_events(self, *scan_classes_psp):
        """
        Обработка событий.
        @param scan_classes_psp: Список паспортов классов сканирования,
            которые необходимо обновить.
        @return: True/False.
        """
        for scan_class_psp in scan_classes_psp:
            events = self._scan_events.get(scan_class_psp, list())
            for event in events:
                event.do()
        return True

    def do_alarms(self, *scan_classes_psp):
        """
        Обработка аварий.
        @param scan_classes_psp: Список паспортов классов сканирования,
            которые необходимо обновить.
        @return: True/False.
        """
        # for scan_class_psp in scan_classes_psp:
        #     alarms = self._scan_alarms.get(scan_class_psp, list())
        #     for alarm in alarms:
        #         alarm.do()
        return True