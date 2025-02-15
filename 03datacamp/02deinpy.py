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


# %%#################################             
# ###################################               CLEANING DATA
# ################################### 

# ###################################               

df.info() 
df['user_type'].describe() 

df['user_type_cat'] = df['user_type'].astype('category') # change column type
df['user_type_cat'].dtype() # it's category now
assert df['user_type_cat'].dtype == 'category'































