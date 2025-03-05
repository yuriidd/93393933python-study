import pandas as pd
import os

#
print(os.getcwd())
#os.chdir('../03datacamp/somedata')
os.chdir('/home/yurii/git/93393933python-study/03datacamp/somedata')
print(os.getcwd())

os.path.exists('/home/yurii/git/93393933python-study/03datacamp/somedata/temperatures.csv')


#
csv = 'temperatures.csv'
df = pd.read_csv(csv, sep = ',')

print(df.head())
print('- - - - \n')

df.info()

df['city2'] = df['city'].replace('A', 'AAA', regex = True)
print(df['city2'].unique() )
df['city'].str.replace('A', 'AAA').head()


df.shape
df.values
df.columns # Unnamed: 0    date    city    country  avg_temp_c    date2
df.index

# # indexes and concatenates columns
# df['Unnamed: 0'].head()

# df2 = df.set_index('Unnamed: 0')
# # df2.index.str.cat(df2['city'].astype(str), sep='-')
# df_i_str = df.set_index('country')
# df_i_str.index.str.cat(df_i_str['city'], sep = '-')

############ test convert to bool

credit_default = ['no','unknown','no','no','no','unknown','yes','unknown','yes','no']
df_need_bool = pd.DataFrame({'credit_default' : credit_default})
df_need_bool


df_need_bool['credit_default'].replace('no', 0)
({'HF -':'Hi'}, regex=True))

df_need_bool['credit_default'].replace({'no': 0, 'unknown': 0, 'yes': 1}).astype(bool)



df['date_dt'] = pd.to_datetime(df['date_str']).dt.date  # convert to date

new_list = ['aaa', 'bbb','ccc']
str.cat(new_list, sep = ' ') 

df_need_bool['concat_col'] = (df_need_bool['credit_default'] + ' - ') 



############
############
############ TODO
# 1 теряется ли хедер, когда когда читаешь вторые 500 строк?
# 2 как срабатывает list(tax_data_first1000)? читается только первая строка?
# 

tax_data_first1000 = pd.read_csv('tax_data_2016.csv', nrows=1000) # 1st read
col_names = list(tax_data_first1000)
tax_data_next500 = pd.read_csv('tax_data_2016.csv',
                               nrows=500,
                               skiprows=1000,
                               header=None,
                               names=col_names)
print(tax_data_next500.head(1)) # >> [1 rows x 147 columns]


############
############
############ TODO
# что за семи джоин и зачем он нада

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19, on='tid')  # inner

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# какой в этом смысл если можно просто пройтись в таблице1 и сделать фильтр по
# значениям, что не встречаются во второй таблице.
# это в sql какойто другой джоин без пересечения

classic_18_dict = {'pid': {8527: 12,
  8586: 12,
  8533: 12,
  8523: 12,
  8558: 12,
  8584: 12,
  8551: 12,
  8535: 12,
  8592: 12,
  8587: 12,
  8557: 12,
  8565: 12,
  8572: 12,
  8541: 12,
  8532: 12,
  8545: 12,
  8528: 12,
  8556: 12,
  8579: 12,
  8589: 12,
  8562: 12,
  8563: 12,
  8539: 12,
  8567: 12,
  8568: 12},
 'tid': {8527: 3483,
  8586: 3416,
  8533: 3489,
  8523: 3479,
  8558: 3440,
  8584: 3414,
  8551: 3433,
  8535: 3491,
  8592: 3422,
  8587: 3417,
  8557: 3439,
  8565: 3447,
  8572: 3454,
  8541: 3497,
  8532: 3488,
  8545: 3501,
  8528: 3484,
  8556: 3438,
  8579: 3409,
  8589: 3419,
  8562: 3444,
  8563: 3445,
  8539: 3495,
  8567: 3449,
  8568: 3450}}

pop_18_dict = {'pid': {3150: 1,
  315: 1,
  2178: 1,
  2772: 1,
  430: 1,
  2138: 1,
  2817: 1,
  1667: 1,
  506: 1,
  1222: 1,
  1146: 1,
  1192: 1,
  3404: 3,
  3234: 1,
  192: 1,
  3249: 1,
  1793: 1,
  862: 1,
  3241: 1,
  2285: 1,
  1600: 1,
  2830: 1,
  1791: 1,
  2163: 1,
  2567: 1,
  70: 1,
  1173: 1,
  402: 1,
  1454: 1,
  721: 1,
  810: 1,
  1487: 1,
  1726: 1,
  1557: 1,
  2003: 1,
  3328: 3,
  2293: 1,
  752: 1,
  2725: 1,
  1499: 1,
  387: 1,
  134: 1,
  1268: 1,
  1538: 1,
  2947: 1,
  2991: 1,
  26: 1,
  1467: 1,
  679: 1,
  2344: 1,
  32: 1,
  1001: 1,
  1615: 1,
  2709: 1,
  463: 1,
  1334: 1,
  1723: 1,
  51: 1,
  2480: 1,
  450: 1,
  1206: 1,
  2464: 1,
  3336: 3,
  1907: 1,
  2550: 1,
  2860: 1,
  605: 1,
  1457: 1,
  2396: 1,
  1952: 1,
  1840: 1,
  755: 1,
  3287: 1,
  3492: 3,
  2949: 1,
  3396: 3,
  3443: 3,
  2470: 1,
  2768: 1,
  2791: 1,
  3407: 3,
  3364: 3,
  3037: 1,
  2102: 1,
  439: 1,
  279: 1,
  184: 1,
  2337: 1,
  2515: 1,
  1506: 1,
  3115: 1,
  2706: 1,
  3424: 3,
  746: 1,
  1157: 1,
  2665: 1,
  1159: 1,
  1105: 1,
  1330: 1,
  2168: 1,
  1760: 1,
  1426: 1,
  410: 1,
  1313: 1,
  1938: 1,
  879: 1,
  2334: 1,
  1514: 1,
  1188: 1,
  921: 1,
  443: 1,
  809: 1,
  52: 1,
  2960: 1,
  937: 1,
  2339: 1,
  1044: 1,
  2029: 1,
  3337: 3,
  139: 1,
  965: 1,
  2398: 1,
  2595: 1,
  1288: 1,
  3332: 3,
  1815: 1,
  1459: 1,
  1532: 1,
  414: 1,
  3383: 3,
  76: 1,
  3453: 3,
  2005: 1,
  17: 1,
  1047: 1,
  1554: 1,
  599: 1,
  2697: 1,
  495: 1,
  1089: 1,
  144: 1,
  211: 1,
  1374: 1,
  299: 1,
  3496: 3,
  805: 1,
  3085: 1,
  2095: 1,
  3169: 1,
  1226: 1,
  501: 1,
  2754: 1,
  196: 1,
  2624: 1,
  2473: 1,
  1844: 1,
  2672: 1,
  289: 1,
  1876: 1,
  729: 1,
  30: 1,
  179: 1,
  2057: 1,
  346: 1,
  2996: 1,
  2659: 1,
  2781: 1,
  867: 1,
  1336: 1,
  229: 1,
  2880: 1,
  1861: 1,
  170: 1,
  949: 1,
  1894: 1,
  3356: 3},
 'tid': {3150: 3063,
  315: 2712,
  2178: 2641,
  2772: 2271,
  430: 919,
  2138: 794,
  2817: 2381,
  1667: 1889,
  506: 3439,
  1222: 2042,
  1146: 1718,
  1192: 1928,
  3404: 2920,
  3234: 2126,
  192: 539,
  3249: 361,
  1793: 3457,
  862: 743,
  3241: 2133,
  2285: 1258,
  1600: 1822,
  2830: 2394,
  1791: 3455,
  2163: 829,
  2567: 1793,
  70: 2592,
  1173: 1761,
  402: 891,
  1454: 1295,
  721: 1191,
  810: 526,
  1487: 1346,
  1726: 2563,
  1557: 1560,
  2003: 692,
  3328: 3243,
  2293: 1266,
  752: 618,
  2725: 2653,
  1499: 1218,
  387: 2587,
  134: 1019,
  1268: 2087,
  1538: 1382,
  2947: 2445,
  2991: 2542,
  26: 3385,
  1467: 1333,
  679: 126,
  2344: 1396,
  32: 3367,
  1001: 987,
  1615: 1837,
  2709: 2212,
  463: 657,
  1334: 3117,
  1723: 2560,
  51: 110,
  2480: 1617,
  450: 2539,
  1206: 375,
  2464: 1601,
  3336: 2840,
  1907: 3049,
  2550: 1712,
  2860: 2682,
  605: 1254,
  1457: 1298,
  2396: 441,
  1952: 43,
  1840: 1779,
  755: 1903,
  3287: 1966,
  3492: 3429,
  2949: 2447,
  3396: 2897,
  3443: 3344,
  2470: 1607,
  2768: 432,
  2791: 2304,
  3407: 2857,
  3364: 2877,
  3037: 2953,
  2102: 765,
  439: 1273,
  279: 2477,
  184: 531,
  2337: 1408,
  2515: 1646,
  1506: 1225,
  3115: 3031,
  2706: 2209,
  3424: 2908,
  746: 612,
  1157: 1739,
  2665: 2155,
  1159: 1744,
  1105: 1692,
  1330: 671,
  2168: 834,
  1760: 3259,
  1426: 1125,
  410: 899,
  1313: 563,
  1938: 29,
  879: 241,
  2334: 1370,
  1514: 1233,
  1188: 1924,
  921: 314,
  443: 2532,
  809: 525,
  52: 166,
  2960: 2458,
  937: 857,
  2339: 1410,
  1044: 1112,
  2029: 2612,
  3337: 2841,
  139: 1137,
  965: 591,
  2398: 443,
  2595: 2006,
  1288: 2763,
  3332: 3247,
  1815: 1426,
  1459: 1325,
  1532: 1376,
  414: 903,
  3383: 2859,
  76: 2598,
  3453: 3175,
  2005: 694,
  17: 3376,
  1047: 1115,
  1554: 1557,
  599: 1248,
  2697: 2200,
  495: 3500,
  1089: 1523,
  144: 1142,
  211: 2320,
  1374: 83,
  299: 2497,
  3496: 3216,
  805: 521,
  3085: 2987,
  2095: 621,
  3169: 3099,
  1226: 2045,
  501: 3445,
  2754: 2270,
  196: 2165,
  2624: 2098,
  2473: 1610,
  1844: 1783,
  2672: 2162,
  289: 2487,
  1876: 306,
  729: 1199,
  30: 3365,
  179: 1476,
  2057: 490,
  346: 2793,
  2996: 2547,
  2659: 2149,
  2781: 2280,
  867: 229,
  1336: 3119,
  229: 2289,
  2880: 2702,
  1861: 291,
  170: 1467,
  949: 869,
  1894: 2227,
  3356: 3171}}

pop_18 = pd.DataFrame(pop_18_dict)
classic_18 = pd.DataFrame(classic_18_dict)


# Merge classic_18_19 with pop_18_19
classic_pop = classic_18.merge(pop_18, on='tid')  # inner
# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18[classic_18['tid'].isin(classic_pop['tid'])]
popular_classic.shape
print(popular_classic)


popular_classic2 = classic_18[classic_18['tid'].isin(pop_18['tid'])]
popular_classic2.shape
print(popular_classic2)

###
import timeit

%%timeit
classic_pop = classic_18.merge(pop_18, on='tid')
popular_classic = classic_18[classic_18['tid'].isin(classic_pop['tid'])]


%%timeit
popular_classic2 = classic_18[classic_18['tid'].isin(pop_18['tid'])]

############
############
############
############
############

import somemodules.hero_funcs

" ".join('op_pa'.split("_")).title()





nums3 = [[1, 2, 3, 4],
         [5, 6, 7, 8]]
zarr = np.array(nums3)

zarr.reshape((2,2,2))

xas = zarr.reshape((2,2,2))

xas.reshape((2,4))


pop_18.index






############
############
############
############
############

import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, None, 4, 5], 'B': [10, None, 30, None, 50]}
df = pd.DataFrame(data)

# Fill NaN values with the previous row value
df.fillna(method='ffill', inplace=True)



df[['A', 'B']].fillna(method='ffill',inplace=False)



df123 = pd.DataFrame()



round(df['A'] / 3, 2)

round(1.2323, 2)

work_dir = '/work/files/workspace'
work_dir + '/asdasdasd'

try:
    
    assert type('workout.csv') == 'str'
    print('ok')
except TypeError:
    print('no ok')

def extract(file_name):
    try:
        assert type(file_name) == 'str'
        file = pd.read_csv('data/' + file_name)
        print(f'INFO: CSV file "{file_name}" loaded.')
        return dataframe
    except ValueError:
        print(f'"{file_name}" is not a string.')
        
workout = extract('workout.csv')
three_keywords = extract('three_keywords.csv')
workout_geo = extract('workout_geo.csv')
three_keywords_geo = extract('three_keywords_geo.csv')

assert type('/work/files/workspace') == str
x = [4,4,3,4,5]
y = [1,3]
type('/work/files/workspace') == str

any(x)
