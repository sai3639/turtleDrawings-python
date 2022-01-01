# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:51:44 2021

@author: saira

"""


filename = input('filename: ')


# read file 
from turtle import * 

with open(filename, 'r') as directions:
    
    # find find number/distance in directions
    
    for line in directions: 
        if ' mi' in line and ' min' not in line and not 'Pass' in line:
            number = line.split(' ')
            num = number[0]
            num = float(num)
    
        elif ' mi' in line and ' min' in line and not 'Pass' in line:
            number = line.split(' ')
            num = number[2]
            num = num.replace('(', '')
            num = float(num)
        
            
        elif ' ft' in line and not' s' in line:
           # print('foot', line)
           number = line.split(' ')
           num = number[0]
           num = float(num)
           num = num*0.000189394
        
        elif ' ft' in line and ' s' in line:
            number = line.split(' ')
            num = number[2]
            num = num.replace('(','')
            num = float(num)
            num = num*0.000189394
            
            
            
            
            
            
          #  forward(num)
        # elif 'Turn right' in line:
        #     right(90)
        # elif 'northeast' in line:
        #     right(45)
        # elif 'Slight right' in line:
        #     right(45)
        # if 'Continue' in line:
        #     forward(num)
        # elif 'Drive' in line:
        #     forward(num)
        # elif 'Turn left' in line:
        #     left(90)
            
            
            
            
            
            
           # print(float(num))
        # if "Slight right" in line:
        #     print('slight', line)
            
            
# convert feet to mi 
done()


            