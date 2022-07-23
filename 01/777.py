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

def main():
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
    
def main():
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