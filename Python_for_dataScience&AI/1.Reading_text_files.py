# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:01:03 2020

@author: Admin
"""

#read test.txt

'''
example = "test.txt"  #setting up the location of file
file1 = open(example, "r")  #setting locationa and mode on variable file
print(file1)
print(file1.name)
print(file1.mode)
print(file1.read())

print(type(file1))
file1.close()       #closing file
'''


#ALTERNATIVE METHOD USING WITH OPEN . AS WE DON'T HAVE TO CLOSE FILE 


with open("test.txt", "r") as file1:
    fileContent = file1.read()
    print(fileContent)
    

print(file1.closed) #verified file is closed



#TO READ ONLY SOME CHARACTES IN FILE WE USE METHOD read()


with open("test.txt", "r") as file2:
    print(file2.read(8))
    print(file2.read(9))
    
    
#TO READ ONLY ONE LINE 
    
with open("test.txt", "r") as file:
    print("first Line: " + file.readline())
    
    
#WE CAN ALSO LOOP TO READ ALL LINES
    

with open("test.txt","r") as fileN:
    i = 0;
    for line in fileN:
        print("Iteration", i, ":", line)
        i = i+1
        
#READ ALL LINES AND SAVE AS A LIST
        
with open("test.txt","r") as filek:
    list = filek.readlines()
    print(list)




