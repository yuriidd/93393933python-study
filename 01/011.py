# -*- coding: utf-8 -*-
"""Created on Tue Aug 30 17:24:32 2022@author: xiaom"""

'''Task 1
School
Make a class structure in python representing people at school. 

Make a base class called Person, a class called Student, 
and another one called Teacher. 

Try to find as many methods and attributes 
as you can which belong to different classes, and keep in mind 
which are common and which are not. For example, the name should be a Person 
attribute, while salary should only be available to the teacher. 
'''

Person_unit
id
fname
lname
phone_number
gov_id {passport
        driver_license}

.set_phone
.set_gov_id
.get_info
.get_info_all
#done

Student_unit
super person
group
lessons (10 subjects)
.set_lessons

.lessons_selection min 5 of 10
.get_lessons_selected
.get_group
#done

Teacher_unit
super person
subject
degree
salary


.set_salary
.get_salary

.set_profile
.get_profile


math
english
spanish
welding
python
swimming
architecture
history
physics
chemistry



import random

def id_random:
    
    return

# gov_id {passport
#         driver_license}
# .set_phone
# .set_gov_id
# .get_info
# .get_info_all
class Person_unit():
    def __init__(self, person_id, first_name, last_name, phone_number=''):
        self.id = person_id
        self.fname = first_name
        self.lname = last_name
        self.phone_number = phone_number
        self.gov_id = {'passport': '', 'driver_license': ''}
    
    def set_phone(self, phone_number):
        self.phone_number = phone_number

    def set_gov_id(self):
        a = input('Passport, please. If there is no - press Enter:')
        self.gov_id['passport'] = a
        a = input('Driver license number, please. If there is no - press Enter:')
        self.gov_id['driver_license'] = a

    def get_info_all(self):
        a = f'ID          | {self.id:<20}|\n' +\
            f'Name        | {self.fname:20}|\n' +\
            f'Last name   | {self.lname:20}|\n' +\
            f'Phone       | {self.phone_number:20}|\n' +\
            f'Passport    | {self.gov_id["passport"]:20}|\n' +\
            f'Driver lic. | {self.gov_id["driver_license"]:20}|'
        return print(a)
    
# ff = 'Ponny'
# gg = 'Erdoha'
# a = f'Name:\n{gg + " " + ff:40}'
# b = 40*'l'
# print(a)
# print(b)
# '''
weron = Person_unit(111, 'Mike', 'Razor', '0734040444')
weron.set_phone('0990330221')
weron.get_info_all()
print(weron.gov_id["passport"])
print(weron.phone_number)
print(None)
print(weron.gov_id)
weron.set_gov_id()

sheron = Person_unit(111, 'Mike', 'Razor')
sheron.get_info()
# '''

# Student_unit
# super person
# group
# lessons (10 subjects)
# .set_lessons

# .lessons_selection min 5 of 10
# .get_lessons_selected

# .get_group = get info all

class Student_unit(Person_unit):
    def __init__(self, person_id, first_name, last_name, group, 
                 phone_number=''):
        super().__init__(person_id, first_name, last_name, phone_number)
        self.group = group
        self.lessons = {'math': '',
                        'english': '',
                        'spanish': '',
                        'welding': '',
                        'python': '',
                        'swimming': '',
                        'architecture': '',
                        'history': '',
                        'physics': '',
                        'chemistry': ''}

    def set_lessons(self):
        print('Type "1" for selecting subject for study or leave empty either:')
        for key in self.lessons.keys():
            self.lessons[key] = input(f'Subject {key}: ')
            
    def get_lessons_selected(self):
        a = 0
        b = ''
        for key in self.lessons.keys():
            if len(self.lessons[key]) > 0:
                a += 1
                b = b + key + ' : ' + self.lessons[key] + '\n'
        if a < 5:
            return print('Not enough lessons selected, '
                         'try set_lessons() function one more time!')
        return print(b)

    def get_info_all(self):
        a = f'ID          | {self.id:<20}|\n' +\
            f'Name        | {self.fname:20}|\n' +\
            f'Last name   | {self.lname:20}|\n' +\
            f'Phone       | {self.phone_number:20}|\n' +\
            f'Passport    | {self.gov_id["passport"]:20}|\n' +\
            f'Driver lic. | {self.gov_id["driver_license"]:20}|\n' +\
            f'Group       | {self.group:20}|'
        return print(a)
    
    def info():
        print("person_id, first_name, last_name, group, phone_number=''")
          
jeron = Student_unit(222, 'Emma', 'Sui', 'EII1501', '0994003005')
jeron = Student_unit(222, 'Emma', 'Sui', 'EII1501')

wepoi = Person_unit(33, 'A', 'AA', '555-55-10')
wepoi_stu =   Student_unit(44, 'B', 'BB', 'BBBBB', '555-55-20')  
wepqw_stu =   Student_unit(77, 'C', 'CC', 'CCCC') 

jeron.get_info_all()
jeron.set_lessons()
jeron.get_lessons_selected()
jeron.set_gov_id()

# zz = {'math': '',
# 'english':'2',
# 'spanish':'2',
# 'welding':'2',
# 'python':'',
# 'swimming':'',
# 'architecture':'',
# 'history':'',
# 'physics':'',
# 'chemistry':''}
# b = '1'
# len(b)
# print(zz)
# for z in zz.keys():
#     print(type(z))
#     print(len(zz[z]))
#     if len(zz[z])>0:
#         print(z +':'+zz[z])
# a = 0
# b = '' 
# for z in zz.keys():
#     if len(zz[z]) > 0:
#         a += 1
#         b = b + z + ' : ' + zz[z] + '\n'
# print(a)
# print(b)
#======================== TEST

# class Person_unit():
#     def __init__(self, person_id, first_name, last_name, phone_number=''):
#         self.id = person_id
#         self.fname = first_name
#         self.lname = last_name
#         self.phone_number = phone_number

# class Student_unit(Person_unit):    # i made error at this place
#     def __init__(self, person_id, first_name, last_name, group, 
#                  phone_number=''):
#         super().__init__(person_id, first_name, last_name, phone_number)
#         self.group = group
        
# wepoi = Person_unit(33, 'A', 'AA', '555-55-10')
# wepoi_stu =   Student_unit(44, 'B', 'BB', 'BBBBB', '555-55-20')  
# wepqw_stu =   Student_unit(77, 'C', 'CC', 'CCCC') 

# class Employee():
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary

# emp1 = Employee(222, 'eff')
# emp4 = Employee(222, 'eff', 1500)

#======================== TEST

Teacher_unit
super person
subject
degree
salary

.set_profile
.get_profile

class Teacher_unit(Person_unit):
    def __init__(self, person_id, first_name, last_name, subject, 
                 salary='', degree='', phone_number=''):
        super().__init__(person_id, first_name, last_name, phone_number)
        self.subject = subject
        self.salary = salary
        self.degree = ''
    
    def get_info_all(self):
        a = f'ID          | {self.id:<20}|\n' +\
            f'Name        | {self.fname:20}|\n' +\
            f'Last name   | {self.lname:20}|\n' +\
            f'Phone       | {self.phone_number:20}|\n' +\
            f'Passport    | {self.gov_id["passport"]:20}|\n' +\
            f'Driver lic. | {self.gov_id["driver_license"]:20}|\n' +\
            f'Subject     | {self.subject:20}|\n' +\
            f'Degree      | {self.degree:20}|\n' +\
            f'Salary      | $ {self.salary:<18}|'
        return print(a)
    
    def set_profile(self):
        a = input('Enter subject for that teacher, please: ')
        self.subject = a
        a = input("Enter teacher's degree, please: ")
        self.degree = a
        a = input('Enter the salary value: ')
        self.salary = a        
    
    def info():
        print("person_id, first_name, last_name, subject, "
              "salary='', degree='', phone_number='')")
        
julia = Teacher_unit(555, 'Julia', 'Ognenka', 'math', 1500)
julia.get_info_all()
Teacher_unit.info()
julia.set_profile()
julia.set_phone('555-55-55-33')

###################################################
###################################################

'''
Task 2

Mathematician

Implement a class Mathematician which is a helper class for doing math 
operations on lists

The class doesn't take any attributes and only has methods:

square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without 
                  positive numbers
filter_leaps (takes a list of dates (integers) and removes those 
              that are not 'leap years'
```

class Mathematician:
    pass

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
'''

class Mathematician:
    def __init__(self):
        pass
    
    def square_nums(self,listt):
        # i = []
        # for k in listt:
        #     i.append(k**2)
        # return list(i)
        result = [k**2 for k in listt]
        return list(result)
    
    def remove_positives(self,listt):
        # i = []
        # for k in listt:
        #     if k < 0:
        #         i.append(k)
        # return list(i)
        result = [k for k in listt if k < 0]
        # result = list(filter(lambda k: k < 0,listt))
        # типа пример замены через лямбду
        return list(result)   

    def filter_leaps(self,listt):
        # i = []
        # for k in listt:
        #     if k % 2 == 0:
        #         i.append(k)
        # return list(i)                
        result = [k for k in listt if k % 2 == 0]
        return list(result) 

m = Mathematician()
m.square_nums([7, 11, 5, 4])
m.remove_positives([-4,5,10,-10])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])

#result = sum([ar[0] if z == ar[0] else -z for z in ar])



###################################################
###################################################

'''
Task 3

Product Store

Write a class Product that has three attributes:
type
name
price

Then create a class ProductStore, which will have some Products and 
will operate with all products in the store. All methods, in case they 
can’t perform its action, should raise ValueError with appropriate error 
information.

Tips: Use aggregation/composition concepts while implementing 
the ProductStore class. You can also implement additional classes to operate 
on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with 
        a predefined price premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount 
        for all products specified by input identifiers (type or name). 
        The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products 
        from the store if available, in other case raises an error. It also 
        increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in 
        the store.
get_product_info(product_name) - returns a tuple with product name and amount 
        of items in the store.
```

class Product:
    pass

class ProductStore:
pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
'''

class Product:
    def __init__(self, type, name, price):
        self.type  = type
        self.name  = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.shop = []
        self.income = 0
        
    def add(self, product, amount):
        self.shop.append([product, amount, round(product.price*1.3,2), 0])
        
    def sell(self, product_name, amount):
        for product in self.shop:
            if product[0].name == product_name: #ищем продукт в магазине
                if product[1] > amount: #достаточное ли количество?
                    product[1] -= amount #списываем из магазина
                    # total = price * (1 - discount) * amount
                    total = product[2] * (100 - product[3]) * 0.01 * amount
                    self.income += round(total,2)
                else: print(f'Product Store has not enough product you want. \
                            Available only {product[1]} units of goods.')

    def get_income(self):
        return self.income
    
    def set_discount(self, type, percent, name=''):
        if name != '': #если есть имя - ищем по имени товара
            for product in self.shop:
                if product[0].name == product_name:
                    product[3] = percent
        else: #иначе перебор по типу товара
            for product in self.shop:
                if product[0].type == type:
                    product[3] = percent
    
    def get_all_products(self):
        for product in self.shop:
                a = f'Type          | {product[0].type:<20}|\n' +\
                    f'Name          | {product[0].name:<20}|\n' +\
                    f'Price         | {product[2]:<20}|\n' +\
                    f'Discount      | {product[3]:<20}|\n' +\
                    f'Available     | {product[1]:<16}qt. |\n'
                print(a)
        
    def get_product_info(self, product_name):
        for product in self.shop:
            if product[0].name == product_name:
                a = f'Type          | {product[0].type:<20}|\n' +\
                    f'Name          | {product[0].name:<20}|\n' +\
                    f'Price         | {product[2]:<20}|\n' +\
                    f'Discount      | {product[3]:<20}|\n' +\
                    f'Available     | {product[1]:<16}qt. |\n'
                print(a)
                
    def get_product_info2(self, product_name):
        for product in self.shop:
            if product[0].name == product_name:    
                return (product[0].name, product[1])
                
tra = [[1,4],2,3,4,5]
tra.index([1,4])
# identifier      
# identifier_type=’name’
       
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
o = Product('Medicines', 'ABC minerals', 500)

shop1 = ProductStore()
shop1.add(p, 10)
shop1.add(p2, 300)
shop1.add(o, 50)

shop1.sell('Ramen', 500)
shop1.sell('Football T-Shirt', 1)
shop1.get_product_info('Football T-Shirt')
shop1.get_product_info2('Football T-Shirt')
shop1.get_all_products()
shop1.set_discount('Sport',5)
        # a = f'ID          | {self.id:<20}|\n' +\
        #     f'Name        | {self.fname:20}|\n' +\
        #     f'Last name   | {self.lname:20}|\n' +\
        #     f'Phone       | {self.phone_number:20}|\n' +\
        #     f'Passport    | {self.gov_id["passport"]:20}|\n' +\
        #     f'Driver lic. | {self.gov_id["driver_license"]:20}|\n' +\
        #     f'Subject     | {self.subject:20}|\n' +\
        #     f'Degree      | {self.degree:20}|\n' +\
        #     f'Salary      | $ {self.salary:<18}|'





###################################################
###################################################

'''
Task 4
Custom exception

Create your custom exception named `CustomException`, 
you can inherit from base Exception class, but extend its functionality 
to log every error message to a file named `logs.txt`. 
Tips: Use __init__ method to extend functionality 
for saving messages to file

```
class CustomException(Exception):
def __init__(self, msg):

'''

msg = 'How much of the fish?'

class CustomException(Exception):
    def __init__(self, msg='errororororororo!!!!!!!'):
        self.msg = msg
        gg = open('D:/py/93393933python-study/01/9/CustomException_log.txt','a')
        gg.write("LOGGINing':'that has been hapened!!\n")
        gg.close()
        super().__init__(self.msg)
        
raise CustomException(msg)  
        