# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:46:51 2020

@author: Sansrit Paudel

"""

'''
Introduction to Classes and Objects
Creating a class
Instances of a Class: Objects and Attributes
Methods
Creating a class
Creating an instance of a class Circle
The Rectangle Class
'''
#import libary

import matplotlib.pyplot as plt


class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
        

RedCircle = Circle(8,'red')     #object 1
RedCircle.drawCircle();

greenCircle = Circle(6,'green')  #object 2
greenCircle.drawCircle(); 

blueCircle = Circle(4,'blue')
blueCircle.drawCircle();

#USE METHOD TO CHANGE THE OBJECT ATTRIBUTE

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

#RETURNS THE METHODS THAT CAN BE APPLIED ON
print(dir(blueCircle))



#creating a new Rectangle class for creating a rectangle objects

class Rectangle(object):
    #constructors
    def _init_(self, width = 3, height = 4 , color = 'r'):
        self.height = height
        self.width = width
        self.color = color
        
    #methods
    def drawReactangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        

blueRec = Rectangle(2, 30,'blue')
blueRec.drawReactangle()