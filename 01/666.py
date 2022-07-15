# -*- coding: utf-8 -*-
"""Created on Wed Jul 13 16:47:34 2022@author: xiaom"""

counter = 1
done = False
while counter <= 10 and not done:
    print('ok')
    done = True
    counter +=1
#######
word_list = ['korok','bird','MooreMoore']
let_list = []
for word in word_list:
    let_set = set()
    for let in word:
        let_set.update(let)
    
    let_list.append(let_set)

print(let_list)
set(let_list[0]) & set(let_list[2])
let_list[0] & let_list[2] & let_list[1]
###############

let_set.append(let)
let = 2
let_set.update(let)
type(let_set)
#########
[x*x for x in range(1,4)]
xxx = []
xxx= [x for x in 'hupilaret' if x not in 'yua']

print('idddifffrrri'.strip('i'))
##########
words = ['cat', 'window', 'defenestrate', 'spacetraveler']
for w in words[:]:
    print(w)
    words.insert(0, w)
    
words
words[:]
#########
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for x in my_range(1, 10, 0.5):
    print(x)
################

cell = []
for i in [2,1,2,3,4]:
    for k in [3,4,2,1]:
        if i != k:
            cell.append((i,k))
zell = [1,2,3,4,5,6,7,8,9,0]

cell = [(i,k) for i in [2,1,2,3,4] for k in [3,4,2,1] if i!=k ]
cell = [(i,k) for i in [2,1,2,3,4] for k in [3,4,2,1] ]
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
zell = [weapon.strip() for weapon in freshfruit]

for fruit in freshfruit: zell.append(fruit.strip())

matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
list(zip(*matrix))
zip(*matrix)
zell = list(zip([2,1,2,3,4],[3,4,2,1,8]))
zell

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)

##############
item_idx
1,0,0 < row_idx
0,1,0 
0,0,1

[ [ 1 if item_idx == row_idx else 0 
   for item_idx in range(0, 3) ] 
 for row_idx in range(0, 3) ]

[ 1 
   if item_idx == row_idx else 0 
   for item_idx in range(0, 3) ] 

[item_idx for item_idx in range(0, 3) ]
[0[0,1,2],1[0,1,2],2[0,1,2]]
aell=[]
# colell=[]
for row_index in range(0,3):
    colell=[]
    for col_index in range(0,3):
        if col_index == row_index:
            colell.append(1)
        else:
            colell.append(0)
    aell.append(colell)
    
print(aell)

[[x for x in range(0,3)] for y in range(0,3)]
# оно там сверху все вверх дном))
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
{ name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }
###
zell = [1,2,3,4,5,6,7,8,9,0]

{name.capitalize() for name in names 
 if len(name)>1 
 if name[0].upper()!='A'}

###########
'''Homework:                Task 1
Make a program that has some sentence (a string) on input and 
returns a dict containing all unique words as keys and the number 
of occurrences as values. '''
#           вариант 1
sentence = 'Make a program that has some sentence a a that'
sent_dict = {}
for key in set(sentence.lower().split()):
    value = 0
    for word in sentence.lower().split():
        if key == word:
            value +=1
    sent_dict[key]=value
print(sent_dict)

sentence.split()[0]
for key in sentence.split():
    print(key)
#           вариант2  
sent_dict['make']=sent_dict['make'] + 1

sentence = 'Make a program that has some sentence a a that that'
sent_dict = {}
for key in set(sentence.lower().split()):
    sent_dict[key]=0
    for word in sentence.lower().split():
        if key == word:
            sent_dict[key] += 1
print(sent_dict)

####
'''                 Task 2
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure 
mentioned above, then computes and returns the total price of stock.'''

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#           вариант1 
total = {}
for key in stock.keys():
    total[key]=stock[key]*prices[key]
print(total)
#           вариант2 
total = {key:stock[key]*prices[key] for key in stock.keys()}
print(total)

#           вариант3 
def totale(xx,yy):
    total1 = {key:xx[key]*yy[key] for key in xx.keys()}
    return total1
print(totale(prices,stock))

###########
'''             Task 3
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) 
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.'''

comp_list = [(i,i**2) for i in range(1,11)]
print(comp_list)
###########