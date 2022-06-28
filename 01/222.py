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


y = 'xxxNAGIBATORxxx'
x = 'LL1ishkaBOY'
z = 'CreateWorld'

print(f'eto on >>{y:>20}<<')
print(f'eto on >>{x:>20}<<')
print(f'eto on >>{z:>20}<<')


'eto on >>{:^20}<< &&{:^20}&&'.format('CreateHold','jujuwu')


# % operator
text = ("%d little pigs come out, "
        "or I'll %s, "
        "and I'll %s, "
        "and I'll blow your %s down." 
        % (3, 'huff', 'puff', 'house'))


print("%d = %s = %s = %s" % (3, 'huff', 'puff', 'house'))

speed = 85
mood = 'good'

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