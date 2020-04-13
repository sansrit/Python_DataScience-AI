# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:41:01 2020

@author: Admin
"""

tuple = ("ram", 3, 2.3)

tuple1 = ("hero", 7)

print(type(tuple))



print(tuple[0]);
print(tuple[2]);
print(tuple[-1]);
print(tuple[-2]);


print(type(tuple[2]));
print(type(tuple[0]));

tuple3 = tuple + tuple1

print(tuple3)


#slicing the array 

print(tuple[:2])

print(tuple[1:2])

#finding length of elements

print(len(tuple))


#sorting

numbers = (9,2,5,2,4,7,1,34,2)

number_sorted = sorted(numbers)

print(number_sorted);


#Nested tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

print(NestedT[2][1][0])

