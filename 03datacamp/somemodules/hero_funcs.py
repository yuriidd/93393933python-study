#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:54:31 2025

@author: yurii
"""

def convert_units(heroes, heights, weights):
    new_hts = [ht * 0.39370  for ht in heights]
    new_wts = [wt * 2.20462  for wt in weights]
    hero_data = {}
    for i, hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data

def convert_units_broadcast(heroes, heights, weights):
    new_hts = heights * 0.39370 # Array broadcasting instead of list comprehension
    new_wts = weights * 2.20462
    hero_data = {}
    for i,hero in enumerate(heroes):
        hero_data[hero] = (new_hts[i], new_wts[i])
    return hero_data
