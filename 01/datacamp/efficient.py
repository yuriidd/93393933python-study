# -*- coding: utf-8 -*-
"""Created on Sun Aug  6 19:55:32 2023@author: xiaom"""

##############

a = [1,2,3]
b = ['a','b']
list(zip(a[0:3], b))
a[0:3]

list(zip(range(5), range(2)))



########################################################            Counter

names = ['Seel', 'Nidorino', 'Fearow', 'Vanilluxe', 'Relicanth', 'Karrablast']
primary_types = ['Water', 'Poison', 'Normal', 'Ice', 'Water', 'Bug']
generations = [1, 1, 1, 5, 3, 5]


# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')
# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')
# Use list comprehension to get each Pokémon's starting letter
starting_letters = [name[0] for name in names]
# Collect the count of Pokémon for each starting_letter
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)

#############################                               combinations
# Import combinations from itertools
from itertools import combinations
# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')
# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')
# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)


######################################################


# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))
# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))
# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))



############################################            eliminating LOOPS


poke_names=['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aerodactyl', 'Aggron']
poke_gens=[4, 1, 3, 5, 1, 3]

# Collect Pokémon that belong to generation 1 or generation 2
gen1_gen2_pokemon = [name for name,gen in zip(poke_names, poke_gens) if gen < 3]
# Create a map object that stores the name lengths
name_lengths_map = map(len, gen1_gen2_pokemon[0])
# Combine gen1_gen2_pokemon and name_lengths_map into a list
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]
print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])

############################################          eliminating LOOPS

stats = array([[ 90,  92,  75,  92,  85,  60],
       [ 25,  20,  15, 105,  55,  90],
       [ 65, 130,  60,  75,  60,  75],
       [ 80,  70,  40, 100,  60, 145],
       [ 80, 105,  65,  60,  75, 130]])

# Create a total stats array
total_stats_np = stats.sum(axis=1)
# Create an average stats array
avg_stats_np = stats.mean(axis=1)
# Combine names, total_stats_np, and avg_stats_np into a list
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]
print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')
top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))


############################################            better LOOPS
# Import Counter
from collections import Counter
# Collect the count of each generation
gen_counts = Counter(generations)
# Improve for loop by moving one calculation above the loop
total_count = len(generations)
for gen,count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3} percentage = {}'
          .format(gen, count, gen_percent))

############################################                better LOOPS
pokemon_types=['Bug', 'Dark', 'Dragon', 'Electric', 'Fairy', 'Fighting']


# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]
# Create an empty list called enumerated_tuples
enumerated_tuples = []
# Append each enumerated_pair_tuple to the empty list above
for i,pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)
# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)

'''
[[1, 'Bug', 'Dark'], [2, 'Bug', 'Dragon'], 
 [3, 'Bug', 'Electric'], [4, 'Bug', 'Fairy'], [5, 'Bug', 'Fighting'], ...'''



#######################################3                better LOOPS
hps=array([ 80.,  60., 131.,  62.,  71., 109.])

# Calculate the total HP avg and total HP standard deviation
hp_avg = hps.mean()
hp_std = hps.std()
# Use NumPy to eliminate the previous for loop
z_scores = (hps - hp_avg)/hp_std
# Combine names, hps, and z_scores
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')

'''
('Abomasnow', 80.0, 0.46797638117739043)
('Abra', 60.0, -0.3271693284337512)
('Absol', 131.0, 2.4955979406858013)'''

# Use list comprehension with the same logic as the highest_hp_pokemon code block
highest_hp_pokemon2 = [(names, hps, z_scores) for names,hps,z_scores in poke_zscores2 if z_scores > 2]
print(*highest_hp_pokemon2, sep='\n')



#######################################3                better LOOPS





















