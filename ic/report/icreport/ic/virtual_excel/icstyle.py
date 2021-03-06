#!/usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import copy

import icprototype

__version__ = (0, 0, 1, 2)

COLOR_ENUM = ('#000000',)


class icVStyles(icprototype.icVPrototype):
    """
    Стили ячеек.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Styles', 'children': []}
        self._style_dict = {}
        
        # Словарь контрольная сумма содержания стиля:словарь атрибутов стиля
        self._md5_styles_dict = {}
        
        # Максимальный идентификатор стиля (введен для оптимизации)
        self.max_style_id = None
        
    def getMaxStyleID(self):
        if self.max_style_id is None:
            styles_id = self.getStylesID()
            if styles_id:
                self.max_style_id = max(styles_id)
            else:
                self.max_style_id = 's0'
        return self.max_style_id

    def get_style_dict(self):
        """
        Словарь стилей по их идентификаторам.
        """
        return self._style_dict

    def init_style_dict(self):
        """
        Инициализация словаря стилей.
        """
        self._style_dict = dict([(style['ID'], style) for style in self._attributes['children']])
        return self._style_dict

    style_dict = property(get_style_dict)

    def createStyle(self):
        """
        Создать стиль.
        """
        style = icVStyle(self)
        attrs = style.create()

        if self._style_dict is None:
            self.init_style_dict()
        else:
            # Просто добавить стиль с словарь стилей (для увеличения производительности)
            self._style_dict[attrs['ID']] = attrs
        return style

    def getStyle(self, ID_):
        """
        Поиск стиля по идентификатору.
        """
        style = None
        if ID_ in self._style_dict:
            style = icVStyle(self)
            style.set_attributes(self._style_dict[ID_])
        else:
            # Попробовать поискать в списке
            find_style = [style_attr for style_attr in self._attributes['children']
                          if style_attr['name'] == 'Style' and style_attr['ID'] == ID_]
            if find_style:
                style = icVStyle(self)
                style.set_attributes(find_style[0])
                # Блин рассинхронизация произошла со словарем
                self.init_style_dict()

        # Если такой стиль не найден, тогда вернуть стиль по умолчанию
        if style is None and ID_ != 'Default':
            return self.getStyle('Default')
        return style

    def _equalStyleElement(self, StyleElementAttr1_, StyleElementAttr2_):
        """
        Сравнение элементов стилей.
        @return: True - элементы равны, False - не равны.
        """
        if ((StyleElementAttr1_ is None) and (StyleElementAttr2_ is not None)) or \
           ((StyleElementAttr1_ is not None) and (StyleElementAttr2_ is None)):
            return False
            
        attrs1 = dict([item for item in StyleElementAttr1_.items() if item[0] not in icprototype.PROTOTYPE_ATTR_NAMES])
        attrs2 = dict([item for item in StyleElementAttr2_.items() if item[0] not in icprototype.PROTOTYPE_ATTR_NAMES])
        equal = True
        for item in attrs1.items():
            try:
                if item[1] == attrs2[item[0]]:
                    pass
                elif type(item[1]) != type(attrs2[item[0]]):
                    value1 = item[1]
                    if isinstance(value1, bool):
                        value1 = int(value1)
                    value2 = attrs2[item[0]]
                    if isinstance(value2, bool):
                        value2 = int(value2)
                    equal = equal and (str(value1) == str(value2))
                else:
                    equal = False
            except KeyError:
                return False

            if equal is False:
                break

        # Если определены дочерние елементы, то рекурсивно проверить и их
        if equal:
            if ('children' in StyleElementAttr1_ and StyleElementAttr1_['children']) or \
               ('children' in StyleElementAttr2_ and StyleElementAttr2_['children']):

                children1 = StyleElementAttr1_['children']
                children2 = StyleElementAttr2_['children']

                if len(children1) != len(children2):
                    return False

                for i, child1 in enumerate(children1):
                    child2 = children2[i]
                    equal = equal and self._equalStyleElement(child1, child2)

                    if equal is False:
                        break
                
        return equal

    def _compare_style_element(self, element, element_name, style):
        """
        Сравнение елемента стиля.
        """
        if element:
            elements = [el for el in style['children'] if el['name'] == element_name]
            if elements:
                equal = self._equalStyleElement(elements[0], element)
            else:
                equal = False
        else:
            equal = True
        return equal

    def _compare_style_elements(self, style,
                                alignment=None,
                                borders=None, font=None, interior=None,
                                number_format=None):
        """
        Сравнение элементов стиля.
        """
        equal_align = self._compare_style_element(alignment, 'Alignment', style)
        equal_border = self._compare_style_element(borders, 'Borders', style)
        equal_font = self._compare_style_element(font, 'Font', style)
        equal_interior = self._compare_style_element(interior, 'Interior', style)
        equal_n_fmt = self._compare_style_element(number_format, 'NumberFormat', style)
        return equal_align and equal_border and equal_font and equal_interior and equal_n_fmt

    def findStyle(self, alignment=None,
                  borders=None, font=None, interior=None,
                  number_format=None):
        """
        Поиск стиля по его содержанию.
        """
        find_style = None

        md5_style = self._calcMD5StyleAttr(alignment, borders, font, interior, number_format)

        find_result = md5_style in self._md5_styles_dict
        if not find_result:
            # Надо поискать стиль
            for i in range(len(self._attributes['children'])):
                style = self._attributes['children'][-i]
                # Если количество элементов стиля не совпадает с количеством
                # искомых элементов, то эти стили не равны
                if len(style['children']) != len([element for element in [alignment, borders, font, interior,
                                                                          number_format] if element is not None]):
                    find_result = False
                    continue
            
                find_result = self._compare_style_elements(style, alignment, borders, font, interior, number_format)

                if find_result:
                    find_style = style
                    break
        else:
            # Искомый стиль есть в хеше
            find_style = self._md5_styles_dict[md5_style]

        if find_result:
            style = icVStyle(self)
            if find_style:
                style.set_attributes(find_style)
                # Прописать в хэшэ
                self._md5_styles_dict[md5_style] = find_style
            return style
        return None

    def _getMD5ElementStr(self, Element_):
        """
        Представить в строковом виде элемент без дополнительных полей.
        """
        return str(dict([(key, Element_[key]) for key in Element_.keys() \
                         if key not in icprototype.PROTOTYPE_ATTR_NAMES]))
        
    def _getMD5AlignmentStr(self, Style_):
        """
        Выравнивание в строковом представлении (для вычисления контрольной суммы).
        """
        align = [element for element in Style_['children'] if element['name'] == 'Alignment']
        if align:
            return self._getMD5ElementStr(align[0])
        return ''        
        
    def _getMD5BordersStr(self, Style_):
        """
        Обрамление в строковом представлении (для вычисления контрольной суммы).
        """
        borders = [element for element in Style_['children'] if element['name'] == 'Borders']
        if borders:
            borders_str = ''
            for border in borders[0]['children']:
                borders_str += self._getMD5ElementStr(border)
            return borders_str
        return ''        

    def _getMD5FontStr(self, Style_):
        """
        Шрифт в строковом представлении (для вычисления контрольной суммы).
        """
        font = [element for element in Style_['children'] if element['name'] == 'Font']
        if font:
            return self._getMD5ElementStr(font[0])
        return ''        
        
    def _getMD5InteriorStr(self, Style_):
        """
        Интерьер в строковом представлении (для вычисления контрольной суммы).
        """
        interior = [element for element in Style_['children'] if element['name'] == 'Interior']
        if interior:
            return self._getMD5ElementStr(interior[0])
        return ''        
        
    def _getMD5NumberFormatStr(self, Style_):
        """
        Формат чисел в строковом представлении (для вычисления контрольной суммы).
        """
        num_fmt = [element for element in Style_['children'] if element['name'] == 'NumberFormat']
        if num_fmt:
            return self._getMD5ElementStr(num_fmt[0])
        return ''        
    
    def _calcMD5StyleAttr(self, alignment=None,
                          borders=None, font=None, interior=None,
                          number_format=None):
        """
        Вычислить контрольную сумму по атрибутам.
        """
        new_style_attr = {'children': []}
        if alignment:
            alignment['name'] = 'Alignment'
            new_style_attr['children'].append(alignment)
        if borders:
            borders['name'] = 'Borders'
            new_style_attr['children'].append(borders)
        if font:
            font['name'] = 'Font'
            new_style_attr['children'].append(font)
        if interior:
            interior['name'] = 'Interior'
            new_style_attr['children'].append(interior)
        if number_format:
            number_format['name'] = 'NumberFormat'
            new_style_attr['children'].append(number_format)
        return self._getMD5Style(new_style_attr)            
        
    def _getMD5Style(self, Style_):
        """
        Контрольная сумма содержания стиля.
        """
        style_str = ''
        # Alignment
        style_str += self._getMD5AlignmentStr(Style_)
        # Borders
        style_str += self._getMD5BordersStr(Style_)
        # Font
        style_str += self._getMD5FontStr(Style_)
        # Interior
        style_str += self._getMD5InteriorStr(Style_)
        # NumberFormat
        style_str += self._getMD5NumberFormatStr(Style_)
        return md5.new(style_str).hexdigest()        

    def _delMD5Style(self, MD5Style_):
        """
        Удалить стиль из кеша.
        """
        if MD5Style_ in self._md5_styles_dict:
            del self._md5_styles_dict[MD5Style_]
            
    def _isMD5StyleID(self, StyleID_):
        """
        Есть ли в кеше стиль с таким идентификатором?
        @return: Возвращает контрольную сумму стиля в кеше или None,
            если стиль не найден.
        """
        result = [i_style for i_style in self._md5_styles_dict.items() if i_style[1]['ID'] == StyleID_]
        if result:
            return result[0][0]
        return None
        
    def getStylesID(self):
        """
        Список идентификаторов стилей.
        """
        return [style['ID'] for style in self._attributes['children']]

    def _createDefaultStyle(self):
        """
        Создать стиль по умолчанию, если его нет.
        @return: Возвращает True-если стиль Default создан,
        и False-если нет.
        """
        styles_id = [style_element['ID'] for style_element in self._attributes['children']]
        if 'Default' not in styles_id:
            default_style = self.createStyle()
            default_style.setID('Default')
            default_style.setAttrs(alignment={'Vertical': 'Bottom'},
                                   font={'FontName': 'Arial Cyr', 'CharSet': 204})
            return True
        return False
    
    def clearUnUsedStyles(self):
        """
        Удаление не используемых стилей.
        @return: Возвращает список идентификаторов удаленных стилей.
        """
        # Создать стиль по умолчанию если он создан
        self._createDefaultStyle()
        
        del_styles_id = []
        styles_id = self.getStylesID()
        # Определение идентификаторов используемых стилей
        used_styles_id = ['Default']
        work_sheets = [element for element in self._parent._attributes['children'] if element['name'] == 'Worksheet']
        for work_sheet in work_sheets:
            tables = [element for element in work_sheet['children'] if element['name'] == 'Table']
            for table in tables:
                if 'StyleID' in table:
                    style_id = table['StyleID']
                    if style_id not in used_styles_id:
                        used_styles_id.append(style_id)
                for tab_element in table['children']:
                    if 'StyleID' in tab_element:
                        style_id = tab_element['StyleID']
                        if style_id not in used_styles_id:
                            used_styles_id.append(style_id)
                    if tab_element['name'] == 'Row':
                        for cell in tab_element['children']:
                            if 'StyleID' in cell:
                                style_id = cell['StyleID']
                                if style_id not in used_styles_id:
                                    used_styles_id.append(style_id)
                                    
        for style_id in styles_id:
            if style_id not in used_styles_id:
                result = self.delStyleByID(style_id)
                if result:
                    del_styles_id.append(style_id)
                
        return del_styles_id
                
    def delStyleByID(self, ID_):
        """
        Удалить стиль по идентификатору.
        """
        try:
            style_idx = self.getStylesID().index(ID_)
        except ValueError:
            return False
        
        if style_idx >= 0:
            del self._attributes['children'][style_idx]
            return True
        return False


class icVStyle(icprototype.icVPrototype):
    """
    Стиль ячеек.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        # self._attributes = dict(DEFAULT_STYLE_ATTR.items()+[('ID', self.newID())])
        self._attributes = {'ID': self.newID(), 'name': 'Style', 'children': []}

    def getID(self):
        """
        Идентификатор стиля.
        """
        return self._attributes['ID']
    
    def setID(self, IDName_):
        """
        Идентификатор стиля.
        @param IDName_: Имя идентификатора.
        """
        self._attributes['ID'] = str(IDName_)
    
    def newID(self):
        """
        Генерация нового идетификатора стиля.
        """
        max_style_id = self._parent.getMaxStyleID()
        max_str_i = ''.join([symb for symb in max_style_id if symb.isdigit()])
        i = int(max_str_i)+1 if max_str_i else 0
        new_id = 's' + str(i)

        # Запомнить максимальный идентификатор стиля
        self._parent.max_style_id = new_id
        return new_id

    def newID_depricated(self):
        """
        Генерация нового идетификатора стиля.
        """
        styles_id = self._parent.getStylesID()
        i = 1
        while ('s'+str(i)) in styles_id:
            i += 1
        
        return 's'+str(i)

    def _delAttr(self, name):
        """
        Удалить из содержания стиля атрибут по имени.
        """
        try:
            idx = [attr['name'] for attr in self._attributes['children']].index(name)
        except ValueError:
            idx = -1
        if idx >= 0:
            del self._attributes['children'][idx]
        return self._attributes
    
    def setAttrs(self, alignment=None,
                 borders=None, font=None, interior=None,
                 number_format=None):
        """
        Заполнение содержания стиля.
        """
        self._attributes['children'] = []
        return self.updateAttrs(alignment, borders, font, interior, number_format)
        
    def updateAttrs(self, alignment=None,
                    borders=None, font=None, interior=None,
                    number_format=None, update_attrs=None):
        """
        Заполнение содержания стиля.
        """
        if update_attrs is None:
            style_attrs = self._attributes['children']
        else:
            style_attrs = update_attrs
            
        if alignment:
            self._delAttr('Alignment')
            alignment['name'] = 'Alignment'
            style_attrs.append(alignment)
        if borders:
            self._delAttr('Borders')
            borders['name'] = 'Borders'
            style_attrs.append(borders)
        if font:
            self._delAttr('Font')
            font['name'] = 'Font'
            style_attrs.append(font)
        if interior:
            self._delAttr('Interior')
            interior['name'] = 'Interior'
            style_attrs.append(interior)
        if number_format:
            self._delAttr('NumberFormat')
            number_format['name'] = 'NumberFormat'
            style_attrs.append(number_format)
        self._attributes['children'] = style_attrs
        
        if self._parent:
            md5_attrs = self._parent._isMD5StyleID(self.getID())
            if md5_attrs:
                self._parent._delMD5Style(md5_attrs)
        return self._attributes

    def getAttrs(self):
        """
        Содержание стиля.
        @return: Словарь внутреннего содержания стиля.
        """
        attrs = {}
        for element in self._attributes['children']:
            if element['name'] == 'Alignment':
                attrs['alignment'] = element
            elif element['name'] == 'Borders':
                attrs['borders'] = element
            elif element['name'] == 'Font':
                attrs['font'] = element
            elif element['name'] == 'Interior':
                attrs['interior'] = element
            elif element['name'] == 'NumberFormat':
                attrs['number_format'] = element
        return attrs
        
    def createAlignment(self):
        """
        Создать выравнивание.
        """
        align = icVAlignment(self)
        attrs = align.create()
        return align

    def createBorders(self):
        """
        Создать обрамление.
        """
        borders = icVBorders(self)
        attrs = borders.create()
        return borders

    def createFont(self):
        """
        Создать шрифт.
        """
        font = icVFont(self)
        attrs = font.create()
        return font

    def createInterior(self):
        """
        Создать заливку.
        """
        interior = icVInterior(self)
        attrs = interior.create()
        return interior

    def createNumberFormat(self):
        """
        Создать формат.
        """
        fmt = icVNumberFormat(self)
        attrs = fmt.create()
        return fmt

HORIZONTAL_ENUM = ('Automatic', 'Left', 'Center', 'Right', 'Fill', 'Justify',
                   'CenterAcrossSelection', 'Distributed', 'JustifyDistributed')
VERTICAL_ENUM = ('Automatic', 'Top', 'Center', 'Bottom', 'Justify',
                 'Distributed', 'JustifyDistributed')
READINGORDER_ENUM = ('RightToLeft', 'LeftToRight', 'Context')

ALIGNMENT_SPC = {'Horizontal': HORIZONTAL_ENUM[0],
                 'Indent': 0,
                 'ReadingOrder': READINGORDER_ENUM[-1],
                 'Rotate': 0,
                 'ShrinkToFit': False,
                 'Vertical': VERTICAL_ENUM[0],
                 'VerticalText': False,
                 'WrapText': False}


class icVAlignment(icprototype.icVPrototype):
    """
    Выравнивание.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Alignment'}


class icVBorders(icprototype.icVPrototype):
    """
    Обрамление.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Borders', 'children': []}

POSITION_ENUM = ('Left', 'Top', 'Right', 'Bottom', 'DiagonalLeft', 'DiagonalRight')
LINESTYLE_ENUM = ('None', 'Continuous', 'Dash', 'Dot', 'DashDot', 'DashDotDot',
                  'SlantDashDot', 'Double')

BORDER_SPC = {'Position': POSITION_ENUM[0],
              'Color': COLOR_ENUM[0],
              'LineStyle': LINESTYLE_ENUM[0],
              'Weight': 0
              }


class icVBorder(icprototype.icVPrototype):
    """
    Обрамление.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Border'}

UNDERLINE_ENUM = ('None', 'Single', 'Double',
                  'SingleAccounting', 'DoubleAccounting')
VERTICALALIGN_ENUM = ('None', 'Subscript', 'Superscript')

FAMILY_ENUM = ('Automatic', 'Decorative', 'Modern', 'Roman', 'Script', 'Swiss')

FONT_SPC = {'Bold': False,
            'Color': COLOR_ENUM[0],
            'FontName': 'Arial',
            'Italic': False,
            'Outline': False,
            'Shadow': False,
            'Size': 10,
            'StrikeThrogh': False,
            'Underline': UNDERLINE_ENUM[0],
            'VerticalAlign': VERTICALALIGN_ENUM[0],
            'CharSet': 0,
            'Family': FAMILY_ENUM[0]
            }


class icVFont(icprototype.icVPrototype):
    """
    Шрифт.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Font'}

PATTERN_ENUM = ('None', 'Solid',
                'Gray75', 'Gray50', 'Gray25', 'Gray125', 'Gray0625',
                'HorizStripe', 'VertStripe', 'ReverseDiagStripe', 'DiagStripe',
                'DiagCross', 'ThickDiagCross', 'ThinHorzStripe', 'ThinVertStripe',
                'ThinReverseDiagStripe', 'ThinDiagStripe',
                'ThinHorzCross', 'ThinDiagCross')

INTERIOR_SPC = {'Color': COLOR_ENUM[0],
                'Pattern': PATTERN_ENUM[1],
                'PatternColor': COLOR_ENUM[0]
                }


class icVInterior(icprototype.icVPrototype):
    """
    Заливка.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'Interior'}

FORMAT_ENUM = ('General', 'General Number', 'General Date',
               'Long Date', 'Medium Date', 'Short Date',
               'Long Time', 'Medium Time', 'Short Time',
               'Currency', 'Euro Currency', 'Fixed', 'Stadart',
               'Percent', 'Scientific', 'Yes/No', 'True/False', 'On/Off')

NUMBERFORMAT_SPC = {'Format': FORMAT_ENUM[0]}
    

class icVNumberFormat(icprototype.icVPrototype):
    """
    Формат.
    """
    def __init__(self, parent, *args, **kwargs):
        """
        Конструктор.
        """
        icprototype.icVPrototype.__init__(self, parent, *args, **kwargs)
        self._attributes = {'name': 'NumberFormat'}
