#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sat Feb 22 13:37:34 2025@author: yurii
"""

# %%#################################             
# ###################################               NumPy array
# ###################################

import numpy as np

# %%################################# 
# ###################################       CREATE
# ###################################
nums_np = np.array(range(5))
nums_np_ints = np.array([1, 2, 3]) # NumPy array homogeneity, all elements is the same type
nums_np_ints.dtype          # >> dtype('int64')

nums_np_floats = np.array([1, 2.5, 3])
nums_np_ints.dtype          # >> dtype('float64')

np.zeros()
np.zeros((5, 3))            # 5 rows, 3 columns array of zeros

np.random.random()
np.random.random((2, 4))    # 2 rows, 4 columns array of random values

np.arange()
np.arange(4)                # array([0, 1, 2, 3])
np.arange(-3, 4)            # array([-3, -2, -1, 0, 1, 2, 3])
np.arange(-3, 4, 3)         # array([-3, 0, 3])

from matplotlib import pyplot as plt
plt.scatter(np.arange(0, 7),
            np.arange(-3, 4))
plt.show()

#
np.array([numpyarray1, numpyarray2])    # 3D array
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])

'''4D array. The .shape of (2, 2, 9, 9) means that there are two sets of 
game/solution pairs. Within each game/solution pair, all arrays have nine rows 
and nine columns. That's exactly right! If there were ten game/solution pairs, 
the .shape would be (10, 2, 9, 9).'''

# .dtype for numbers may be int64, int32, float64, float32, <U12
float32_array = np.array([1.32, 5.78, 175.55], dtype=np.float32)

boolean_array = np.array([[True, False], [False, False]], dtype=np.bool_)
boolean_array.astype(np.int32)
'''array([[1, 0],
          [0, 0]], dtype=int32)'''

np_array.shape

#
help(np.unique)
help(np.ndarray.flatten)

# %%################################# 
# ###################################       SLICE
# ###################################
# list vs np array
nums = [-2, -1, 0, 1, 2]    # list
nums ** 2                   # >> ERROR , can't operate ** in list

nums_np = np.array([-2, -1, 0, 1, 2])
nums_np ** 2                # >> array([4, 1, 0, 1, 4])

# list vs np array
nums2 = [[1, 2, 3],
         [4, 5, 6]]
nums2[0][1]                 # >> 2

nums2_np = np.array(nums2)
nums2_np[0, 1]              # >> 2
print(nums_np[1,:])         # Print second row of nums [4, 5, 6]
nums[:,2] = nums[:,2] + 1   # Replace the third column of nums


[row[0] for row in nums2]   # >> [1, 4]
nums2_np[:, 0]              # >> [1, 4] , is like select 1st column

sudoku_game[3:6, 3:6]       # slise 2d array
sudoku_game[3:6:2, 3:6:2]   # 2 is step value

# sorting
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]

np.sort(sudoku_game)        # default axis is 1 (column), sort looks like
[[0, 0, 0, 0, 0, 0, 1, 3, 5, 9],]

np.sort(sudoku_game, axis=0)    # sort every 1st element between all rows

# Create an array, xq, which contains only trunk diameters for trees with 
# even row indices from 50 to 100, inclusive. (indicies, not rows)
xq = tree_census[50:101:2, 2]





# %%#################################       
# ###################################       FILTERING
# ###################################
# fancy indexing
nums_np > 0                 # boolean mask, like with dataframes
print(nums_np)              # >> array([False, False, False, True, True])
nums_np[nums_np > 0]        # >> array([1, 2])

one_to_six = np.arange(1, 7)
mask = one_to_six % 2 == 0      # boolean mask
one_to_six[mask]                # >> array([2, 4, 6])

classroom_ids_and_sizes = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
classroom_ids_and_sizes[:, 1] % 2 == 0  # create condition on 2nd column
# >> array([ True, False, False,  True])
classroom_ids_and_sizes[:, 0][classroom_ids_and_sizes[:, 1] % 2 == 0]

#
np.where(classroom_ids_and_sizes[:, 1] % 2 == 0)
(array([0, 3]),)        # show indicies (not values) which meet condition

row_ind, column_ind = np.where(sudoku_game == 0)     # tuple of indicies

np.where(sudoku_game == 0, "", sudoku_game)     # like find and replace
np.where(classroom_ids_and_sizes > 25, "", classroom_ids_and_sizes)
array([['1', '22'],
       ['2', '21'],
       ['3', ''],
       ['4', '']], dtype='<U21')
trunk_stump_diameters = np.where(tree_census[:, 2] == 0,    # condition
                                 tree_census[:, 3],         # if true
                                 tree_census[:, 2])         # if false
#
vectorized_len = np.vectorize(len)
vectorized_len(array) > 2
array([ True, False,  True])

vectorized_upper = np.vectorize(str.upper)

# %%#################################
# ###################################       CONCAT
# ###################################
classroom_ids_and_sizes = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
new_classroom = np.array([[5, 30], [6, 17]])
grade_levels_and_teachers = np.array([[1, "James"], [1, "George"],
                                      [3,"Amy"], [3, "Meehir"]])


np.concatenate((classroom_ids_and_sizes, new_classroom))    # axis = 0
np.concatenate((classroom_ids_and_sizes, grade_levels_and_teachers), axis=1)
array([['1', '22', '1', 'James'],
       ['2', '21', '1', 'George'], .. )

# you should reshape to concat same size shapes 
array_1D = np.array([1, 2, 3])
column_array_2D = array_1D.reshape((3, 1))

#
np.delete(classroom_data, 1, axis=0)    # delete 2nd row (row with index 1)
np.delete(classroom_data, 2, asix=1)    # delete 3rd coulmn (col with index 2)

private_block_indices = np.where(tree_census[:,1] == 313879)
# Delete the rows for trees on block 313879 from tree_census_no_stumps
tree_census_clean = np.delete(tree_census_no_stumps,
                              private_block_indices, axis=0)



# %%#################################
# ###################################       AGGREGATION
# ###################################

.sum()                  # summing all data, result is one number
np_array.sum(axis=0)    # summing all rows in each column = column TOTAL
np_array.sum(axis=1)    # summing all columns in each row = row TOTAL

.min()
.max()
.mean()
, keepdims=True     # saves shape compatibility, .sum(axis=1) results array (n,)
                    # with keepdims=True row summary .sum(axis=1) >> (n, 1)

.cumsum(axis=0)     # column cummulative sum

#
cum_sums_by_client = security_breaches.cumsum(axis=0)
plt.plot(np.arange(1, 6), cum_sums_by_client[:, 0], label="Client 1")
plt.plot(np.arange(1, 6), cum_sums_by_client.mean(axis=1), label="Average")
plt.legend()
plt.show()

# broadcasting (+, -, *, ..)
shape(10, 5) + shape(10, 1)
shape(2, 5) + shape(1, 5)
shape(3, 4) + shape(4, )

np.arange(10).reshape((2, 5)) + np.array([0, 1]).reshape((2, 1))



# %%#################################
# ###################################       EXTRACT, LOAD
# ###################################

# extract
with open("logo.npy", "rb") as file:
    logo_rgb_array = np.load(file)

# load
with open("dark_logo.npy", "wb") as file:
    np.save(file, dark_logo)

# %%#################################
# ###################################       TRANSFORMATION
# ###################################

np_array.flatten()
np_array.reshape()

# total flip
flipped_logo = np.flip(logo_rgb_array)
plt.imshow(flipped_logo)
plt.show()

#
flipped_rows_logo = np.flip(logo_rgb_array, axis=0)
flipped_colors_logo = np.flip(logo_rgb_array, axis=2)
flipped_except_colors_logo = np.flip(logo_rgb_array, axis=(0, 1))

#
array = np.array([[1.1, 1.2, 1.3],
                  [2.1, 2.2, 2.3],
                  [3.1, 3.2, 3.3],
                  [4.1, 4.2, 4.3]])

np.flip(array)
array([[4.3, 4.2, 4.1],
       [3.3, 3.2, 3.1],
       [2.3, 2.2, 2.1],
       [1.3, 1.2, 1.1]])

np.transpose(array)
array([[1.1, 2.1, 3.1, 4.1],
       [1.2, 2.2, 3.2, 4.2],
       [1.3, 2.3, 3.3, 4.3]])

transposed_logo = np.transpose(logo_rgb_array, axes=(1, 0, 2))
plt.imshow(transposed_logo)
plt.show()

# split
rgb = np.array([[[255, 0, 0], [255, 255, 0], [255, 255, 255]],
                [[255, 0, 255], [0, 255, 0], [0, 255, 255]],
                [[0, 0, 0], [0, 255, 255], [0, 0, 255]]])

red_array = rgb[:, :, 0]
green_array = rgb[:, :, 1]
blue_array = rgb[:, :, 2]

red_array               # 1
array([[255, 255, 255],
       [255,   0,   0],
       [0,   0,   0]])

red_array, green_array, blue_array = np.split(rgb, 3, axis=2)
red_array               # 2
array([[[255], [255], [255]],
       [[255], [  0], [  0]],
       [[  0], [  0], [  0]]])
red_array.shape
(3, 3, 1)

red_array_2D = red_array.reshape((3, 3))
array([[255, 255, 255],
       [255,   0,   0],
       [  0,   0,   0]])
red_array_2D.shape
(3, 3)

# like slice 4 time dataset every 3 rows (it was 12 total), now 4 x 3 rows
q1_sales, q2_sales, q3_sales, q4_sales = np.split(monthly_sales, 4, axis=0)
print(q1_sales)
array([[ 4134, 23925,  8657],
       [ 4116, 23875,  9142],
       [ 4673, 27197, 10645]])

# stack
red_array, green_array, blue_array = np.split(logo_rgb_array, 3, axis=2)
plt.imshow(red_array)
plt.show()

red_array = np.zeros((1001, 1001)).astype(np.int32)
green_array = green_array.reshape((1001, 1001))
blue_array = blue_array.reshape((1001, 1001))

stacked_rgb = np.stack([red_array, green_array, blue_array], axis=2)
plt.imshow(stacked_rgb)
plt.show()













# %%#################################
# ###################################       1
# ###################################






