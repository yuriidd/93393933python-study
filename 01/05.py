# -*- coding: utf-8 -*-
"""Created on Sun Jul 10 06:01:13 2022@author: xiaom"""


#=================== TUPLE    LIST SET
s = 'asdfghjkl'
for x in s: print(x)




m_op = ('093', '073', '066', '098', '050', '097', '067')
l_op = list(m_op)
for op in sorted(m_op):
    print(op)


for op in l_op:
    print(op)

if '093' in l_op:
    print('h')

i=0
while i < len(m_op):
    print(m_op[i])
    i += 2

# s.index
# l_op.index
# l_op.remove('060')
# print(m_op)


qq = range(10, 21)
for x in qq:
    print(x, end='-')

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tuple(sorted(m_op + tup2))
tup3 = tup1 + tup2
sorted(tup2)


for x in tup2:
    print(type(x))
    print(x.isalnum())
    # print(isinstance(x, str))
    
'6'.isdigit()
'6dd'.isalnum()

# type('sfsdf') #is str

a = {'093', '073', '066', '098', '050', '097', '067'}
b = {'093', '073', '066', '098', '020', '023', '091'}

'''union, intersection, symmetric difference, etc.'''

a - b
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

a.update([3,6,7],(10,20,30))
a.remove('023')
a.discard('393')

a = {'093', '073', '066', '098', '050', '097', '067'}
print(a)
print(a.pop())
print(a)

aa = set(range(10, 21))

A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}

print(l_op.sort())
###########
lang = ['Python', 'Java', 'JavaScript']
print(enumerate(lang))
xzz = list(enumerate(lang))
xzz
for i,x in enumerate(lang,9):
    print(x,i)
xzz = tuple(enumerate(lang)) 


m = list([1, 2, 3])
n = m

m.pop()

a =  10
# id(a)
# Out[10]: 2747480631888

a += 5
# id(a)
# Out[12]: 2747480632048

b = 10
# id(b)
# Out[14]: 2747480631888

my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)
my_list.insert(2,4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(6.5))
print(my_list.index(4.5))
my_list.remove(6.5)
print(my_list)
del my_list[0]
print(my_list)


s = 'lolo'
id(s)

s = 'yolo'
a = 'lolo'
id(a)
my_set = {False, 3, 4.5, 6, 'cat'}
your_set = {99, 3, 100}
his_set = {3, 100}
###
your_set >= his_set
his_set.issubset(your_set)
###
capitals = {"Iowa": "Des Moines", "Wisconsin": "Madison", 'Zimma': 'Blue'}
capitals['Leto']='Red'
capitals['Leto']='Fine'
'''capitals[2]''' # error
capitals.remove('Leto')
capitals.keys()
capitals.values()
capitals.items()
type(capitals.items())
type(capitals)
capitals.get('Letto')
capitals['Iowa']
#######################
'''Homework:            Task 1
The greatest number
Write a Python program to get the largest number from a list of random 
numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
'''

import random
gn_list = []
# for i in range(10):
#     gn_list.append(random.randrange(1,100))
k = 0
while k < 10:
    gn_list.append(random.randrange(1,100))
    k += 1
print(max(gn_list))


########
'''Task 2
Exclusive common numbers.
Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers between the 2 initial 
lists without any duplicates.
Constraints: use only while loop and random module to generate numbers'''

import random
ge_list = []
gl_list = []
i = 0
while i < 10:
    ge_list.append(random.randrange(1,10))
    gl_list.append(random.randrange(1,10))
    i += 1
gg_list = list(set(ge_list) | set(gl_list))
print(gg_list)
###########
'''             Task 3
Extracting numbers.
Make a list that contains all integers from 1 to 100, then find all integers 
from the list that are divisible by 7 but not a multiple of 5, and 
store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration'''
import random
gr_list = []
gx_list = []
r = 0
while r < 10:
    gr_list.append(random.randrange(1,100))
    if gr_list[r] > 6 and (gr_list[r] % 7) == 0 and (gr_list[r] % 5) != 0:
        gx_list.append(gr_list[r])
    r += 1
print('full:', gr_list, '\n7-5:', gx_list)

# if 21 > 6 and (21 // 7) == 0 and (21 // 5) != 0:
#     print(True)
    
############

z1 = zip(mutants, powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)
# wtf ?