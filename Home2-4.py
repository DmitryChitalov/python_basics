# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 02:55:29 2022

@author: z2- soft developer
"""

# Task4

user_msg = input("Enter your message:")
user_list = []
count = 1
for i in user_msg.split():
    print(count, i[:10])
    count += 1
    user_list.append(i)
print(count, user_list)

for n, m in enumerate(user_msg.split(), start=1):
    print(f"{n}- {m[:10]}")
    