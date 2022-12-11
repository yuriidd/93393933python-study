# -*- coding: utf-8 -*-
"""Created on Thu Jul 28 11:19:22 2022@author: xiaom"""

#################### OPEN   files
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



######## 


