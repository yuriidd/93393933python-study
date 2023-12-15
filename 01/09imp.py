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
    

#####                                       import  JSON    from life

tweets_data = []
# Open connection to file
tweets_file = open('tweets.txt', "r")

for line in tweets_file:
    tweet = json.loads(line)           # json.loads()
    tweets_data.append(tweet)
tweets_file.close()




#####  
#####  
#####  
#####                       XPATH
'''

'/html/body'
'//p'
'/div[@class="superclass 1"]'
'/html/body/a/@href'                    - only attribute href from <a>
'//a[contains(@class, "class 1")]'      - only class in which "class 1" is substring
//div[3]/a

//p[@id="p-example"]/text()    
//p[@id="p-example"]//text()


'''

############################## 
from scrapy import Selector

html = '\n<html>\n<body>\n<div>Div 1: <p>paragraph 1</p></div>\n<div>Div 2: <p>paragraph 2</p> <p>paragraph 3</p> </div>\n<div>Div 3: <p>paragraph 4</p> <p>paragraph 5</p> <p>paragraph 6</p></div>\n<div>Div 4: <p>paragraph 7</p></div>\n<div>Div 5: <p>paragraph 8</p></div>\n</body>\n</html>\n'

sel = Selector( text = html )
# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )

divs.extract_first() 
divs[1].extract()
    # got first item in list

divs[2].xpath('./*')
#Out[7]:
#[<Selector xpath='./*' data='<p>paragraph 4</p>'>,
# <Selector xpath='./*' data='<p>paragraph 5</p>'>,
# <Selector xpath='./*' data='<p>paragraph 6</p>'>]
divs[2].xpath( './p[3]' )
# Out[6]: [<Selector xpath='./p[3]' data='<p>paragraph 6</p>'>]


#########################
from scrapy import Selector
import requests

url = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'
html = requests.get( url ).content
sel = Selector( text = html )
len( sel.xpath('//*') )



#########################

response.url






################
#################
#################                       make spider
# Import scrapy library
import scrapy
# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
# Inspect Your Class
#               inspect_class(YourSpider)

#################                    make spider next step                       
# Import scrapy library
import scrapy
# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com","https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
  # Inspect Your Class
#               inspect_class( YourSpider )
#################   

class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = "https://www.datacamp.com", callback = self.parse )
  # parse method
  def parse( self, response ):
    pass

#################  
# Import the scrapy library
import scrapy
# Create the Spider class
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow( url = link, callback = self.parse_descr)
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr
# Inspect the spider
inspect_spider( DCdescr )

#################  #################                 spider DONE
# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    crs_title_ext = crs_title.extract_first().strip()
    ch_titles = response.css('h4.chapter__title::text')
    ch_titles_ext = [t.strip() for t in ch_titles.extract()]
    dc_dict[ crs_title_ext ] = ch_titles_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

'''
A preview of DataCamp Courses:
---------------------------------------

TITLE: Cleaning Data in R
	Chapter 1: Introduction and exploring raw data
	Chapter 2: Preparing data for analysis
	Chapter 3: Tidying data
	Chapter 4: Putting it all together
	Chapter 5: Introduction and exploring raw data
	Chapter 6: Tidying data
	Chapter 7: Preparing data for analysis
	Chapter 8: Putting it all together

TITLE: Introduction to R
	Chapter 1: Intro to basics
	Chapter 2: Vectors
	Chapter 3: Matrices
	Chapter 4: Factors
	Chapter 5: Data frames
	Chapter 6: Lists

TITLE: Introduction to Machine Learning
	Chapter 1: What is Machine Learning
	Chapter 2: Classification
	Chapter 3: Clustering
	Chapter 4: Performance measures
	Chapter 5: Regression
	Chapter 6: What is Machine Learning
	Chapter 7: Performance measures
	Chapter 8: Classification
	Chapter 9: Regression
	Chapter 10: Clustering

'''

# dc_dict = 
{'Introduction to R': ['Intro to basics',
  'Vectors',
  'Matrices',
  'Factors',
  'Data frames',
  'Lists'],
 'Data Visualization in R with ggvis': ['The Grammar of Graphics',
  'Transformations',
  'Customizing Axes, Legends, and Scales',
  'Lines and Syntax',
  'Interactivity and Layers',
  'The Grammar of Graphics',
  'Lines and Syntax',
  'Transformations',
  'Interactivity and Layers',
  'Customizing Axes, Legends, and Scales'],
 'Cleaning Data in R': ['Introduction and exploring raw data',
  'Preparing data for analysis',
  'Tidying data',
  'Putting it all together',
  'Introduction and exploring raw data',
  'Tidying data',
  'Preparing data for analysis',
  'Putting it all together'],
 'Reporting with R Markdown': ['Authoring R Markdown Reports',
  'Embedding Code',
  'Compiling Reports',
  'Configuring R Markdown (optional)'],
 'Intro to Python for Data Science': ['Python Basics',
  'Functions and Packages',
  'Python Lists',
  'NumPy',
  'Python Basics',
  'Python Lists',
  'Functions and Packages',
  'NumPy'],
 'Introduction to Machine Learning': ['What is Machine Learning',
  'Classification',
  'Clustering',
  'Performance measures',
  'Regression',
  'What is Machine Learning',
  'Performance measures',
  'Classification',
  'Regression',
  'Clustering'],
 'Intermediate R - Practice': ['Conditionals and Control Flow',
  'Loops',
  'Functions',
  'The apply family',
  'Utilities'],
 'Data Manipulation in R with dplyr': ['Introduction to dplyr and tbls',
  'Filter and arrange',
  'Group_by and working with databases',
  'Select and mutate',
  'Summarize and the pipe operator',
  'Introduction to dplyr and tbls',
  'Select and mutate',
  'Filter and arrange',
  'Summarize and the pipe operator',
  'Group_by and working with databases'],
 'Intermediate R': ['Conditionals and Control Flow',
  'Functions',
  'Utilities',
  'Loops',
  'The apply family',
  'Conditionals and Control Flow',
  'Loops',
  'Functions',
  'The apply family',
  'Utilities'],
 'Data Analysis in R, the data.table Way': ['Data.table novice',
  'Data.table yeoman',
  'Data.table expert']}



#################  #################   
#################  #################   
url_short='https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css( 'p.course__description::text' )
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)

################################################ parse many answers
# parse method
def parse(self, response):
  # Extracted course titles
  crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
  # Extracted course descriptions
  crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
  # Fill in the dictionary: it is the spider output
  for crs_title, crs_descr in zip(crs_titles, crs_descrs):
    dc_dict[crs_title] = crs_descr



################################################             to PD  


# Create list of columns to use
cols = ['zipcode','agi_stub','mars1','MARS2','NUMDEP']
# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)
# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())




################################################             to PD  
vt_data_first500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500)
# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv", 
                       		  nrows = 500,
                       		  skiprows = 500,
                       		  header=None,
                       		  names = list(vt_data_first500))
# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())


################################################             to PD  

# Create dict specifying data types for agi_stub and zipcode
data_types = {'zipcode': 'str'       ,
			  'agi_stub': 'category'}
# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype = data_types)
# Print data types of resulting frame
print(data.dtypes.head())


################################################             to PD 

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}
# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)
# View rows with NA ZIP codes
print(data[data.zipcode.isna()])




################################################             to PD  w errs
try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)
  # View first 5 records
  print(data.head())
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")



################################################              PD      excel

# Create string of lettered columns to load
col_string = "AD, AW:BA"
# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows = 2, 
                        usecols = col_string)


###

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name=1)
# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name='2017')
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0,'2017'])
# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=None)




##########################################       PD      excel name sheets

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  #print (type(df))
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()





##########################################         excel     
##########################################                  na/missing/BOOLEAN
# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")
# Count NA values in each column
print(survey_data.isna().sum())

###########
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                              "AttendedBootCampYesNo": bool},
                              true_values=['Yes'],
                              false_values=['No'])
# View the data
print(survey_subset.head())


##########################################          excel
##########################################                      datetime
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates = ['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())


######
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ['Part2StartDate','Part2StartTime']}
# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)
# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())


######
# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], 
                                             format="%m%d%Y %H:%M:%S")
# Print first few values of Part2EndTime
print(survey_data["Part2EndTime"].head())




##########################################     pd
##########################################            import          SQL

# Import sqlalchemy's create_engine() function
from sqlalchemy import create_engine
# Create the database engine
engine = create_engine('sqlite:///data.db')
# View the tables in the database
print(engine.table_names())



###########
# Create the database engine
engine = create_engine('sqlite:///data.db')
# Load hpd311calls without any SQL
hpd_calls = pd.read_sql('hpd311calls', engine)
# View the first few rows of data
print(hpd_calls.head())


# Create a SQL query to load the entire weather table
query = """
SELECT * FROM weather;
"""
# Load weather with the SQL query
weather = pd.read_sql(query, engine)




############################################
############################################
try:
    # Load the JSON with orient specified
    df = pd.read_json("dhs_report_reformatted.json",
                      orient='split')
    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census", 
            y="total_individuals_in_shelter")
    plt.show()
except ValueError:
    print("pandas could not parse the JSON.")




############################################                       JSON
############################################
import requests

headers={'Authorization': 'Bearer mhmt6jn3SFPVC1u6pfwgHWQvsa1wmWvCpKRtFGRYlo4mzA14SisQiDjyygsGMV2Dm7tEsuwdC4TYSA0Ai_GQTjKf9d5s5XLSNfQqdg1oy7jcBBh1i7iQUZBujdA_XHYx'}
params={'term': 'cafe', 'location': 'NYC'}

api_url = "https://api.yelp.com/v3/businesses/search"
# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)
# Extract JSON data from the response
data = response.json()
# Load data to a dataframe
cafes = pd.DataFrame(data['businesses'])
# View the data's dtypes
print(cafes.dtypes)


#################
# Create dictionary that passes Authorization and key string
headers = {'Authorization': "Bearer {}".format(api_key)}
# Query the Yelp API with headers and params set
response = requests.get(api_url, headers = headers, params = params)
data = response.json()
# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data['businesses'])
print(cafes.name)



############################################      norm                 JSON
# Load json_normalize()
from pandas.io.json import json_normalize 
# Isolate the JSON data from the API response
data = response.json()
# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep='_')
# View data
print(cafes.head())

############################################      norm 2                JSON
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates', 'latitude'], 
                          		  ['coordinates', 'longitude']],
                    		meta_prefix='biz_')
# View the data
print(flat_cafes.head())




############################################   chunk50-50     JSON
# Add an offset parameter to get cafes 51-100
params = {"term": "cafe", 
          "location": "NYC",
          "sort_by": "rating", 
          "limit": 50,
          "offset": 50}
result = requests.get(api_url, headers=headers, params=params)
next_50_cafes = json_normalize(result.json()["businesses"])
# Append the results, setting ignore_index to renumber rows
cafes = top_50_cafes.append(next_50_cafes, ignore_index=True)
# Print shape of cafes
print(cafes.shape)





################################### 




























