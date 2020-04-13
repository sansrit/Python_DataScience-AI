# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:22:49 2020

@author: Admin
"""

'''
Loops
Range
What is for loop?
What is while loop?
Quiz on Loops
'''

#RANGE

#range(3) includes 0,1,2;
print(range(4))


number = [6,12,3]

month = ['jan','feb','march']

N = len(number)

for i in range(N):
    print(number[i])
    
    

for i in range(0,7):
    print(i)
    
    
    

#EXAMPLE OF FOR LOOP , TO GO THROUGH THE LIST:
    
    

for maina in month:  #maina is varianle created
    print(maina)
    


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0,5):
    print("before square", i , "is", squares[i])
    squares[i] = 'weight'
    print("After square", i, 'is', squares[i])
    
    
    

# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"

# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 

print ("Return type:",type(obj1) )
print (list(enumerate(l1))) 

print(obj1)

# changing start index to 2 from 0 
print (list(enumerate(s1,2))) 



for i , square in enumerate(squares):
    print(i, square)
    


#WHILE LOOP
    
    
dates = [1982,1980, 1973, 2000]  #creating list

#initializations

i = 0 
year = 0 

while(year != 1973):
    year = dates[i]
    i = i+1
    print(year)
print("It took", i, "repreataions to get out of loop.")




# Write your code below and press Shift+Enter to execute
for i in range(-5, 6):
    print(i)
    
'''   
Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

Write your code below and press Shift+Enter to execute
​
'''
sq = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
    ​k = 0 
    while(sq[k] == 'orange'):
    new_squares.append(sq[i])
    k= k+1
print(new_squares)
