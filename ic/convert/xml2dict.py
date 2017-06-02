#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Модуль конвертора файлов Excel в xml формате в словарь.
"""

# Подключение библиотек
import sys

from xml.sax import xmlreader
import xml.sax.handler

# Описания функций
DEFAULT_XML_TAG = 'Excel'

TAG_KEY = '__tag__'
CHILDREN_KEY = '__children__'
VALUE_KEY = '__value__'

__version__ = (0, 0, 1, 4)


def XmlFile2Dict(XMLFileName_, encoding='utf-8'):
    """
    Функция конвертации файлов Excel в xml формате в словарь Python.
    @param XMLFileName_: Имя xml файла. 
    @return: Функция возвращает заполненный словарь, 
        или None в случае ошибки.
    """
    xml_file = None
    try:
        xml_file = open(XMLFileName_, 'r')

        input_source = xmlreader.InputSource()
        input_source.setByteStream(xml_file)

        xml_reader = xml.sax.make_parser()
        xml_parser = icXML2DICTReader(encoding=encoding)
        xml_reader.setContentHandler(xml_parser)

        # включаем опцию namespaces
        xml_reader.setFeature(xml.sax.handler.feature_namespaces, 1)
        xml_reader.parse(input_source)
        xml_file.close()

        return xml_parser.getData()
    except:
        if xml_file:
            xml_file.close()
        info = str(sys.exc_info()[1])
        print(u'Error read file <%s> : %s.' % (XMLFileName_, info))
        return None


# Описания классов
class icXML2DICTReader(xml.sax.handler.ContentHandler):
    """
    Класс анализатора файлов Excel-xml формата.
    """
    def __init__(self, encoding='utf-8', *args, **kws):
        """
        Конструктор.
        """
        xml.sax.handler.ContentHandler.__init__(self, *args, **kws)

        # Выходной словарь
        self._data = {TAG_KEY: DEFAULT_XML_TAG, CHILDREN_KEY: []}
        # Текущий заполняемый узел
        self._cur_path = [self._data]

        # Текущее анализируемое значение
        self._cur_value = None

        # Кодировка
        self.encoding = encoding

    def setName(self, name):
        self._data[TAG_KEY] = name

    def getName(self):
        return self._data[TAG_KEY]

    def getData(self):
        """
        Выходной словарь.
        """
        return self._data

    def _eval_value(self, value):
        """
        Попытка приведения типов данных.
        """
        if type(value) is unicode:
            value = value.encode(self.encoding)
            
        try:
            # Попытка приведения типа
            return eval(value)
        except:
            # Скорее всего строка
            return value
        
    def characters(self, content):
        """
        Данные.
        """
        if content.strip():
            if self._cur_value is None:
                self._cur_value = ''
            self._cur_value += content.encode(self.encoding)

    def startElementNS(self, name, qname, attrs):
        """
        Разбор начала тега.
        """
        # Имя элемента задается кортежем
        if type(name) is tuple:

            # Имя элемента
            element_name = name[1].encode(self.encoding)

            # Создать структуру,  соответствующую элементу
            self._cur_path[-1][CHILDREN_KEY].append({TAG_KEY: element_name, CHILDREN_KEY: []})
            self._cur_path.append(self._cur_path[-1][CHILDREN_KEY][-1])
            cur_node = self._cur_path[-1]

            # Имена параметров
            element_qnames = attrs.getQNames()
            if element_qnames:
                # Разбор параметров элемента
                for cur_qname in element_qnames:
                    # Имя параметра
                    element_qname = attrs.getNameByQName(cur_qname)[1].encode(self.encoding)
                    # Значение параметра
                    element_value = attrs.getValueByQName(cur_qname).encode(self.encoding)
                    cur_node[element_qname] = element_value

    def endElementNS(self, name, qname): 
        """
        Разбор закрывающего тега.
        """
        # Сохранить проанализированное значение
        if self._cur_value is not None:
            self._cur_path[-1][VALUE_KEY] = self._cur_value
            self._cur_value = None

        del self._cur_path[-1]


def default_test():
    """
    Тестовая функция.
    """
    rep_file = None
    xml_file = None
    xml_file = open(sys.argv[1], 'r')

    input_source = xmlreader.InputSource()
    input_source.setByteStream(xml_file)
    xml_reader = xml.sax.make_parser()
    xml_parser = icXML2DICTReader()
    xml_reader.setContentHandler(xml_parser)
    # включаем опцию namespaces
    xml_reader.setFeature(xml.sax.handler.feature_namespaces, 1)
    xml_reader.parse(input_source)
    xml_file.close()


def create_pkl_files_test():
    """
    Создание выходной структуры в файле pickle.
    """
    import pickle, time, cPickle
    
    start_time = time.time()
    print(u'START Pickle file create test')
    
    data = XmlFile2Dict('./testfiles/SF02.xml')
    print(u'READ ... ok Time(s): <%s>' % (time.time()-start_time))

    start_time = time.time()
    f_out = open('./testfiles/SF02.txt', 'wt')
    f_out.write(str(data))
    f_out.close()
    print(u'WRITE text ... ok Time(s): <%s>' % (time.time()-start_time))
    
    start_time = time.time()
    f_out = open('./testfiles/SF02.pkl', 'w')
    pkl = pickle.Pickler(f_out)
    pkl.dump(data)
    f_out.close()
    print(u'WRITE pickle ... ok Time(s): <%s>' % (time.time()-start_time))
    
    start_time = time.time()
    f_out = open('./testfiles/SF02.cpk', 'w')
    pkl = cPickle.dump(data, f_out)
    f_out.close()
    print(u'WRITE cPickle ... ok Time(s): <%s>' % (time.time()-start_time))


def fb_prj_test():
    """
    Тестирование чтения файла проекта wxFormBuilder.
    """
    fb_prj_filename = './testfiles/tst.fbp'

    result = XmlFile2Dict(fb_prj_filename)
    result[TAG_KEY] = 'wxFormBuilderProject'
    from ic.utils import ic_res
    ic_res.SaveResourceText('./testfiles/debug.log', result, True)
    cmd = 'gedit ./testfiles/debug.log'
    import os
    os.system(cmd)


if __name__ == '__main__':
    fb_prj_test()
