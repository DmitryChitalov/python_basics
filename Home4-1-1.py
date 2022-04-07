# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 03:30:01 2022

@author: z2- soft developer
"""

# Task1

import sys


def user_salary(mk_in_hr, rt_in_hr, bonus):
    return (mk_in_hr * rt_in_hr) + bonus


file, mk_in_hr, rt_in_hr, bonus = sys.argv

print(user_salary(float(mk_in_hr), float(rt_in_hr), float(bonus)))
