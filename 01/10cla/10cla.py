# -*- coding: utf-8 -*-
"""Created on Mon Aug  1 06:09:59 2022@author: xiaom"""

###############             CLASSES
####### gate logic program

class Car():
    
    total_number_cars = 0
    
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_km_driven = 0
        Car.total_number_cars += 1
        
    def repaint(self, color):
        self.color = color
        
    def kmdriven(self, km):
        self.total_km_driven += km
        
my_car= Car('uqw','shishiga', '1980', 'black')

print(my_car.model)
print(my_car.brand)
print(my_car.year)
print(my_car.color)
print(my_car.total_km_driven)
my_car.brand = 'Toyo'

my_car.kmdriven(400)
my_car.repaint('yellow')

print(Car.total_number_cars)

#########
class FClass:
    year = 0
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def do_it(self):
        self.a += 100
        self.b += 100
        print(f'New values: A >> {self.a}. B >> {self.b}')
        return self.a + self.b

aa = FClass()
ss = FClass()
id(aa) == id(ss)
aa.year
aa.year = 2
ss.year
FClass.year

bb = FClass(3,25)
cc = FClass

bb == cc
type(bb)
type(cc)

dd = cc()
dd == cc
dd == bb
type(dd)

print(bb.do_it())
ss = bb.do_it()
bb.a

spam = 1
def scope_test():
    def do_local():
        spam = 'local spam'
    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'
        def do_non2():
            nonlocal spam
            spam = 'nonlocal 2 spam'
        do_non2()
    def do_global():
        global spam
        spam = 'global spam'
    spam = 'scope spam'
    do_local()
    print('after local : ', spam)
    spam = 'scope spam'
    do_nonlocal()
    print('after do_nonlocal : ', spam)
    spam = 'scope spam'
    do_global()
    
    print('after global : ', spam)
    
scope_test()
print('after scope test : ', spam)

####################
'''             поиск наименьшего общего делителя'''
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

print(gcd(20, 10))

############################################################
'''     Task 1
A Person class
Make a class called Person. Make the __init__() method take firstname, 
lastname, and age as parameters and add them as attributes. Make another 
method called talk() which makes prints a greeting from the person 
containing, for example like this: “Hello, my name is Carl Johnson and 
I’m 26 years old”.

'''

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} '
              f'and I’m {self.age} years old.')

Caleb = Person('Caleb', 'Curry', 20)

Caleb.talk()

#########################################################
'''         Task 2
Doggy age
Create a class Dog with class attribute `age_factor` equals to 7. 
Make __init__() which takes values for a dog’s age. Then create a method 
`human_age` which returns the dog’s age in human equivalent.
'''

class Dog:
    age_factor = 7
    def __init__(self, dog_age):
        self.dog_age = dog_age
    def human_age(self):
        return Dog.age_factor * self.dog_age

tuzik = Dog(9)
tuzik.human_age()
#########################################################
'''             Task 3
TV controller
Create a simple prototype of a TV controller in Python. It’ll use 
the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel 
                    numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last 
                    one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel 
                    is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and 
                    returns "Yes", if the channel N or 'name' exists in 
                    the list, or "No" - in the other case.
 
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.

```
CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
pass
controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
'''

channel_list = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self,channels):
        self.channel_list = channels
        self.current = self.channel_list[0]
        
    # channels swapping
    def first_channel(self):  #done
        self.current = self.channel_list[0]
        print(self.current)
        
    def last_channel(self):  #done
        self.current = self.channel_list[-1:]
        print(self.current)
        
    def next_channel(self): #done
        try:
            self.current = \
                self.channel_list[self.channel_list.index(self.current) + 1]
        except IndexError:
            self.current = self.channel_list[0]
        print(self.current)    
    
    def previous_channel(self): #done
        try:
            self.current = \
                self.channel_list[self.channel_list.index(self.current) - 1]
        except IndexError:
            self.current = self.channel_list[-1:]
        print(self.current)    
        
    def current_channel(self): #done
        print(self.current) 
        return self.current
    
    def turn_channel(self, channel_number): #done
        if (channel_number - 1) in range(len(self.channel_list)):
            self.current = self.channel_list[channel_number - 1]
        print(self.current) 
    
    # 
    def is_exist(self, channel):    #done
        if type(channel) == int \
                and (channel - 1) in range(len(self.channel_list)):
            print('Yes')
        elif type(channel) == str and channel in self.channel_list:
            print('Yes')
        else:
            print('No')
    
controller = TVController(channel_list)

controller.first_channel() #is ok
controller.current 
controller.last_channel()  #is ok
controller.current 
controller.next_channel()
controller.current 
controller.previous_channel()
controller.current 
controller.current_channel()
controller.current 
controller.turn_channel(6)
controller.turn_channel(2)
controller.turn_channel(0)
controller.current 
controller.is_exist(3)
controller.is_exist(0)
controller.is_exist('BBC')
controller.is_exist('BBC222')
controller.current 

controller.current 

'BBC' in channel_list

channel = 5
type(channel) == int

range(len(channel_list) - 1)
channel_list = ["BBC", "Discovery", "TV1000"]
a = channel_list[-1]
a = channel_list[len(channel_list) - channel_list.index(a) + 1]
len(channel_list)

bool(channel_list.index('BBC'))
channel_list.index('TV1000') in range(len(channel_list))


try:
    a = channel_list[channel_list.index(a) + 1]
except IndexError:
    a = channel_list[0]

e = 3
(e - 1) in range(len(channel_list))

g = [a for a in range(3)]
g
'''
0 1 2

    2 + 1 = 3

3 - 2 + 1


'''
#############################################################
''' Logic Gates for current circuit
Logic Gates --- Unary Gate  --- NOT
Logic Gates --- Binary Gate --- AND
Logic Gates --- Binary Gate --- OR

'''


class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None
        
    def get_label(self):
        return self.label     
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self,lbl):
        super(BinaryGate, self).__init__(lbl)
        self.pin_a = None
        self.pin_b = None
        
    def get_pin_a(self):
        if self.pin_a == None:
            return int(input('enter PIN A for gate '
                         f'"{self.get_label()}": '))
        else:
            return self.pin_a.get_from().get_output()
        
    def get_pin_b(self):
        if self.pin_b == None:
            return int(input('enter PIN B for gate '
                         f'"{self.get_label()}": '))
        else:
            return self.pin_b.get_from().get_output()
    
    def set_next_pin(self, connector):
        if self.pin_a == None:
            self.pin_a = connector
        elif self.pin_b == None:
            self.pin_b = connector
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
                         
class UnaryGate(LogicGate):
    def __init__(self,lbl):
        LogicGate.__init__(self,lbl)
        self.pin = None

    def get_pin(self):
        if self.pin == None:
            return int(input('enter PIN for gate '
                         f'"{self.get_label()}": '))     
        else:
            return self.pin.get_from().get_output()
        
    def set_next_pin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

'''
LogicGate.__init__(self, lbl)
    super().__init__(lbl)
    super(UnaryGate, self).__init__(lbl)
    super().__init__("UnaryGate", lbl)
'''

class AndGate(BinaryGate):
    def __init__(self,lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NandGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 0
        else:
            return 1        

class NorGate(BinaryGate):
    def __init__(self,lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,lbl):
        super().__init__(lbl)
        
    def perform_gate_logic(self):
        a = self.get_pin()
        if a == 1:
            return 0
        else:
            return 1

class Connector():
    def __init__(self, from_gate, to_gate): #con1 = Connector(and1, not2)
        self.source_gate = from_gate
        self.target_gate = to_gate
        to_gate.set_next_pin(self) # (con1 as parametr)
    def get_from(self):
        return self.source_gate
    def get_to(self):
        return self.target_gate
# NorGate
# Nand Gate

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.get_output())


not1 = NotGate("not1")
not2 = NotGate("not2")
con1 = Connector(not1,not2)
print(not2.get_output())

and1 = AndGate("and1") # 0-1  in     0 out
not3 = NotGate("not3") # 0 in        1out
con1 = Connector(and1,not3)
print(not3.get_output()) 

or1 = OrGate("or1")

and1 = AndGate("and1") 
or1 = OrGate("or1")
con1 = Connector(and1,or1)
print(or1.get_output()) 

and1 = AndGate("and1") 
and2 = AndGate("and2") 
and3 = AndGate("and3") 
con1 = Connector(and1,and3)
con2 = Connector(and2,and3)
print(and3.get_output()) 

'''
#NOT (( A and B) or (C and D)) is that same as 
#NOT( A and B ) and NOT (C and D). 

A 0
B 0
C 1
D 1
'''
and1 = AndGate("and1") #0 exit
and2 = AndGate("and2")  #1 exit
or1 = OrGate("or1") #1 exit
con1 = Connector(and1,or1)
con2 = Connector(and2,or1)
not1 = NotGate("not1") #0 exit
con2 = Connector(or1,not1)
print(not1.get_output())   #0 exit


and1 = AndGate("and1") #0 exit
and2 = AndGate("and2")  #1 exit
nor1 = NorGate("nor1") #0 exit
con1 = Connector(and1,nor1)
con2 = Connector(and2,nor1)
print(nor1.get_output()) 