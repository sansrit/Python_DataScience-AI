# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 12:26:04 2020

@author: Admin
"""

#SETS .. FORM GARDA REPEATIATIVE VAYE NI LAST MA UNIQUE ELEMENTS HARU LAY FILL UP HUNXA


#CREATING A SET

set_a = {"nepal", "bhutan", "nepal", "bangladesh", "afganistan","india"}

print(set_a)


#CONVERT LIST TO SET


list_a = [1,2,3,4,1,3,6,7,]

converted_set_a = set(list_a);
#method set is used


print(converted_set_a)

#ADDING ELEMENTS ON SET

set_a.add("pakistan")
print(set_a)


#.remove method is used to delete elemets


#VERIFICATION

print("nepal" in set_a)


# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
intersection = album_set1 & album_set2

print(album_set1.difference(album_set2) )

album_set1.intersection(album_set2)   
album_set1.union(album_set2)

print(set(album_set1).issuperset(album_set2) )



A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print(sum(A))
print(sum(B))

album_set1.issubset(album_set2)