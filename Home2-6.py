# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 03:28:04 2022

@author: z2- soft developer
"""

# Task 6

product_structure = {
    "Name": str,
    "Price": int,
    "Quantity": int,
    "Units": str,
}

product_list = []
product_counter = 1

while True:
    decision = input(f"Goods = {len(product_list)}, will it be added? [y/n] ").lower()

    if decision == 'n':
        break
    else:
        product_info = {}

        for pr_name, pr_type in product_structure.items():
            user_input = input(f"Fill the field '{pr_name}': ")
            product_info[pr_name] = pr_type(user_input)

        product_list.append((product_counter, product_info))
        product_counter += 1
print(product_list)
product_analysis = {}

for analysis_key in product_structure.keys():
    item_list = []

    for product in product_list:
        item_list.append(product[1][analysis_key])

    product_analysis[analysis_key] = item_list

print(product_analysis)

