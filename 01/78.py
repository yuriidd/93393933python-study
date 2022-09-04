# -*- coding: utf-8 -*-
"""Created on Sat Jul 16 07:31:47 2022@author: xiaom"""

''' a tree of size 3
   *
  ***
 *****

'''
# def print_tree(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(' ', end='')
#         for s in range(2*i+1):
#             print('*', end='')
#         print()

# def print_cri(n):
#     for i  in range(1,n+1):
#         print(' '*(n-i+1) + '*'*(2*i-1))
#     print()
    
# def print_cri2(n):
#     for i  in range(1,n+1):
#         for j in range(n-i+1):
#             print(' ', end='')
#         for s in range(2*i-1):
#             print('*', end='')
#         # print(' '*(n-i+1) + '*'*(2*i-1))
#         print()
# #########

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']     
# ggwp = map(len,freshfruit)
# print(list(ggwp))

# ########################
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# freshfruit.sort()

#############################
'''                          MONKEY             '''
'''function that generates a string'''
'''function that will score each generated string by comparing 
            the randomly generated string to the goal.'''
'''function will repeatedly call generate and score, 
            then if 100% of the letters are correct we are done.'''

import random

def generate_one(strlen):
    alphabet = 'qazwsxedcrfvtgbyhnujmikolp '
    res = ''
    for i in range(strlen):
        res = res + alphabet[random.randrange(25)]
    return res

def score(goal, teststring):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            num_same += 1
    return num_same / len(goal)

# def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generate_one(26)
#    best = 0
    while score(goalstring,newstring) < 1:
        newstring = generate_one(26)
        print(newstring)

main()

for i in range(10):
    print(score('lollolol',generate_one(26)))
######################################################
def genstr(len_sgoal):
    alphabet = 'qazwsxedcrfvtgbyhnujmikolp '
    result = [alphabet[random.randrange(26)] for i in range(len_sgoal)]
    return result

def scoring(goal_string,generated_string):
    return goal_string == generated_string
    
# def main():
    sgoal = list('kuope') # input from user or type what you generate ar last
    # sgen = '' # ??
    counter = 0
    while scoring(sgoal,genstr(len(sgoal))) is False:
        counter += 1
    else:
        print('GOOD\n' + str(counter) + ' times passed')

    
    
# def
# len(genstr(6))
# sgoal = 26
# guest_arrivals = [alphabet[random.randrange(26)] for i in range(len_sgoal)]
# for k in range(20):
#     print(random.randrange(5))
k = 3
i = 0
while i < 10:
    print('1st branch')
    if k ==5:
        break
    else:
        print('2nd branch')
    print('3rd branch')
    i += 1
print('zebra')


print(
      (lambda x, y: (x + y)/2)
      (4, 3)
      )
#########
def hello():
  print("Hello World") 
  return("hello")

def hello_noreturn():
  print("Hello World")
  
# Multiply the output of `hello()` with 2 
hello() * 2

# (Try to) multiply the output of `hello_noreturn()` with 2 
hello_noreturn() * 2

# Define `plus()`
def plus(a,b):
  sum = a + b
  return (sum, a)

# Call `plus()` and unpack variables 
sum, a = plus(3,4)

# Print `sum()`
print(sum)
################
from functools import reduce
my_list = [1,2,3,4,5,6,7,8,9,10]

# Use lambda function with `filter()`
filtered_list = list(filter(
    lambda x: (x*2 > 10), 
    my_list))
# Use lambda function with `map()`
mapped_list = list(map(lambda x: x*2, my_list))
# Use lambda function with `reduce()`
reduced_list = reduce(lambda x, y: x+y, my_list)

print(filtered_list)
print(mapped_list)
print(reduced_list)

##############
'''Homework:
Task 1
A simple function.
Create a simple function called favorite_movie, which takes a string 
containing the name of your favorite movie. The function should then 
print “My favorite movie is named {name}”.

'''
def favorite_movie(movie):
    print("my favourite movi is named {name}".format(name = movie))
    
favorite_movie('pulp fiction')
###################
'''
Task 2
Creating a dictionary.
Create a function called make_country, which takes in a country’s name 
and capital as parameters. Then create a dictionary from those two, 
with ‘name’ as a key and ‘capital’ as a parameter. Make the function 
print out the values of the dictionary to make sure that it works as intended.'''

def make_country(country, capital):
    dicti = {country.capitalize(): capital.capitalize()}
    return dicti

make_country('japan', 'tokio')

##############
'''Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple 
arithmetic operator as a first parameter (to keep things simple let it 
only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) 
as the second parameter. Then return the sum or product of all the numbers 
in the arbitrary parameter. For example:


the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42  
'''

def make_operation(operation, *ar):
    operands = []
    print(ar)
    print(sum(ar))
    for o in ar:
        if type(o) is int:
            continue
        else:
            print('args is not good')
            break
    # start = operands[0]
    if operation == '+':
        result = sum(ar)
    elif operation == '-':
        result = sum([ar[0] if z == ar[0] else -z for z in ar])
    elif operation == '*':       
        result = ar[0]
        for z in ar[1:]:
            result *= z
    return result
make_operation('*', 3,4,5)

x = 5 
z = 10
result = lambda x,z: z - x
    # operands = [i for i in *ar is type(*ar)]
    # if type('+') is str:
    #     if [*operands] is int:
ar = [1,2,1,2,1,2] 

result = sum([ar[0] if z == ar[0] else -z for z in ar[1:]])
z = lambda x: (start - x)        
    result = 

if [my_list] is int:
    print('yy')
    
[my_list] is int

ar=['2','3']

sum(my_list)

operands = [i for i in ar if type(i)==int]
ar=[1,2,3,4,5,6]
sum(ar)

[ar[0] if z == ar[0] else -z for z in ar ]


[ [ 1 if item_idx == row_idx else 0 
   for item_idx in range(0, 3) ] 
 for row_idx in range(0, 3) ]



######################
'''Homework:                Task 1
Write a function called oops that explicitly raises an IndexError exception 
when called. Then write another function that calls oops inside a try/except 
state­ment to catch the error. What happens if you change oops to raise 
KeyError instead of IndexError?
'''
def oops():
        raise IndexError()

def oopsiki():
    try:
        oops()
    except KeyError:
        print('index')
    else:
        print('no index')
        
#############
'''Task 2
Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided 
by b, construct a try-except block which raises an exception if the two values 
given by the input function were not numbers, and if value b was zero 
(cannot divide by zero).   
'''

def fuqwe():
    try:
        a = int(40)
        b = int('d')
        # a = int(input('1st:'))
        # b = int(input('2nd:'))
        s = a ** 2 / b
        return s
    except ValueError:
        print('enter int values')
    except ZeroDivisionError:
        print('b valur is zero. we cant devide on it. try again') 
    # except:
    #     print('there are more errors')
    print('program ends')

g = fuqwe()

gg = ['no output' if g==None else g][0]
print('g is: ',gg)