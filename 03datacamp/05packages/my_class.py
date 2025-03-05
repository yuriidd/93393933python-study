#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Feb 24 12:21:52 2025 @author: yurii"""

# Define a minimal class with an attribute
class MyClass:
    """A minimal example class    
    
    :param value: value to set as the ``attribute`` attribute    
    :ivar attribute: contains the contents of ``value`` passed in init    
    """
    
    # Method to create a new instance of MyClass
    def __init__(self, value):
        # Define attribute with the contents of the value param        
        self.attribute = value


# ################################### 

from token_utils import tokenize
# -- or
#from .token_utils import tokenize  
# -- if you install packages to current directory


class Document:
    
    def __init__(self, text, token_regex=r'[a-zA-Z]+'):
        self.text = text        
        self.tokens = self._tokenize()
            
    def _tokenize(self):
        return tokenize(self.text)


# ################################### inheritance

from .parent_class import ParentClass

class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
        self.child_attribute = "I'm a child class attribute!"

child_class = ChildClass()
print(child_class.child_attribute)
print(child_class.parent_attribute)



# #####

class Parent:
    def __init__(self):
        print("I'm a parent!")
        
class SuperChild(Parent):
    def __init__(self):
        super().__init__()
        print("I'm a super child!")
        
class Grandchild(SuperChild):
    def __init__(self):
        super().__init__()
        print("I'm a grandchild!")
        
grandchild = Grandchild()
# >> I'm a parent!
# >> I'm a super child!
# >> I'm a grandchild!

sm = SocialMedia('@DataCamp #DataScience #Python #sklearn')

# What methods does sm have?   ̄\_(?)_/ ̄
dir(sm)

'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'_count_hashtags', '_count_mentions', '_count_words', '_tokenize', 
'hashtag_counts', 'mention_counts', 'text', 'tokens', 'word_counts']
'''

# ################################3
class Document2:
    """Analyze text data    
    
    :param text: text to analyze    
    
    :ivar text: text originally passed to the instance on creation    
    :ivar tokens: Parsed list of words from text    
    :ivar word_counts: Counter containing counts of hashtags used in text    
    """
    def __init__(self, text):        
        self.texio = text


























