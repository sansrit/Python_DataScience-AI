# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:04:14 2020

@author: Admin
"""

#create list

List = ["sansrit paudel", 12.2, 1998]

L = ["Dikshya", 3, 2000]

#INDEXING

'''
print('the same element using negative and positive indexing:\n Postive:',List[0], 
'\n Negative:' , List[-3]  )
print('the same element using negative and positive indexing:\n Postive:',List[1],
'\n Negative:' , List[-2]  )
print('the same element using negative and positive indexing:\n Postive:',List[2],
'\n Negative:' , List[-1]  )

'''

# SLICING AND EXTENDING

print(List[1:3])



List.extend(L)
List.append("Single")

print(List)



#LIST ARE MUTABLE 

random = [2,3,4]

print("Before change:", random)

random[0] = 'paudel';

print("after change:", random)

#DELETING LIST VALUES

del(random[0]);
print(random)

#SPLITING THE LIST ELEMENTS

chutiyaou = 'dal bhat';
seperate = '20,80,43,9';

print(chutiyaou.split())
print(seperate.split(','))

#Copy by reference
# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


#If data is cloned seperate object is created with makes immutable
# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])


# Clone (clone by value) the list A

B = A[:]
print(B)
 

