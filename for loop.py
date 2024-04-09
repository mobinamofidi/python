# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:16:41 2024

@author: mobin
"""
sum=0
age=int(input("age"))
for i in range(age+1):
  
      sum=(sum+i**2)
print(sum) 
    
m=1+2**2+3**2
print(m)

sum=0
age=int(input("age"))
for i in range(age+1):
    sum=(sum+i)+(i**2)
print(sum)
    
m=1**1+1**2+2+2**2
print(m) 


#temp=int(input("what is temp of weather?"))
sum=1
for i in range(5,26):
         sum=sum+i 
print(sum)



n=int(input("age"))

sum=0
for i in range(n):
 sum=sum+i   
print(sum)


import time
for seconds in range(0,28,2):
    print(seconds)
    time.sleep(1)
    
print("happy new year")

rows=int(input("enter row"))
column=int(input("enter column"))
symbol=input("enter your symbol")

for i in range(rows) :
 for j in range(column) :
  print(symbol,end=" ")
 print()
 
 
 
 for num in range (1,9):
     print("mob")
     print(num*3+1_10)




scores=[("mobina",10),("aghdas",0),("gabri,20")]
for person in scores:
  name=person[0]
  score =person[1]
  print("hello" + name + " your score is " + str(score))

























 
     
    
    
    