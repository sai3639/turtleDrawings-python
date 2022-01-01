# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:32:58 2021

@author: saira

"""

from turtle import * 

def drawsquare():
    """Draw a square and return to originial position and orientation"""
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)    # To return to starting orientation

drawsquare()
up()            # Pick up pen - no drawing
forward(150)
down()          # Put pen down and start drawing
drawsquare()    

help(drawsquare)
done()          # So the window doesn't disappear, use with PyCharm and Spyder
