# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:45:05 2020

@author: Admin
"""

with open("check.txt", 'w') as next_test:
    next_test.write("Hello sindhupalchowk ")
  
    


#READ FILE
    
with open("check.txt", 'r') as testwrite_file:
    print(testwrite_file.read())
    
    
    
    
with open("check.txt", 'w') as next_test:
    next_test.write("this is line A\n")
    next_test.write("this is line B\n")
    
    
    
with open("check.txt", 'r') as testwrite_file:
    print(testwrite_file.read())
    
    

with open("check.txt", 'a') as testwrite_file:
    testwrite_file.write("This is line C \n")
    
    
    
with open("check.txt", 'r') as testwrite_file:
    print(testwrite_file.read())
    
    
    
    