# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 12:03:21 2021

@author: saira

"""

#from turtle import *

filename = input('filename: ')


# read file 

with open(filename, 'r') as directions:
    list1 = []
    list2 = []
    for line in directions:
        if line != '\n':
            list2.append(line)
            if len(list2) == 2 or len(list2) == 3:
                list1.append(list2)
        else:
            list2 = []
   # print(list1)
   
   # interpret 
   
    for item in list1:
       for x in item:
           x = x.lower()
           
           # categorize info
           
           if len(item) == 2:
               number = item[1]
               direction = item[0]
           elif len(item) == 3:
               number = item[2]
               # direction1 = item[0]
               # direction2 = item[1]
               direction = item[:2]
        
           print(direction)    
           # isolate number from units
           number = number.split(' ')
           print(number)
           # if 'ft' in x and 's' in x:
           #     number1 = number[2]
           #     number1 = number1.split(',')