#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Tue Mar  4 17:56:32 202@author: yurii"""

# #################################
# #################################             LOAD data
# #################################
# 

def extract(file_name):
    try:
        assert type(file_name) == str
        dataframe = pd.read_csv('data/' + file_name)
        print(f'INFO: CSV file "{file_name}" loaded.')s
        return dataframe
    except ValueError:
        print(f'"{file_name}" is not a string.')
        
workout = extract('workout.csv')
three_keywords = extract('three_keywords.csv')
workout_geo = extract('workout_geo.csv')
three_keywords_geo = extract('three_keywords_geo.csv')

# add os.path.exists if needed
# assert isinstance('sourdough', str)







