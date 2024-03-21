f'''
# ! method over-riding
# * ploymorphism in classes

class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 9%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()


# ? Eg:2
class USA:
    def langauge(self):
        print("English")

    def captail(self):
        print("washigton DC")

class India(USA):
    def language(self):
        print("none")

    def capital(self):
        print("New delhi")

I = India()
I.language()
I.capital()

# Eg:
# polymorphism using objects

# c1, c2-->c1 = print(c1),print(c2)
# f1, f2


# * Eg:
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

# obj2.f1()


# ! Encapsulationj1 n
class car:
    name = "BMW" # private variable
    print(_name)

c1 = car()
print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error

# * ---> Eg:2
# ? Accessing private date outside the class
class c1:
    _phone = '7997867703'

    def display(self):
        print(self._phone)
c = c1()
c.display()

# * ---> Eg:3
# ? declare private method
class class1:
    def _m1(self):
        print("Iam saikumar")

    def _init_(self):
        self.m1()
c= class1()
c._m1() # error

'''

# ? nested class
class class1:
    class class2:
        name = "sidhu"

        def display(self):
            print(self.name)




















        
















































