'''
# ----> while loop
# ----> break using while loop

# eg:1
# 1.) Iterate from 20 to 30 and break the loop in 27

i = 20
while i<31:
    if i ==27:
        break
    print(i)
    i+=1

# 2.)
i = 1
while i<31:
    print(i)
    if i==27:
        break
    i+=1

i = 20
while i<31:
    if i==27:
        print(i)
        break
    i+=1
# 4.)  
i = 1
while i<15:
      print(i)
      if i==14:
          break
      i+=1

# !-----> continue
# ---> Eg:1
i = 20
while i<31:
    i=i+1
    if i==27:
        continue
    print(i)


i = 1
while i<50:
        print(i)
        if i==45:
           break
        i+=2

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

i=12
sum=0
while i<22:
    sum=sm+i
    i+=1
    print(sum)


# ! Eg:6
# Find the average of value from 20 to 25

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
print(sum/count)

# !------> Nested for loop
# Eg:1

for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)
     
# Eg:22
# * * * * 
# * * * * 
# * * * * 
# * * * *

rows = int(input("enter the rows:"))
cols= int(input("enter the cols: "))

for row in range (rows):
    for col in range(cols):
        print("*", end=" ")
    print()

for row in range(5):
     for col in range(5):
         sum= sum+1 
         print(sum, end=" ")
    print()


#! to print stars in right angled triangle


for row in range(0,6):
    for col in range(0, row+1):
        print("*", end=" ")
    print()

#* * * * * *
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

for row in range(6, 0,-1):
    for col in range(0, row):
        print("*", end=" ")
    print()

for row in range(0, 5):
    for col in range (0, 6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
11 = [1, 4, 1, 7, 7.5, "p", "i"]
# print(11)
'''
# Positive indexing
#print(lst1[0])
#print(lst1[4])
#print(lst1[20])

# ? --> Positive indexing
print(1st1[0])
#print(1st1[4])
print(1st1[20]) --> error

# ? -----> Negative indexing
# lst = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# print(lst1[-1])
# print(lst1[-5])

# ? ----> slicing
lst = [1, 4, 1, 7,89.7, 7.5, "p", "i"]
# lst1[start_index:end_index:step]

# print(lst1[0:4])
# print(lst1[6:8])
# print(lst1[3:6])
# print(lst1[:5])
# print(lst1[:])

# print(lst1[0:7:1]) # lst[0.7] --> both are same
# print(lst1[0:7:2])

# trail = int(input())


lst = [1, 4, 1, 7, 89.7, 7.5, "p", "1"]
# print(lst1[-4:-1])
# print(lst1[-1:-4]) --> []
# print(lst1[-7:-1])
# print(lst1[-7:-1:2])












    











