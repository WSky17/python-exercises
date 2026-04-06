#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 07:56:27 2022

@author: warren
"""


#Exercise 3.1 Odd or even

# 🚨 Don't change the code below 👇
# =============================================================================
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# 
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("This is an odd number")
#     
# =============================================================================

#practice if/else/ elif
# =============================================================================
# 
# print ("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# 
# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     elif age >=45 and age <= 56:
#         print ("Your ticket is free")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
# 
# =============================================================================

# Exercise 3.2 BMI 2.0

# =============================================================================
# 
# =============================================================================


# Exercise 3.3 Leap Year Exercise 

# =============================================================================
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# 
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print ("Not leap year.")  
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")
# =============================================================================

# =============================================================================
# #Exercise 3.4 Pizza Order 
# 
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# # 🚨 Don't change the code above 👆
# 
# #Write your code below this line 👇
# bill = 0
# 
# if size == "S":
#     bill += 15
# 
# elif size == "M":
#     bill += 20
# 
# else:
#     bill += 25
# 
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# 
# if extra_cheese == "Y":
#     bill +=1
# 
# print (f"Your final bill is ${bill}")
# =============================================================================


#Exercise 3.5 Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#count letter in true in both names and add
# =============================================================================
# first_count = name1.lower().count("t") + name2.lower().count("t")
# 
# first_count += name1.lower().count("r") + name2.lower().count("r")
# 
# first_count += name1.lower().count("u") + name2.lower().count("u")
# 
# first_count += name1.lower().count("e") + name2.lower().count("e")
# 
# #count letter in love for both names and add
# 
# second_count = name1.lower().count("l") + name2.lower().count("l")
# 
# second_count += name1.lower().count("o") + name2.lower().count("o")
# 
# second_count += name1.lower().count("v") + name2.lower().count("v")
# 
# second_count += name1.lower().count("e") + name2.lower().count("e")
# 
# loveScore = first_count*10 + second_count
# =============================================================================
combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

true = t + r + u + e
love = l + o + v + e
loveScore = int (str(true) + str(love))

if (loveScore <10) or (loveScore >90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >=40) and (loveScore <=50):
    print(f"Your score is {loveScore}, you are alright together.") 
else:
    print(f"Your score is {loveScore}.")

