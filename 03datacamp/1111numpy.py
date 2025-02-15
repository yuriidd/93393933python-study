# -*- coding: utf-8 -*-
"""Created on Sat Jul 16 07:31:47 2022@author: xiaom"""

import numpy as np

g = [2,3,4,5,4,3,1,6]
gg = np.array(g)
r = gg > 3
gg[gg> 3]
gg[r]
gg[gg == 3]
print(2+gg[r][0:2])

gg[r][0:2]
np.array([True, 1, 2]) + np.array([3, 4, False])

x = ["a", "b", "c"]
x[1]

np_x = np.array(x)
np_x[1]

np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)

np_mat[:,0:1]

np_matte = np.array([[1, 2,9],
                   [3, 4,7],
                   [5, 6,5]])
np_matte[:,0:2]
np_matte[:,2] == np_matte[:,2:3]
np_matte.index(np_matte>2)

x = ["Jan","Feb","Mar","Apr"]
x[0] = 'July'
x = np.array([[1, 2, 7],
              [7, 7, 1]])
y = np.array([[6, 5, 5], 
              [0, 6, 1]])

x+y
############################
gg.dtype


