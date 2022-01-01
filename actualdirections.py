# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 11:20:26 2021

@author: saira

"""
from turtle import *

filename = input('filename: ')


# read file 

with open(filename, 'r') as directions:
    list1 = []
    list2 = []
    numberlist = []
    directionlist = []
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
    #for x in item:
     #   x = x.lower()
        
        # categorize info
        
        if len(item) == 2:
            number = item[1]
            numberlist.append(number)
            direction = item[0]
            directionlist.append(direction)
        elif len(item) == 3:
            number = item[2]
            numberlist.append(number)
            # direction1 = item[0]
            # direction2 = item[1]
            direction = item[0]
            direction1 = item[1]
            directionlist.append(direction)
     
            
        # isolate number from units
        number = number.split(' ')
        
        # if number line contains () then the actual distance needed to travel 
        # is the third item in the list
        if len(number) == 4:
            number = number[2]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        # convert from ft to miles 
     # #   if 'ft' in x and 's' not in x:
     #        number[0] == float(number[0]) * 0.000189394
     #  #  elif 'ft' in x and 's' in x:
     #   #     number2 = number[2].split(',')
        
     #    # convert from miles to pixels
     #    if 'mi' in x and 'min' not in x:
     #        number[0] == float(number[0]) * 6082561
            
        
     #    # change directions to something turtlegraphics can read
        
     #    # turn  full right
     #    if 'right' in x and not 'slight' in x:
     #        right(90)
        
     #    # slight right 
     #    elif 'right' in x and 'slight' in x:
     #        right(45)
            
     #    # turn full left
     #    if 'left' in x and not 'slight' in x:
     #        left(90)
            
     #    # slight left
     #    if 'left' in x and not 'slight' in x:
     #        left(45)
            
     #    # if 'continue' in x:
        #     forward(number[0])
       # print(number[0])
done()
               
            
               
               
        
         
                
               
            
           
           
    