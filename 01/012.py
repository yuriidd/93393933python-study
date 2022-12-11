# -*- coding: utf-8 -*-
"""Created on Tue Sep  6 20:51:18 2022@author: xiaom"""

############################# 



import builtins
a = dir(builtins)

for x in dir(builtins):
    i = 1
    if x.find('tuple') >=0:
        print(str(x) + ' yes' + str(i))
        i += 1
'ArithmeticErrorsum'.find('sum')
