# -*- coding: utf-8 -*-
"""Created on Tue Aug  2 07:50:33 2022@author: xiaom"""

# greatest common divisor ()
# наибольший общий делитель. нужен для упрощения дроби
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

#
class FractionClass:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        
    # represent 1
    def __str__(self):
        return '{:d}/{:d}'.format(self.num, self.den)
    # represent 2 method show()
    def show(self):
        return f'{self.num:d}/{self.den:d}'
    
    # methods numeric
    # addition
    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return FractionClass(new_num // common, new_den // common)    
    
    # multiplication
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return FractionClass(new_num // common, new_den // common)
    
    # subtraction
    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return FractionClass(new_num // common, new_den // common)
    
    # divition 
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = other.num * self.den
        common = gcd(new_num, new_den)
        return FractionClass(new_num // common, new_den // common)
    
    # equality
    def __eq__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 == num2
    
    # lower or equal
    def __le__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 <= num2
    
    # grater or equal
    def __ge__(self, other):
        num1 = self.num * other.den
        num2 = other.num * self.den
        return num1 >= num2
    
    
# self    other   
# 1-3      1-2
# 2-6      3-6


s = FractionClass(1,4)
w = FractionClass(2,8)
q = FractionClass(1,3)
e = FractionClass(1,2)

print(s+w)
print(e-q)
s.show()
print(w*q)

# a = 7
# b = 9
# f'{a:d}'    
# f'{a:d}/{b:d}'