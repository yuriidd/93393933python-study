# # -*- coding: utf-8 -*-
# """
# Created on Sun Jun 26 15:33:42 2022

# @author: YuriiZ
# """


address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
      {'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
      {'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')

s=str(address_book[0:1])

'xxxNAGIBATORxxx'.find('N')
y = 'xxxNAGIBATORxxx'
x = 'LL1ishkaBOY'
z = 'CreateWorld'
print(f'eto on >>{y:>20}<<')
print(f'eto on >>{x:>20}<<')
print(f'eto on >>{z:>20}<<')
'eto on >>{:^20}<< &&{:^20}&&'.format('CreateHold', 'jujuwu')


x[:10]

# % operator
text = ("%d little pigs come out, "
        "or I'll %s, "
        "and I'll %s, "
        "and I'll blow your %s down." 
        % (3, 'huff', 'puff', 'house'))


print("%d = %s = %s = %s" % (3, 'huff', 'puff', 'house'))

speed = 85
mood = 'oooooogggggggd1'

if speed >= 80:
    print('License and registration please')
    if mood == 'terrible' or speed >= 100:
      print('You have the right to remain silent.')
    elif mood == 'bad' or speed >= 90:
      print("I'm going to have to write you a ticket.")
      print('TAKE A TICKET')
    else:
          print("Let's try to keep it under 80 ok?")  
else:
      print("aaaaaaaaaaaaaa?")
      
      
if speed >= 80: print('You are so busted')
else: print('Have a nice day')

#######################################

'dayz' not in 'Have A Nice Day'

# xx2 = 'Have\tA\tNice\tDay'
xx2 = 4

print('\t', xx2, '\t', xx2)
'com.realpython.com'.str

print('\t'.join(['a','b','c']).expandtabs(10).strip('a'))
':'.join(list(x))

':'.join(list(x)) == ':'.join(x)

'com.realpython.com'.partition('.')
'aaa,bbb,ccc'.rsplit(',',1)
'a\ra'.splitlines(4)

rb'ffg\xddbar'[4]
aa2=b'ffgddbar'
type(aa2)

# str(0x00) == '\x00' #/????????

import math
math.ceil( 100.01)
round(100.000056, 3)

import random
random.choice(text)

random.randrange(1, 100,10)
list1 = [34,65,2,66,85,36,8,77]

print(random.shuffle(list1))
random.shuffle(list1)

''''ЗАДАНИЕ 1'''
#вариант 1
name1 = 'YuriiZ'
datet = '2nd of Jule'
print('Good day %s! %s is a perfect day to learn some python.' 
      % (name1, datet))

#вариант 2
# print('Good day %s! %s is a perfect day to learn some python.')
print(f'Good day {name1}! {datet} is a perfect day to learn some python.')

#вариант 2
textish2 = 'Good day {}! {} is a perfect day to learn some python.'
print(textish2.format(name1, datet))

#вариант 3
textish2 = 'Good day {1}! {0} is a perfect day to learn some python.'
print(textish2.format(datet, name1))

#вариант 4
textish4 = 'Good day {zname}! {zday} is a perfect day to learn some python.'
print(textish4.format(zday = datet, zname = x))


# ==========
data = ("John", "Doe", 53.44)
format_string = "Hello"
print('%s %s %s. Your current balance is $%.2f.' 
      % (format_string, data[0], data[1], data[2]))
# ==========

'''ЗАДАНИЕ 2'''
# len(x)
# x.rjust(len(x)+1)
xname = 'Yurii'
xlname = 'Z'
print('Hello', xname+xlname.rjust(len(xlname)+1), '\b! Nice to see you!')

''''ЗАДАНИЕ 3'''
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

j=-17
k=3

print('j = {} and k = {}'.format(j,k))
print('j + k =', j+k)
print('j - k =', j-k)
print('j / k =', j/k)
print('j * k =', j*k)
print('version 1: j ** k =', j**k)
print('version 2: j ** k =', pow(j,k))
print('modulus of j and k :', abs(j),'and',abs(k))
print('Floor division: j // k =', j//k)


lo = 'dffdgo'
lo.upper()
lo

