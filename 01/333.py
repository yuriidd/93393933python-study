# -*- coding: utf-8 -*-
"""Created on Sun Jul  3 15:12:18 2022 @author: xiaom"""

bool(1)
True


# a = 0
# while a < 10:
#     a = a + 1
#     if a > 5:
#         print (a,">",5)
#     elif a <= 7:
#         print (a,"<=",7)
#     else:
#         print ("Neither test was true")

guess = int(input('f'))



while True:
    inp = input('lolo?\n')
    if inp == 'x':
        break
    try:
        guess = int(inp)
    except ValueError:
        print('Your guess should be a number')
    else:
        gout = int(input('type 1 for out:\n'))
        if gout == 1: break 


# while True:
#     inp = input('lolo?\n')
#     if guess = int(inp) is True:
    
#         print('Your guess should be a number')
#     else:
#         gout = int(input('type 1 for out:\n'))
#         if gout == 1: break 

x = int(input('1st valeu plz:\n'))
y = int(input('1st valeu plz:\n'))
z = int(input('1st valeu plz:\n'))

xyz = z+y+z
print(xyz/3)
###################################

summ = 0.0
print ("This program will take several numbers, then average them.")
count = int(input("How many numbers would you like to sum:  "))
current_count = 0

while current_count < count:
    current_count += 1
    we = float(input('giiime the number:\n'))
    summ = summ + we
print('the summ is: {}'.format(summ/count))
###################################
# калькулятор среднего числа
# (1+2+3)/3 = 2 срерднее. 2*кол-во-цифр-до и получаю сумму всех чисел
#  (1+2+3+2)/4 = 2
# или (2_как_прошлое_значение-среднего * (4 - 1) + 2как-новая-цифра)/4 = 2

si_counter = 0
avg_summary = 0

while True:
    si_counter = si_counter + 1
    dai_number = int(input('dai dai number:\n'))
    avg_summary = (avg_summary * (si_counter - 1) + dai_number)/si_counter
    print('new value of overall avg is: {:.2f}'.format(avg_summary))

###################################"##
#" 1
"""Write a password guessing program to keep track of how many times 
the user has entered the password wrong. 
If it is more than 3 times:  print (You have been denied access)  
+ and terminate the program. 
If the password is correct: print (You have successfully logged in) + 
and terminate the program."""

user_password = '1234'
pass_counter = 0
while pass_counter<4:
    input_pass = input('enter your password: \n')
    if input_pass == user_password:
        print('You have successfully logged in!')
        break
    else:
        pass_counter += 1
        print ('You have been denied access')
        
########### ниже пример из книги
while True:
	pass_guess = input("Please enter your password: ")
	guess_count += 1
	if pass_guess == correct_pass:
		print ('You have successfully logged in.')
		break
	elif pass_guess != correct_pass:
		if guess_count >= 3:
			print ("You have been denied access.")
			break
        
###########################################  2
'''
Write a program that asks for two numbers. 
If the sum of the numbers is greater than 100: 
print (That is a big number and terminate the program).
'''

while True:
    qw = float(input('1st number: \n'))
    qwe = float(input('2nd number: \n'))
    if qw+qwe > 100:
        print('That is a big number')
        break


###########################################  3
'''
Write a program that asks the user their name. 
If they enter your name, say "That is a nice name." 

If they enter "John Cleese" or "Michael Palin", 
tell them how you feel about them ;), otherwise tell them 
"You have a nice name."
'''

namex = input('i ask your NAME: \n')
if namex == 'Yurii':
    print("That is a nice name.")
elif namex == 'John Cleese' or namex == 'Michael Palin':
    print('I feel good about you xD')
else:
    print('You have a nice name.')

###########################################  4
'''
Ask the user to enter the password. If the password is correct 
print "You have successfully logged in" and exit the program. 
If the password is wrong print "Sorry the password is wrong" 
and ask the user to enter the password 3 times. 
If the password is wrong print "You have been denied access" and 
exit the program.
'''

true_pass = '1234'
input_pass00 = input('enter your password: \n')
if input_pass00 == true_pass:
    print("You have successfully logged in")
else: 
    print("Sorry the password is wrong")
    while True:
        
        input_pass01 = input('enter your password: \n')
        input_pass02 = input('enter your password: \n')
        input_pass03 = input('enter your password: \n')
        if input_pass01 == input_pass02 == input_pass03 == true_pass:
            print("You have successfully logged in")
            break
        else:
            print("You have been denied access")
            break
        
########################################### cool
'''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'''
number = int(input("Enter a number to get its absolute value:"))
res = (-number, number)[number > 0]

number = int(input("Enter a number to get its absolute value:"))
res = (lambda: number, lambda: -number)[number < 0]()

number = int(input("Enter a number to get its absolute value:"))
res = number if number > 0 else -number

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)
########################################### 

# def numbp():
#     res = number
# def numbm():
#     res = -number
# number = int(input("Enter a number to get its absolute value:"))
# if number > 0:
#     numbp()
# else:
#     numbm()
# print(res)
#  ^^ no good ^^



opera = input('which method?: \n')
oper1 = int(input('what value?: \n'))
oper2 = int(input('2nd value?: \n'))
result = {
  'a': lambda: oper1 * oper2,
  'b': lambda: oper1 + oper2,
  'c': lambda: oper1 / oper2,
  'd': lambda: print('just chill')
}

result[opera]()

####################
'''Homework:
                            Task 1
String manipulation
Write a Python program to get a string made of 
the first 2 and the last 2 chars from a given string. 
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'
Expected Result : 'held'
Sample String: 'my'
Expected Result : 'mymy'
Sample String: ' x'
Expected Result: Empty String

Tips:
Use built-in function len() on an input string
Use positive indexing to get the first characters of a string 
and negative indexing to get the last characters'''

string = input('input any string:\n').strip()

if len(string) >= 2:
    print('result is:\n'+string[0:2]+string[-2:])
else:
    print('result is:\nEmpty String')
    
#############
'''
                                    Task 2
The valid phone number program.
Make a program that checks if a string is in the right format for 
a phone number. The program should check that the string contains only 
numerical characters and is only 10 characters long. Print a suitable message 
depending on the outcome of the string evaluation.
'''
pnumber = '0660900909'
pnumber = '1234567890'
pnumber = input('enter phone number, 10 chars long').replace(' ','')

if len(pnumber) == 10 and pnumber.isdigit() \
    and pnumber[:3] in ('093', '073', '066', '098', '050', '097', '067'):
    print('well done bro')
else:
    print('i sad 10 chars phone, canadian')
#ree = ' 3 4   4'.replace(' ','')

#############
'''
                    task 3
The name check.
Write a program that has a variable with your name stored (in lowercase) 
and then asks for your name as input. The program should check if your input 
is equal to the stored name even if the given name has another case, e.g., 
if your input is “Anton” and the stored name is “anton”, it should return True.
'''

my_name = 'yurii'
if in_name := input('enter your name:\n').lower() == my_name:
    print('True')
else:
    print("He-a")

#############

import sys
print(sys.path)

