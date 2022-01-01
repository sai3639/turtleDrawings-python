# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 15:45:06 2021

@author: saira

"""
from turtle import *
filename = input('filename: ')
with open(filename, 'r') as directionID:
    #print(directionID)
    #list1 = []
    for line in directionID:
        list1 = [] ## every loop = empty list, follow directions, then empty the list for the next set? 
        line.strip('\n')
        if line != '\n':
            list1.append(line)
            for i in line:
                if i.isdigit():
                    print(i)
        if 'right' in line:
            print(line)
        # if line.isdigit():
        #     print(line)
        #     # draw the thing
        # if line == '\n':
        #     break
    print(list1)
        # if line.isdigit()
        
    # directionID = directionID.read()
    # for line in directionID:
    #     direction = directionID.strip('\n')
    #     print(direction)
    #for line in directionID:
        
        # if line == '':
        #     line = line.split()
        # print(line)
        #direction = line.strip('\n').split('\n')
      #  print(direction)