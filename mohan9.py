'''
ass-1
#2.)find the uncommon words from 2 strings
#s1="Hello how are you"
#s2="Hello how is"
#s1 = s1.split(" ")
#s2 = s2.split(" ")
#for val in s1:
#    if val not in s2:
#        print(val)      
#for val in s2:
#    if val not in s1:
#        print(val)
#3.)write a code print the 8th fibanocii number
#0,1,1,2,3,5,8
#num = 8
#n1 = -1
#n2 = 1
#for val in range(num):
#    ans = n1+n2
#    print(ans)
#    n1 = n2
#    n2 = ans
# constructors
#eg-2
#unparametarised constructor
#class profile:
#    def __init__ (self):
#         print("hello world")
#obj =profile()
#obj.__init__()
#'''

#eg-3
#parameterised constructor
#class profile:
#      def __init__(self,id,name,age):
#          print(id,name,age)
#obj = print(1,"sai",21)


# ? Eg:4
# class c1:
#    email = "sid@gmail.com"

#    def m1(self):
#        name = "sid"
#        place = "cbe"
#        print(name, place)
#        print(self.email)

# object = c1()
# object.m1()

# ? Eg:5
#class c1:
#    def m1(self):
#        name = "janu"
#        age = 20
#        return name, age
#    def display(self):
        # ! print(name, age)
        # !print(self.name,self.age)
#        print(self.m1())
#object = c1()
# object.display()

# ? Eg:6
#class class1:
#    def __init__(self):
#       self.name = "janu"
#       self.email = "janu@gmail.com"
       # return name, email #error ---> cannot use return with constructor

#    def display(self):
#        print(self.name, self.email)
#c1 = class1()
#c1.display()

# ! -------> Inheritance

# The process of utilising the methods and attributes of parent class
# through the object of child class it is called as inheritance
# * single Inheritance
# ? It has only one parent class and only one child class
# ! Eg:1
# class parent(child):
#    def m1(self):
#        print("Iam parent class")

# class child:
#     def m1(self):
#        print("Iam child class")

# p = parent()
# p.m2()

# obj = child()
# obj.m1()

# ! Eg:2
#class c1:
#    def __init__(self):
#        print("Iam constructor from parent class")

#class child1(c1):
#    pass
#obj = child1()

# ! Eg:3
# class parent:
#    name = "sidhu"

# class child(parent):
#    name = "name1"

#    def display(self):
#        print(self.name)

# d = child()
# d.display()

# ! Multilevel inheritance
# ? Eg:1
# class voice:
#   def sound(self):
#        print("All the animals have their own voices")

#class dog(voice):
#    def dog_voice(self):
#        print("bark")

# class cat(voice):
#    def cat_voice(self):
#        print("Meow")

# class parrot(cat):
#    def parrot_voice(self):
#        print("speak")

# all = parrot()
# all.dog_voice()  
# all.cat_voice()
# all.sound()
# all.parrot_voice()

# ! EXAMPLE:2
#class honda_city:
#    def honda_city_engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
#        print(cc, Hp, torque, fuel_type, num_of_piston)
#    def honda_city_body_specs(self, color, weight, height, length, vehicle_type):
#        print(color, weight, height, length, vehicle_type)
#class amaze(honda_city):
#    def engine_specs(self, cc, Hp, torque, fuel_type,num_of_piston):
#        print(cc, Hp, torque, fuel_type, num_of_piston)
#    def amaze_body_specs(self, color, weight, height, length, vehicle_type):
#        print(color, weight, height, length, vehicle_type)
#class civic(amaze):
#    def civic_engine_spees(self, cc, Hp, torque, fuel_type,num_of_piston):
#        print(cc, Hp, torque, fuel_type, num_of_piston)
#    def civic_body_specs(self, color, weight, height, length, vehicle_type):
#        print(color, weight, height, length, vehicle_type)
#class Honda(civic):
#    pass
#honda = Honda()
#honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
#honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")
#
# * Multiple Inheritance
# ? It has multiple parent and 1 child
#class while_pertol:
#    def function_w(self):
#        print("used to Airplans")
#class Organic_petrol:
#    def function_o(self):
#        print("used for Bike, cars")
#class premium_petrol:
#    def function_p(self):
#        print("spots cars, bikes")
#class petrol(while_pertol, Organic_petrol, premium_petrol):
#    def defanition(self):
#        print("Petrols types")
#p=petrol()
#p.defanition()
#p.function_o()

# > Eg:2
# mro --> method resolution Order
#def add(self, a, b):
#        print(a+b)
#    def mul(self,a,b):
#        print(a%b)

#class subract:
#    def sub(self, a, b):
#        print(a-b)
#class multiply:
#    def mul(self, a, b):
#        print(a*b)
#class division(addition, subtract, multipy):
#    def div(self, a, b):
#        print(a/b)
#calc = division()
#calc.add(3,4)
#calc,mul(4,2)


# ! Heirarical inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance
class c1:
    def m1(self):
        print("Class1")
        
      def m3(self):
      print("class2")

class c4(c2):
   def m4(self):
      print("class 3")

class c5(c4):
   def m5(self):
      print("class 4")
      
class c6(c5, c3):
   def m6(self):
       print("class 4")
obj = c6()
obj.m3()

# ! ------------> polymorphism

























        
       
class
