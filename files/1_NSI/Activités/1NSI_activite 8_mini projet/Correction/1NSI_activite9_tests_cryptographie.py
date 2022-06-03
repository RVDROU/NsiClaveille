# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:12:24 2018

@author: herve
"""

from decryptageCheGuevara import *

table=['6','38','32','4','8','30','36','34','39','31','78','72','70','76','9','79','71','58','2','0','52','50','56','54','1','59']
messageSansCle='728226763672902729763624825039972976248726520970768387282287607097632985258452768726763652852587097690976867676976328252585864399729764588248327287632346760728483865871528708760487695870676439854'


TexteDecoupe=decoupeTexteCrypte(messageSansCle,table)
texteClair=decrypteAlphabet(TexteDecoupe,table)
print(texteClair)