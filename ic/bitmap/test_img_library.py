#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Библиотека образов.
"""
#--- Imports ---
from wx import ImageFromStream, BitmapFromImage
from wx import EmptyIcon
import cStringIO
#--- Image Library File ---


#--- BEGIN Add
def getAddData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00OIDAT8\x8d\xdd\x92A\n\x800\x0c\x04\x93\xf4\xddj\x1en2\xdeD\n\x8a\x90\
\xda\x83\x0b{\xdc\xc9\x1c\xa2jM*\xb1\xd2\xfaS\xc0\xb6.\x90\x01\x19d\xec\xcc7\
x\x1d\xb5v\xd6\xdd\x11\x91\xc7\x02\\7c\r\xeel\xfa\xabC\r\xca\x00\xfd\xf1+O\
\x03\x1c\xa2\x15%\xe0\xea\xaf/F\x00\x00\x00\x00IEND\xaeB`\x82' 

def getAddBitmap():
    return BitmapFromImage(getAddImage())

def getAddImage():
    stream = cStringIO.StringIO(getAddData())
    return ImageFromStream(stream)

def getAddIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAddBitmap())
    return icon

Add=getAddBitmap()

#--- END Add



#--- BEGIN Addres
def getAddresData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x01^IDAT8\x8d\xa5\x93=KBQ\x18\xc7\x7f\xe7\x9e\x9b\xa5\x82\xe6\x12\x81}\
\x00[B-\x02m)\x9a\x15\xa1!\xdaj\nDz\xd9\n\xa2\xc5Z\xa5\xa1\x10\xca1\x9a\xc2>\
@M\x8d-IK_\xa0\x0f\xa0\xa0\xe0\xcb\xbd\x9e\x86\x8b\xe6\xed\\+\xe8\x0fg8\xcf\
\xf3\x7f\x1e~\xe7\xf0<B\x18\x92\xff\xc8\x1c\xbd$\x16\x96\xd58cze\x8b\xab\xf2\
\xa1\xd0\x12\xc2\x90\xc3\x93\x8c\xa7\x94\x97\x92\xf1\x94\xaa\xd7[j}mC\x8d\
\xfa\x85!1~\xc2\xb3,E\xa7\xdd\x07 \x1c\x0ep{w\xc3R'\xed\xa2\xf4l0(\xb4-E\xbb\
\xe3\xf8\x17\x13ir\xd9\x1c\xb6mQ\xbe|\x1e61\xbf\x17w\xda},\x1bL\t\xfb\x07\
\x17\x00T*\xf7\xd4j\x1f\xf8|&\xa5R\xc1\xe5\xd7\x08\xda\x1d\x85\xdfo09\xf5\
\x95\x9a\x99\r\x91\xcd\xcd\x13\x9d\x8bh\xb4\x1aA0h\x90\xcf\x97\\\xb1b\xf1\
\x1a\x80\xe3\xa3]\xad\x81F\xd0j\xf55\xd3@\xcdf\xf7w\x82\xa7\xc7wv\xb67i4zT\
\x1f\xaa\x00\x9c\x9e\x14\x10\x12|\x13\xfa\x9fk\x91X,\n@4\x1a\x1e\xc6\x84\x04\
e{Si\x04\xa1P\x80\xc8t\x10!\xe1\xfcl\x8fn\xcfy\x924%\xa0\x0f\xaaF \rgZ\x95\r\
\xdd^\x9f@\xc0\xd9\x15\xdb\xf2F\xd0\x082\x99Uo\xd61r5x}{\x11\xa3S\xf6\x17\
\x89\xff\xae\xf3\'\xaf6yd\xef\xdd,5\x00\x00\x00\x00IEND\xaeB`\x82' 

def getAddresBitmap():
    return BitmapFromImage(getAddresImage())

def getAddresImage():
    stream = cStringIO.StringIO(getAddresData())
    return ImageFromStream(stream)

def getAddresIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAddresBitmap())
    return icon

Addres=getAddresBitmap()

#--- END Addres



#--- BEGIN Adduser
def getAdduserData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00\xeaIDAT8\x8d\x95\x93=\x0e\x82@\x14\x84g\x81cp\x02--,LH4\x9c\xc0\x9e\
\xde\x18\xa5\xa2\xe6\xa7\xa7\x12b\xec5\xa1\xf3\x08\x90\x98XZ\xea\t8\x82\xad\
\xae\x05\xd9\xcd\xe3\'\xeb2\x15\xc9\xdb\xf9\x98\xd9\x07\x8c\x19&T\xe2\xdf\
\x0f\x17\xcf\xcc0Ywn\xe8\x98\xeb\xba\xee\xc1\xb4\x00\xd4\\\x14\xc5\xe0\x9c\
\xd1\n\xe7\xd5R\xbe\xc1++F\x13\xd8\xb6\xdd\x18:5z\t\x9c \x90q\xf7\xbb\x03\
\x00H\xf3P\rK\x15\x7f:\x99A@\xa8\xb2\xdc\xe7'\x89EcS]\\\x17\xb8F\x98\x03x\
\xaf\x13\x00\xc0\xf3\xf5\xe8\x9d\xb3h\xecn\r\x00\xb8\xa5\xa9*d\x03\xa0\x87\
\x9c \xf8kj\x01\xbc\xb2\x92\xb7:\xb4\x85\xd3\xf1\xae\x04\xfc\xfd\x0e\x84D\
\xff,\xf7[\xab\xec\x01\xc6\xc4\x07:k\xa4ut\xa5]\x81*\x8eB\x1eG!\xd7\x02l\xb6\
\x0b%\x88\x8d\xf9\x9d\x01 I\x92\xd6\xfc\x07|KaaO\xb8sZ\x00\x00\x00\x00IEND\
\xaeB`\x82' 

def getAdduserBitmap():
    return BitmapFromImage(getAdduserImage())

def getAdduserImage():
    stream = cStringIO.StringIO(getAdduserData())
    return ImageFromStream(stream)

def getAdduserIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAdduserBitmap())
    return icon

Adduser=getAdduserBitmap()

#--- END Adduser
#--- BEGIN Add_row
def getAdd_rowData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x02\
\x00\x00\x00\x90\x91h6\x00\x00\x00\x03sBIT\x08\x08\x08\xdb\xe1O\xe0\x00\x00\
\x00UIDAT(\x91\x9d\x92A\x0e\xc0 \x0c\xc3\x9c\x89\xff\x7f9;\x0c\xc4\x81\t\x1a\
rEFN[\xd9&J\n\xb4\x14{2\x9f\x0b\xa0+!\x01*\x00\xea\xf6\x12\x80-i\xdfG?\x8f[\
\xe0\xa2\xb4=\xbf\xb4\xcf5>cCq\x11cJ\x03+(\x85\x89\x81\xf8\xf8\x0ekZ\xf3\x02\
\x9e\xcc'\xfeQ\xd7\xb2\xd3\x00\x00\x00\x00IEND\xaeB`\x82' 

def getAdd_rowBitmap():
    return BitmapFromImage(getAdd_rowImage())

def getAdd_rowImage():
    stream = cStringIO.StringIO(getAdd_rowData())
    return ImageFromStream(stream)

def getAdd_rowIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAdd_rowBitmap())
    return icon

Add_row=getAdd_rowBitmap()

#--- END Add_row
#--- BEGIN Add_col
def getAdd_colData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x02\
\x00\x00\x00\x90\x91h6\x00\x00\x00\x03sBIT\x08\x08\x08\xdb\xe1O\xe0\x00\x00\
\x00UIDAT(\x91\xed\x92A\x0e\xc0 \x08\x04w\x1a\xff\xffe<\xb4\x1a\x05\xb4\xf1\
\xd0[\xf7D\x02\xb3,\t\x98\x99\xa2@\x92\xb2V\xe1\xee5E\xde\r0N\x00\xd1\x93\
\xd9\xe5J\xf2lU\xa2\x9f$\x1b\xea\x17\xe0\xd9\x0e\xbdv7x\xa0s\xabH\xc77\xfc\
\xc0'\x00\xf9{\xafU\x01me\x1b\x1e\x14t%\x1c\x00\x00\x00\x00IEND\xaeB`\x82' 

def getAdd_colBitmap():
    return BitmapFromImage(getAdd_colImage())

def getAdd_colImage():
    stream = cStringIO.StringIO(getAdd_colData())
    return ImageFromStream(stream)

def getAdd_colIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAdd_colBitmap())
    return icon

Add_col=getAdd_colBitmap()

#--- END Add_col

#--- BEGIN ggggg
def getgggggData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x01\rIDAT8\x8dcddbf\xa0\x04\xb0\xe0\x920\xd43\xfb\x8f\xcc?\x7f\xe9\x14#\
6uL\xf8L?{\xfe\x18\xc3\xd9\xf3\xc7\x18\x18\x18\x18\x18\xa6O9\xf4\x1f\x9b\x1a\
\xbc\x06\x10\x03(6\x00g\x180000|\xfd\xfa\x9d\xe1\xc7\x8f?x\r`ddb\xc6\x080\
\x18\xd8\xb5g'\xc3\x87\x0f_\x18\xc2B\x82\xb1j>\x7f\xe9\x14#\xdc\x80\xc9S\x17\
10000HJ\xf21\xb0\xb223\xfc\xfe\xfd\x97\xe1\xf9\xf3O\x0cO\x1e}bx\xff\xfe\x07\
\x83\xae\xbe\x18\x83\x9c\x9c \\\xb3\xbf\xaf/CZZ\x0f\xc2\x0b\x97/\xbeb````x\
\xf2\xe8\x13\\\xd1\xfb\xf7?\x18\xd8\xd9\xfe1\xe8\xeaK\xc05\xcb\xc8\x08\xa3\
\xb8\x02n\xc0\xacY%\x18N\xec\xed\x9b\xcb +'\x80\xd3\x0bp\x03\xce_:\xc5\x88\
\x1e\xcf\xb3f\x950\xa8\xa8\x8a\xc1\xf9ii=\xb8\r````\xc8\xcc\xb1CIi\xd8\x02\
\x16]\r\x03\x03\x11\xe9\x00\xdd\xcf$\x1b@\x08\xe0MH\xfe\xbe\xbe\xe4\x1b\x80-\
`\xb1\x01\x00\xb5\x95O\x83\xcf\xa1\xb5n\x00\x00\x00\x00IEND\xaeB`\x82' 

def getgggggBitmap():
    return BitmapFromImage(getgggggImage())

def getgggggImage():
    stream = cStringIO.StringIO(getgggggData())
    return ImageFromStream(stream)

def getgggggIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getgggggBitmap())
    return icon

ggggg=getgggggBitmap()

#--- END ggggg
