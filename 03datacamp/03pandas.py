#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Created on Tue Feb 18 13:23:17 2025 @author: yurii
"""

# %%#################################             
# ###################################               TRANSFORM dataframe
# ################################### 

df.info()
df.head()
df.shape    # >> (16500, 6)
df.describe()
df.values
df.columns  # >> Index(['date', 'city', 'country'], dtype='object')
df.index    # >> RangeIndex(start=0, stop=16500, step=1)


audible.describe()                      # Look at the numeric columns
audible.describe(exclude=[np.number])   # Look at the non numeric columns

#
df.sort_values('city')
df.sort_values('city', ascending = False)
df.sort_values(['city', 'state'], ascending = [False, True])
df['city']
df[['city', 'state']]

#
df['weight_kg'] = df['weight_gramm'] / 1000

df['num_legs'].sample(n=3, random_state=1)

#

mins = (audible['time'].str.extract(r'(\d+)\smin', expand=True)
                        .fillna(0).astype(int))
audible['time'] = audible['time'].str.replace('hrs', 'hr')

#
audible[subset_cols].duplicated().sum()         # same
audible.duplicated(subset=subset_cols).sum()    # same




# %%#################################             
# ###################################               AGGREGATING dataframe
# ################################### 

df['height'].mean()  .median() .mode() .min() .max() .var() .std()
df['height'].sum()   .quantile()

# .agg() method
def pct30(column):
    return column.quantile(0.3)
df['weight'].agg(pct30)
df[['weight', 'height']].agg(pct30)
df['weight'].agg([pct30, pct40])

# cumulative methods
df['weight'].cumsum()  .cummax() .cummin() .cumprod()

#
df.drop_duplicates(subset=['name', 'lastname'])

df['name'].value_counts() .values_counts(sort = True)
df['name'].value_counts(normalize = True)

#
df.groupby('city')['population'].sum() 
df.groupby(['state', 'city'])['population'].agg([min, max, sum])

grp_stock_data = raw_stock_data.groupby(by=["col1"], axis=0).mean()

#
df.pivot_table(values='weight', index='color') # mean default agg
df.pivot_table(values='weight', index='color', aggfunc=np.median) # numpy
df.pivot_table(values='weight', index='color', aggfunc=[np.mean, np.median])

df.pivot_table(values='weight', index='col', columns='cat1')
# fill_value=0, margins=True


# %%#################################             
# ###################################          SLICING and INDEXING DataFrames
# ################################### 

df['height'] > 50       # logical condition, result: bool array
df[df['height'] > 50]   # subset
isin_od_ki = df['city'].isin(['Odessa', 'Kioto']) # logical condition
df[isin_od_ki]          # subset
df[(df['population'] > 100000) & (df['city'] == 'Tokyo')]   # subset

#
df_ind = df.set_index('col1')
df_ind.reset_index()
df_ind.reset_index(drop = True)

#
df[df['name'].isin(['Rimma', 'Oxia'])] # is subset by filtering rows
df_ind2 = df.set_index('name')
df_ind2.loc[['Rimma', 'Oxia']] # .loc is subset by indexes, looks much better !

df_ind3 = df.set_index(['model', 'color'])
df_ind3.loc[[('Model1', 'black'), ('Model2', 'pink')]] # is subset

df_ind3.sort_index(level = ['model', 'color'], ascending = [True, False])

# index and sort df
df_ind3.loc['red':'black'] # in context of dataset values, slice as list[2:4]
df_ind3.loc[('Model5', 'black'):('Model10', 'white')]

df_ind3.loc[:, 'col3':'col6'] # slice columns

df.iloc[2:5, 1:4] # rows and columns. df isn't indexed

# pivoted slice
df_piv = df.pivot_table(values='weight', index='name', columns='cat1')
df_piv.loc['Abba':'Emma']
df_piv.mean(axis = "index")
df_piv.mean(axis = "columns")

df["column"].dt.year / .dt.month ..

mean_temp_by_year = temp_by_country_city_vs_year.mean(axis = "index")
type(mean_temp_by_year)  # pandas.core.series.Series   # shape is (14,)
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

#
audible['time'][audible['time'].str.contains('minutes')].sample(n=10)



# %%#################################             
# ###################################          Visualizing DataFrames
# ################################### 

import matplotlib.pyplot as plt

#
df['weight'].hist()
plt.show()
df['weight'].hist(bins = 20)

#
df_sum_pop_by_city = df.groupby('city')['population'].sum() 
df_sum_pop_by_city.plot(kind = 'bar')
plt.show()
df_sum_pop_by_city.plot(kind = 'bar', title = 'Sum Population by City')

#
df_dogweight # columns: date, weight
df_dogweight.plot(x = 'date', y = 'weight', kind = 'line')
plt.show()
# , rot = 45 (rotate x axis text), kind = 'scatter'

#
df[df['sex']='F']['weight'].hist()
df[df['sex']='M']['weight'].hist() # or .hist(alpha = 0.7)
plt.legend(['F', "M"])
plt.show() # hist on hist, one cover another

# missing values, NaN = Not a Number
df.isna()       # bool df
df.isna().any() # bool but summary for each column
df.isna().sum()

df.isna().sum().plot(kind = 'bar')
plt.show()

df.dropna()     # remove rows with missing values
avocado = avocado.dropna(subset='categories_tags', inplace=True)
df.fillna(0)

#
# Plot histograms of all the numerical columns
audible.hist(figsize=(10, 10), bins=100)
plt.show()

#



# %%#################################             
# ###################################          CREATE DataFrames
# ################################### 

# 1 FROM LIST of dictionaries
list_of_dicts = [
    {'name': 'Mary', 'lastname': 'Storm', 'height': 175},
    { ... },
    { ... }
    ]
df = pd.DataFrame(list_of_dicts) # with columns: name, lastname, height

# 2 FROM DICTIONARY of list, key - column name, value - list of columna values
dict_of_lists = {
    'name': ['Mary', 'Aizawa'],
    'lastname': ['Storm', 'Kateo'],
    'height': [175, 169]
    }
df = pd.DataFrame(dict_of_lists)

#
df.rename(columns={"col1": "aaa", "col2": "bbb"})  # inplace

# READ CSV
df = pd.read_csv('medals.csv')

# SAVE CSV
df.to_csv('medals_slice.csv')
df.to_csv('economics.csv', index = False)


# %%#################################             
# ###################################          Data RESHAPING
# ################################### 

df.set_index('club')[['name', 'nationality']].transpose() # not very useful

# ################ PIVOT
df.pivot(index='year', columns='name')  # all measures show
df.pivot(index='year', columns='name', values='weight')

# drop duplicates
df = df.drop(4, axis = 0) # pivot wont work with duplicates, it can't aggregate
df.pivot(index='year', columns='name')

# ################ PIVOT tables
df.pivot_table(index='year', columns='name', values='weight', aggfunc='mean')
df.pivot_table(index='year', columns='name', aggfunc='mean')
# index= can be multi index ['name', 'lastname']
# margins=True : that's Total

# ################ Wide > Long > Wide Format
df.melt(id_vars=['first', 'last'])
df.melt(id_vars=['first', 'last'], value_vars=['age', 'height'],
        var_name='feature', value_name='amount')
# var_name='feature' is columns with dimention names

#
pd.wide_to_long(df, stubnames = ['age', 'weight'], i = 'name', j = 'year')

# example 1
'''                          title ratings2019 sold2019 ratings2020 sold2020
0                  Mostly Harmless         4.2      456         4.3      436
1           The Hitchhiker's Guide         4.8      980         4.9      998
2 El restaurante del fin del mundo         4.5      678         4.6      638'''

pd.wide_to_long(df, stubnames = ['ratings', 'sold'], i = 'title', j = 'year')

'''                                      ratings    sold
                             title  year 
0                  Mostly Harmless  2019     4.2     456
1           The Hitchhiker's Guide  2019     4.8     980'''
# , sep = '_'  for column names such as 'ratings_2019' etc
# , suffix = '\w+' for extract suffix such as 'ratings_two' >> 'two'

df.reset_index(drop = False, inplace = True)
publication_features = pd.wide_to_long(books_hunger, 
                i=['title','language'], 
                j='feature', 
                stubnames=['publication','page'], 
                sep=' ', 
                suffix = '\w+')

# example 2
'''                            main_title version  number_pages  number_ratings
0    Sherlock Holmes: The Complete Novels   Vol I          1059           24087
1    Sherlock Holmes: The Complete Novels  Vol II           709           26794
2  Adventures of Sherlock Holmes: Memoirs   Vol I           334            2184
3  Adventures of Sherlock Holmes: Memoirs  Vol II           238            1884'''

sh_long = pd.wide_to_long(books_sh, stubnames='number', 
                          i=['title', 'subtitle', 'volume'], 
                          j='feature', sep='_', suffix='\w+')

'''                                                                    number
    title                         subtitle             volume feature        
    Sherlock Holmes                The Complete Novels I      pages      1059
                                                              ratings   24087
                                                       II     pages       709
                                                              ratings   26794
    Adventures of Sherlock Holmes  Memoirs             I      pages       334
                                                              ratings    2184
                                                       II     pages       238
                                                              ratings    1884'''

# ################ SPLIT columns
#
df['title'].str.split(':')
df['title'].str.split(':').str.get(0)
df['title'].str.split(':', expand=True)

df[['main_title','subtitle']] = df['title'].str.split(':', expand=True)
df.drop('title', axis=1, inplace=True) # 1st arg may be a list of columns

#
df['name'].str.cat(df['lastname'], sep=' ') # >> 'name lastname'

df_i_str = df.set_index('country')
df_i_str.index.str.cat(df_i_str['city'], sep='-')
df_i_str.index.str.split('-', expand=True) # multi level index coutry city

new_list = ['aaa', 'bbb','ccc']
df2['name'].str.cat(new_list, sep=' ') 


# %%#################################             
# ###################################        STACKING and UNSTACKING DataFrames
# ################################### 

df.set_index(['age','country'], inplace = True)

# creating multi index usings array
new_array = [['yes', 'no', 'yes'], ['no', 'yes', 'no']]
df2.index = pd.MultiIndex.from_arrays(new_array, names = ['member', 'creadit_card'])

'''                 credit_score age  country  num_products exited
member credit_card          
   yes          no           619  43   France             1    Yes 
    no         yes           608  34  Germany             0     No
   yes         yes           502  23   France             1    Yes'''

#
index = pd.MultiIndex.from_arrays([['Wick', 'Wick', 'Shelley', 'Shelley'],
                                   ['John', 'Julien', 'Mary', 'Frank']],
                                  names = ['last', 'first'])
columns = pd.MultiIndex.from_arrays([['2019', '2019', '2020', '2020'],
                                     ['age', 'weight', 'age', 'weight']],
                                     names = ['year', 'feature'])
patients = pd.DataFrame(data, index = index, columns = columns)
print(patients)
'''         year        2019        2020
         feature  age weight  age weight
   last    first
   Wick     John   25     68   26     72     
          Julien   31     72   32     73
Shelley     Mary   41     68   42     69
           Frank   32     75   33     74'''

# .stack() all to indexes
patients_stacked = patients.stack()
print(patients_stacked)
'''                 year  2019 2020
   last   first  feature
   Wick    John      age    25   26
                  weight    68   72
         Julien      age    31   32
                  weight    72   73
 Shelley  Mary       age    41   42
                  weight    68   69
         Frank       age    32   33
                  weight    75   74 '''

patients.stack(level = 0)  # year will stuck but age\weight
patients.stack(level = 'year') # same as level = 0

#
df.unstack(level = 0) # level = [0, 1] // ['name', 'type']

df.swaplevel(0, 2)
df.swaplevel(0, 1, axis = 1)

# replace missing values when unstack
patients.unstack(level = 'year', fill_value = 'No') 
df3.stack(dropna = False) # True is default, shows index levels with full missing values
df3.stack(dropna = False).fillna()


# %%#################################             
# ###################################        Advanced Data RESHAPING
# ################################### 

''' axis = 1   -- to apply over a column axis 
mean(axis = 1) of measure1 and three types of it (24.2   2.6   18.6) is 15.133 
'''

sales_df.stack().sum(axis = 1).unstack()
sales_df.unstack(level = 0).mean(axis = 1)
sales_df.stack().groupby(level = 'shop').sum()

sales_df.groupby(level = 1).median().stack(level = [0, 1]).unstack(level = 'year')
sales_df.diff(axis = 1, periods = 2)

# ######### EXPLODE method
print(cities)
'''       city  country               zip_code
0  Los Angeles      USA  [90001, 90004, 90008]
1       Madrid    Spain  [28001, 28004, 28005]
2        Rabat  Morocco         [10010, 10170] '''

cities_explode = cities['zip_code'].explode() 
# zip_code is a list of values [90001, 90002, 90003]

# 1
cities[['city', 'country']].merge(cities_explode, 
                                  left_index = True, right_index = True)
cities_explode = cities.explode('zip_code')
# .merge and .explode have the same result
# next is reset index. it has view as 0,0,0,1,1,1,2,2,2, ..
cities_explode.reset_index(drop = True, inplace = True)

# 2
# if zip_code is coma separated values 12, 123, 123, but not a list
cities.assign(zip_code = cities['zip_code'].str.split(',')).explode('zip_code')

# ######### JSON
# #
from pandas import json_normalize
json_normalize(json_data)

df_norm = json_normalize(json_data, sep = '_')

json_normalize(json_data, record_path = 'books') # lead to lists of jsons in json
json_normalize(json_data, record_path = 'books', meta = ['name', 'last'])

# #
writers = ['Mary Shelley', 'Ernest Hemingway']
books = ["{'title': 'Frankenstein', 'year': 1818}",
         "{'title': 'The Old Man and the Sea', 'year': 1951}"]
collection = pd.DataFrame(dict(writers = writers, books = books))
print(collection)
'''         writers                                               books
0      Mary Shelley             {'title': 'Frankenstein', 'year': 1818}
1  Ernest Hemingway  {'title': 'The Old Man and the Sea', 'year': 1951} '''

# convert nested data 1
import json
books = collection['books'].apply(json.load).apply(pd.Series)
print(books)
'''                  title  year
0             Frankenstein  1818
1  The Old Man and the Sea  1951 '''

collection = collection.drop(columns='books')
pd.concat([collection, books], axis = 1) # that's not union

# convert nested data 2
import json
books = collection['books'].apply(json.load).to_list()
books_dump = json.dumps(books)
new_books = pd.read_json(books_dump)
print(new_book)
'''                  title  year
0             Frankenstein  1818
1  The Old Man and the Sea  1951 '''

pd.concat([collection['writers'], new_books], axis = 1)


# %%#################################             
# ###################################        DataFrame Iteration
# ################################### 

# ############## 1, iteration
for i in range(len(df)):
    row = df.iloc[i]
    type(row)           # ?
    # your code


# ############## 2, iteration using .iterrows()
for i, row in df.iterrows():
    type(row)           # >> <class 'pandas.core.series.Series'>
    # your code


# ############## 3, iteration using .itertuples()
for i, row in df.itertuples():
    type(row)           # >> named tuple (from collections) 
                        #Pandas(Index=0, Team='ARI', Year=2012, W=81)
    # your code

%%timeit                # >> 527 ms
for row_tuple in team_wins_df.iterrows():
    print(row_tuple)
# >> 527 ms ± 41.1 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit                # >> 7.48 ms
for row_namedtuple in team_wins_df.itertuples():
    print(row_namedtuple)
# >> 7.48 ms ± 243 μs per loop (mean ± std. dev. of 7 runs, 100 loops each)

row_tuple[1]['Team']    # is a series
row_namedtuple.Team     # names tuple, access using a row's dot reference


# ############## 4, iteration using .apply()
df.apply(   lambda row: calc_run_diff(row['RS'], row['RA'])     , axis = 1   )
        # axis = 1 means iterate over rows

%%timeit                # >> 86.8 ms
run_diffs_iterrows = []
for i,row in baseball_df.iterrows():
    run_diff = calc_run_diff(row['RS'], row['RA'])
    run_diffs_iterrows.append(run_diff)
baseball_df['RD'] = run_diffs_iterrows
# >> 86.8 ms ± 3 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit                # >> 30.1 ms
run_diffs_apply = baseball_df.apply(
         lambda row: calc_run_diff(row['RS'], row['RA']), axis=1)
baseball_df['RD'] = run_diffs_apply
# >> 30.1 ms ± 1.75 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

#
df_totals = df.apply(sum, axis=0)                           # sum each column
total_runs_scored = df[['RS', 'RA']].apply(sum, axis=1)     # sum each row

textual_playoffs = df.apply(            # use lamdba to apply another function
    lambda row: text_playoffs(row['Playoffs'])     , axis=1)
rays_df['Playoffs'].apply(text_playoffs)  # alternative above


# ############## 5, iteration using broadcasting (FASTEST approach)

wins_np = df['W'].values                            # result is numpy array
run_diffs_np = df['W'].values - df['A'].values      # broadcasting
df['RD'] = run_diffs_np                             # FASTEST iteration


# %%#################################             
# ###################################                       data INGESTION
# ################################### 

# ################################### flat files
df = pd.read_csv('file.csv')
df = pd.read_csv('file.tsv', sep='\t')

#
col_names = ['name', 'lastname', 'phone']
col_nums = [0, 1, 2, 4]
df = pd.read_csv('file.csv', usecols = col_names)   # or col_nums
pd.read_csv('1.csv'
            , nrows = 1000                  # number of rows
            , skiprows = 1000               # rows to skip
            , header = None )               # No header cause of skiprows

#
tax_data_first1000 = pd.read_csv('tax_data_2016.csv', nrows=1000) # 1st read
col_names = list(tax_data_first1000)
tax_data_next500 = pd.read_csv('tax_data_2016.csv',
                               nrows = 500,
                               skiprows = 1000,
                               header = None,
                               names = col_names)
print(tax_data_next500.head(1)) # >> [1 rows x 147 columns]

#
df.dtypes
df = pd.read_csv('1.csv', 
        dtype = {'zipcode': str, 'agi': 'category'})  # specify data type
df = pd.read_csv('1.csv', na_values = {'zipcode': 0}) # treat 0 as NaN values

df = pd.read_csv('1_corrupted.csv',
            error_bad_lines = False,    # skip unparseable records
            warn_bad_lines = True)      # see messages when records are skipped
# >> b'Skipping line 3: expected 147 fields, saw 148\n'


# ################################### Excel files
df = pd.read_excel('123.xlsx')

''', nrows= , skiprows= , usecols= , dtype=     work same as at read_csv() '''
df = pd.read_excel('123.xlsx', skiprows = 2, usecols='W:AB, AR')

df = pd.read_excel('123.xlsx', sheet_name = 1)   # second sheet
dict_of_df = pd.read_excel('123.xlsx', sheet_name=None) # return dict of df

# if your excel file has sheets with the same columns
df_all = pd.DataFrame()
for sheet_name, frame in dict_of_df.items():
    frame['Year'] = sheet_name
    df_all = pd.concat([df_all, frame])
print(df_all.Year.unique())

# boolean values
df = pd.read_excel('bool.xlsx', dtype{'col1': bool, 'col2': bool},
                   true_values = ['Yes'],   # for bool columns
                   false_values = ['No'] )  # for bool columns

# dates
date_cols = ['Part1StartTime', 'Part1EndTime']
df = pd.read_excel('bool.xlsx', 
                   parse_dates = dates_cols)

date_cols = ['Part1StartTime', 'Part2EndTime',
     ['Part2StartDate', 'Part2StartTime']]
     # 1st col is date, 2nd is time parse into one column timestamp

date_cols = {'Part1Start': 'Part1StartTime',
             'Part1End': 'Part1EndTime',
             'Part2Start': ['Part2StartDate', 'Part2StartTime']}

format_string = '%m%%d%Y %H:%M:%S'# non-standard cols format after importing file
df['Part2End'] = pd.to_datetime(df['Part2End'], format=format_string)


# ################################### DataBases
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db')

weather = pd.read_sql('weather', engine) # load entire weather table by table name
weather = pd.read_sql('SELECT * FROM weather', engine) 

engine.table_names()


# ################################### JSON / API
df = pd.read_json('123.json', orient = 'split')
# "records" orientation, "columns", "split", "index"
'''Look at 02deinpy.py           JSON >> python'''

# #
import requests

# 1
api_url = 'https://api.yelp.com/v3/businesses/search'
# Set up parameter dictionary according to documentation
params = {'term': 'bookstore',
          'location': 'San Francisco'}
# Set up header dictionary w/ API key according to documentation
headers = {'Authorization': 'Bearer {}'.format(api_key)}
response = requests.get(api_url, params=params, headers=headers) # Call the API
data = response.json() # it's a dict
bookstores = pd.DataFrame(data['businesses'])

# 2
from pandas.io.json import json_normalize

api_url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': 'Bearer {}'.format(api_key)}
params = {'term': 'bookstore', 'location': 'San Francisco'}
response = requests.get(api_url, params = params, headers = headers)
data = response.json()

'''Deeply Nested Data
json_normalize()
record_path:    string/list of string attributes to nested data
meta:           list of other attributes to load to dataframe
meta_prefix:    string to prefix to meta column names '''
bookstores = json_normalize(data['businesses'], sep = '_')

print(list(bookstores))
'''
['alias',  
 'categories', 
 'coordinates_latitude', 
 'coordinates_longitude', 
 ... 
 'location_address1', 
 'location_address2', 
 'location_address3', 
 'location_city', 
 'location_country', 
 'location_display_address', 
 'location_state', 
 'location_zip_code', 
 ... 
 'url'] 
'''
    
print(bookstores.categories.head())    
'''
0    [{'alias': 'bookstores', 'title': 'Bookstores'}]
1    [{'alias': 'bookstores', 'title': 'Bookstores'...
2     [{'alias': 'bookstores', 'title': 'Bookstores'}]
3     [{'alias': 'bookstores', 'title': 'Bookstores'}]
4    [{'alias': 'bookstores', 'title': 'Bookstores'...
Name: categories, dtype: object 
'''


#
print(data["businesses"][0])
'''
{'id': 'CBmrwh7jHn88M4v8Q9Qyyg',
 'alias': 'white-noise-brooklyn-2',
 'name': 'White Noise',
 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/rcNRZr7mVv-vb-PKMMrsLw/o.jpg',
 'is_closed': False,
 'url': 'https://www.yelp.com/biz/white-noise-brooklyn-2?adjust_creative=w1T_agSsZFkZALqEYIiCXQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=w1T_agSsZFkZALqEYIiCXQ',
 'review_count': 15,
 'categories': [{'alias': 'coffee', 'title': 'Coffee & Tea'}],
 'rating': 4.5,
 'coordinates': {'latitude': 40.6893582571548, 'longitude': -73.9884148165584},
 'transactions': [],
 'location': {'address1': '71 Smith St',
  'address2': '',
  'address3': None,
  'city': 'Brooklyn',
  'zip_code': '11201',
  'country': 'US',
  'state': 'NY',
  'display_address': ['71 Smith St', 'Brooklyn, NY 11201']},
 'phone': '',
 'display_phone': '',
 'distance': 1856.1270355932324}
'''

# 3
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path = 'categories')
print(flat_cafes.head())    # saves only 'categories' branch

'''In [2]: data["businesses"]
              alias              title
0            coffee       Coffee & Tea
1            coffee       Coffee & Tea
2  coffeeroasteries  Coffee Roasteries
3             cafes              Cafes
4            coffee       Coffee & Tea
''' 

# 4
df = json_normalize(data['businesses'], sep = '_',
                    record_path = 'categories',
                    meta = ['name',
                            'alias',
                            'rating',
                            ['coordinates', 'latitude'],
                            ['coordinates', 'longitude']],
                    meta_prefix = 'biz_')

'''In [2]: data["businesses"]
              alias              title           biz_name                   biz_alias biz_rating biz_coordinates_latitude biz_coordinates_longitude
0            coffee       Coffee & Tea        White Noise      white-noise-brooklyn-2        4.5                   40.689                   -73.988
1            coffee       Coffee & Tea           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
2  coffeeroasteries  Coffee Roasteries           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
3             cafes              Cafes           Devocion         devocion-brooklyn-3        4.0                   40.689                   -73.983
4            coffee       Coffee & Tea  Coffee Project NY  coffee-project-ny-new-york        4.5                   40.727                   -73.989
'''

# 5
params = {'term': 'bookstore', 'location': 'San Francisco',
          'offset' = 20}  # maybe offset at API response


# ################################### pandas concatenating
# .concat()
df_full = pd.concat([df1, df2],
                    ignore_index = True)        # to renumber rows

# .merge()
merged = call_counts.merge(weather,
                           left_on = 'created_date', 
                           right_on = 'date')


# %%#################################             
# ###################################                       data LOAD
# ################################### 

#
connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/market"
db_engine = sqlalchemy.create_engine(connection_uri)

clean_stock_data.to_sql(
    name="filtered_stock_data",
    con=db_engine,
    if_exists="append",         # "replace"
    index=True,
    index_label="timestamps"
    )


# %%#################################             
# ###################################               JOINING dataframe
# ################################### 
import pandas as pd
#
dfx_dfy = dfx.merge(dfy,        # INNER JOIN is default argument
                    on='ward')  # 'ward' is a column name, become single
dfx_dfy = dfx.merge(dfy, how='inner',  # how='outer', left, right
                    on='ward', suffixes=('_ward', '_cen'))

dfx_dfy = dfx.merge(dfy, on=['address', 'zip'])

df1_df2_df3 = (df1.merge(df2, on=['col1', 'col2']) 
                        .merge(df3, on='col55', suffixes('_bus', 'ward')))

#
df1_df2 = df1.merge(df2, on='id', how='left')
df1_df2 = df1.merge(df2, how='left',
                    left_on='id', right_on='movie_id')

df1_df2 = df1.merge(df2, left_on='id', left_index=True,
                    right_on='movie_id', right_index=True)

# semi join
genres_tracks = genres.merge(top_tracks, on='gid')
top_genres = genres[genres['gid'].isin(genres_tracks['gid'])]
print(top_genres.head())
  gid  name           
0 1    Rock           
1 2    Jazz           
2 3    Metal          
3 4    Alternative & Punk
4 6    Blues

# anti join
genres_tracks = genres.merge(top_tracks, on='gid', how='left', indicator=True)
gid_list = genres_tracks.loc[genres_tracks['_merge'] == 'left_only','gid']
non_top_genres = genres[genres['gid'].isin(gid_list)]
print(non_top_genres.head())
  gid  name          
0 5    Rock And Roll 
1 9    Pop           
2 11   Bossa Nova    
3 12   Easy Listening
4 13   Heavy Metal

#
tracks.merge(specs, on='tid',
             validate='one_to_one')  # validate connection
# one_to_many, many_to_one, may_to_many

# ###
pd.merge_ordered(df1, df2, on='date',
                 suffixes=('_aapl', '_mcd'),
                 fill_method='ffill')  # filled by value row before(up)

ctry_date = pd.merge_ordered(gdp, pop, on=['date', 'country'],
                             fill_method='ffill')
on=['country', 'date'] # order changes and filling takes values from appropriate country

# merges on nearest value, not exact = fuzzy matching
pd.merge_asof(visa, ibm, on=['date_time'],
              suffixes=('_visa', '_ibm'))
    director='forward' # 'nearest', backward

# ################################### .query

stocks.query('nike >= 90')
stocks.query('nike > 90 and disney < 98')  # or
stocks.query('stock=="disney" or (stock="nike" and close < 90)')

# ################################### .melt









# ################################### .concat

pd.concat([inv_jan, inv_feb, inv_mar]) # index 0,1,2 repeat
   iid  cid  invoice_date  total
0  1    2    2009-01-01    1.98 
1  2    4    2009-01-02    3.96 
2  3    8    2009-01-03    5.94 
0  7    38   2009-02-01    1.98 
1  8    40   2009-02-01    1.98 
2  9    42   2009-02-02    3.96 
0  14   17   2009-03-04    1.98 
1  15   19   2009-03-04    1.98 
2  16   21   2009-03-05    3.96

pd.concat([inv_jan, inv_feb, inv_mar],
          ingore_index=True)            # index 0 - 8

   iid  cid  invoice_date  total
0  1    2    2009-01-01    1.98 
1  2    4    2009-01-02    3.96 
2  3    8    2009-01-03    5.94 
3  7    38   2009-02-01    1.98 
4  8    40   2009-02-01    1.98 
5  9    42   2009-02-02    3.96 
6  14   17   2009-03-04    1.98 
7  15   19   2009-03-04    1.98 
8  16   21   2009-03-05    3.96

pd.concat([inv_jan, inv_feb, inv_mar],
          ignore_index=False,
          keys=['jan','feb','mar'])

       iid  cid  invoice_date  total
jan 0  1    2    2009-01-01    1.98 
    1  2    4    2009-01-02    3.96 
    2  3    8    2009-01-03    5.94 
feb 0  7    38   2009-02-01    1.98 
    1  8    40   2009-02-01    1.98 
    2  9    42   2009-02-02    3.96 
mar 0  14   17   2009-03-04    1.98 
    1  15   19   2009-03-04    1.98 
    2  16   21   2009-03-05    3.96

#
pd.concat([inv_jan, inv_feb],
          sort=True)   # sort columns and concat on column names

pd.concat([inv_jan, inv_feb],
          join='inner')  # order columns is the same as input tables

pd.concat([inv_jan, inv_feb],
          verify_integrity=True)  # Checks index column overlapping, default False



# ################################### group by
counted_df = licenses_owners.groupby('title').agg({'account':'count'})
'''                 account
title                      
ASST. SECRETARY         111
BENEFICIARY               4
CEO                     110'''

licenses_zip_ward.groupby('alderman').agg({'income':'median'})

pop_vac_lic = (land_cen_lic.groupby(by=['ward', 'pop_2010', 'vacant'], as_index=False)
               .agg({'account':'count'}))

genre_count = genres_movies.groupby('genre').agg({'id':'count'})
'''              id
genre              
Action            7
Adventure         9
Animation         2
Comedy            3'''

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})

#
animals.groupby("kind").sum()
      height  weight
kind                
cat     18.6    17.8
dog     40.0   205.5

animals.groupby("kind", as_index=False).sum()
  kind  height  weight
0  cat    18.6    17.8
1  dog    40.0   205.5

# choose filter after groupby
groups = df.groupby(by=['A'])
print(groups.apply(lambda g: g[g['B'] == g['B'].max()]))

# filter df after groupby, you should reset index !!
wo_grouped = workout.groupby('year').sum().reset_index()
wo_condition = wo_grouped['workout_worldwide'] == wo_grouped['workout_worldwide'].max()
year_str = str(wo_grouped[wo_condition]['year'])







# %%#################################             
# ###################################                       
# ################################### 



265897







