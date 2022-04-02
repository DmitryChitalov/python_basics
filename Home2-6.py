# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 03:28:04 2022

@author: z2- soft developer
"""

# Task6

goods = []
count = 1
name = "name"
goods_name = ""
price = "price"
goods_price = ""
quantity = "quantity"
goods_quantity = ""
units = "units"
goods_units = "pieces"
analysis = []

for i in range(3):
    goods_name = input("What is it the name of the good which you're interested in?\n")
    goods_price = input("What price of a good does it available for you?\n")
    goods_quantity = input("How many pieces d\'you want to buy?\n")

    goods.append([(count, {name: goods_name, price: goods_price, quantity: goods_quantity, units: goods_units})])

    count += 1

print(goods)
