# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:15:05 2020

@author: Sansrit Paudel
"""

'''
What is Numpy?
Type
Assign Value
Slicing
Assign Value with List
Other Attributes
Numpy Array Operations
Array Addition
Array Multiplication
Product of Two Numpy Arrays
Dot Product
Adding Constant to a Numpy Array
Mathematical Functions
Linspace
'''


#import
import numpy as np
import time 
import sys
import matplotlib.pyplot as plt

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)






a = np.array([0,1,2,4,3,5,67,3])

print("a[0]:", a[0])
print("a[3]:", a[3])

print(type(a))

print(a.dtype)

b = np.array([2.12,3.23])
print(type(b))
print(b.dtype)


a[0] = 15


peice = a[1:5]
print(peice)

print(a.size)
print(a.ndim)
print(a.shape)
print(a.mean())  #finding the mean value form list


print(a.std()) ##finding the standrd deviations

print(a.max()) #returns the maximum value in list


#NUMPY ARRARY OPERATIONS 

u = np.array([1,0])
v = np.array([0,1])
z = u+v
#Plotvec1(u,v,z)


#Adding constant number in numpy
u = np.array([1,2,3,4])
print(u+1)


#MATHEMATICAL FUNCTIONS

print(np.pi)

x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(y)


#lINSPACE

print(np.linspace(0, 10 , num = 5))
#here 0 is starting unit and 10 is ending with 5 division in total

x = np.linspace(0, 2*np.pi, num = 120)
y = np.sin(x)
plt.plot(x,y)

