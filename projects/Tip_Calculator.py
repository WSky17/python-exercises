#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:20:08 2022

@author: warren
"""

# Tip Calulator

print("Welcome to the tip calculator\n")

total_bill = float(input("What was the total bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_People = int(input("How many people to split the bill? "))

tip_percentage = tip/100

tip_amt = total_bill * tip_percentage

each_pays = round((total_bill + tip_amt) / num_People, 2)
each_pays = "{:.2f}".format(each_pays)

print (f"Each person should pay: ${each_pays}")