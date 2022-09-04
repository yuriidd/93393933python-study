# -*- coding: utf-8 -*-
"""Created on Sun Aug 14 17:57:25 2022  @author: yuriizd"""

# print('after scope test : ')

# from abc import ABC, abstractmethod

class PayrollSystem:
    
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'--- Check amount: {employee.calculate_payroll()}')
            print('')

class Employee():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.xx = 100
    # @abstractmethod
    # def calculate_payroll(self):
    #     pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary
        
    def calculate_payroll(self):
        return self.weekly_salary
    
class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked
        
    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission
        
    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
    
# salary_employee1 = SalaryEmployee(1, 'Simona', 1500)
# salary_employee2 = SalaryEmployee(2, 'Jane Brown', 1700)
# hourly_employee1 = HourlyEmployee(3, 'Skotch Zee', 18, 38)
# commission_employee1 = CommissionEmployee(4, 'Kek Cheburek', 1300, 120)

# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee1, 
#     salary_employee2,
#     hourly_employee1,
#     commission_employee1 ])


#######################
# расширение работников для интерфейса ProductivitySystem ""

class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')

class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')

class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')

class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')

# интерфейc ProductivitySystem
class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            employee.work(hours)
        print('')


# правильно будет разбить, конечно, так - 
# import hr
# import employees
# import productivity
# а добавление уже сотрудников и расчет выполнять в текущем файле


manager = Manager(1, 'Mary Poppins', 3000)
secretary = Secretary(2, 'John Smith', 1500)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(4, 'Jane Doe', 40, 15)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker ]

productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)

# класс объявлен но работает не так как нужно, т.к. в наследовании есть
# параметры, которые не передаются при создании объекта
class TemporarySecretary(HourlyEmployee, Secretary):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name, hours_worked, hour_rate)

# смотрим порядок наследования
TemporarySecretary.__mro__

class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hour_rate, hours_worked):
        HourlyEmployee.__init__(self, id, name, hour_rate, hours_worked)
        
    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)

temporary_secretary1 = TemporarySecretary(5, 'Ann Smith', 9, 40)

employees = [temporary_secretary1]

productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)





#######################
#######################
#######################
#######################
#######################


# In productivity.py

class ProductivitySystem:
    def track(self, employees, hours):
        print('Tracking Employee Productivity')
        print('==============================')
        for employee in employees:
            result = employee.work(hours)
            print(f'{employee.name}: {result}')
        print('')

class ManagerRole:
    def work(self, hours):
        return f'screams and yells for {hours} hours.'

class SecretaryRole:
    def work(self, hours):
        return f'expends {hours} hours doing office paperwork.'

class SalesRole:
    def work(self, hours):
        return f'expends {hours} hours on the phone.'

class FactoryRole:
    def work(self, hours):
        return f'manufactures gadgets for {hours} hours.'


# In hr.py

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')

class SalaryPolicy:
    def __init__(self, weekly_salary):
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class HourlyPolicy:
    def __init__(self, hours_worked, hour_rate):
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate

class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission):
        super().__init__(weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission

# In employees.py

from hr import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from productivity import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_salary):
        SalaryPolicy.__init__(self, weekly_salary)
        super().__init__(id, name)

class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_salary, commission):
        CommissionPolicy.__init__(self, weekly_salary, commission)
        super().__init__(id, name)

class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)

# получается что все сделали реорганизацию классов
# в один модуль вошло: ProductivitySystem и роли для продуктивности
# в другой: PayrollSystem и варианты оплаты сотрудников
# в третий: Employee и классы сотрудников, в которые наследуются сотрудники, 
# роль оплаты и вариант оплаты. этим мы избегаем проблему диаманта 


# HAS-A relation
class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)










































