# -*- coding: utf-8 -*-
"""Created on Sat Aug  5 22:01:38 2023@author: xiaom"""


####################################
####################################
####################################
####################################                MATCH  1 STRING  


'''
Out[5]:

<bound method NDFrame.head of        rest_name     rest_addr      city       phone          cuisine_type
0    arnie morton  s of chicago   435 s. la cienega blv .     los angeles  3102461501      america
1           art  s delicatessen       12224 ventura blvd.     studio city  8187621221      merican
2                     campanile       624 s. la brea ave.     los angeles  2139381447     amurican
3                         fenix    8358 sunset blvd. west       hollywood  2138486677     americen
4            grill on the alley           9560 dayton way     los angeles  3102760615    americann
..                          ...                        ...            ...         ...          ...
331           vivande porta via         2125 fillmore st.   san francisco  4153464430      italian
332          vivande ristorante      670 golden gate ave.   san francisco  4156739245      italian
333                world wrapps         2257 chestnut st.   san francisco  4155639727     american
334                     wu kong             101 spear st.   san francisco  4159579300        asian
335                   yank sing           427 battery st.   san francisco  4155414949      asianne

'''



# Import process from thefuzz
from thefuzz import process
# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

'''
unique_types

array(['america', 'merican', 'amurican', 'americen', 'americann',
       'asiane', 'itali', 'asiann', 'murican', 'italien', 'italian',
       'asiat', 'american', 'americano', 'italiann', 'ameerican',
       'asianne', 'italiano', 'americin', 'ammericann', 'amerycan',
       'aamerican', 'ameriican', 'italiaan', 'asiian', 'asiaan',
       'amerrican', 'ameerrican', 'ammereican', 'asian', 'italianne',
       'italiian', 'itallian'], dtype=object)'''

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))
# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))
# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))

'''
[('asian', 100), ('asiane', 91), ('asiann', 91), ('asiian', 91), ('asiaan', 91), ('asianne', 83), ('asiat', 80), ('italiann', 72), ('italiano', 72), ('italianne', 72), ('italian', 67), ('amurican', 62), ('american', 62), ('italiaan', 62), ('italiian', 62), ('itallian', 62), ('americann', 57), ('americano', 57), ('ameerican', 57), ('aamerican', 57), ('ameriican', 57), ('amerrican', 57), ('ammericann', 54), ('ameerrican', 54), ('ammereican', 54), ('america', 50), ('merican', 50), ('murican', 50), ('italien', 50), ('americen', 46), ('americin', 46), ('amerycan', 46), ('itali', 40)]
[('american', 100), ('americann', 94), ('americano', 94), ('ameerican', 94), ('aamerican', 94), ('ameriican', 94), ('amerrican', 94), ('america', 93), ('merican', 93), ('ammericann', 89), ('ameerrican', 89), ('ammereican', 89), ('amurican', 88), ('americen', 88), ('americin', 88), ('amerycan', 88), ('murican', 80), ('asian', 62), ('asiane', 57), ('asiann', 57), ('asiian', 57), ('asiaan', 57), ('italian', 53), ('asianne', 53), ('italiann', 50), ('italiano', 50), ('italiaan', 50), ('italiian', 50), ('itallian', 50), ('italianne', 47), ('asiat', 46), ('itali', 40), ('italien', 40)]
[('italian', 100), ('italiann', 93), ('italiano', 93), ('italiaan', 93), ('italiian', 93), ('itallian', 93), ('italianne', 88), ('italien', 86), ('itali', 83), ('asian', 67), ('asiane', 62), ('asiann', 62), ('asiian', 62), ('asiaan', 62), ('asianne', 57), ('amurican', 53), ('american', 53), ('americann', 50), ('asiat', 50), ('americano', 50), ('ameerican', 50), ('aamerican', 50), ('ameriican', 50), ('amerrican', 50), ('ammericann', 47), ('ameerrican', 47), ('ammereican', 47), ('america', 43), ('merican', 43), ('murican', 43), ('americen', 40), ('americin', 40), ('amerycan', 40)]
'''

#
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], 
                          limit=len(restaurants.cuisine_type))
# Inspect the first 5 matches
print(matches[0:5])
'''[('italian', 100, 11), ('italian', 100, 25), ('italian', 100, 41), 
('italian', 100, 47), ('italian', 100, 49)]'''

#
#    
# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] >= 80:
    # Select all rows where the cuisine_type is spelled this way, 
    #and set them to the correct cuisine
    restaurants.loc[restaurants['cuisine_type'] == match[0], 
                    'cuisine_type'] = 'italian'

#
##                          same        IN LOOP         for all categories
#           well done

# Iterate through categories
for cuisine in categories:  
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(cuisine, restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['cuisine_type'] == match[0]] = cuisine
# Inspect the final result
print(restaurants['cuisine_type'].unique())

'''         ['american' 'asian' 'italian']            '''


####################################
####################################                MATCH   STRING  PAIRS
import recordlinkage
# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()
# Block pairing on cuisine_type
indexer.block('cuisine_type')
# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)

'''
In [1]:
pairs
Out[1]:
MultiIndex([(  0,  0),
            (  0,  1),
            (  0,  7),
            (  0, 12),
            (  0, 13),
            (  0, 20),
            (  0, 27),
            (  0, 28),
            (  0, 39),
            (  0, 40),
            ...
            (284, 63),
            (284, 66),
            (287, 24),
            (287, 63),
            (287, 66),
            ( 40, 18),
            (281, 18),
            (288, 18),
            (302, 18),
            (308, 18)],
           length=3631)

'''

# Create a comparison object
comp_cl = recordlinkage.Compare()
# Find exact matches on city, cuisine_types - 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')
# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold = 0.8) 
# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

'''
           city  cuisine_type  name
    0   0      0             1   0.0
        1      0             1   0.0
        7      0             1   0.0
        12     0             1   0.0
        13     0             1   0.0
    ...      ...           ...   ...
    40  18     0             1   0.0
    281 18     0             1   0.0
    288 18     0             1   0.0
    302 18     0             1   0.0
    308 18     0             1   0.0
    
    [3631 rows x 3 columns]'''

###
potential_matches[potential_matches.sum(axis = 1) >= 3]
'''
       city  cuisine_type  name
0  40     1             1   1.0
1  28     1             1   1.0
2  74     1             1   1.0
3  1      1             1   1.0
4  53     1             1   1.0
8  43     1             1   1.0
9  50     1             1   1.0
13 7      1             1   1.0
14 67     1             1   1.0
17 12     1             1   1.0
20 20     1             1   1.0
21 27     1             1   1.0
5  65     1             1   1.0
7  79     1             1   1.0
12 26     1             1   1.0
18 71     1             1   1.0
6  73     1             1   1.0
10 75     1             1   1.0
11 21     1             1   1.0
16 57     1             1   1.0
19 47     1             1   1.0
15 55     1             1   1.0'''


# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]
# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)
# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]
# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)



