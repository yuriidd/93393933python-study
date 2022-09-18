# -*- coding: utf-8 -*-
"""Created on Wed Jul  6 02:48:55 2022@author: xiaom"""

'''
Homework:
                        Task 1
The Guessing Game.
Write a program that generates a random number between 1 and 10 
and lets the user guess what number was generated. The result should be 
sent back to the user via a print statement.
'''
import random
secret = random.randrange(1,10)
feel = int(input('what\'s the secret? (int)\n'))
if secret == feel:
    print(f'you\'re luckie! {secret} is right')
else:
    print('nonono')
    
###################
'''                     Task 2
The birthday greeting program.
Write a program that takes your name as input, and then your age as input 
and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”   
'''
name = input('name?')
age = int(input('age?'))
print(f'Hello {name}, on yout next birthday you\'ll be {age+1} years')

###################
'''                     Task 3
Words combination
Create a program that reads an input string and then creates and prints 
5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 
5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> 
‘hlelo’, ‘olelh’, ‘loleh’ …
Tips: Use random module to get random char from string)
'''
# from random import shuffle
shake = list(input('>> what i should shake?\n'))
print('>> look at char\'s party:')
i = 1
while i < 6:
    i += 1
    random.shuffle(shake)
    # print('look at char\'s party:', shake[0]+shake[1]+shake[2]+shake[3]+shake[4])
    print(''.join(shake))
    # ''.join(map(str,shake))

# shuffle(shake)
# random.choice(shake)

###################
'''Task 4
The math quiz program
Write a program that asks the answer for a mathematical expression, checks 
whether the user is right or wrong, and then responds with 
a message accordingly.
'''

byge = int(input('ckoka 6yge 6yge 6yge?: (3+8)*3-4\n'))
if byge == 29:
    print('good')
else:
    print('bad')
    
    