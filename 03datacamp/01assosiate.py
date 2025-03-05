#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 4 2025
@author: yurii
"""
# ####################   DataCamp - Associate Python Developer
 

# Define a function called concat            *ARGS
def concat(*args):
  result = ''           # Create an empty string
  for arg in args:      # Iterate over the Python args tuple
    result += " " + arg
  return result

print(concat("Python", "is", "great!"))     # Call the function


# #################################         **KWARGS

# Define a function called concat
def concat(**kwargs):
  result = ""                       # Create an empty string
  for kwarg in kwargs.values():     # Iterate over the Python kwargs
    result += " " + kwarg
  return result

print(concat(start="Python", middle="is", end="great!"))    # Call the function


# #################################         lambda

#
(lambda x, y: x**y)(2, 3)
(lambda x: sum(x)/len(x))([3, 6, 9])

# map() applies a function to all element in an iterable
names = ['linda', 'Rimma', 'Jane', 'May']

capitalize = map(lambda x: x.capitalize(), names)
print(capitalize)           # >> <map object at 0x7554bb940580>
print(list(capitalize))     # >> 8


# %%
#
type("User Name 187")               # >> str
type("User Name 187") == 'str'      # >> False
type("User Name 187") == "str"      # >> False
print(type('User Name 187'))        # >> <class 'str'>

" ".join('op_pa'.split("_")).title()    # >> Op Pa


# %%
# #######################               ERRORs

#
def sqrt(x):
    if x < 0:
        raise ValueError('x must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be an int or float')

#
if validate_password(password) == False:
    raise ValueError("Error inputted puser password. Check wheter defined user password is correct.")
    return False

#
def func01():
    try:
        validate_user(' ', 'yurii@gmail.com', '_123MNmm123Rewe')
        # wrong name generates ValueError message, then you catch it
        # with "except ValueError:"
        # ! but better to learn more deep
    except ValueError:
        print("Check input data. Incorrect data have been entered.")
        return False
    
func01()

#
# %%

# #########################         python TOOLBOX 1 - 1/3
# ######################### 

# #########################    iterables and iterators
#
values = range(1, 5)
print(values)
print(sum(values) * 2)

#
# Create a list of strings: mutants         enumerates
mutants = []
aliases = []
powers = []
mutant_list = list(enumerate(mutants))
for index1, value1 in enumerate(mutants):
    print(index1, value1)
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)

#
mutant_data = list(zip(mutants, aliases, powers))
mutant_zip = zip(mutants, aliases, powers)
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

#
z1 = zip(mutants, powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# Check if unpacked tuples are equivalent to original tuples
print(result1 == mutants)
print(result2 == powers)

#
names_type1 = [*zip(names, primary_types)]
print(*names_type1[:5], sep='\n')           # cool unpack print

# ######################                CSV >> pandas df ()
# #1
import pandas as pd
counts_dict = {}
for chunk in pd.read_csv('tweets.csv', chunksize = 10):
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1
print(counts_dict)

# #2
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    counts_dict = {}
    for chunk in pd.read_csv(csv_file, chunksize = c_size):
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1
    return counts_dict
result_counts = count_entries('tweets.csv', 10, 'lang')
print(result_counts)

#
nums = [1, 4, 9, 13]
nums2 = [x + 1 for x in nums]
# nums3 = (lambda x: x + 1)(iter(nums)      that's not working :(

pairs2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
'''[ output expression  for  iterator variable  in  iterable 
                                        if  predicate expression ]'''
# new_fellowship = [member if len(member)>=7 else '' for member in fellowship]

#
qwe = range(0,5)
type(qwe)
qweqwe = (x for x in qwe)
type(qweqwe)

#
def num_sequence(n):
    """Generate values from 0 to n."""    
    i = 0
    while i < n:
        yield i        
        i += 1

result = num_sequence(5)
print(type(result))

for item in result:   
    print(item)

#
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""
    for person in input_list:
        yield len(person)

for value in get_lengths(lannister):
    print(value)


# ####################                dictionary  >>  pandas df
#
import pandas as pd
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""
    zipped_lists = zip(list1, list2)    # Zip lists: zipped_lists
    rs_dict = dict(zipped_lists)        # Create a dictionary: rs_dict
    return rs_dict                      # Return the dictionary

feature_names = ['col1', 'col2']  # list with col names
row_vals = ['man', 'yurii']       # list with values of 1 row
row_lists = [['woman', 'oxia'], ['man', 'yurii']]      
# list of lists with values of many row

lists2dict(feature_names, row_vals)
# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]
df = pd.DataFrame(list_of_dicts)    # Turn list of dicts into a DataFrame: df
print(df.head())    # Print the head of the DataFrame


# #############################           CSV > list
# 
with open('world_dev_ind.csv') as file:     # Open a connection to the file
    file.readline()             # Skip the column names
    for j in range(0,1000):     # Process only the first 1000 rows
        # Split the current line into a list: line
        line = file.readline().split(',')

#      read LINES through generator-object
#      that's example, not solution
# 
def read_large_file(file_object):   #Define read_large_file()
    """A generator function to read a large file lazily."""
    while True:
        data = file_object.readline()   # Read a line from the file: data
        if not data:        # Break if this is the end of the file
            break
        yield data          # Yield the line of data

# #1
with open('world_dev_ind.csv') as file:     # Open a connection to the file
    gen_file = read_large_file(file) # Create a generator object for the file: gen_file
    print(next(gen_file))    # Print the first three lines of the file

# #2
with open('world_dev_ind.csv') as file: # Open a connection to the file
    for line in read_large_file(file):
        row = line.split(',')# Iterate over the generator from read_large_file()


# ####################        CSV > pandas        using iterator (chunks)
# #1
import pandas as pd
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)
print(next(df_reader))
print(next(df_reader))

# #2
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
data = pd.DataFrame()
for df_urb_pop in urb_pop_reader:
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])
    pops_list = list(pops)
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    data = pd.concat([data, df_pop_ceb])
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


# %%
# ####################              f strings

print(f"Rank #: {top_ten_rank} - { name }")


#
squirrels_by_park = {'Union Square Park': []}

squirrels_madison = [{'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Sitting',
  'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': 'Cinnamon',
  'activities': 'Foraging',
  'interactions_with_humans': 'Indifferent'},
 {'primary_fur_color': 'Gray',
  'highlights_in_fur_color': None,
  'activities': 'Climbing, Foraging',
  'interactions_with_humans': 'Indifferent'}]

squirrels_union = ('Union Square Park',
 [{'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Cinnamon',
   'activities': 'Climbing, Eating',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Cinnamon',
   'highlights_in_fur_color': None,
   'activities': 'Foraging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Running, Digging',
   'interactions_with_humans': 'Runs From'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Digging',
   'interactions_with_humans': 'Indifferent'},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': 'Black',
   'activities': 'Climbing',
   'interactions_with_humans': None},
  {'primary_fur_color': 'Gray',
   'highlights_in_fur_color': None,
   'activities': 'Eating, Foraging',
   'interactions_with_humans': None}])

# Assign squirrels_madison as the value to the 'Madison Square Park' key
squirrels_by_park['Madison Square Park'] = squirrels_madison # OK

# TASK: Update the 'Union Square Park' key in the squirrels_by_park dictionary 
#       with the data in the squirrels_union tuple.
# Update squirrels_by_park with the squirrels_union tuple
squirrels_by_park.update([squirrels_union]) # look at how tuple update dict !

for park_name in squirrels_by_park:
    (print(park_name, [squirrel.get('primary_fur_color', 'N/A') 
                           for squirrel in squirrels_by_park[park_name]])
     )

squirrels_madison.items()


# %%
# ####################                Counter

from collections import Counter
penguins_species_counts = Counter([penguin['Species'] for penguin in penguins])
print(penguins_species_counts)
print(penguins_species_counts.most_common(3))


# ####################                dataclass

weight_log = [('Gentoo', 230.0, 5500.0, 'MALE'),
 ('Gentoo', 229.0, 5800.0, 'MALE'),
 ('Gentoo', 225.0, 5400.0, 'MALE'),
 ('Gentoo', 219.0, 5250.0, 'MALE'),
 ('Gentoo', 210.0, 4300.0, 'FEMALE'),
 ('Gentoo', 216.0, 4925.0, 'MALE')]

from dataclasses import dataclass
@dataclass
class WeightEntry:
    species: str # Define the fields on the class
    body_mass: int
    flipper_length: int
    sex: str
        
    @property # Define a property that returns the body_mass / flipper_length
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length

labeled_entries = [] # Create the empty list: labeled_entries

# Iterate over the weight_log entries
for species, flipper_length, body_mass, sex in weight_log:
    # Append a new WeightEntry instance to labeled_entries
    labeled_entries.append(WeightEntry(species, flipper_length, body_mass, sex))
# Print a list of the first 5 mass_to_flipper_length_ratio values
print([entry.mass_to_flipper_length_ratio for entry in labeled_entries[:5]])


# %%
# ############################             date, datetime, timezone
# ############################  

from datetime import date
hurricane_andrew = date(1992, 8, 24)
hurricane_andrew.weekday()
d1 = date(1992, 8, 24)
d2 = date(1994, 9, 26)
delta = d2 - d1
print(delta.days)

from datetime import timedelta
td = timedelta(days=29)
d1 + td

print(d1)           # ISO format
d1.isoformat()      # ISO format
d1.strftime('%Y')   # %Y%m%d %B %j 

from datetime import datetime
dt = datetime(1994, 9, 26, 15, 23, 5)   # %H %M %S
dt_hr = dt.replace(minute = 1, seconds = 5, microseconds = 0)
dt.hour

dt2 = datetime.strptime('2017-03-04 14:44:13', '%Y-%m-%d %H:%M:%s')
(d2 - d1).total_seconds()       # duration.total_seconds()
delta1 = timedelta(seconds = 5)

# Convert from unix timestamp  >> result: 2017-12-30 15:19:13
print(datetime.fromtimestamp(1514665153.0))

from datetime import timezone
ET = timezone(timedelta(hours=-5))
dtz = datetime(2017, 12, 30, 15, 9, 3, tzinfo = ET)
IST = timezone(timedelta(hours=5, minutes=30))      # India

print(dtz)                              # > 2017-12-30 15:09:03-05:00
print(dtz.astimezone(IST))              # > 2017-12-31 01:39:03+05:30
print(dtz.replace(tzinfo=timezone.utc)) # > 2017-12-30 15:09:03+00:00

#
from dateutil import tz   # includes rule for changing time in timezones

et = tz.gettz('America/New_York')   #
last = datetime(2017, 12, 30, 15, 9, 3, tzinfo=et)

tz.datetime_ambiguous(dtz)  # check whether timestamp in ending daylight period
tz.enfold(second_1am)# it refers to the time after the daylight savings time change.

#               !!-! better put everything in UTC 
#

# ############################          datetime in      pandas
# dt = datetime package/module >> 
# from datetime import datetime as dt

riders = pd.read_csv('bikes.csv', parse_dates = ['Start date', 'End date'])

(  rides['Start date'] = pd.to_datetime(rides['Start date'], 
                                     format="%Y-%m-%d %H:%M:%S")   )
rides['Duration'].dt.total_seconds().head(5)
rides['Duration'] = (rides['End date'] - rides['Start date']).dt.total_seconds()
rides.resample('M', on = 'Start date')['Duration seconds'].mean().plot()

rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
rides['Start date'].dt.Year # .dt.month ; .dt.day_name() : .dt.weekday
rides['Start date'].dt.tz_convert('Europe/London')


# %%
# ############################              context manager
# ############################ 

@contextlib.contextmanager
def my_context():
    print('hello')
    yield 42
    print('goodbye')

with my_context() as foo:
    print('foo is {}'.format(foo))

# >> hello
# >> foo is 42
# >> goodbye

#                                           context manager
# Time the execution of a context block.
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.
  Yields:    None"""
  start = time.time()
  yield  # Send control back to the context block
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

# >> This should take approximately 0.25 seconds
# >> Elapsed: 0.25s

#                                           context manager
#
@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.
  Args:     filename (str): The location of the file to read
  Yields:    file object  """
  read_only_file = open(filename, mode='r')   # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  read_only_file.close()   # Close read_only_file

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())

#
#   1                                        context manager
def copy(src, dst):
    """Copy the contents of one file to another.  
    Args:    
    src (str): File name of the file to be copied.    
    dst (str): Where to write the new file.  """
    with open(src) as f_src:       # Open the source file and read in the contents
        contents = f_src.read()
    with open(dst, 'w') as f_dst:  # Open the destination file and write out the contents
        f_dst.write(contents)

#
#   2
def copy(src, dst):
    with open(src) as f_src:            # Open both files
        with open(dst, 'w') as f_dst:
            for line in f_src:          # Read and write each line, one at a time  
                f_dst.write(line)
# second "with open()..." has access to both src and dst files

#
#                                           context manager
with stock('NVDA') as nvda:   # Open "NVDA.txt" for writing as f_out
  with open("NVDA.txt", 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

#                                           context manager
#   example CHANGE/RESET pattern
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.
  Args:    directory (str): The path to a directory to work in.  """
  current_dir = os.getcwd()
  os.chdir(directory)
  try:    # Add code that lets you handle errors
    yield
  finally:    # Ensure the directory is reset, # whether there was an error or not
    os.chdir(current_dir)

#                                           
# ############################                 decorators theme

dict_of_functions = {
    'func1': my_function,
    'func2': open,
    'func3': print     }
dict_of_functions['func3']('I am printing with a value of a dict!')
# >> I am printing with a value of a dict!

#
# cool
def has_docstring(func):
  """Check to see if the function `func` has a docstring.
  Args:     func (callable): A function.
  Returns:     bool   """
  return func.__doc__ is not None

ok = has_docstring(load_and_plot_data)
if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

#
#
def create_math_function(func_name):
  if func_name == 'add':
    def add(a, b):
      return a + b
    return add
  elif func_name == 'subtract':
    def subtract(a, b):
      return a - b
    return subtract
  else:
    print("I don't know that one")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))
subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))

#
# cool
def wait_until_done():
  def check_is_done():
    global done   # Add a keyword so that wait_until_done()  doesn't run forever
    if random.random() < 0.1:
      done = True
  while not done:
    check_is_done()
done = False
wait_until_done()
print('Work done? {}'.format(done))

#
# ############################                 closures
# Nonlocar variables attached to a returned function

my_func = foo(x)
len(my_func.__closure__)
my_func.__closure__[0].cell_contents
print(my_func.__closure__ is not None)

print([cell.cell_contents for cell in new_function.__closure__])
# >> [3, 4, 22, {'chocolate': 'yummy'}]

#
# ############################                 decorators
# they changes behavior of entire function
# ##### code 1    is equivalent    code 2
# code 1
def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper

def multiply(a, b):
    return a * b

multiply = double_args(multiply)
multiply(1, 5)
# >> 20

# code 2
def double_args(func):
    def wrapper(a, b):
        return func(a * 2, b * 2)
    return wrapper

@double_args
def multiply(a, b):
    return a * b

multiply(1, 5)
# >> 20

#
# 
def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    func(*args)     # Call the function being decorated with *args
    print('After {}'.format(func.__name__))
  return wrapper    # Return the nested function

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)


# %%
# ############################           Regular Expressions in Python

'dfdf gdfh dfg {1} sdfsdf {0}'.format('123', '345')

#
courses = ['artificial intelligence', 'neural networks']
plan = {    'field': courses[0],
            'tool': courses[1]    }
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"
print(my_message.format(data=plan))

#
from datetime import datetime
get_date = datetime.now()

message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

print(message.format(today = get_date))
print(f"Today's date is {get_date:%B %d, %Y}.")

#
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

#
from string import Template
wikipedia = Template("$tool is a $description")
wikipedia.substitute(tool=tool1, description=description1)

the_answers = Template("Check your answer 1: $answer1, and your answer 2: $answer2")
try:    # Use safe_substitute to replace identifiers
    print(the_answers.safe_substitute(answers))
except KeyError:
    print("Missing information")
#dict 'answers' has only 1 key 'answer1', so method substitute will raise an error

#
import re

re.findall(r"mov", "mov ax, cx. And move it faster!")
re.split(r"mov", "heh, you should mov ax, cx. And move it faster!")
re.sub(r"mov", "dance" ,"heh, you should mov ax, cx. And move it faster!")

'''
\d      digit
\D      non-digit
\w      word
\W      non-word
\s      whitespace      "Data\sEngineering"
\S      non-whitespace
{n}     n times
{n, m}  n times at least, m times at most
+       once or more         r"apple+"  >>  '+' applies to e and not to apple
*       zero times or more
?       zero time or once
.       any character
^       anchor to beginning
()      groups
|       alternation
(?:regex)      non-capturing groups
(?P<name>)     named groups
\1             backreference (\1, \2, \3 ...)
(?=regex)      positive look-ahead
(?!regex)      negative look-ahead
(?<=regex)     positive look-behind
(?<!=regex)    negative look-behind
'''

re.search(r"\w{9}\d{4}", my_string) #password1234
re.search(r"\d+-\d+", my_string)    # 3-4 , 10-04
re.search(r"\w+\W*\w+", my_string)  # 
# Write regex to match http links and print out result
print(re.findall(r"http\S*", tweet))
# Write regex to match user mentions and print out result
print(re.findall(r"@\S*", tweet))

re.match(r"?", "string")

#       greedy and non greedy matching
string = "I want to see that <strong>amazing show</strong> again!"
string_notags = re.sub(r"<.+?>", "", string)

#Did you include +? in the regex as a lazy quantifier that looks 
#for numbers that occur one or more times?
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis) #lazy matching
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis) #greedy matching

#
x_str = "Absd (asd asd) fggsdf sdgs dgfsf (sfg sdf sdf)"
sentences_found_greedy = re.findall(r"\(.+?\)", x_str)
# if you use greedy pattern r"\(.*\)" you will return next string:
#   '(asd asd) fggsdf sdgs dgfsf (sfg sdf sdf)
# with 1st and last parentheses

#
# ##########################        groups

we_str = "Clary has 2 friends who she spends a lot time with. Susan has 3 brothers while John has 4 sisters."

re.findall(r'[A-Za-z]+\s\w+\s\d+\s\w+', we_str)
# ['Clary has 2 friends', 'Susan has 3 brothers', 'John has 4 sisters']
re.findall(r'([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', we_str)
# [('Clary', '2', 'friends'), ('Susan', '3', 'brothers'), ('John', '4', 'sisters')]

re.search(r"(\d[A-Za-z])+", "My user name is 3e4r5t6yh")
re.findall(r"(\d)+", "My lucky number are 23431 and 32")    #['1', '2']
re.findall(r"(\d+)", "My lucky number are 23431 and 32")    #['23431', '32']

regex_email = r"([A-Za-z0-9]+\S+)@"  # Write a regex that matches email

# alternation       |
re.findall(r"(\d+)\s(cat|dog|bird)", "A aaff 2 cats, 4 dogs aesdf sdf sdf.")

# non-capturing groups      ?:      >> (?:regex)
re.findall(r"(\d+)(?:th|rd)", "Today is 23rd May. Tomorrow is 24th May.") # ['23', '24']

# Did you include (.+?) in the regex as the third capturing group 
# to match anything but a whitespace once or more times?
'''I totally love the concert The Book of Souls World Tour.'''
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\."

#
text_str = "Austin, 78701"
cities = re.search(r"([A-Za-z]+).*?(\d{5})", text_str)
cities.group(2)     #   '78701'
cities.group(0)

#
cities = re.search(r"(?P<city>[A-Za-z]+).*?(?P<zipcode>\d{5})", text_str)
cities.group("city")    # 'Austin'

# backreference
sentence1 = "I wish you happy happy birthday!" # repeated word: happy happy
re.findall(r"(\w+)\s\1", sentence1)  # ['happy']
re.sub(r"(\w+)\s\1", r"\1", sentence1) # 'I wish you happy birthday!' >> no more 2 happy

sentence2 = "New code is 123123. Enter 123123 to open."
re.findall(r"(?P<code>\d{6}).*?(?P=code)", sentence2) # ['123123']

re.sub(r"(?P<word>\w+)\s(?P=word)", r"\g<word>", sentence1) # no more repeated word

# catch opened HTML tags: <b>dsfad asd  </b>
match_tag =  re.match(r"^<(\w+)>.*?</\1>", "<b>dsfad asd sdsd </b>")

# ####### look-ahead
srt1 = "ab.txt sent, my.txt sent, his.txt error"
re.findall(r"\w+\.txt(?=\ssent)", srt1) # ['ab.txt', 'my.txt']  positive look-ahead 
re.findall(r"\w+\.txt(?!\ssent)", srt1) # ['his.txt']           negative look-ahead 

# ####### look-behind
srt2 = "Member: Martin Flame, Member: Rimma Sue, Past: Julia Minnesota."
re.findall(r"(?<=Member:\s)\w+\s\w+", srt2)             #   positive look-behind 

srt3 = "My white cat is slipping, but his black dog is barking." # lol)
re.findall(r"(?<!white\s)(cat|dog)", srt3)             #   negative look-behind 


# %%
#
# ###################################                   O O P
'''
Class   A blueprint/template used to build objects
Object  A combination of data and functionality; An instance of a class
State   Data associated with an object, assigned through attributes
Behavior    An object's functionality, defined through methods
'''

# Customer version 1
class Customer:
    def identify(self, name):
        print("I am Customer " + name)

cust = Customer()
cust.identify("Laura") # is the same as       Customer.identify(cust, "Laura")
Customer.identify(cust, "Laura") # ! is the same as       cust.identify("Laura")

# Customer version 2
class Customer:
    def set_name(self, new_name):
        self.name = new_name
    def identify(self):
        print("I am Customer " + self.name)

cust = Customer()
cust.set_name('Yurii DDD')
cust.identify()

# Customer version 3
class Customer:
    def __init__(self, name): # init method is called every time an object is created
        self.name = name

cust = Customer('Yurii DDD')

# Customer version 4
class Customer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        
cust = Customer('Yurii DDD', 150000)

#
# ###################################                   O O P
'''
Encapsulation
Inheritance
Polymorphism
'''

#       Encapsulation
# Eployee
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod 
    def from_file(cls, filename):       # use class method to create object
        with open(filename, "r") as file:
            name = file.readline().strip()
            salary = int(file.readline().strip())
        return cls(name, salary)        # return an object

# employee_data.txt:
# John Smith
# 40000
emp = Employee.from_file("employee_data.txt")
print(emp.name)

#
self.year, self.month, self.day = year, month, day
parts = datestr.split("-")
year, month, day = int(parts[0]), int(parts[1]), int(parts[2])

#
#       Inheritance

#
class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        BankAccount.__init__(self, balance)
        self.interest_rate = interest_rate
    def compute_interest(self, n_periods = 1) # new functionality
        return self.balance * ( (1 + self.interest_rate) ** n_periods - 1)
    
acct = SavingsAccount(1000, 0.3)
acct.interest_rate

#
class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit
    def deposit (self, amount):
        self.balance += amount
    def withdraw(self, amount, fee = 0):  #rewrite original from BankAcc + add new argument
        if amount <= self.limit:
            BankAccount.withdraw(self, amount + fee)
        else:
            pass    # won't run if the condition isn't met

# compare same instances of classes
class Customer:
    def __init__(self, acc_id, name):
        self.acc_id, self.name = acc_id, name
    def __eq__(self, other):
        print("__eq__() is called")
        return (self.acc_id == other.acc_id) and (self.name == other.name)
#           and (type(self) == type(other))
# add type clause to exampt comparison of parent and child classes

#
class Customer:
    def __init__(self, name):
        self.name = name
        self.balance = balance
    def __repr__(self): # notice the ' ... ' around name
        return f"Customer('{self.name}', {self.balance})"
    def __str__(self):
        cust_str = f"""
        Customer:
            name: {self.name}
            balance: {self.balance}
            """
        return cust_str

#
# ########### Exeptions

class BalanceError(Exception):
    pass

class Customer:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError("Balance has to be non-negative!")
        else:
            self.name = name
            self.balance = balance

# %%

#
# ################################























