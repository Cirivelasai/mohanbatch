set1 = {'Python', 'Java', 'Data Science'}
set2 = {'ML', 'AI', 'R Language', 'Python'}
set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c = 0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in set1:
            if val in set2 or val in set3:
                flag=1
                break
    if c==2:
        for val in set2:
            if val in set1 or val in set3:
                flag=1
                break

    if c==3:
        for val in set3:
            if val in set2 or val in set1:
               flag=1
               break
if flag==0:
    print("Disjoint")
else:
    print("joint")
           

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)

#--->functions
# Defination
# Function is a block of code which is used to perform a specific
# functionality
# Function can be created using def keyword

# Function has 3 parts
# Function declaration
# Function defanition
# Function call

#eg:1
def greet():  #function definition
    print("greeting user!!")


#eg:2
#function with parameters
def greeting(name): #name is parameter
    print("welcome",name)
for val in range(3):
    username=input("enter the name:")
    greeting(username) #user name is argument
eg:3




# 1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
