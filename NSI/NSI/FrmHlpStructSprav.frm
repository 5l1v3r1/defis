{'FrmHlpStructSprav': {'style': 0, 'activate': u'1', 'prim': u'', 'description': None, 'alias': None, '__item_id': 0, '_uuid': u'9c92e0796297eefc6f588834cbc569e2', 'component_module': None, 'init_expr': None, 'child': [{'activate': u'1', 'show': u'1', 'recount': None, 'keyDown': u'#\t\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043d\u0430\u0436\u0430\u0442\u0438\u044f \u043a\u043b\u0430\u0432\u0438\u0448\r\nkey=evt.GetKeyCode()\r\nif key==wx.WXK_ESCAPE and not evt.ShiftDown() and not evt.AltDown():\r\n    result=None\r\n    _root_obj.EndModal(wx.ID_CANCEL)\r\n_resultEval=True', 'border': 0, 'size': (600, 400), 'style': 536877120, 'foregroundColor': None, 'span': (1, 1), 'title': u'\u0412\u044b\u0431\u0435\u0440\u0438 \u0438\u0437 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430', 'component_module': None, 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'Dialog', '__item_id': 1, 'onClose': u'_resultEval=True', '_uuid': u'd5f2b4627f8159064c972cac4c01e1ba', 'moveAfterInTabOrder': u'', 'killFocus': u'None', 'flag': 0, 'child': [{'activate': u'1', 'prim': u'', 'name': u'\u0414\u0430\u043d\u043d\u044b\u0435_1028', '__item_id': 2, '_uuid': u'b1d63b9d816023dc28a351f2b86e21fa', 'init_expr': None, 'child': [{'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'imp_277', '__item_id': 3, 'modules': {'ic.dlg.msgbox': [u'MsgBox']}, '_uuid': u'69ccfbf191e686136453e0e448a1f138', 'proportion': 0, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u"_ret_field = 'name'", 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}, {'activate': u'1', 'name': u'NsiList', '__item_id': 4, '_uuid': u'77348b29d7b3b63c70a3f9314accd7bb', 'docstr': u'ic.db.icdataset-module.html', 'filter': u'', 'alias': None, 'res_query': u'NsiList', 'init_expr': None, 'file': u'NsiList.tab', 'type': u'DataLink', 'link_expr': u''}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'imp_id_nsi_list', '__item_id': 5, 'modules': {'NSI.spravfunc': [u'*']}, '_uuid': u'6d68a95c34b2602697bdde74f6fca606', 'proportion': 0, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u"#\t\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c id \r\nprint 'SCRIPT  ENTER sprav_type=', sprav_type\r\n_id_nsi_list = _NsiList.select(_NsiList.q.type==sprav_type)[0].id\r\nprint 'SCRIPT _ID_NSI_LIST=', _id_nsi_list", 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}, {'activate': u'1', 'name': u'NsiStd', '__item_id': 6, '_uuid': u'afb7a3ddf54cf447555cc9f2d5aef769', 'docstr': u'ic.db.icdataset-module.html', 'filter': u'select id from NsiStd where id_nsi_list=1', 'alias': None, 'res_query': u'@_NsiList.get(_id_nsi_list).tab', 'init_expr': u'None', 'file': u'NsiStd.tab', 'type': u'DataLink', 'link_expr': u''}, {'activate': u'1', 'name': u'NsiLevel', '__item_id': 7, '_uuid': u'529e04f27314271d48f428dfe0a5b025', 'docstr': u'ic.db.icdataset-module.html', 'filter': u'', 'alias': None, 'res_query': u'@getNsiLevelClassName()', 'init_expr': None, 'file': u'NsiLevel.tab', 'type': u'DataLink', 'link_expr': u''}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'SetTitleDlg_2460', '__item_id': 8, 'modules': {}, '_uuid': u'd5d4e1f73bad90edd0ef35b81cb8717a', 'proportion': 0, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u'spr_name=_NsiList.select(_NsiList.q.type==sprav_type)[0].name\r\n_root_obj.SetTitle(spr_name)', 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}], 'type': u'Group'}, {'hgap': 0, 'style': 0, 'activate': u'1', 'layout': u'vertical', 'name': u'DefaultName_946_1503_1754', '__item_id': 9, 'type': u'BoxSizer', 'span': (1, 1), '_uuid': u'c904c8d537767f9c3a3e51b9b28d8931', 'proportion': 0, 'alias': None, 'flag': 0, 'init_expr': None, 'child': [{'activate': 1, 'show': 1, 'borderRightColor': (255, 255, 255), 'recount': None, 'refresh': None, 'borderTopColor': (250, 250, 250), 'font': {}, 'border': 0, 'alignment': (u'centred', u'middle'), 'size': (50, 27), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'label': u'', 'source': None, 'backgroundColor': None, 'isSort': False, 'type': u'HeadCell', 'shortHelpString': u'', '__item_id': 10, '_uuid': u'46cac73e1d4d542fd7515e27d7ffdbcd', 'moveAfterInTabOrder': u'', 'flag': 8192, 'child': [{'activate': u'0', 'show': u'1', 'text': u"grp_cod=filter(lambda s: type(s)==type(''),NsiStd.filter['cod'])\r\ngrp_cod=''.join(grp_cod)\r\ntitle=' '\r\nif not grp_cod:\r\n    title=_NsiList.select(_NsiList.q.type==typSprav)[0].name\r\nelse:\r\n    title=_NsiStd.select(_NsiStd.q.cod==grp_cod)[0].name\r\n#\u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415 \u041d\u0443\u0436\u043d\u043e \u0445\u043e\u0442\u044f \u0431\u044b \u0441\u0442\u0440\u043e\u043a\u0443 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0442\u044c\r\n#\u0438\u043d\u0430\u0447\u0435 \u043e\u0448\u0438\u0431\u043a\u0430!\r\nif not title:\r\n    title=' '\r\n_resultEval=title", 'keyDown': u'None', 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 11}, 'border': 0, 'size': (-1, 18), 'style': 0, 'foregroundColor': (1, 67, 165), 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticText', '__item_id': 11, '_uuid': u'f6a6a85fd854d567f835ae117cf815c5', 'moveAfterInTabOrder': u'', 'flag': 2048, 'recount': None, 'name': u'default_1209_9894', 'refresh': None, 'alias': None, 'init_expr': u'None', 'position': (31, 3)}, {'activate': u'1', 'show': u'1', 'text': u"grp_cod=filter(lambda s: type(s)==type(''),sprav_code)\r\ngrp_cod=''.join(grp_cod)\r\ntitle=''\r\nif not grp_cod:\r\n    title=_NsiList.select(_NsiList.q.type==sprav_type)[0].name\r\nelse:\r\n    title=_NsiStd.select(_NsiStd.q.cod==grp_cod)[0].name\r\n#\u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415 \u041d\u0443\u0436\u043d\u043e \u0445\u043e\u0442\u044f \u0431\u044b \u0441\u0442\u0440\u043e\u043a\u0443 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0442\u044c\r\n#\u0438\u043d\u0430\u0447\u0435 \u043e\u0448\u0438\u0431\u043a\u0430!\r\nif not title:\r\n    title=' '\r\n_resultEval=title", 'refresh': None, 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 11}, 'border': 0, 'size': (-1, 18), 'style': 0, 'foregroundColor': (1, 67, 165), 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticText', '__item_id': 12, '_uuid': u'a6ebd9ffde82d5c939330d96f495dfe4', 'moveAfterInTabOrder': u'', 'flag': 2048, 'recount': None, 'name': u'default_1209_17249', 'keyDown': None, 'alias': u'None', 'init_expr': u'', 'position': (31, 3)}, {'activate': 1, 'show': 1, 'hlp': None, 'refresh': [], 'file': u'@common.imgHelp', 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'Image', '__item_id': 13, '_uuid': u'a3508eaa78c046fb98adc02ad7f34dc4', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': [], 'field_name': None, 'name': u'DefaultName_10717', 'keyDown': None, 'alias': None, 'init_expr': None, 'position': (5, 5)}], 'borderStep': 0, 'borderLeftColor': (250, 250, 250), 'name': u'HeadCell_9215_9543_16837', 'borderBottomColor': (1, 67, 165), 'keyDown': u'None', 'alias': None, 'init_expr': u'if isLevel(sprav_type,len(filter(lambda x: x<>None,sprav_code))+1):\r\n\tself.SetForegroundColour(wx.Colour(0,0,0))\r\nelse:\r\n\tself.SetForegroundColour(wx.Colour(0,0,255))', 'position': (-1, -1), 'backgroundType': 0}, {'activate': u'0', 'show': u'1', 'recount': None, 'refresh': None, 'border': 0, 'size': (20, 20), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'title': u'default', 'proportion': 0, 'source': None, 'backgroundColor': (207, 207, 231), 'type': u'Window', '__item_id': 14, '_uuid': u'c2880dd556a28db9c33a1d768e39a83d', 'moveAfterInTabOrder': u'', 'flag': 8192, 'child': [{'activate': u'1', 'show': u'1', 'text': u"grp_cod=filter(lambda s: type(s)==type(''),sprav_code)\r\ngrp_cod=''.join(grp_cod)\r\ntitle=''\r\nif not grp_cod:\r\n    title=_NsiList.select(_NsiList.q.type==sprav_type)[0].name\r\nelse:\r\n    title=_NsiStd.select(_NsiStd.q.cod==grp_cod)[0].name\r\n#\u0412\u041d\u0418\u041c\u0410\u041d\u0418\u0415 \u041d\u0443\u0436\u043d\u043e \u0445\u043e\u0442\u044f \u0431\u044b \u0441\u0442\u0440\u043e\u043a\u0443 \u0441 \u043f\u0440\u043e\u0431\u0435\u043b\u043e\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0430\u0442\u044c\r\n#\u0438\u043d\u0430\u0447\u0435 \u043e\u0448\u0438\u0431\u043a\u0430!\r\nif not title:\r\n    title=' '\r\n_resultEval=title", 'keyDown': None, 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 11}, 'border': 0, 'size': (-1, 18), 'style': 0, 'foregroundColor': (0, 0, 0), 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticText', '__item_id': 15, '_uuid': u'1742e7ade0dcbdd17c70383eba2a6509', 'moveAfterInTabOrder': u'', 'flag': 2048, 'recount': None, 'name': u'default_1209', 'refresh': None, 'alias': u'None', 'init_expr': None, 'position': (10, 3)}, {'activate': u'0', 'show': u'1', 'text': u"@\r\ngrp_cod=filter(lambda s: type(s)==type(''),sprav_code)\r\ngrp_cod=''.join(grp_cod)\r\ntitle=''\r\nif not grp_cod:\r\n    title=_NsiList.select(_NsiList.q.type==sprav_type)[0].name\r\nelse:\r\n    title=_NsiStd.select(_NsiStd.q.cod==grp_cod)[0].name\r\n_resultEval=title", 'keyDown': None, 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 11}, 'border': 0, 'size': (-1, 18), 'style': 0, 'foregroundColor': (0, 0, 0), 'span': (1, 1), 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticText', '__item_id': 16, '_uuid': u'86ac56a4708caade352d09ac156b52d2', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'name': u'default_1209_3057', 'refresh': None, 'alias': None, 'init_expr': u'None', 'position': (10, 3)}], 'name': u'defaultWindow_771_1115_3729', 'keyDown': None, 'alias': u'None', 'init_expr': u'if isLevel(sprav_type,len(filter(lambda x: x<>None,sprav_code))+1):\r\n\tself.SetForegroundColour(wx.Colour(0,0,0))\r\nelse:\r\n\tself.SetForegroundColour(wx.Colour(0,0,255))', 'position': (-1, -1)}, {'activate': u'0', 'show': u'1', 'keyDown': None, 'border': 0, 'size': (-1, 1), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'layout': u'horizontal', 'proportion': 0, 'source': None, 'backgroundColor': None, 'type': u'StaticLine', '__item_id': 17, '_uuid': u'dc191e97cd5add7e2f91ea41003ec71e', 'style': 0, 'flag': 8192, 'recount': None, 'span': (1, 1), 'name': u'Div_4691', 'refresh': None, 'alias': None, 'init_expr': None, 'position': (-1, -1)}, {'activate': u'1', 'span': (1, 1), 'name': u'sp', '__item_id': 18, 'type': u'SizerSpace', '_uuid': u'dc191e97cd5add7e2f91ea41003ec71e', 'proportion': 0, 'alias': None, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'border': 0, 'size': (0, 3)}, {'activate': u'1', 'show': u'1', 'proportion': 0, 'buttonDel': 0, 'refresh': None, 'border': 0, 'size': (200, 20), 'moveAfterInTabOrder': u'', 'foregroundColor': None, 'span': (1, 1), 'onPrint': None, 'buttonAdd': 0, 'source': u'NsiStd', 'onAdd': None, 'backgroundColor': None, 'type': u'DatasetNavigator', '__item_id': 19, 'buttonPrint': 0, '_uuid': u'f44ab21ae2af61a5298b208b8c1a27e8', 'onHelp': None, 'style': 512, 'onUpdate': None, 'flag': 8192, 'object_link': None, 'recount': None, 'onDelete': None, 'name': u'nav', 'keyDown': None, 'alias': None, 'init_expr': None, 'buttonHelp': 0, 'position': (-1, -1), 'buttonUpdate': 0}, {'line_color': (200, 200, 200), 'activate': u'0', 'show': u'1', 'cols': [{'sort': None, 'pic': u'N', 'attr': None, 'ctrl': None, '__item_id': 21, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 22, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'label': u'id_nsi_list', 'keyDown': None, 'hlp': None, 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'0', 'recount': u'None', 'getvalue': u'', 'type': u'GridCell', 'valid': u'None', 'name': u'id_nsi_list'}, {'activate': u'1', 'ctrl': None, 'pic': u'S', 'getvalue': u'', 'show': u'1', 'label': u'\u0422\u0438\u043f', 'width': 70, 'init': u"_NsiList.get(dataset.filter['id_nsi_list']).type", 'valid': u'None', 'type': u'GridCell', 'sort': u'1', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 24, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'shortHelpString': u'', '__item_id': 23, '_uuid': u'6733d163813455a1231458c8bd250419', 'recount': None, 'hlp': None, 'attr': u'R', 'setvalue': u'', 'name': u'type', 'keyDown': None, 'init_expr': None}, {'sort': u'1', 'pic': u'S', 'attr': None, 'ctrl': None, '__item_id': 25, 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 26, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'label': u'\u043a\u043e\u0434', 'hlp': None, 'valid': u'None', 'name': u'cod'}, {'sort': None, 'setvalue': u'', 'attr': None, 'ctrl': None, '__item_id': 27, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 28, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'italic', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 10}, 'type': 'cell_attr', 'alignment': u"('left', 'middle')"}, 'pic': u'S', 'keyDown': u'None', 'label': u'\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435', 'width': 200, 'init': u'None', 'activate': u'1', 'recount': None, 'hlp': None, 'type': u'GridCell', 'valid': u'None', 'getvalue': u'', 'name': u'name'}, {'sort': None, 'pic': u'N', 'attr': None, 'ctrl': None, '__item_id': 29, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 30, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'label': u'N1', 'keyDown': None, 'hlp': None, 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': u'None', 'getvalue': u'', 'type': u'GridCell', 'valid': None, 'name': u'n1'}, {'sort': None, 'pic': u'N', 'attr': None, 'ctrl': None, '__item_id': 31, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 32, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'getvalue': u'', 'keyDown': None, 'label': u'N2', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'hlp': None, 'type': u'GridCell', 'valid': None, 'name': u'n2'}, {'sort': None, 'pic': u'N', 'attr': None, 'ctrl': None, '__item_id': 33, 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 34, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'label': u'N3', 'hlp': None, 'valid': None, 'name': u'n3'}, {'sort': None, 'pic': u'S', 'attr': None, 'ctrl': None, '__item_id': 35, 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 36, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'label': u'S1', 'hlp': None, 'valid': None, 'name': u's1'}, {'sort': None, 'pic': u'S', 'attr': None, 'ctrl': None, '__item_id': 37, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 38, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'hlp': None, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'label': u'S2', 'type': u'GridCell', 'valid': u'None', 'name': u's2'}, {'sort': None, 'pic': u'S', 'attr': None, 'ctrl': None, '__item_id': 39, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 40, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'label': u'S3', 'keyDown': None, 'hlp': u'None', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'recount': None, 'getvalue': u'', 'type': u'GridCell', 'valid': u'None', 'name': u's3'}, {'sort': None, 'pic': u'F', 'attr': None, 'ctrl': None, '__item_id': 41, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 42, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'hlp': None, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': u'None', 'setvalue': u'', 'activate': u'1', 'recount': None, 'label': u'F1', 'type': u'GridCell', 'valid': None, 'name': u'f1'}, {'sort': None, 'pic': u'F', 'attr': None, 'ctrl': None, '__item_id': 43, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 44, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'label': u'F2', 'keyDown': None, 'hlp': None, 'width': 50, 'init': u'None', 'setvalue': u'', 'activate': u'1', 'recount': None, 'getvalue': u'', 'type': u'GridCell', 'valid': None, 'name': u'f2'}, {'sort': None, 'pic': u'F', 'attr': None, 'ctrl': None, '__item_id': 45, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 46, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'getvalue': u'', 'keyDown': None, 'label': u'F3', 'width': 50, 'init': u'None', 'setvalue': u'', 'activate': u'1', 'recount': None, 'hlp': None, 'type': u'GridCell', 'valid': u'None', 'name': u'f3'}, {'sort': u'None', 'pic': u'N', 'attr': u'W', 'ctrl': u'None', '__item_id': 47, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 48, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'label': u'\u0421\u0447\u0435\u0442\u0447\u0438\u043a', 'keyDown': u'None', 'hlp': u'None', 'width': 100, 'init': u'None', 'setvalue': u'', 'activate': u'1', 'recount': u'None', 'getvalue': u'', 'type': u'GridCell', 'valid': u'None', 'name': u'count'}], 'refresh': None, 'addRec': None, 'border': 0, 'size': (200, 200), 'style': 33554432, 'foregroundColor': None, 'span': (1, 1), 'delRec': None, 'source': u'Sprav', 'row_height': 22, 'selected': None, 'proportion': 1, 'getattr': None, 'label': u'Grid', 'post_del': None, 'init': None, 'backgroundColor': None, 'fixRowSize': 0, 'type': u'GridDataset', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 49, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'fixColSize': 0, '__item_id': 20, 'post_init': None, '_uuid': u'e43c0aaa77fb744b164c6c5169a6e51b', 'moveAfterInTabOrder': u'', 'docstr': u'ic.components.icgrid.html', 'flag': 8192, 'recount': None, 'label_attr': {'foregroundColor': (255, 255, 255), 'name': '', '__item_id': 50, 'activate': u'1', 'backgroundColor': (100, 100, 100), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'label_attr', 'alignment': (u'left', u'middle')}, 'name': u'default_533_1062', 'label_height': 20, 'changed': None, 'keyDown': u'None', 'alias': None, 'init_expr': None, 'position': (-1, -1)}, {'activate': u'1', 'span': (1, 1), 'name': u'sp_2112', '__item_id': 51, 'type': u'SizerSpace', '_uuid': u'e43c0aaa77fb744b164c6c5169a6e51b', 'proportion': 0, 'alias': None, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'border': 0, 'size': (0, 3)}, {'activate': u'1', 'show': u'1', 'activated': u"cur_row=row\r\ncod_struct=get_hlp_code(sprav_type,sprav_code,NsiStd.rec.cod)\r\nresult=HlpSprav(sprav_type,ParentCode=cod_struct,field=sprav_field,rec=NsiStd.rec,parentForm=self)\r\nif result:\r\n\t_esp['_dict_obj']['DlgHlpSprav'].EndModal(wx.ID_OK)\r\nelse:\r\n\tself.SetCursor(cur_row)", 'cols': [{'activate': u'0', 'ctrl': None, 'pic': u'S', 'getvalue': u'', 'show': u'1', 'label': u'\u0422\u0438\u043f', 'width': 70, 'init': u"_NsiList.get(dataset.filter['id_nsi_list']).type", 'valid': u'None', 'type': u'GridCell', 'sort': u'1', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 54, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'shortHelpString': u'', '__item_id': 53, '_uuid': u'6733d163813455a1231458c8bd250419', 'recount': None, 'hlp': None, 'attr': u'R', 'setvalue': u'', 'name': u'type', 'keyDown': None, 'init_expr': None}, {'sort': u'1', 'pic': u'S', 'attr': None, 'ctrl': None, '__item_id': 55, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 56, 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': (u'left', u'middle')}, 'label': u'\u2022 \u041a\u043e\u0434', 'keyDown': None, 'hlp': None, 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'1', 'init_expr': None, 'recount': None, 'show': u'1', 'getvalue': u'', 'type': u'GridCell', 'valid': u'None', 'name': u'cod'}, {'sort': u'1', 'setvalue': u'', 'attr': None, 'ctrl': None, '__item_id': 57, 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 58, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': u'bold', 'name': u'defaultFont', 'family': u'sansSerif', 'faceName': u'Times New Roman', 'type': u'Font', 'underline': 0, 'size': 10}, 'type': 'cell_attr', 'alignment': u"('left', 'middle')"}, 'pic': u'S', 'keyDown': u'None', 'label': u'\u2022 \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435', 'width': 400, 'init': u'None', 'activate': u'1', 'init_expr': None, 'recount': None, 'show': u'1', 'hlp': None, 'type': u'GridCell', 'valid': u'None', 'getvalue': u'', 'name': u'name'}, {'sort': None, 'pic': u'N', 'attr': None, 'ctrl': None, '__item_id': 59, 'type': u'GridCell', 'cell_attr': {'foregroundColor': (0, 0, 0), 'name': '', '__item_id': 60, 'activate': u'1', 'backgroundColor': (255, 255, 255), 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'type': 'cell_attr', 'alignment': u"('centred', 'top')"}, 'keyDown': None, 'getvalue': u'', 'width': 50, 'init': None, 'setvalue': u'', 'activate': u'0', 'recount': u'None', 'label': u'id_nsi_list', 'hlp': None, 'valid': u'None', 'name': u'id_nsi_list'}], 'keyDown': None, 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 547, 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'selected': u'', 'proportion': 1, 'source': u'NsiStd', 'getattr': u'None', 'backgroundColor': None, 'type': u'ListDataset', '__item_id': 52, '_uuid': u'534073af46b6cf93d904edc6f0b8cb9a', 'moveAfterInTabOrder': u'', 'keydown': u'', 'flag': 8192, 'recount': [], 'name': u'ListDS', 'refresh': u'None', 'alias': None, 'init_expr': u'None', 'indxFldFind': 0, 'position': (-1, -1), 'onInit': None}, {'activate': u'1', 'name': u'ssp_5223', '__item_id': 61, '_uuid': u'22e7212653a1123749fc0cbc370b2fb0', 'proportion': 0, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'type': u'SizerSpace', 'size': (0, 5)}, {'hgap': 0, 'style': 0, 'activate': u'1', 'layout': u'horizontal', 'description': None, 'alias': None, 'component_module': None, 'type': u'BoxSizer', '_uuid': u'22e7212653a1123749fc0cbc370b2fb0', 'proportion': 0, 'name': u'DefaultName_2044_4234', '__item_id': 62, 'flag': 2304, 'position': (0, 0), 'init_expr': None, 'child': [{'activate': u'1', 'show': u'1', 'keyDown': None, 'font': {'style': u'regular', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'   \u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a   ', 'source': None, 'mouseDown': u'None', 'backgroundColor': None, 'type': u'Button', '__item_id': 63, '_uuid': u'80a672313a965b938a216da65796c15a', 'moveAfterInTabOrder': u'', 'flag': 256, 'recount': None, 'name': u'btn_edit', 'mouseUp': u'None', 'refresh': None, 'alias': None, 'init_expr': None, 'position': (-1, -1), 'onInit': None, 'keyCode': u'None', 'mouseContextDown': u'None', 'mouseClick': u'#\u0412\u044b\u0437\u044b\u0432\u0430\u0435\u043c \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430\r\n\r\n#\t1. \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u043c \u0440\u0430\u0437\u043c\u0435\u0440 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f \u0438 \u0441\u0442\u0440\u0443\u043a\u0442\u0443\u0440\u043d\u044b\u0439 \u0444\u0438\u043b\u044c\u0442\u0440 \u0434\u043b\u044f \u0441\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0430\r\ntry:\r\n\ttry:\r\n\t\tn_level=sprav_code.index(None)+1\r\n\texcept:\r\n\t\tn_level=1\r\n\t#id_nsi_list_=NsiStd.rec.id_nsi_listID\r\n\tid_nsi_list_=_NsiList.select(_NsiList.q.type==sprav_type)[0].id\r\n\tlevelLen = _NsiLevel.select(AND(_NsiLevel.q.id_nsi_listID==id_nsi_list_,\r\n\t\t_NsiLevel.q.level==n_level))[0].level_len\r\n\tflt_cod=sprav_code[:n_level-1]\r\n\tflt_cod.append(levelLen)\r\n\tflt ={"NsiStd":{"id_nsi_list":id_nsi_list_, \'cod\':flt_cod}}\r\nexcept:\r\n\tflt = {"NsiStd":{"id_nsi_list":NsiStd.rec.id_nsi_listID}}\r\n\tprint \'------------------------------------------------------------------------------------------------------\'\r\n\tprint \'SCRIPT ATTRIBUTE WARNING: Do not find level(1) len for structual filter\', flt\r\n\t\r\n#\t2. \u0412\u044b\u0437\u044b\u0432\u0430\u0435\u043c \u0444\u043e\u0440\u043c\u0443 \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f\r\nprint \'SCRIPT ATTRIBUTE: filter=\', flt,sprav_code\r\ncur_row=_dict_obj[\'ListDS\'].currentItem\r\nResultForm(NsiEdtFormName(sprav_type), filter=flt, parent=_dict_obj[\'DlgHlpSprav\'],bBuff=True)\r\n_dict_obj[\'ListDS\'].RefreshData()\r\n_dict_obj[\'ListDS\'].SetCursor(cur_row)'}, {'activate': u'1', 'show': u'1', 'keyDown': None, 'font': {'style': u'bold', 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'    Enter, Dbl-Click - \u0432\u044b\u0431\u0440\u0430\u0442\u044c    ', 'source': None, 'mouseDown': u'None', 'backgroundColor': None, 'type': u'Button', 'description': None, '__item_id': 64, '_uuid': u'be81eaba66caeb1621087cd13b3d6a68', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'name': u'btn_choose', 'mouseUp': u'None', 'refresh': None, 'alias': None, 'init_expr': u'', 'position': (-1, -1), 'onInit': None, 'keyCode': None, 'mouseContextDown': u'None', 'mouseClick': u"#\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043a\u0443\u0440\u0441\u043e\u0440\u0430\r\ncur_row=_dict_obj['ListDS'].currentItem\r\ncod_struct=get_hlp_code(sprav_type,sprav_code,NsiStd.rec.cod)\r\nresult=HlpSprav(sprav_type,ParentCode=cod_struct,field=sprav_field,rec=NsiStd.rec,parentForm=_dict_obj['DlgHlpSprav'])\r\nif result:\r\n\t_esp['_dict_obj']['DlgHlpSprav'].EndModal(wx.ID_OK)\r\nelse:\r\n\t_dict_obj['ListDS'].SetCursor(cur_row)"}, {'activate': u'1', 'show': u'1', 'keyDown': None, 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'component_module': None, 'proportion': 0, 'label': u'ESC - \u043e\u0442\u043c\u0435\u043d\u0430', 'source': None, 'mouseDown': u'None', 'backgroundColor': None, 'type': u'Button', '__item_id': 65, '_uuid': u'bd311acf9af0f53f355a4029c284988e', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'name': u'btn_escape', 'mouseUp': None, 'refresh': None, 'alias': None, 'init_expr': None, 'position': (-1, -1), 'onInit': None, 'keyCode': None, 'mouseContextDown': None, 'mouseClick': u"result=None\r\n_esp['_dict_obj']['DlgHlpSprav'].EndModal(wx.ID_CANCEL)\r\n_resultEval=True"}, {'activate': u'0', 'show': u'1', 'mouseClick': u"#try:\r\nresult=HlpSprav(sprav_type,Level=sprav_level+1, ParentCode=result)[1]\r\n_esp['_dict_obj']['DlgHlpSprav'].EndModal(wx.ID_OK)\r\n#except:\r\n#print 'HlpSpravForm Error', sprav_type, sprav_level, result,", 'font': {'style': None, 'name': u'defaultFont', 'family': None, 'faceName': u'', 'type': u'Font', 'underline': 0, 'size': 8}, 'border': 0, 'size': (-1, -1), 'style': 0, 'foregroundColor': None, 'span': (1, 1), 'proportion': 0, 'label': u'\u0421\u043b\u0435\u0434\u0443\u044e\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c >>', 'source': None, 'mouseDown': None, 'backgroundColor': None, 'type': u'Button', '__item_id': 66, '_uuid': u'1984ba95afa7cfc2f425c44045753b16', 'moveAfterInTabOrder': u'', 'flag': 0, 'recount': None, 'keyDown': None, 'name': u'btn_next', 'mouseUp': None, 'refresh': None, 'alias': None, 'init_expr': None, 'position': (-1, -1), 'keyCode': u'None', 'mouseContextDown': u'None'}], 'span': (1, 1), 'border': 0, 'vgap': 0, 'size': (-1, -1)}, {'activate': u'1', 'name': u'ssp_5223_5792', '__item_id': 67, '_uuid': u'22e7212653a1123749fc0cbc370b2fb0', 'proportion': 0, 'flag': 0, 'init_expr': None, 'position': (-1, -1), 'type': u'SizerSpace', 'size': (0, 5)}], 'position': (-1, -1), 'border': 0, 'vgap': 0, 'size': (-1, -1)}], 'setFocus': None, 'name': u'DlgHlpSprav', 'refresh': None, 'alias': None, 'init_expr': None, 'position': (-1, -1), 'onInit': None}, {'style': 0, 'activate': u'1', 'span': (1, 1), 'name': u'imp_580_1067', '__item_id': 68, 'modules': {}, '_uuid': u'dc793e2b008d07efa2c25b3a82391fbe', 'proportion': 0, 'object': None, 'alias': None, 'flag': 0, 'init_expr': u"_dict_obj['ListDS'].SetCursor(0)\r\n#_dict_obj['ListDS'].Focus(0)", 'type': u'Import', 'position': (-1, -1), 'border': 0, 'size': (-1, -1)}], 'type': u'Group', 'name': u'FrmHlpStructSprav'}}