# -*- coding: utf-8 -*-
"""Created on Sun Sep 11 13:57:23 2022@author: xiaom"""

#======================= DATAFRAME pandas
import pandas as pd

############ HOW TO CREATE   DATAFRAME 1
# 1st from dictionaries
# method              dictionary of lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

cars_dict = {'country': names, 'drives_right': dr, 'cars_per_capita': cpc}
cars = pd.DataFrame(cars_dict)
cars.index = row_labels

###########################
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

# ==================== HOW TO CREATE   DATAFRAME   2 
#                   list of lists

feature_names = ['CountryName',
 'CountryCode',
 'IndicatorName',
 'IndicatorCode',
 'Year',
 'Value']
row_lists = [['Arab World',
  'ARB',
  'Adolescent fertility rate (births per 1,000 women ages 15-19)',
  'SP.ADO.TFRT',
  '1960',
  '133.56090740552298'],
 ['Arab World',
  'ARB',
  'Age dependency ratio (% of working-age population)',
  'SP.POP.DPND',
  '1960',
  '87.7976011532547'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, old (% of working-age population)',
  'SP.POP.DPND.OL',
  '1960',
  '6.634579191565161'],
 ['Arab World',
  'ARB',
  'Age dependency ratio, young (% of working-age population)',
  'SP.POP.DPND.YG',
  '1960',
  '81.02332950839141'],
 ['Arab World',
  'ARB',
  'Arms exports (SIPRI trend indicator values)',
  'MS.MIL.XPRT.KD',
  '1960',
  '3000000.0'],
 ['Arab World',
  'ARB',
  'Arms imports (SIPRI trend indicator values)',
  'MS.MIL.MPRT.KD',
  '1960',
  '538000000.0'],
 ['Arab World',
  'ARB',
  'Birth rate, crude (per 1,000 people)',
  'SP.DYN.CBRT.IN',
  '1960',
  '47.697888095096395'],
 ['Arab World',
  'ARB',
  'CO2 emissions (kt)',
  'EN.ATM.CO2E.KT',
  '1960',
  '59563.9892169935'],
 ['Arab World',
  'ARB',
  'CO2 emissions (metric tons per capita)',
  'EN.ATM.CO2E.PC',
  '1960',
  '0.6439635478877049'],
 ['Arab World',
  'ARB',
  'CO2 emissions from gaseous fuel consumption (% of total)',
  'EN.ATM.CO2E.GF.ZS',
  '1960',
  '5.041291753975099'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (% of total)',
  'EN.ATM.CO2E.LF.ZS',
  '1960',
  '84.8514729446567'],
 ['Arab World',
  'ARB',
  'CO2 emissions from liquid fuel consumption (kt)',
  'EN.ATM.CO2E.LF.KT',
  '1960',
  '49541.707291032304'],
 ['Arab World',
  'ARB',
  'CO2 emissions from solid fuel consumption (% of total)',
  'EN.ATM.CO2E.SF.ZS',
  '1960',
  '4.72698138789597'],
 ['Arab World',
  'ARB',
  'Death rate, crude (per 1,000 people)',
  'SP.DYN.CDRT.IN',
  '1960',
  '19.7544519237187'],
 ['Arab World',
  'ARB',
  'Fertility rate, total (births per woman)',
  'SP.DYN.TFRT.IN',
  '1960',
  '6.92402738655897'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions',
  'IT.MLT.MAIN',
  '1960',
  '406833.0'],
 ['Arab World',
  'ARB',
  'Fixed telephone subscriptions (per 100 people)',
  'IT.MLT.MAIN.P2',
  '1960',
  '0.6167005703199'],
 ['Arab World',
  'ARB',
  'Hospital beds (per 1,000 people)',
  'SH.MED.BEDS.ZS',
  '1960',
  '1.9296220724398703'],
 ['Arab World',
  'ARB',
  'International migrant stock (% of population)',
  'SM.POP.TOTL.ZS',
  '1960',
  '2.9906371279862403'],
 ['Arab World',
  'ARB',
  'International migrant stock, total',
  'SM.POP.TOTL',
  '1960',
  '3324685.0']]

row_lists[0]

# method of creating DF: from LIST + add columns names
df = pd.DataFrame(row_lists)
df.columns = feature_names 

# ==================== HOW TO CREATE   DATAFRAME  3
# 3nd method of creating DF: from DICT
# DF use dict's keys as a colums name
#                                       list of dictionaries
def lists2dict(list1 , list2):
    return dict(zip(list1, list2))
     
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
df2 = pd.DataFrame(list_of_dicts)
df2.info()
#================== Iterator + chunk loading file
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)


######### ?

#test - how to get all row in indicator_name which starts from CO2?? simple
df[df['IndicatorName'] == 'CO2 emissions (kt)']

################
# For each store type, aggregate unemployment and fuel_price_usd_per_l: 
    #get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')
[['unemployment','fuel_price_usd_per_l']].agg([min,max,np.mean,np.median])



#####################################    groupby
df['Year'] = df['Year'].astype(int) #convert strings in column to int
df.dtypes
df_yearsummary1 = df.groupby('CountryCode')['Year'].sum()
df_yearsummary2 = df.groupby(['CountryName','CountryCode'])['Year'].sum()
type(df_yearsummary2)

print(df_yearsummary2)
df_yearsummary2.dtypes
df_yearsummary2.info() 
# you can see that <class 'pandas.core.series.Series'>
# Series name = values in it


#####################################