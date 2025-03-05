#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:33:56 2025 @author: yurii
"""

#  DataCamp - Data Engineer in Python
# ###################################             IMPORT DATA 1
# ################################### 
# ################################### 

# ###################################             file > python
# 1
filename = 'he_powd.txt'
file = open(filename, mode='r')   # 'r' is read
file.close()

# 2
with open(filename, 'w') as file: # 'w' is write
    print(file.read())


# ###################################           file > NumPY
# 1
import numpy as np
filename = 'MNIST.txt'
data = np.loadtxt(filename, delimiter = ',') # '\t'
data = np.loadtxt(filename, delimiter = ',', skiprows = 1)
data = np.loadtxt(filename, delimiter = ',', dtype = str, usecols = [1, 2, 5])


# ###################################           file > pandas
# 1
import pandas as pd
filename = 'winerrwe-black.csv'
data = pd.read_csv(filename)    # DataFrame
# , nrows = 5           specify how many rows to read
# , header = None , comment='#' , 
# , sep=','  '\t'      separator
# , na_values=[____] list to identify null values NA / NaN / 'Nothing' etc
data.head()
data.to_numpy()       # convert to numpy array


# ################################### 
# ###################################           pickled files > python  
#
import pickle
with open('pickled_fruit.pkl', 'rb') as file:
    data = pickle.load(file)


# ###################################               Excel >> pandas
import pandas as pd
file = 'urbanpop.xlsx'
data = pd.ExcelFiles(file)
print(data.sheet_names)     # >> ['1960-1966', '1967-1974', '1975-2011']

df1 = data.parse('1960-1966')   # sheet name as string
df2 = data.parse(0)             # sheet index, as a float
# .parse(0, skiprows= [1], names= ['col1_newname','col2_newname', ..])
# .parse(0, usecols=[0,1,3,6])


# ###################################           SAS, stata >> pandas
import pandas as pd
from sas7bdat import SAS7BDAT 
with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()
    
data = pd.read_stata('urbanpop.dta')  # stata


# ###################################               HDF5 >> 
import h5py
filename = 'H-H1_LOSC_4_V1_815411200-4096.hdf5'
data = h5py.File(filename, 'r')
print(type(data))   # <class 'h5py._hl.files.File'>

for key in data.keys():   # as dict
    print(key)         #      meta , quality , strain   

print( np.array(data['meta']['Description']) ) 


# ###################################               scipy >>
import scipy
filename = 'workspace.mat'
mat = scipy.io.loadmat(filename)
print(type(mat))   # dict


# ###################################           SQL database connect
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Northwind.sqlite')
table_names = engine.table_names()
print(table_names)    # table names as a list


# ###################################           SQLAlchemy > SQL db >> pandas 
# 1
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.sqlite')
con = engine.connect()
rs = con.execute("SELECT * FROM orders")
df = pd.DataFrame(rs.fetchall())   
df.columns = rs.keys()     
con.close()    # !

print(df.head())

# 2
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')

with engine.connect() as con:    # and no con.close()
    rs = con.execute("SELECT * FROM orders")
    df = pd.DataFrame(rs.fetchall())   # pd.DataFrame(rs.fetchmany(5)) 
    df.columns = rs.keys()     

print(df.head())


# ###################################       pandas > SQL db >> pandas    !!!
#
engine = create_engine('sqlite:///Northwind.sqlite')
df = pd.read_sql_query("SELECT * FROM orders", engine)


# %%#################################             
# ###################################               IMPORT DATA 2
# ################################### 

# ###################################               web flat >> python
# 1
from urllib.request import urlretrieve
url = 'http://archive.edu/ssdfsfsdf.csv'
urlretrieve(url, 'ssdfsfsdf.csv')   # saves file locally
df = pd.read_csv('ssdfsfsdf.csv', sep=';')  # as usual

# 2
import pandas as pd
df = pd.read_csv(url, sep=';')  # put URL direct to pd.read_csv()


# ###################################               web Excel >> pandas
import pandas as pd
url = 'http://archive.edu/ssdfsfsdf.csv'
xls = pd.read_excel(url, sheet_name=None) # read_excel() is a dict
print(xls.keys())


# ###################################               web GET http >> python
# 1
from urllib.request import urlopen, Request 
url = 'https://www.wikipedia.org'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()

# 2
import requests
url = 'https://www.wikipedia.org'
r = requests.get(url)
text = r.text

# 3
from bs4 import BeautifulSoup
import requests
url = 'https://www.crummy.com/software/BeautifulSoup/'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc)

print(soup.prettify()) # prints as formatted html
print(soup.title)      # as attribute
print(soup.get_text())

for link in soup.find_all('a'):
    print(link.get('href'))


# ###################################               JSON >> python
import json
with open('unicorns.json', 'r') as json_file:
    json_data = json.load(json_file)
print(json_data)   # >> dict

# if nested or varying "schema" you should iterate over dictionary components
type({    
 "863703000": {        
     "price": {            
         "open": 0.12187,            
         "close": 0.09791        
         },        
     "volume": 1443120000    
 },     
 "863789400": {    
 }
})

for key in raw_data.keys():             # Loop over keys
    # code
for value in raw_data.values():         # Loop over values
    # code
for key, value in raw_data.items():     # Loop over keys and values
    # code

volume = entry.get("volume")    # Parse data from dictionary using .get()
ticker = entry.get("ticker", "DCMP")
# Call .get() twice to return the nested "open" value
open_price = entry.get("price").get("open", 0)

# ### 1
parsed_stock_data = []
# Loop through each key-value pair of the raw_stock_data dictionary
for timestamp, ticker_info in raw_stock_data.items():
    parsed_stock_data.append([
        timestamp,
        ticker_info.get("price", {}).get("open", 0),  # Parse the opening price
        ticker_info.get("price", {}).get("close", 0),  # Parse the closing price
        ticker_info.get("volume", 0)  # Parse the volume
        ])
# Create a DataFrame, assign column names, and set an index
transformed_stock_data = pd.DataFrame(parsed_stock_data)
transformed_stock_data.columns = ["timestamps", "open", "close", "volume"]
transformed_stock_data = transformed_stock_data.set_index("timestamps")

# ### 2
{
    "01M539": {
        "street_address": "111 Columbia Street",
        "city": "Manhattan",
        "scores": {
              "math": 657,
              "reading": 601,
              "writing": 601
        }
  }, ...
}
normalized_testing_scores = []
for school_id, school_info in raw_testing_scores.items():
	normalized_testing_scores.append([
    	school_id,
    	school_info.get("street_address"),  # Pull the "street_address"
    	school_info.get("city"),
    	school_info.get("scores").get("math", 0),
    	school_info.get("scores").get("reading", 0),
    	school_info.get("scores").get("writing", 0),
    ])
print(normalized_testing_scores[:2])
[['02M260', '425 West 33rd Street', 'Manhattan', None, None, None], 
 ['06M211', '650 Academy Street', 'Manhattan', None, None, None]]
# then to df with separate created columns



# ###################################               API > JSON >> python
import requests
url = 'https://www.omdbapi.com/?t=hackers'
r = requests.get(url)
json_data = r.json()  # >> dict

# for key, value in json_data.items():
#     print(key + ':', value)

import json
json_from_string = json.loads(r.text) #alternative, but long way to take a dict


# ###################################               [list of dict] >> pandas
import pandas as pd
# tweets_data is a list of dictionaries
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])


# ###################################               [list of lists] >> pandas
df = pd.DataFrame(flattened_rows)
df.columns = ['timestamps', 'open', 'close', 'volume']
df.set_index('timestamps')



# %%#################################             
# ###################################               CLEANING DATA
# ################################### 

# ###################################               

df.info() 
df['user_type'].describe() 

df['user_type_cat'] = df['user_type'].astype('category') # change column type
df['user_type_cat'].dtype # it's category now
assert df['user_type_cat'].dtype == 'category'# do nothing if True either Error

df['duration_trim'] = df['duration'].str.strip('minutes')


# ###################################               OUT of RANGE values

df[df['avg_rating'] > 5]   # rating shoudn't be more than 5

# DROP
df = df[df['avg_rating'] <= 5] # DROP values using filtering
df.drop(df[df['avg_rating'] > 5].index, inplace = True)#DROP values using .drop()

# convert
df.loc[df['avg_rating'] > 5, 'avg_rating'] = 5 # avg_rating > 5 become 5
assert df['avg_rating'].max() <= 5

# dates
df['date_dt'] = pd.to_datetime(df['date_str']).dt.date  # convert to date

today_date = dt.date.today()
df = df[df['date_dt'] < today_date] # DROP values using filtering
df.drop(df[df['date_dt'] > today_date].index, inplace = True)# using .drop()
df.loc[df['date_dt'] > today_date, 'date_dt'] = today_date
assert df.date_dt.max().date() <= today_date


# ###################################               DUPLICATES

duplicates = df.duplicated()  # duplicates is True False massive
df[duplicates]      # see them

#
column_names = ['first_name', 'last_name', 'address']
duplicates = df.duplicated(subset = column_names, keep = False)
# keep: Whether to keel ('first'), ('last') or all ('False') duplicates values
df[duplicates].sort_values('first_name')

df.drop_duplicates(inplace = True)
# inplace : drops duplicated rows inside DF w/o creating new object (!)

# treat duplications
column_names = ['first_name', 'last_name', 'address']
summaries = {'height': 'max', 'weight': 'mean'} # aggregation
df = df.groupby(by = column_names).agg(summaries).reset_index()

assert df.shape[0] == 0 # Assert duplicates are processed


# ###################################               INCONSISTENT values

# set differences to find uniq values, that is inconsistent >> {'Z+', ..} etc
inconsistent_categories = set(df['cat_type']).difference(df2['cat_type'])

inconsistent_rows = df['cat_type'].isin(inconsistent_categories) # bool
df[inconsistent_rows]  #see inconsistents row with all columns
inconsistent_data = df[inconsistent_rows]

consistent_data = df[~inconsistent_rows] # drop incons. and get cons. data only
# df['cat_type'].unique()

# ## value consistency
df['status'] = df['status'].str.upper()  # .str.lower() .capitalize()
df['status'].values_counts()
df['status'] = df['status'].str.strip()  # strip whitespacesscatterplo

# 1 create categories
group_names = ['0-200K', '200K-500K', '500K+']
df['income_group'] = pd.qcut(df['income'], q = 3, labels = group_names)
print(df[['income_group', 'income']])
#   income_group   income
#   200K-500K      189000  # ?? sometimes it happens - incorrect quick-cut

# 2 create categories
ranges = [0, 200000, 500000, np.inf]  # numpy as np
group_names = ['0-200K', '200K-500K', '500K+']
df['income_group'] = pd.cut(df['income'], bins = ranges, labels = group_names)

# ## map categories
mapping = {'Microsoft':'DesktopOS', 'MacOS':'DesktopOS', 'Linux':'DesktopOS',
           'IOS':'MobileOS', 'Android':'MobileOS'}
df['operating_system'] = df['operating_system'].replace(mapping)
df['operating_system'].unique()

# ## fixind strings
df['phone_num'] = df['phone_num'].replace('+', '00') 

#
digits = phones['phone_num'].str.len()
phones.loc = [digits < 10, 'phone_num'] = np.nan  # NaN

assert phones['phone_num'].str.len().min() >= 10
assert phones['phone_num'].str.contains('+|-').any() == False

df['phone_num'] = df['phone_num'].str.replace(r'\D+', '') # regexp 

# 1 assess and replace values
df_filtered = df.loc[df['temperatures'] > 40, 'temperatures'] # ?
df_fixed_range = (df_filtered - 32) * (5/9)
df.loc[df['temperatures'] > 40, 'temperatures'] = df_fixed_range

assert df['temperatures'].max() < 40

# 2 assess and replace date values
pandas.to_datetime() # do most you need

#
df['birth'] = pd.to_datetime(df['birth']) # ValueError: month must be in 1..12
df['birth'] = pd.to_datetime(df['birth'], 
                             infer_datetime_format = True, 
                             errors = 'coerce') # returns NA for failed
df['birth'] = df['birth'].dt.strftime('%d-%m-%Y')

# example
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
assert banking['acct_cur'].unique() == 'dollar' # check if only dollars left

# crossfield validation 1 nums
sum_classes = flights[['econom_cl', 'business_cl', 'first_cl']].sum(axis = 1) #
passenger_equ = sum_classes == flights['total_passengers']
consistent_pass = flights[passenger_equ]
inconsistent_pass = flights[~passenger_equ]

# crossfield validation 2 dates
df['birth'] = pd.to_datetime(df['birth'])
today = dt.date.today()
age_manual = today.year - df['birth'].dt.year
age_equ = age_manual == df['age'] # check with just calculated
consistent_pass = df[age_equ]
inconsistent_pass = df[~age_equ]

# ## missing values, NA, NaN etc
"""
Missing Completely at Random: No systematic relationship between a column's 
        missing values and other or own values.
Missing at Random: There is a systematic relationship between a column's 
        missing values and other observed values.
Missing not at Random: There is a systematic relationship between a column's 
        missing values and unobserved values."""


df.isna() # bool, show missing values
df.isna().sum()

import missingno as msno              # we can plot them
import matplotlib.pyplot as plt
msno.matrix(df) # or choose your columns
plt.show()

missing = df[df['col2'].isna()]
complete = df[~df['col2'].isna()]

missing.describe() #  complete.describe()

sorted_df = df.sort_values(by = 'col1')  # replot
msno.matrix(sorted_df)
plt.show()

df_dropped = df.dropna(subset = ['col2']) # drop NA
col2_mean = df['col2'].mean()                # or take mean of entire column
df_imputed = df.fillna({'col2': col2_mean})  # and replace NA

df.fillna(value={"open": 0, "close": .5}, axis=1)
df["open"].fillna(df["close"], inplace=True)  # replace by next column value

# ###################################               STRING comparison
from thefuzz import fuzz
fuzz.WRatio('Reeding', 'Reading') # >> 86

from thefuzz import process
string = 'Houston Rockets vs Loas Angeles Lakers'
choises = pd.Series(['Rockets vs Lakers', 'Lakers vs Rockets',
                     'Houston vs Los Angeles', 'Heat vs Bulls'])
process.extract(string, choices, limit = 2)
# >> [('Rockets vs Lakers', 86, 0),('Lakers vs Rockets', 86, 1)]

for state in categories['state']: # match and replace with correct values
    match = process.extract(state, survey['state'], limit = survey.shape[0])
    for potencial_match in matches:
        if potencial_match[1] >= 80:
            survey.loc[survey['state'] == potencial_match[0], 'state'] = state

# ###################################               RECORD LINKAGE 
import recordlinkage

indexer = recordlinkage.Index()
indexer.block('state') # generate pairs blocked on state column
pairs = indexer.index(census_A, census_B)

compare_cl = recorslinkage.Compare() # compare object
compare_cl.exact('date_of_birth', 'date_of_birth', label = 'date_of_birth')
compare_cl.exact('state', 'state', label = 'state')
compare_cl.string('surname', 'surname', theshold = 0.85, label = 'surname')
compare_cl.string('address_1', 'address_1', threshold = 0.85, label = 'address_1')

potential_matches = compare_cl.compute(pairs, census_A, census_B)
# finding the only pairs we want
matches = potential_matches[potential_matches.sum(axis = 1) >= 3 ]

matches.index
diplicate_rows = matches.index.get_level_values(1)
print(census_B_index) # ?? census_B.index maybe

# findinng duplicates in census_B dataframe
census_B_duplicates = census_B[census_B.index.isin[diplicate_rows]]
# finding new rows in census_B
census_B_new = census_B[~census_B.index.isin(duplicate_rows)]

full_census = census_A.append(census_B) # end


# %%#################################             
# ###################################             Writing EFFICIENT Python Code
# ###################################

# ############ map()
nums = [1.5, 2.3, 3.4, 4.5, 5.0]
rnd_nums = map(round, nums)
print(list(rnd_nums))

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

names_map  = map(str.upper, names) # Use map to apply str.upper to each element in names
print(type(names_map)) # Print the type of the names_map
names_uppercase = [*names_map] # Unpack names_map into a list

# ############ lambda
sqrd_nums = map(lambda x: x ** 2, rnd_nums)

# ############ enumerate()
# 1
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name) 
print(indexed_names)

# 2
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# 3
indexed_names_unpack = [*enumerate(names, start = 1)]
print(indexed_names_unpack)


# ###################################           RUNTIME
import timeit
# %timeit - single line
%timeit random_nums = np.random.rand(1000) # measures runtime with %timeit
%timeit  -r2 -n10 random_nums = np.random.rand(1000) # -r runs, -n loops

times = %timeit  -o random_nums = np.random.rand(1000) # -o save to a variable
times.timings
times.best
times.worst

#' %%timeit - cell mode
%%timeit
nums = []
for x in range(10):
    nums.append()

#
f_time = %timeit -o format_dict = dict()
l_time = %timeit -o format_dict = {}
diff = (f_time.average - l_time.average) * 

%timeit [num for num in range(51)]
%timeit [*range(51)]


# ###################################           RUNTIME code profiling
pip install line_profiler
import line_profiler

#
import numpy as np
heroes = ['Batman', 'Superman', 'Wonder Woman']
hts = np.array([188.0, 191.0, 183.0])
wts = np.array([95.0, 101.0, 74.0])

# 1
def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]
    hero_data = {}
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data

convert_units(heroes, hts, wts)
print(convert_units(heroes, hts, wts))
'''{'Batman': (np.float64(74.01559999999999), np.float64(209.4389)), 
    'Superman': (np.float64(75.19669999999999), np.float64(222.66661999999997)), 
    'Wonder Woman': (np.float64(72.0471), np.float64(163.14188))}'''

%load_ext line_profiler
%lprun -f       # -f for functions
%lprun -f convert_units convert_units(heroes, hts, wts) # line-by-line times

'''Timer unit: 1e-09 s

Total time: 2.5244e-05 s
File: /tmp/ipykernel_22833/3822844671.py
Function: convert_units at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units(heroes, heights, weights):
     2         4      16186.0   4046.5     64.1      new_hts = [ht * 0.39370  for ht in heights]
     3         4       2959.0    739.8     11.7      new_wts = [wt * 2.20462  for wt in weights]
     4         1        350.0    350.0      1.4      hero_data = {}
     5         4       3370.0    842.5     13.3      for i, hero in enumerate(heroes):
     6         3       1508.0    502.7      6.0          hero_data[hero] = (new_hts[i], new_wts[i])
     7         1        871.0    871.0      3.5      return hero_data'''
# list comprehention uses amount of %time (at datacamp example)

# 2
def convert_units_broadcast(heroes, heights, weights):
    new_hts = heights * 0.39370 # Array broadcasting instead of list comprehension
    new_wts = weights * 2.20462
    hero_data = {}
    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data

%load_ext line_profiler
%lprun -f convert_units_broadcast convert_units_broadcast(heroes, hts, wts)

'''Timer unit: 1e-09 s

Total time: 5.7318e-05 s
File: /tmp/ipykernel_22833/681880844.py
Function: convert_units_broadcast at line 1

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     1                                           def convert_units_broadcast(heroes, heights, weights):
     2         1      38084.0  38084.0     66.4      new_hts = heights * 0.39370 # Array broadcasting instead of list comprehension
     3         1       9813.0   9813.0     17.1      new_wts = weights * 2.20462
     4         1        267.0    267.0      0.5      hero_data = {}
     5         4       3715.0    928.8      6.5      for i,hero in enumerate(heroes):
     6         3       4725.0   1575.0      8.2          hero_data[hero] = (new_hts[i], new_wts[i])
     7         1        714.0    714.0      1.2      return hero_data
'''
# in my local test array operations takes more time (((((


# ###################################   RUNTIME code profiling for MEMORY USAGE
pip install line_profiler
import memory_profiler

#
import sys

nums_list = [*range(1000)]
sys.getsizeof(nums_list)    # >> 8056

nums_np = np.array(range(1000))
sys.getsizeof(nums_np)      # >> 8112

# #######
'''Functions must be imported when using `memory_profiler`
    example: hero_funcs.py                                '''
from hero_funcs import convert_units
%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes, hts, wts)

#
import os
#print(os.getcwd()) #os.chdir('../03datacamp/somedata')
os.chdir('/home/yurii/git/93393933python-study/03datacamp/somemodules')
from hero_funcs import convert_units
%load_ext memory_profiler
%mprun -f convert_units convert_units(heroes, hts, wts)

'''Filename: /home/yurii/git/93393933python-study/03datacamp/somemodules/hero_funcs.py

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     9    132.1 MiB    132.1 MiB           1   def convert_units(heroes, heights, weights):
    10    132.1 MiB      0.0 MiB           4       new_hts = [ht * 0.39370  for ht in heights]
    11    132.1 MiB      0.0 MiB           4       new_wts = [wt * 2.20462  for wt in weights]
    12    132.1 MiB      0.0 MiB           1       hero_data = {}
    13    132.1 MiB      0.0 MiB           4       for i, hero in enumerate(heroes):
    14    132.1 MiB      0.0 MiB           3           hero_data[hero] = (new_hts[i], new_wts[i])
    15    132.1 MiB      0.0 MiB           1       return hero_data
'''


# ###################################                   Gaining efficiencies         

# ###################################           Counting

# 1, standard version
poke_types = ['Grass', 'Dark', 'Fire', 'Fire', ...] # Pokémon's type (720 total)
type_counts = {}
for poke_type in poke_types:
    if poke_type notin type_counts:        
        type_counts[poke_type] = 1
    else:        
        type_counts[poke_type] += 1
print(type_counts)
'''{'Rock': 41, 'Dragon': 25, 'Ghost': 20, 'Ice': 23, 'Poison': 28, 
    'Grass': 64, 'Flying': 2, 'Electric': 40, 'Fairy': 17, 'Steel': 21, 
    'Psychic': 46, 'Bug': 65, 'Dark': 28, 'Fighting': 25, 'Ground': 30, 
    'Fire': 48,'Normal': 92, 'Water': 105}'''

# 2, using Counter class
poke_types = ['Grass', 'Dark', 'Fire', 'Fire', ...]
from collections import Counter
type_counts = Counter(poke_types)
print(type_counts)
'''Counter({'Water': 105, 'Normal': 92, 'Bug': 65, 'Grass': 64, 'Fire': 48, 
            'Psychic': 46, 'Rock': 41, 'Electric': 40, 'Ground': 30, 
            'Poison': 28, 'Dark': 28, 'Dragon': 25, 'Fighting': 25, 'Ice': 23, 
            'Steel': 21, 'Ghost': 20, 'Fairy': 17, 'Flying': 2}) '''

    
# ###################################           Combinations with loop

# 1, standard version
poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
combos = []
for x in poke_types:
    for y in poke_types:
        if x == y:
            continue
        if ((x,y) notin combos) & ((y,x) notin combos):
            combos.append((x,y))
print(combos)
'''[('Bug', 'Fire'), ('Bug', 'Ghost'), ('Bug', 'Grass'), ('Bug', 'Water'), 
    ('Fire', 'Ghost'), ('Fire', 'Grass'), ('Fire', 'Water'), 
    ('Ghost', 'Grass'), ('Ghost', 'Water'), ('Grass', 'Water')]'''

# 2, using itertools.combinations
poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
from itertools import combinations
combos_obj = combinations(poke_types, 2)
print(type(combos_obj))     # >> <class 'itertools.combinations'>
combos = [*combos_obj]      # convert to list
print(combos)
'''[('Bug', 'Fire'), ('Bug', 'Ghost'), ('Bug', 'Grass'), ('Bug', 'Water'), 
    ('Fire', 'Ghost'), ('Fire', 'Grass'), ('Fire', 'Water'), 
    ('Ghost', 'Grass'), ('Ghost', 'Water'), ('Grass', 'Water')]'''

# ###################################          Membership testing

list_a = ['Bulbasaur', 'Charmander', 'Squirtle']
list_b = ['Caterpie', 'Pidgey', 'Squirtle'] 
set_a = set(list_a)             # {'Bulbasaur', 'Charmander', 'Squirtle'}
set_b = set(list_b)             # {'Caterpie', 'Pidgey', 'Squirtle'}
set_a.intersection(set_b)       # {'Squirtle'}

%%timeit set_a.intersection(set_b) # this is faster than lists comparison 
# in nested for loop

# membership
# The same 720 total Pokémon in each data structure
names_list  = ['Abomasnow', 'Abra', 'Absol', ...]
names_tuple = ('Abomasnow', 'Abra', 'Absol', ...)
names_set   = {'Abomasnow', 'Abra', 'Absol', ...}

%timeit 'Zubat' in names_list
# >> 7.63 μs ± 211 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
%timeit 'Zubat' in names_tuple
# >> 7.6 μs ± 394 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
%timeit 'Zubat' in names_set
# >> 37.5 ns ± 1.37 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# sets is very fast

# unique values
unique_types_set = set(primary_types) # just convert to set


# ###################################            Eliminating loops

# 1
%%timeit
totals = []
for row in poke_stats:
    totals.append(sum(row))
140 μs ± 1.94 μs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# 2
%timeit 
totals_comp = [sum(row) for row in poke_stats]
114 μs ± 3.55 μs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# 3 
%timeit totals_map = [*map(sum, poke_stats)]
95 μs ± 2.94 μs per loop (mean ± std. dev. of 7 runs, 10000 loops each) # best


# ###################################   Eliminating loops with built-in modules

poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']

# 1 Nested for loop approach
combos = []
for x in poke_types:
    for y in poke_types:
        if x == y:
            continue
        if ((x,y) notin combos) & ((y,x) notin combos):
            combos.append((x,y))
            
# 2 Built-in module approach
from itertools import combinations
combos2 = [*combinations(poke_types, 2)]


# ###################################    Eliminate loops with NumPy

poke_stats = np.array([    [90,  92, 75, 60],    
                           [25,  20, 15, 90],    
                           [65, 130, 60, 75],    
                           ...                  ])

# 1
%%timeit
avgs = []
for row in poke_stats:
    avg = np.mean(row)
    avgs.append(avg)
print(avgs)             # >> [79.25, 37.5, 82.5, ...]
# >> 5.54 ms ± 224 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

# 2
%timeit avgs_np = poke_stats.mean(axis=1)
print(avgs_np)          # >> [ 79.25  37.5   82.5  ...]
# >> 23.1 μs ± 235 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)


# ###################################           Writing better loops

# ### 1 Onetime calculation loop
for pokemon, attack in zip(names, attacks):
    total_attack_avg = attacks.mean()
    if attack > total_attack_avg:
        a = 1

total_attack_avg = attacks.mean() # that is 2 times faster
for pokemon, attack in zip(names, attacks):
#   total_attack_avg = attacks.mean() - this calculates only once, move it up
    if attack > total_attack_avg:
        a = 1

# ### 2 Holistic conversion loop
poke_data = []
for poke_tuple in zip(names, legend_status, generations):
    poke_list = list(poke_tuple)
    poke_data.append(poke_list)
print(poke_data)
# >> [['Pikachu', False, 1], ['Squirtle', False, 1], ['Articuno', True, 1], ...]

# that's ~ 20% faster
for poke_tuple in zip(names, legend_status, generations):
    poke_data_tuples.append(poke_tuple)
    poke_data = [*map(list, poke_data_tuples)]
print(poke_data)
# >> [['Pikachu', False, 1], ['Squirtle', False, 1], ['Articuno', True, 1], ...]


# %%#################################             
# ###################################          Software Engineering Principles   
# ###################################

import numpy as np
help(np.busday_count)

@> pip install pycodestyle
@> pycodestyle dict_to_array.py

# Import needed package
import pycodestyle
style_checker = pycodestyle.StyleGuide()
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])
print(result.messages)

'''
nay_pep8.py:1:1: E265 block comment should start with '# '
nay_pep8.py:2:6: E225 missing whitespace around operator
nay_pep8.py:4:2: E131 continuation line unaligned for hanging indent
nay_pep8.py:5:6: E131 continuation line unaligned for hanging indent
nay_pep8.py:6:1: E122 continuation line missing indentation or outdented
'''


# ###################################            packages
'''See at ./05packages/05packages.py'''


# ###################################             CLASSES

'''See at ./05packages/my_class.py'''


# ###################################             docstrings
def tokenize(text, regex=r'[a-zA-z]+'):
    """Split text into tokens using a regular expression
    
    :param text: text to be tokenized
    :param regex: regular expression used to match tokens using re.findall 
    :return: a list of resulting tokens
    
    >>> tokenize('the rain in spain')
    ['the', 'rain', 'in', 'spain']
    """
    return re.findall(regex, text, flags=re.IGNORECASE)


# ###################################       DOCTEST, PYTEST
import doctest
doctest.testmod()


    # Links and additional tools
    
    # Sphinx - Generate beautiful documentation
    # Travis CI - Continuously test your code
    # GitHub & GitLab - Host your projects with git
    # Codecov - Discover where to improve your projects tests
    # Code Climate - Analyze your code for improvements in readability




























