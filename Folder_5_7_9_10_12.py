 # Functions
# def mean(value):
#     if isinstance(value, dict):
#         mean = sum(value.values()) / len(value)
#     else:
#         mean = sum(value) / len(value)
#     to3dp = (f"{mean:.3f}")
#     return to3dp
#
# # mean([2,3,31,21,3,1,5,78,11])
# my_dict = {"Harry":22,"Estel":89,"Joe":62}
# print(mean(my_dict))

# For advanced purposes, to check for type of any variable,...
# use isinstance(variable) rather than type(variable)

# Using the round function
# numbers = [2.1,4.7,8.2,11.23]
# for num in numbers:
#     print(round(num)

# Playing aroud with while loops
# while True:
#     username = input("Please enter your name: ")
#     if username == "admin":
#         break
#     else:
#         continue

# Challenge 1
# def sentence_maker():
#     entry = ""
#     while True:
#         text = input("""Say Something: """ )
#         if text == "/end":
#             break
#         if text.startswith(("how","what","why")):
#             entry += text.capitalize() + "?"+ " "
#         else:
#             entry += text.capitalize() + "." + " "
#     print(entry)
#
# sentence_maker()

# Example inf
# temp = [221, 232, 653, -934, 844]

# new_temp = []
# for t in temp:
#     new_temp.append(t/10)
# print(new_temp)

# Using list comprehensions
# new_temp = [t / 10 if t != -934 else 0 for t in temp]
# print(new_temp)

# def area(a, b):
#     return a*b
# print(area(a = 4,b = 3)) #This contains positional/keyword arguments
# print(area(4, 3)) #This contains non-keyword arguments

# If you create a function that takes in as many arguments as you want, use the *args keyword for non-keywords arguments
# def mean(*args):
#     return args
# print(mean(1,2,4,'a',5))

# If you create a function that takes in as many arguments as you want, use the *kwargs keyword for keywords arguments
# def mean(**kwargs):
#     return kwargs
# print(mean(a=2,b=4,c=53,d=23))
# print(type(mean(a=2,b=4,c=53,d=23)))

# File Processing
# with open('/home/spacey/Projects_with_Python/fruits.txt','a+') as p:
#     p.write("\nAluguitogui\nCucumber\nTomato\nOkro\nGarlic\n")
#     p.seek(0)
#     contents = p.read()
#     print(contents)
# # p.close()

#Using buit_in modules
# using the sleep method
# import time
# # time.sleep(5)
# # Writing a py_file that changes its contents every 5 secs
# while True:
#     with open('/home/spacey/Projects_with_Python/fruits.txt') as p:
#         print(p.read())
#         time.sleep(10)
#

# Writing a script that executes every 10 secs even if the file is missing
# import os
# import sys
# import time
#
# while True:
#      if os.path.exists('/home/spacey/Projects_with_Python/fruits.txt'):
#          with open('/home/spacey/Projects_with_Python/fruits.txt') as p:
#              print(p.read())
#      else:
#         print("File does not exist. please make sure file exists")
#      time.sleep(10)

#Writing a python script that reads a csv file and prints the average temperature every 10 secs
# First install pandas with pandas
# A collection of modules --> Package
# import os
# import sys
# import time
# import pandas as pd
#
# while True:
#   if os.path.exists('/home/spacey/Projects_with_Python/temps_today.csv'):
#       data = pd.read_csv('/home/spacey/Projects_with_Python/temps_today.csv')
#       print(data.mean())
#   else:
#      print("File does not exist. please make sure file exists")
#   time.sleep(10)


