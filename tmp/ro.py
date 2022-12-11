# -*- coding: utf-8 -*-
"""Created on Sun Oct 16 20:36:39 2022@author: xiaom"""

'''
Cast Time (seconds) = VCT + FCT

VCT (seconds) = (BaseVCT - Sum_VCT) × 
    (1 − SQRT[{DEX × 2 + INT} ÷ 530]) × 
    (1 − Sum_GearVCTReduc ÷ 100) × 
    (1 − Sum_SkillVCTReduc ÷ 100)


FCT (seconds) = (BaseFCT - Sum_FCT) × (1 − Max_FCTReduc ÷ 100)

'''
import math

# GUST FC = 1.5      and VC = 6.3 sec
gust_fct = 1.5
gust_vct = 6.3
dex = 170
intellect = 160
sum_gear_vct = 5 + 7 + 6
sum_skill_vct = 0
vct = gust_fct * (1 - math.sqrt(dex * 2 + intellect) / 530) \
    * (1 - sum_gear_vct / 100) \
    * (1 - sum_skill_vct / 100)
fct = gust_fct
cast_time = vct + fct  
print(cast_time)
    



