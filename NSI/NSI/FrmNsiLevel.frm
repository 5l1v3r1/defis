{'FrmNsiLevel': {'style': 0, 'activate': u'1', 'prim': u'', 'name': u'FrmNsiLevel', 'alias': None, '_uuid': u'456cfd4d96247a96dbe95b90312445d5', 'component_module': None, 'init_expr': None, 'child': [{'activate': u'1', 'show': u'1', 'child': [{'style': 0, 'activate': u'1', 'prim': u'', 'name': u'\u0414\u0430\u043d\u043d\u044b\u0435_1028', '_uuid': u'eb9cca3cd277bcc4a452cf107352225f', 'alias': None, 'init_expr': None, 'child': [{'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'imp_277', 'proportion': 0, '_uuid': u'0efe909ad588a3ff439ae257ac2eac3c', 'modules': {'ic.dlg.msgbox': [u'*'], 'NSI.spravfunc': [u'*']}, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u'', 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}, {'activate': u'1', 'name': u'NsiLevel', '_uuid': u'69c67863f5875e4dce32339ef46135e1', 'docstr': 'ic.db.icdataset-module.html', 'filter': u'', 'alias': None, 'res_query': u'NsiLevel', 'init_expr': None, 'file': u'NsiLevel.tab', 'type': u'DataLink', 'link_expr': u''}, {'activate': u'1', 'name': u'NsiList', '_uuid': u'fac0a0fd1b97db2a3158b8b04425b03a', 'docstr': u'ic.db.icdataset-module.html', 'filter': u'', 'alias': None, 'res_query': u'NsiList', 'init_expr': None, 'file': u'NsiList.tab', 'type': u'DataLink', 'link_expr': u''}], 'type': u'Group'}, {'hgap': 0, 'style': 0, 'activate': u'1', 'layout': u'vertical', 'name': u'DefaultName_946_1503_1754', 'position': (-1, -1), 'type': u'BoxSizer', '_uuid': u'a8ee4753772c5fc080591ece4b597aa5', 'proportion': 0, 'alias': None, 'flag': 8192, 'init_expr': u'', 'child': [{'activate': 1, 'show': 1, 'borderRightColor': (167, 160, 150), 'child': [{'activate': u'1', 'show': u'1', 'text': u"#\t\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c \u0438\u043c\u044f \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u0443\u044e \u0441 \u0442\u0438\u043f\u043e\u043c \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430\r\ntry:\r\n\tobj = _NsiList.get(NsiLevel.filter['id_nsi_list'])\r\n\r\n\t# \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c \u0442\u0438\u043f \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430\r\n\ttype_sprav = obj.type\r\n\t_resultEval=obj.name\r\nexcept:\r\n\ttype_sprav = ''\r\n\t_resultEval = '<\u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u043a\u043e\u0434\u043e\u0432>'", 'refresh': None, 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 11}, 'border': 0, 'size': (-1, 18), 'style': 0, 'foregroundColor': (0, 0, 0), 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticText', '_uuid': u'f09cd03334860bfe9ef6dd431b2716f7', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'name': u'titleText', 'keyDown': None, 'alias': None, 'init_expr': None, 'position': wx.Point(31, 5)}, {'activate': 1, 'show': 1, 'hlp': None, 'keyDown': None, 'file': u'@common.imgHelp', 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'Image', '_uuid': u'99ba8d063918b1ae81024747ed48eb9d', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': [], 'field_name': u'None', 'name': u'DefaultName_11135', 'refresh': [], 'alias': None, 'init_expr': None, 'position': wx.Point(5, 5)}], 'refresh': None, 'borderTopColor': (167, 160, 150), 'font': {}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': wx.Size(643, 27), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'', 'source': None, 'backgroundColor': None, 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u'', 'backgroundColor2': None, '_uuid': u'682a2bf9a7146738963c77a20c2ddd50', 'style': 0, 'bgrImage': None, 'flag': 8192, 'recount': None, 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 1, 'borderLeftColor': (167, 160, 150), 'name': u'HeadCell_3469_4256', 'borderBottomColor': (167, 160, 150), 'keyDown': None, 'alias': None, 'init_expr': None, 'position': wx.Point(0, 0), 'backgroundType': 0, 'onInit': u'self.SetRoundCorners((1,1,1,1))'}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'description': None, 'alias': None, 'type': u'SizerSpace', '_uuid': u'7f2c09094008b480d1bccfc44fe37af2', 'proportion': 0, 'name': u'sp1', 'component_module': None, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'border': 0, 'size': (0, 2)}, {'activate': u'1', 'show': u'1', 'proportion': 0, 'buttonDel': 1, 'keyDown': None, 'border': 0, 'size': (200, 20), 'style': 512, 'foregroundColor': None, 'span': (1, 1), 'onPrint': None, 'buttonAdd': 1, 'source': u'NsiLevel', 'onAdd': None, 'backgroundColor': None, 'type': u'DatasetNavigator', 'buttonPrint': 0, '_uuid': u'79e138563bf01e827e3d7569c6b09d5d', 'onHelp': None, 'moveAfterInTabOrder': u'', 'onUpdate': None, 'flag': 8192, 'object_link': None, 'recount': None, 'onDelete': None, 'name': u'default_1014', 'refresh': None, 'alias': None, 'init_expr': None, 'buttonHelp': 0, 'position': wx.Point(0, 38), 'buttonUpdate': 0}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'description': None, 'alias': None, 'type': u'SizerSpace', '_uuid': u'be012cb633b9e007966bb5ac980440dd', 'proportion': 0, 'name': u'sp1_818', 'component_module': None, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'border': 0, 'size': (0, 5)}, {'activate': 1, 'show': 1, 'recount': None, 'keyDown': None, 'font': {}, 'border': 0, 'alignment': (u'left', u'middle'), 'size': (-1, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'source': None, 'backgroundColor': (235, 235, 235), 'type': u'Head', 'description': None, '_uuid': u'687b3e73cd03d5805de0c58a74b2f044', 'style': 0, 'flag': 8192, 'child': [{'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, 22), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0422\u0438\u043f', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u'\u0422\u0438\u043f \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430', 'backgroundColor2': None, '_uuid': u'07098b846ece6d81b2077c0ed9ea1e4d', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (100, 100, 100), 'name': u'type', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 0), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0423\u0440\u043e\u0432.', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': u'True', 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u'\u041d\u043e\u043c\u0435\u0440 \u0443\u0440\u043e\u0432\u043d\u044f \u043a\u043e\u0434\u0430', 'backgroundColor2': None, '_uuid': u'60cd1b60597155db8e1c8680b97493b3', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'level', 'borderBottomColor': (100, 100, 100), 'refresh': u'None', 'alias': None, 'init_expr': u'None', 'position': (0, 1), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0418\u043c\u044f', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u'\u0418\u043c\u044f \u0443\u0440\u043e\u0432\u043d\u044f', 'backgroundColor2': None, '_uuid': u'13a07fb2479d9335c8708701c6b1de08', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'name', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 2), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0420\u0430\u0437\u043c\u0435\u0440', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u' \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043e\u0434\u0430\r\n \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f\r\n', 'backgroundColor2': None, '_uuid': u'321c0a0a17f958421712e5934c520989', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'level_len', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 3), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': u'None', 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0422\u0438\u043f \u0443\u0440.', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u' \u0422\u0438\u043f \u043a\u043e\u0434\u0430 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f\r\n - [True]  \u0441\u0442\u0440\u043e\u043a\u043e\u0432\u044b\u0439\r\n - [Fasle] \u0447\u0438\u0441\u043b\u043e\u0432\u043e\u0439\r\n', 'backgroundColor2': None, '_uuid': u'e501e3ad4720ff7981344b9ec7211d01', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'level_type', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 4), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u' \u0418\u043c\u044f \u0444\u043e\u0440\u043c\u044b \r\n \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f', 'backgroundColor2': None, '_uuid': u'5f57a416bff112ffb2886956af10e66a', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'edit_form_id', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 5), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0412\u044b\u0431\u043e\u0440', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u' \u0418\u043c\u044f \u0444\u043e\u0440\u043c\u044b \r\n \u0432\u044b\u0431\u043e\u0440\u0430 ', 'backgroundColor2': None, '_uuid': u'e878e22f71e7e6b28e588f050babfb17', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'hlp_form_id', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 6), 'backgroundType': 1, 'onInit': None}, {'activate': u'0', 'show': 1, 'borderRightColor': (100, 100, 100), 'recount': None, 'keyDown': None, 'borderTopColor': (182, 182, 182), 'font': {'style': u'bold', 'size': 8, 'underline': False, 'family': u'sansSerif', 'faceName': u'Arial'}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, -1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'\u0414\u043e\u0441\u0442\u0443\u043f', 'source': None, 'backgroundColor': (255, 255, 255), 'isSort': False, 'type': u'HeadCell', 'borderWidth': 1, 'description': None, 'shortHelpString': u' \u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\r\n \u0434\u043e\u0441\u0442\u0443\u043f\u0430', 'backgroundColor2': None, '_uuid': u'4452741fea80f44db5b2e90c97aaf9ff', 'style': 0, 'bgrImage': None, 'flag': 0, 'child': [], 'cursorColor': (100, 100, 100), 'borderStyle': None, 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'access', 'borderBottomColor': (100, 100, 100), 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 7), 'backgroundType': 1, 'onInit': None}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0422\u0438\u043f', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u'', 'nest': None, '_uuid': u'831b67dae955798db512ad4070c4406e', 'flag': 0, 'child': [], 'name': u'LType', 'round_corner': [1, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 0)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0423\u0440\u043e\u0432.', 'isSort': 1, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u'', 'nest': None, '_uuid': u'808826f0c6908cd83c61cafb1efa80dd', 'flag': 0, 'child': [], 'name': u'LLevel', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 1)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0418\u043c\u044f', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u'', 'nest': None, '_uuid': u'ac1f21b042ed64a0c1b741d3a0cd1f36', 'flag': 0, 'child': [], 'name': u'LName', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 2)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0420\u0430\u0437\u043c\u0435\u0440', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u' \u0420\u0430\u0437\u043c\u0435\u0440 \u043a\u043e\u0434\u0430\r\n \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f\r\n', 'nest': None, '_uuid': u'1c7ec517f2f9940481f71a0639975f05', 'flag': 0, 'child': [], 'name': u'LLevel_len', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 3)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0422\u0438\u043f \u0443\u0440.', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u' \u0422\u0438\u043f \u043a\u043e\u0434\u0430 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f\r\n - [True]  \u0441\u0442\u0440\u043e\u043a\u043e\u0432\u044b\u0439\r\n - [Fasle] \u0447\u0438\u0441\u043b\u043e\u0432\u043e\u0439\r\n', 'nest': None, '_uuid': u'c17be07515ea175755c982bc472a11c6', 'flag': 0, 'child': [], 'name': u'LLevel_type', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 4)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u' \u0418\u043c\u044f \u0444\u043e\u0440\u043c\u044b \r\n \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f', 'nest': None, '_uuid': u'27be8ff4c5f37ebb1a628675c2322785', 'flag': 0, 'child': [], 'name': u'LEdit_form_id', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 5)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 0, 1], 'label': u'\u0412\u044b\u0431\u043e\u0440', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u' \u0418\u043c\u044f \u0444\u043e\u0440\u043c\u044b \r\n \u0432\u044b\u0431\u043e\u0440\u0430 ', 'nest': None, '_uuid': u'911280b9cf42bd081c1c140d8bb2bedb', 'flag': 0, 'child': [], 'name': u'LHlp_form_id', 'round_corner': [0, 0, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 6)}, {'activate': 1, 'proportion': 0, 'border': 0, 'size': (50, -1), 'style': 0, 'span': (1, 1), 'component_module': None, 'przn_border': [1, 1, 1, 1], 'label': u'\u0414\u043e\u0441\u0442\u0443\u043f', 'isSort': 0, 'scheme': u'GOLD', 'type': u'NsiLabelCell', 'description': None, 'shortHelpString': u' \u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u0440\u0430\u0432\r\n \u0434\u043e\u0441\u0442\u0443\u043f\u0430', 'nest': None, '_uuid': u'5ce1678ec774b17e7a4d6401e13e488b', 'flag': 0, 'child': [], 'name': u'LAccess', 'round_corner': [0, 1, 0, 0], 'alias': None, 'init_expr': None, 'position': (0, 7)}], 'name': u'HeadLevel', 'refresh': None, 'alias': None, 'init_expr': None, 'position': (0, 0), 'onInit': None}, {'line_color': (210, 214, 223), 'activate': u'1', 'show': u'1', 'cols': [{'sort': u'1', 'setvalue': u'', 'attr': None, 'ctrl': None, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'pic': u'S', 'keyDown': None, 'hlp': None, 'width': 70, 'init': u'None', 'activate': u'0', 'recount': None, 'label': u'id\\n\u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430', 'type': u'GridCell', 'valid': u'None', 'getvalue': u'', 'name': u'id_nsi_list'}, {'activate': u'1', 'ctrl': None, 'pic': u'S', 'hlp': u'None', 'style': 0, 'show': u'1', 'label': u' \\n\u0422\u0438\u043f', 'width': 70, 'init': u'@type_sprav', 'valid': u'None', 'type': u'GridCell', 'sort': u'1', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '_uuid': None, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'shortHelpString': u'', '_uuid': u'6322a084dc375c1e7826afd563978dca', 'recount': None, 'getvalue': u'', 'attr': u'R', 'setvalue': u'', 'name': u'type', 'keyDown': None, 'alias': None, 'init_expr': u'None'}, {'activate': u'1', 'ctrl': None, 'pic': u'99', 'getvalue': u'', 'show': u'1', 'label': u' \\n\u0423\u0440\u043e\u0432\u0435\u043d\u044c', 'width': 70, 'init': u"@MaxVal(_NsiLevel, type_sprav, 'level')+1", 'valid': u'1,100', 'type': u'GridCell', 'sort': u'1', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'shortHelpString': u'', '_uuid': u'1049d25e7456eb551cf02aeebe2395b8', 'recount': u'None', 'hlp': u'None', 'attr': None, 'setvalue': u'', 'name': u'level', 'keyDown': u'None', 'init_expr': None}, {'sort': None, 'pic': u'S', 'attr': None, 'ctrl': u'None', 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'keyDown': None, 'getvalue': u'', 'width': 100, 'init': None, 'setvalue': u'', 'activate': u'1', 'init_expr': None, 'recount': None, 'label': u'\u0418\u043c\u044f \\n\u0443\u0440\u043e\u0432\u043d\u044f', 'hlp': None, 'valid': u'None', 'name': u'name'}, {'activate': u'1', 'ctrl': u'None', 'pic': u'99', 'hlp': u'', 'show': u'1', 'label': u'\u0420\u0430\u0437\u043c\u0435\u0440\\n\u043a\u043e\u0434\u0430\\n\u0443\u0440\u043e\u0432\u043d\u044f', 'width': 50, 'init': u'1', 'valid': u'1,10', 'type': u'GridCell', 'sort': None, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'shortHelpString': u'', '_uuid': u'608ee69652363f6d2e74b9f856882f89', 'recount': u'None', 'getvalue': u'', 'attr': u'W', 'setvalue': u'', 'name': u'level_len', 'keyDown': u'None', 'init_expr': None}, {'activate': u'1', 'ctrl': u'', 'pic': u'B', 'getvalue': u'', 'show': u'1', 'label': u'\u0422\u0438\u043f \\n\u043a\u043e\u0434\u0430 \\n\u0443\u0440\u043e\u0432\u043d\u044f ', 'width': 100, 'init': u'1', 'valid': u'0,1', 'type': u'GridCell', 'sort': u'None', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'shortHelpString': u'', '_uuid': u'e40272be4fb104cd1ed97d0b4f8b0d33', 'recount': u'None', 'hlp': u'None', 'attr': u'W', 'setvalue': u'', 'name': u'level_type', 'keyDown': None, 'init_expr': None}, {'sort': None, 'pic': u'S', 'attr': None, 'ctrl': None, 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'keyDown': None, 'getvalue': u'', 'width': 100, 'init': u'FrmStructSprav', 'setvalue': u'', 'activate': u'1', 'init_expr': None, 'recount': None, 'label': u'\u0424\u043e\u0440\u043c\u0430 \\n\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f', 'hlp': u'None', 'valid': None, 'name': u'edit_form_id'}, {'sort': None, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'attr': None, 'ctrl': None, 'pic': u'S', 'hlp': None, 'keyDown': None, 'getvalue': u'', 'width': 100, 'init': u'FrmHlpStructSprav', 'setvalue': u'', 'activate': u'1', 'init_expr': None, 'recount': u'None', 'label': u'\u0424\u043e\u0440\u043c\u0430 \\n\u0432\u044b\u0431\u043e\u0440\u0430', 'type': u'GridCell', 'valid': None, 'name': u'hlp_form_id'}, {'activate': u'1', 'ctrl': None, 'pic': u'CH', 'hlp': None, 'style': 0, 'component_module': None, 'label': u' \\n \u0414\u043e\u0441\u0442\u0443\u043f', 'width': 100, 'init': None, 'valid': u'r-, -w, rw', 'type': u'GridCell', 'sort': None, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '_uuid': None, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'description': None, 'shortHelpString': u'', '_uuid': u'e02b96a5c0375dba899edbee8766f99e', 'recount': None, 'getvalue': u'', 'attr': None, 'setvalue': u'', 'name': u'access', 'keyDown': None, 'alias': None, 'init_expr': None}], 'row_height': 18, 'keyDown': u'#\t\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448\u044c \u0413\u0440\u0438\u0434\u0430\r\nkey=evt.GetKeyCode()\r\nprnt = _dict_obj[\'DlgNsiLevel\']\r\nif key==wx.WXK_F3:\r\n    print \'============================= F3 -\', key\r\n    ResultForm("FrmNsiNotice", filter={"NsiNotice":{"id_nsi_level":NsiLevel.getId()}}, parent=prnt)\r\n    _dict_obj[\'gridLevel\'].SetFocus()\r\n\r\nelif key==wx.WXK_ESCAPE and not evt.ShiftDown() and not evt.AltDown():\r\n\t_dict_obj["DlgNsiLevel"].EndModal(wx.ID_CANCEL)\r\n\r\n', 'border': 0, 'post_select': None, 'size': (200, 200), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'delRec': None, 'component_module': None, 'selected': None, 'proportion': 1, 'getattr': u'#iter_rowcol(self, [(234,234,234), None])', 'label': u'Grid', 'source': u'NsiLevel', 'init': u"val = self.GetView().getNameValue('level_type', row)\r\nprint '>>> LEVEL_TYPE:', val", 'backgroundColor': None, 'fixRowSize': 0, 'type': u'GridDataset', '_uuid': u'd41d505f3986aa16c02feca31fb6be88', 'fixColSize': 0, 'description': None, 'post_del': None, 'post_init': None, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '_uuid': u'589618cc4a3f803e846e567be9c3ed62', 'activate': u'1', 'backgroundColor': (247, 247, 247), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'style': 0, 'docstr': u'ic.components.icgrid.html', 'flag': 8192, 'dclickEditor': None, 'recount': None, 'label_attr': {'foregroundColor': (255, 255, 255), 'name': '', '_uuid': None, 'activate': u'1', 'init_expr': None, 'backgroundColor': (115, 115, 185), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'label_attr', 'alignment': (u'left', u'middle')}, 'name': u'gridLevel', 'label_height': 50, 'changed': None, 'onSize': None, 'alias': u'', 'init_expr': u"header = _dict_obj['HeadLevel']\r\nself.SetHeader(header, False, True)\r\nself.ReconstructHeader()", 'position': (-1, -1), 'onInit': None, 'refresh': u'None'}, {'activate': u'1', 'name': u'sp1_2420', '_uuid': u'8aecd5ff3e13809beeb3bead16250fb1', 'proportion': 0, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'type': u'SizerSpace', 'size': (0, 5)}, {'hgap': 0, 'style': 0, 'activate': u'1', 'layout': u'horizontal', 'name': u'DefaultName_382_3187', 'position': (0, 0), 'border': 0, '_uuid': u'5b4786e261a5f800252512b83d6a0f46', 'proportion': 0, 'alias': None, 'flag': 256, 'init_expr': None, 'child': [{'activate': u'1', 'show': u'1', 'mouseClick': u'prnt = _dict_obj[\'DlgNsiLevel\']\r\nResultForm("FrmNsiNotice", filter={"NsiNotice":{"id_nsi_level":NsiLevel.getId()}}, parent=self)\r\n_dict_obj[\'gridLevel\'].SetFocus()', 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'label': u'F3 - \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e\u043b\u0435\u0439', 'source': None, 'mouseDown': u'None', 'backgroundColor': None, 'type': u'Button', '_uuid': u'a3dc06ddb34272ab9fa8f56bfdfc09d1', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'keyDown': None, 'name': u'F3', 'mouseUp': u'None', 'refresh': None, 'alias': None, 'init_expr': None, 'position': wx.Point(263, 320), 'keyCode': None, 'mouseContextDown': u'None'}, {'refresh': None, 'activate': u'0', 'show': u'1', 'mouseClick': u'ResultForm("FrmNsiLevel", filter={"CodStruct":{"id_nsi_list":self.evalSpace["_sources"]["SprType"].getId()}}, parent=self)', 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'label': u'F4 - \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u0430 \u043a\u043e\u0434\u0430', 'source': None, 'mouseDown': u'None', 'backgroundColor': None, 'type': u'Button', '_uuid': u'9e866c499ed53a6c543dcdb2c1659341', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'name': u'F4_339', 'mouseUp': None, 'keyDown': None, 'alias': None, 'init_expr': None, 'position': (-1, -1), 'keyCode': None, 'mouseContextDown': None}], 'span': (1, 1), 'type': u'BoxSizer', 'vgap': 0, 'size': (-1, -1)}, {'activate': u'1', 'name': u'sp1_2769', '_uuid': u'e5e8c606424602a35a95a40ac047d15b', 'proportion': 0, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'type': u'SizerSpace', 'size': (0, 5)}], 'span': (1, 1), 'border': 0, 'vgap': 0, 'size': (-1, -1)}], 'keyDown': None, 'border': 0, 'size': (650, 400), 'style': 536877120, 'foregroundColor': None, 'span': (1, 1), 'title': u'\u0421\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u044b \u043a\u043e\u0434\u043e\u0432', 'component_module': None, 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'Dialog', 'description': None, 'onClose': None, '_uuid': u'eb9cca3cd277bcc4a452cf107352225f', 'moveAfterInTabOrder': u'', 'killFocus': None, 'flag': 0, 'recount': None, 'setFocus': None, 'name': u'DlgNsiLevel', 'refresh': None, 'alias': None, 'init_expr': u'', 'position': (-1, -1), 'onInit': None}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'imp_2776', 'proportion': 0, '_uuid': u'45b20f79d25e82d5c1391fcfdb41f19b', 'modules': {}, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u"method('SetLastRow', 'NSI', locals(), grid=_dict_obj['gridLevel'])", 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}], 'type': u'Group', 'description': None}}