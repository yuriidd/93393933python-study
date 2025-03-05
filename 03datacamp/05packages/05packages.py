#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Feb 24 11:04:56 2025 @author: yurii"""

# Project folder

'''
05packages
├── 05packages.py
├── my_class.py
├── my_package
│   ├── __init__.py
│   └── utils.py
└── requirements.txt
'''

#~& pip install -r requirements.txt 

# %%#################################             
# ###################################               
# ###################################

# Import utils submodule from ./my_package/utils.py
import my_package.utils
my_package.utils.we_need_to_talk(break_up=True)  # Decide to start seeing other people


# ###################################
# Import custom package
import my_package     # imports from __init__.py
my_package.we_need_to_talk(break_up=False)  # Realize you're with your soulmate



# from ./my_package/setup.py

from setuptools import setup
setup(name='my_package',
      version='0.0.1',
      description='An example package for DataCamp.',
      author='Adam Spannbauer',
      author_email='spannbaueradam@gmail.com',
      packages=['my_package'],
      install_requires=['matplotlib',
                        'numpy==1.15.4',
                        'pycodestyle>=2.4.0'])



# ###################################
# import Class
import my_package

# Create instance of MyClass
my_instance = my_package.MyClass(value='class attribute value')

# Print out class attribute value
print(my_instance.attribute)


# ################################### inheritance

from .parent_class import ParentClass

class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        self.child_attribute = "I'm a child class attribute!"

child_class = ChildClass()
print(child_class.child_attribute)
print(child_class.parent_attribute)







