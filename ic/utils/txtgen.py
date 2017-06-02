#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Генератор текста по контексту. 
В качестве контекста может выступать любая словарная структура.
Простой аналог генератора страниц в Django.
Синтаксис такой же, что в дальнейшем позволит испльзовать 
Django в качестве генератора.
"""

import re

from ic import config
from ic.log import log

__version__ = (0, 0, 1, 4)

VAR_PATTERN = r'(\{\{.*?\}\})'


def gen(sTxt, dContext=None):
    """
    Генерация текста.
    @param sTxt: Tекст шаблона.
    @param dContext. Контекст.
        В качестве контекста может выступать любая словарная структура.
        По умолчанию контекст - локальное пространство имен модуля config.
    @return: Сгенерированный текст.
    """
    if dContext is None:
        dContext = dict()
        for name in config.__dict__.keys():
            dContext[name] = config.get_cfg_var(name)
    return auto_replace(sTxt, dContext)


def _getVarName(sPlace):
    """
    Определить имя переменной замены.
    """
    return sPlace.replace('{', '').replace('}', '').strip()


def auto_replace(sTxt, dReplaces=None):
    """
    Запуск автозамен из контекста.
    @param sTxt: Редактируемый текст.
    @param dReplaces: Словарь замен, если None, то берется locals().
    @return: Возвращается отредактированный текст или None в 
        случае возникновения ошибки.
    """
    if dReplaces is None:
        dReplaces = locals()
            
    if sTxt and (dReplaces is not None):
            
        replace_places = re.findall(VAR_PATTERN, sTxt)
        replaces = dict([(place, dReplaces.get(_getVarName(place), '')) for place in replace_places])
            
        for place, value in replaces.items():
            log.info('INFO. Replace %s to %s' % (place, value))
            if type(value) not in (str, unicode):
                value = str(value)
            sTxt = sTxt.replace(place, value)
            
        return sTxt
        
    return None
    

if __name__ == '__main__':
    log.init(config)
    txt = u'Тестовые замены {{ DEBUG_MODE }}'
    print(gen(txt))
