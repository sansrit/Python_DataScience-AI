# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 08:50:48 2020

@author: Admin
"""


#FINDINGS
#LOCAL VARIABLE AND GLOBAL VARIABLE CAN HAVE SAME NAME

'''
Functions
What is a function?
Variables
Functions Make Things Simple
Pre-defined functions
Using if/else Statements and Loops in Functions
Setting default argument values in your custom functions
Global variables
Scope of a Variable
Quiz on Loops
'''

'''
What is a Function?
You can define functions to provide the required functionality. Here are simple rules to define a function in Python:

Functions blocks begin def followed by the function name and parentheses ().
There are input parameters or arguments that should be placed within these parentheses.
You can also define parameters inside these parentheses.
There is a body within every function that starts with a colon (:) and is indented.
You can also place documentation before the body
The statement return exits a function, optionally passing back a value
'''


def add(a):
    b = a+1
    print(a, "if you add one ", b)
    return(b)
    

add(8)

#DEFINE A FUNCTION FOR MULTIPLE TWO NUMBERS

def Mult(a,b):
    c = a*b
    print(c)
    return(c)
    
    
Mult(7,9)
Mult(9.8,12.42)
Mult(2, "Sansrit ")

#VARIABLES 

def con(a,b):
   return(a + b)
    
con("Sansrit", "Paudel")



#predefined functions

numbers = [1,2,4,2,6,4]

num= sum(numbers)

print(num)


#USE OF IF ELSE STATEMENTS AND LOOPS IN FUCTIONS

# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Rajesh Hamal", "Thriller", 1980)
print(x)


#print list using for loop

def PrintList(the_list):
    for elements in the_list:
        print(elements)
        
PrintList([1,3,4,5,'cat'])

def con(a, b):
    return(a + b)

con('dal','bhat')









