# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:31:58 2020

@author: Sansrit
"""


import numpy as np
import matplotlib.pyplot as plt

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]


#converting the list into numpy array

A = np.array(a)
print(A)

print(A.ndim) #shows dimension

print(A.shape) #shows the 3x3 dimensions
print(A.size) #shows the total no of elemens

print(A[1,1]) #accessing matrix

# Access the element on the first row and first and second columns

print(A[0][0:2])


# Access the element on the first and second rows and third column

print(A[0:2, 2])

X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
Z = X + Y
print(Z)



# Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])

#MATRIX MULTIPLICATIONS

Z = np.dot(A,B)

print(Z)

# Calculate the sine of Z

print(np.sin(Z))

# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
# Get the transposed of C

print(C.T)
print(C.ndim)
