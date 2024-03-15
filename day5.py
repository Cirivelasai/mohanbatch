'''-

# ! ---> common functions for list

l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))

l1 = [6,8,9,"p","u"]
print(max(l1))
print(min(l1))

l1=[6,7,8,9,0,8.89,-5,0.78]
#index()
print(l1.index(9))

l1=[6,7,8,9,0,0.89,-5,0.78]

print(l1.count(6))

# ! some functions which is specifically used for list
To add element inside list
insert()----> to add element at specific index function
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
l1.insert(2,"cars")
print(l1)

# ? To delete element from list
l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
# po() -->last element will be deleted
l1.pop()
print(l1)

# pop(index_value)-->used to delete element at specific index
# l1.pop(4)
 # 4 is index value
 # print(l1)

 # remove(element)---> used to delete element directly
 l1.remove(8.89)
 print(l1)

#* clear() ---> to complete all element in list
 l1.clear()
 print(l1)

# ? ---> join 2 lists

l1=[0,0,8]
l2=["p","o","t",34]
print(l1+l1)

# dr
# extend() ---> to combine 2 lists
l1.extend(l2)
print(l1)
# ? ------> copy()

import copy
l1=[8,9,0,[5,6],[3,2,1]]
print(l1[-1][1])--> to index nested list

l2=copy.copy(l1)
l1.append(209)
print(l1)
print(l2)

l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)                                                                                                                        .
print(l1)



# ! ----> Tuple

1.) tuple have to be surrounded by ()
2.) The element inside tuple are not changable
3.) The element inside tuple are indexed
4.) The element will excuted in order
5.) It is heterogenous
6.) It allow duplicate element



# * eg:
t1 = (8, 8, 9, 5.78, [9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))
'''

l1=[8]
print(type(l1))#list

l1=(8,)
print(type(l1))#tuple

l1=8,9
print(type(l1))#tuple

#len(),min(),max(),index(),count()--->all same as list



# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples

t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1 + t2)

# To add all element inside list and tuple
sum()
l1 = (8, 9, 7, 6)
print(sum(11))

# ! ---->strings
s1 = 'o'
print(type(s1))

s1 = "u"
print(type(s1))

s1 = "hello world"
# * To acess string
print(s1)
# indexing and string ---> same as list and tuple
print(s1[0:5])


# functions of string
s1="helloworld"
# ? to convert all characters to upper case
s1="HFREDGiou"
print(s1,lower())


# strip()
s1="where are you"
print(s1.strip())
print(s1.rstrip())
print(s1.strip())


# split()--->
s1="where are you?"
# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
'''
# join the strings
'''
s1 = "hello"
s2 = "world"
print(s1+s2)
'''

#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))


# * join() -->
l1 = ["hey" ,"there"]
print(" ".join(l1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
characters =len(s1)
#print(characters)
'''
words = s1.split(" ")
print(words)


words = s1.split(" ")
print(len(words))

'''
#sentences = s1.split('.')
#print(len(sentences))


sentences = s1.split('.')
for val in sentences:
    if val =='':
        index = sentences.index('')
        sentences.pop(index)
print(len(sentences))






















































