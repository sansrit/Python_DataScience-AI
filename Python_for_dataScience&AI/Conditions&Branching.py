# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:02:22 2020

@author: Admin
"""

#CONDITION STATEMENTS

'''COMPARISION OPERATORS
equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
'''

# Condition Equal

a = 5
a == 6

print(a==6)
print(a!= 6)

#use diffrent comparision operators


#BRANCHING


#IF STATEMENT EXAMPLE


age =  12

if age > 12:
    print("you can ride bicycle")
    
elif age == 12:
    print("You have low immune system")
    
else: 
    print("you are too young")
    
    
print("stay home in lockdown")


#LOGICAL OPERATORS
'''
and
or
not
'''

#CORONA TESTING THINGS

test1 = "cough"
test2 = "fever"
test3 = "returned form aboard"

if(test1 and test2):
    print("you are infectd by corona")
else:
    print("you are healthy")



album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
    
    


# Condition statement example

album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")
    
    
    
