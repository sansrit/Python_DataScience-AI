# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:32:37 2020

@author: Admin
"""

# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}

Corona_Nep = {"ktm": 3, "bharatpur": 10, "barabise":17 }


print(Dict)

#ACCESS BY KEYS

print(Dict["key1"])



#GET ALL THE KEYS

print(Corona_Nep.keys())

#GET ALL THE VALUES BY VALUE METHOD

print(Corona_Nep.values())

#APPEND THE VALUE 

Corona_Nep['Sindhuli'] = '6';

print(Corona_Nep)



#DELETE

del(Dict['key1'])

print(Dict)


#VERIFY KEY IS IN DICTONARY

print('ktm' in Corona_Nep)