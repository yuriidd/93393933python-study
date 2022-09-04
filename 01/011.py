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
