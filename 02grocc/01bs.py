#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:47:58 2025

@author: yurii
"""

'''          groccing - 01 binary search
'''

any_list = [1,2,3,4,5,6,7,8,9]

# m=len(any_list)/2

# any_list[len(any_list)/2]


# %% 
# ################# ch1                     binary_search

any_list = [1,2,3,4,5,6,7,8,9]

def binary_search(list, item):

    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        
        if item == guess:
            return mid
        
        if item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None
        
print(binary_search(any_list, 3))


# %%
# ################# ch2                    selection_sort

some_arr = [5,7,9,2,4,77,11,6,3,15]

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
print(find_smallest(some_arr))

#

def selection_sort(arr):
    new_arr = []
    
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr

print(selection_sort(some_arr))


# %%
# ################# ch3                 recursion

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    
    while pile is not emplty:
        box = pile.grab_a_box()
        
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key!")


def look_for_key_recursion(box):
    
    for item in box:
        if item.is_a_box():
            look_for_key_recursion(item)
        elif item.is_a_key():
            print("found the key!")


def countdown(i):
    print(i)
    
    if i <= 0:
        return
    else:
        countdown(i - 1)

countdown(6)


# ################# ch3                 stek


def greet(name):
    print('Hello, ' + name + '!')
    greet2(name)
    print('Getting ready to say bye...')
    bye()
    
def greet2(name):
    print('How are you, ' + name + '?')
def bye():
    print('OK bye!')

some_name = 'Yurii'    
greet(some_name)


# ################# ch3                 factorial

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


# %%
# ################# ch4                 task 4.1


def sum_arr(arr):
    total = 0
    for x in arr:
        total += x
    return total

# # bad choice
# def sum_arr_rec(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr.pop(0) + sum_arr_rec(arr)

def sum_arr_rec(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum_arr_rec(arr[1:])

# testlist = [1,2,3,4,5,6,7,8,9]
# sum_arr_rec(testlist)


# ################# ch4                  task 4.2

def sum_arrlen_rec(arr):
    if arr == []:
        return 0
    else:
        return 1 + sum_arrlen_rec(arr[1:])

sum_arrlen_rec(testlist)
len(testlist)


# ################# ch4                  task 4.3

def maxval_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_maxval = maxval_arr(arr[1:])
    return arr[0] if arr[0] > sub_maxval else sub_maxval
    # but there is an issue: you should calculate lists with at least 2 numbers


# ################# ch4                  task 4.4

'''
What is the base and recursion cases for binary search?
Base case is a massive with 1 element, and our search condition is equal
to this element.
Recursion case is to drop half massive and repeat.
'''


# ################# ch4                 quick_sorting


def quick_sorting(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less    = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sorting(less) + [pivot] + quick_sorting(greater)

print(quick_sorting([10,5,3,14,8]))


# %%
# ################# ch5             hash_tables

w1 = {}
w1["a1"] = True
w1['b1'] = True 

voted = {}
def check_voter(name):
    if voted.get(name):
        print('Kick them out!')
    else:
        voted[name] = True
        print('Let them vote!')

#
cache = {}
def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data


# %%
# ################# ch5             BFS, breadth-first_search


# non-directional graph
graph = {}
graph['you'] = ['alice', 'olga', 'alexey', 'ivan', 'karina', 'denis']

graph['alice'] = []
graph['alexey'] = ['kostya', 'emmy']
graph['olga'] = ['elena', 'irina']
graph['ivan'] = ['sergey', 'anatolii-electric']
graph['karina'] = []
graph['denis'] = ['anatolii-electric']

graph['kostya'] = []
graph['emmy'] = []

graph['elena'] = []
graph['irina'] = []

graph['sergey'] = []
graph['anatolii-electric'] = []

#

from collections import deque


def search(name):
    search_queue = deque()
    search_queue += graph[name] 
    searched = []
    
    while search_queue:
        person = search_queue.popleft()
        
        if not person in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True 
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search('you')


# %%
# ################# ch7             deixtra algorithm

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

#
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2 
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

#
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

#
def find_lowest_cost_node(node):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# %%
# ################# ch8             approximate algorithm

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['k1'] = set(['id', 'nv', 'ut'])
stations['k2'] = set(['wa', 'id', 'mt'])
stations['k3'] = set(['or', 'nv', 'ca'])
stations['k4'] = set(['nv', 'ut'])
stations['k5'] = set(['ca', 'az'])

final_stations = set([])

#
while states_needed:
    best_station = None
    states_covered = set()
    for stations, states_for_station in stations.item():
        covered = states_needed & states_for_station
        
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            
    states_needed -= states_covered
    final_stations.add(best_station)


# %%
# ################# ch9  




















