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
#####################################
#####################################
#####################################

print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])
# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)
# Print rows with inconsistent category
print(airlines[cat_clean_rows])
# Print rows with consistent categories only
print(airlines[~cat_clean_rows])



# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})
# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()



# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']
# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)
# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}
airlines['day_week'] = airlines['day'].replace(mappings)





# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")
# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")
# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False





# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()
# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]
# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40
print(airlines_survey['survey_response'])


#############
'''
In [2]:
banking.head()
Out[2]:

    cust_id  acct_amount acct_cur  inv_amount account_opened last_transaction
0  8C35540A     44244.71   dollar    35500.50       03-05-18         30-09-19
1  D5536652     86506.85   dollar    81921.86       21-01-18         14-01-19
2  A631984D     77799.33   dollar    46412.27       26-01-18         06-10-19
3  93F2F951     93875.24     euro    76563.35       21-08-17         10-07-19
4  DE0A0882     99998.35     euro    18669.01       05-06-17         15-01-19
'''

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'
# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1
# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'
# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'


##

# Print the header of account_opend
print(banking['account_opened'].head())
# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Infer datetime format
                                           infer_datetime_format = True,
                                           # Return missing value for error
                                           errors = 'coerce') 
# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')
print(banking['acct_year'])

##


# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']
# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']
# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]
# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])



# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year
# Find rows where age column == ages_manual
age_equ = banking['age'] == ages_manual
# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]
# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])


###############
'''The pandas, missingno and matplotlib.pyplot packages have been imported 
as pd, msno and plt respectively. 
'''
# Print number of missing values in banking
print(banking.isna().sum())
# Visualize missingness matrix
msno.matrix(banking)
plt.show()


# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

missing_investors.describe()
investors.describe()

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by = 'age')
msno.matrix(banking_sorted)
plt.show()

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])
# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5
# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})
# Print number of missing values
print(banking_imputed.isna().sum())

'''
    cust_id             0
    acct_amount         0
    inv_amount          0
    account_opened      0
    last_transaction    0
    dtype: int64
'''



#################################################3
for row in rangers_df.iterrows():
    x = 1
  #### ####  
    
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in rangers_df.itertuples():
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)
    
    
############################3############################3  
run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    run_diffs.append(run_diff)
# Append new column
yankees_df['RD'] = run_diffs
print(yankees_df)    
    
print(yankees_df[yankees_df['RD'] == 309])





    
############################3############################3  
'''In [2]:
rays_df[:6]
Out[2]:

       RS   RA   W  Playoffs
2012  697  577  90         0
2011  707  614  91         1
2010  802  649  96         1
2009  803  754  84         0
2008  774  671  97         1'''


    
# Gather sum of all columns
stat_totals = rays_df.apply(sum, axis=0)
print(stat_totals)    
    
######   
# Gather total runs scored in all games per year
total_runs_scored = rays_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)    
#######
# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = rays_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)


#############################################

# Display the first five rows of the DataFrame
print(dbacks_df.head())

'''
  Team League  Year   RS   RA   W    G  Playoffs
0  ARI     NL  2012  734  688  81  162         0
1  ARI     NL  2011  731  662  94  162         1
2  ARI     NL  2010  713  836  65  162         0
3  ARI     NL  2009  720  782  70  162         0
4  ARI     NL  2008  720  706  82  162         0'''

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')



############                                      PND can calc as NP aarays
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df['W'].values, baseball_df['G'].values)
# Append a new column to baseball_df that stores all win percentages
baseball_df['WP'] = win_percs_np

print(baseball_df.head())


############ 
############ 
############  
def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)

# Apply predict_win_perc to each row of the DataFrame
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# Calculate the win percentage predictions using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np
print(baseball_df.head())



###################################      
###################################                             MERGE (JOIN)   
# Merge crosswalk into cafes on their zip code fields
cafes_with_pumas = cafes.merge(crosswalk,
                        left_on = 'location_zip_code',
                        right_on= 'zipcode')
# Merge pop_data into cafes_with_pumas on puma field
cafes_with_pop = cafes_with_pumas.merge(pop_data,
                       left_on = 'puma',
                       right_on = 'puma' )
# View the data
print(cafes_with_pop.head())





###################################   transpose

# Change the DataFrame so rows become columns and vice versa
fifa_transpose = fifa_players.set_index('name')[['height', 'weight']].transpose()
# Print fifa_transpose
print(fifa_transpose)









