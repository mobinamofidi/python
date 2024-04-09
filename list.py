# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:36:59 2024

@author: mobin
"""
#write one variable
fruit="apple"
print(fruit)

#more than one variable list variable
fruits=["apple","orange","banana","coconut"]
print(fruits)

#use index operator
print(fruits[0:4])
#use indext inversely
print(fruits[::-1])

#every second 
print(fruits[::2])

#for fruit in fruits
print(fruit)
#methods we can perfrom
print(dir(fruits))
print(help(fruits))

#print length and list 

print(len(fruits))
print(list(fruits))
#apple is in list or not
print("apple" in fruits)

#want to change 

#fruits.append("pineeapple")
print(fruits)
    #fruits.append(["berry","pineapple","qiwi"])
print(fruits)


#to remove element
#fruits.remove("apple")
print(fruits)

#insert a value at a given index
#fruits.insert(0,"qiwi")
print(fruits)


#sort of fruits
#fruits.sort()
#fruits.reverse()
print(fruits)

#fruits.clear()
print(fruits)


#index
fruits.index("apple")
print(fruits)
fruits.index("banana")

#count
print(fruits.count("banana"))
print(sorted(fruits))

print("  *  ".join(fruits))



















