#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Библиотека образов.
"""
print('Load Image Library',str(__file__))
#--- Imports ---
from wx import ImageFromStream, BitmapFromImage
from wx import EmptyIcon
import cStringIO
#--- Image Library File ---

#--- BEGIN imgSpeedometer
def getimgSpeedometerData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x00\xc6IDAT8\x8d\xcd\x93\xb1\r\xc20\x10E\xff9a\x04\n:\x16\xa1I\xb2\x05R\
:\x10EX!\x96#\xb1\x01E\x14\xbat\x99\xe2\n\x16\xa1\xa3`\x86\xe4\xa8\x0c\x0e\
\xb2E\xa4\x14\xf0%\x17>\xdd\xf3?\xfb\xcbD*\xc2\x1c\xa9Y\xf4_\x1c\x10\xfb\x8a\
F\xb7\xe2\xabk\x93\x93\xbb\x97\xa1\x17r\x1f\xb1\xa8+Y\xde\xd7_]\xb5\xc9I\x86\
^\x98\xf9}\x85\xa2\xae\xbc\xae>Y8I3\x8a?\xe1\xc7\xea\x86\xf3\xa1$\x1fht+\xa5\
\xde\x82\x99\xb1\xe8:\x00\x00\x1d\x9b\xd3\xc89\x04\xbb\xce\x16\xde4\x17\x1a\
\xa50\x05N\xd2\xec\xd5s\xdd\xefdR\x8c>\xd8\xca\x1b\xa3\x0b\x02@\x08\x06\x00\
\x90\x8a\x82\x0b\x80\x00\x10f\x96POp\x02;6\x80\xb0;\x00\xfa\xf9o|\x02-\xa4\\\
\xf0]\xcb\xf2%\x00\x00\x00\x00IEND\xaeB`\x82' 

def getimgSpeedometerBitmap():
    return BitmapFromImage(getimgSpeedometerImage())

def getimgSpeedometerImage():
    stream = cStringIO.StringIO(getimgSpeedometerData())
    return ImageFromStream(stream)

def getimgSpeedometerIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getimgSpeedometerBitmap())
    return icon

imgSpeedometer=getimgSpeedometerBitmap()

#--- END imgSpeedometer
#--- BEGIN Agent
def getAgentData():
    return '\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\
\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\
\x00\x01XIDAT8\x8d\x9d\x92OJ\xc3@\x14\xc6\x7f/\xf1\x18bO\xe0N\xb7B\xa1\x82G\
\x10*hs\x86\xae{\x82\xae\x8b\xab\xb4\x05\xeb\xf4\x08\x86\x08\x81\x80+\xbbs\
\xd7\xac\xd2\xce\xa2;O\xd0>\x17\x9a1\xff\xa4\xe0\x83\x81o\x86\xf9~\xef{\xc3\
\x88x>\xf5\x1a<\xdc+\xc0t6\x97\xb2n\\\x04\xa4\x0e(\x1b\xb6\x9b\\\x01\xb2,\
\xa3\xdb\xed"\x9e\xdf\x80xm\xd4\xba\x19 \x08\x02\x07?\n\x18<\xdc\xebh4r\xe64\
M\x01\x08\xc3\xb0\x01\x11\xf1|\x9e\x17O\xba^\xaf+\x90<\xcf\t\xc3\xb0\x8d_\
\x19E\xc4\xf3\x1b\xd4N\xa7\xd3j,\xc0EMgs\xa9<\xa2\x1e\xf6\x15P\x10\x04.zY\
\x97\x13\x9c\xd4;<\xf5z\x00\xf4\xe3\x18\x91\xef{\xaa\xeatc\x9cz\x02\xd5\xeaC\
/\xae\xaf\x9d\xbe\x1a\x0e9\xbb\xb9\xf9;\x81x\xbe\x88H\x05\xd2\x8fc\xb6Q\x04\
\xc0\xa7\xb5\x8d\x04\x8d\x11\xca\xb5\x8d"\xd2\xf1\xd8\xed\xcfoo\x8f\x8fP\xe8\
\xcd\xcb\x8b;/:\x7f,\x97\xdc\xbd\xbe\xba\xb4\x85\x00P@\xad\xb5\x9a$\x89\x1ac\
\xb48k[I\x92(\xa0\xe2\xf9xz\xd8\xab\xb5\x16k-Y\x96\xb1\xdb\xed\\\xe7\xd5\xbb\
\xe5q\xf2\xc6\xe3\xe4\x8d\xd5\xfbw\n\xfb\x93\xc6\x18\x83\x1e\xf6z\x02\xbf\
\xff\xbdl6\xc6pqy\xea\x8c\x17\x97\xa7\xadM\xe4\'\xd6\xbf\xeb\x0bg[\xbd\xdd\
\xf8H\xa3\x8a\x00\x00\x00\x00IEND\xaeB`\x82' 

def getAgentBitmap():
    return BitmapFromImage(getAgentImage())

def getAgentImage():
    stream = cStringIO.StringIO(getAgentData())
    return ImageFromStream(stream)

def getAgentIcon():
    icon = EmptyIcon()
    icon.CopyFromBitmap(getAgentBitmap())
    return icon

Agent=getAgentBitmap()

#--- END Agent
