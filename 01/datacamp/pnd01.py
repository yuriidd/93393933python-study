# -*- coding: utf-8 -*-
"""Created on Sun Sep 11 13:57:23 2022@author: xiaom"""

#======================= DATAFRAME pandas
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars_dict = {'country':names, 'drives_right': dr, 'cars_per_capita': cpc}
cars = pd.DataFrame(cars_dict)
cars.index = row_labels

cars.iloc[[3]]

# Series
print(cars.loc['JPN'])
print(cars.iloc[2])
print(type(cars.loc['JPN']))
cars.loc[:, 'drives_right']
cars.iloc[:, 2]

# DataFrame
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1,6]])
print(type(cars.iloc[[1,6]]))
cars.loc[:, ['drives_right']]
cars.iloc[:, [2]]


# ====================
whois128 = pd.read_csv('D:/py/93393933python-study/dc/somedata/geofeeds.csv')
# imported, but CSV has no zero row with column label?
# how to fix it at ?
whois128 = pd.read_csv('D:/py/93393933python-study/dc/somedata/geofeeds.csv', 
                       index_col = 1)

whois128['RO-B']
whois128.iloc[[5]]
whois128.iloc[[0]]

# ====================
#np arrays
.logical_and()
.logical_or()
.logical_not()

import numpy as np
cpc = [809, 731, 588, 18, 200, 70, 45]
cpcqwe = np.array(cpc)

cpcqwe < 100
#Out[23]: array([False, False, False,  True, False,  True,  True])

np.logical_and(cpcqwe > 100, cpcqwe < 800)
#Out[24]: array([False,  True,  True, False,  True, False, False])
cpcqwe[np.logical_and(cpcqwe > 100, cpcqwe < 800)]
#Out[25]: array([731, 588, 200])

# ==================== FILTERING
'''use cars dataset'''

cars['drives_right']
dr = cars['drives_right']
select = cars[dr]
print(select)


# ====================  FOR
for l, row in cars.iterrows():
    pass

for lab, row in cars.iterrows():
    print(lab)
    print(row)
    print()
cars
cars.loc['RU', "new_col"] = 1
# method 1 - low eff
for lab, row in cars.iterrows():
    cars.loc[lab, "new_col"] = len(row['country'])

print(cars)
cars.loc[['RU'],['country']]

# method 2 - best way
cars["new_col"] = cars['country'].apply(len)

print(cars.loc[['RU'],['country']])

cars[['country']]

