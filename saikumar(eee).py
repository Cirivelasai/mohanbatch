#a=7,8
#print(a)
#print(type(a))

'''
a,b=c=7,8
print(a)
print(b)
print(c)
'''
#a=b,c=4,2
#print(a,b,c)
                     #------->swapping of variables
#a=7
#b=5
                 #c=a
                 #a=b
                 #b=c
                 #print(a,b)

#eg:2
'''
a=a+b
b=a-b
a=a-b
print(a,b)
'''
#a,b=b,a
#print(a,b)       #only in python#

#----->id().....>used to find the memory adress of the variable
'''
print(id(a))
print(id(b))
'''
#......>keywords
#keywords are reserved words which is provides special meaning to compiler or interpretor
'''
import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
print(len(keyword.kwlist))
'''
#to check of the string is keyword or not
#print(keyword.iskw("if"))
'''
----->literals
literal is the constant value assigned to a variable
a variable is consider to be constant when it is defines in caps
 a=78    #a is variable
 A=78   #A is constant
'''
'''
# hash()....>it creats a hash value for constant datatypes and provides error for non constant datatypes
n1=89+7j
print(hash(n1))

f1=[7,8,9]
print(hash(f1))
#error ...>list is non -constant or mutable datatype
'''
"""
a=3
b=3
print(id(a))
print(id(b))
"""

#-----> operators
# ? operators are symboles which is used to perform various operations between 2or more operands
'''
arithmatic operator
logical operator
relational or comparison operator
bitwise operator
identity operator
membership operator
'''
# * --->arithmatic operation  ===>+ , - , * , / , % , // , **
#eg:1
a=8
b=5
c=9
print(a+b+c)


 #input()---->used to get the runtime input
#eval()--->used to get the runtime values of all data type
'''
n1=int(input("enter the value:"))
print(n1)


n1=eval(input("enter the value:"))
print(n1)
'''

a=4
b=2
print(a/b)          #is used to get the quotient value
print(a%b)       #is used to get the remainder value

#   // ----> floor division

a=20
b=10
print(a//b)  #----->the output will be inn integer & the output will be based on floor value

#   **   ----->used for power of a number
print(2**4)  #...>16

#assignme      ----->   +-=  ,   -=  ,  /=  ,  *=  ,  //=  ,  **=  ,  &=  ,  |=

a=3
a+=2
print(a)

# comparison  ----->==,  >  ,  <  ,  !=  , <= , >=

a=8
b=7
print(a>b)

a=9
b=5
print(a==b)

#bitwise operator ---->& ,  |  ,^  ,  ~  ,  << ,  >>
a=7
b=4
print(a&b)

# AND
# eg:1
# a = 6
# if a:
#      print("yes")
else:
    print("no")

# n = int(input("enter the number:"))
# if n %2==0:
#      print(n, "is odd")

# sum:2
# name, age, nationality
# 18 above, Indian

name = input("enter the name: ")
age = int(input("enter the age: "))
nationallity=input("enter the nation: ")

if age >18 and nationality=="Indian":
    print("eligible for vote")
else:
    print("not eligible")















