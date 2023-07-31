# -*- coding: utf-8 -*-
"""Created on Thu Jul 28 11:19:22 2022@author: xiaom"""

#################### OPEN   files                               IMPORT
################### CSV




with open('D:/py/93393933python-study/01/9/weekdays.txt') as week_file:
    weekdays = [day.rstrip() for day in week_file.readlines()]
    
print(weekdays)

username = 'Kalina'
with open('user_info.txt', 'w') as fileobject:
    fileobject.write(username)
    
with open('user_info.txt') as fileobject:
    username2 = fileobject.read()
print('hello ' + username2 + '11!')    
###################################

import json
#create dict of a person
cj = {}
cj['first name'] = 'Carl'
cj['last name'] = 'Johnson'
cj['cars']= [{'brand': 'Chevrolet', 
              'model': '1964 Impala', 
              'color': 'black'},
             {'brand': 'Ferrari', 
              'model': '1987 Testarossa', 
              'color': 'white'}]
cj['has_a_dog'] = True
cj['money_in_pocket'] = 500

with open('D:/py/93393933python-study/01/9/cj.json', 'w') as fileoblect:
    json.dump(cj, fileoblect)

with open('D:/py/93393933python-study/01/9/cj.json') as fileobject:
    cjr = json.load(fileobject)
    
for k,v in cjr.items():
    print(k,':', v)

# 'w' - делает ввод строки
ff = open('D:/py/93393933python-study/01/9/weekdays2.txt','w')
# 'r+' - делает ввод строки по последней позиции
ff = open('D:/py/93393933python-study/01/9/weekdays2.txt','r+')
ff = open('D:/py/93393933python-study/01/9/weekdays2.txt','r')
print(ff.name)
print(ff.closed)
print(ff.mode)
print(ff.read())
ff.close()

ff.write('1111111')
ff.write('8newday')
print(ff.read())
ff.write( "Python_is_a_great_language.\nYeah its great!!\n")
string = ff.read(1)
print(string)

position = ff.tell()
print ("Current file position : ", position)

ff.seek(27,0)


with open('D:/py/93393933python-study/01/9/cj.json', 'w') as fileoblect:
    json.dump(cj, fileoblect)

print(json.dumps(cjr, sort_keys=True, indent=2, separators=(',', ':')))
print(json.dumps(cjr, indent=2))

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

import os

os.rename('cj.json', 'cjjjjj.json')
os.mkdir('aoi')
os.getcwd()
os.rmdir('aoi')


###########'########3

'''Task 1
Files

Write a script that creates a new output file called myfile.txt and 
writes the string "Hello file world!" in it. Then write another script that 
opens myfile.txt, and reads and prints its contents. Run your two scripts 
from the system command line. 

Does the new file show up in the directory where you ran your scripts? 
What if you add a different directory path to the filename passed to open?

Note: file write methods do not add newline characters to your strings; 
add an explicit ‘\n’ at the end of the string if you want to fully 
terminate the line in the file.'''

gg = open('D:/py/93393933python-study/01/9/myfile.txt','w')

gg.write('Hello file world!\n')
gg.close()


zz = open('D:/py/93393933python-study/01/9/myfile.txt','r')

a = zz.read()
# print(zz.read())
print(a)
zz.close()


#############
############3
################     CSV
import csv


########  simple open - read each line - close
csvfile = open('D:\py\93393933python-study\dc\somedata\geofeeds.csv', 'r')

column_names = ['route', 'country code', 'country state', 'city','?']
for row in csv.DictReader(csvfile, fieldnames=column_names):
    print(row)
csvfile.read()
csvfile.read(100) # read first 100 symbols
                                # how to read first few lines?
csvfile.close()



######
######
######
########  =====================================     to  NUMPY
import numpy as np
digits = np.loadtxt('digits.csv', delimiter=',')


# Import file: data
data = np.loadtxt('digits.csv', delimiter='\t', dtype=str)
# Import data as floats and skip the first row: data_float
data_float = np.loadtxt('digits.csv', delimiter='\t', dtype='float', skiprows=1)

# ------                  np.genfromtxt
data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)
# data[0]               # for print row
# data['Fare']          # for print column
 

#########                                           np.recfromcsv()
# You'll only need to pass file to it because 
# it has the defaults delimiter=',' and names=True in addition to dtype=None!
# Import file using np.recfromcsv: d
data = np.recfromcsv('titanic.csv')
print(data[:3])


#########  
#########  
#########                       to  PANDAS
import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()


#
data = pd.read_csv('titanic_corrupted.csv', sep='\t', comment='#', na_values='Nothing')
# comment takes characters that comments occur after in the file, 
# which in this case is '#'. na_values takes a list of strings to recognize 
# as NA/NaN, in this case the string 'Nothing'.



########                            pickle
import pickle
# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
    

    


########                                               XLSx
######## 
######## 
xls = pd.ExcelFile(file)
print(xls.sheet_names)
# ['1960-1966', '1967-1974', '1975-2011']

df1 = xls.parse(0)
df2 = xls.parse('1960-1966')

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=1, names=['Country','AAM due to War (2002)'])
# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=1, names=['Country'])






















########                                   Importing SAS files
######## 
######## 
import pandas as pd
from sas7bdat import SAS7BDAT     # SAS7BDAT функция для чтения САС

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

########                                   Importing Stata files (dta)
df = pd.read_stata('filename.dta')

########
########
 ########                                 Importing HDF5
import numpy as np
import h5py

data = h5py.File('LIGO_data.hdf5', 'r')
# Print the keys of the file
for key in data.keys():
    print(key)
strain = np.array(data['strain']['Strain'])




######## 
######## 
########                                   Importing MATLAB
import scipy.io
mat = scipy.io.loadmat('albeck_gene_expression.mat')






######## 
######## 
########                                   Importing     SQL
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()

#                                       var 1
# Open engine connection: con
con = engine.connect() 
# Perform query: rs
rs = con.execute("SELECT * FROM Album")
# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
# Close connection
con.close()

df.columns = rs.keys()  # before close


#                                       var 2
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(3))
    df.columns = rs.keys()


#                                       var 3
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)





######## 
########                    Importing     URL
########                                   Importing     URL csv
from urllib.request import urlretrieve
import pandas as pd

url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Save file locally
urlretrieve(url, 'winequality-red.csv')



########
########
######## ########                             URL         XLSx    2 
# Import package
import pandas as pd
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'
# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name=None)



########
########
########
########                                        Open URL   1
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"
# This packages the request: request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Print the datatype of response
print(type(response))
response.close()

#or
html = response.read()
print(html)
response.close()




########
########
########
########                                        get HTML   1
import requests

url = 'http://www.datacamp.com/teach/documentation'
# Packages the request, send the request and catch the response: r
r = requests.get(url)
# Extract the response: text // Use the text attribute of the object r 
# to return the HTML of the webpage as a string; store the result in a variable text.
text = r.text 
print(text)



########
########
########
########                                        get  HTML  2

# Import packages
import requests
from bs4 import BeautifulSoup
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)
# Extracts the response as html: html_doc
html_doc = r.text
# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()
print(pretty_soup)


guido_title = soup.title
guido_text = soup.get_text()
soup.head
soup.body

a_tags = soup.find_all('a') # get a href links
for link in a_tags:
    print(link.get('href'))
# got clean urls w/o tags





########
########
########
########                                        import  JSON
import json

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


########
########
########
########                                        import  JSON        from URL
import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)


#####                                       import  JSON        from URL   2
import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'
r = requests.get(url)
json_data = r.json()

for k in json_data.keys():
    print(k + ': ', json_data[k])
    











