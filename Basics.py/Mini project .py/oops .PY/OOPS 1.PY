#OOP IN PYTHON (OOBJECT ORIENTED PROGRAMMING )
#TO MAP THE REAL WORLD SCENARIOS WE STARTED USING OBJECTS IN CODE.
#####ABSTRACTION
#####ENCAPSULATION
#####INHERITANCE
#####POLYMORPHISM

######________________CLASS FUNCTION______________###########
# class student:
#      name = "karan"
# s1 = student()
# print(s1.name)
# #Default constructors 
#     def __init__(self):
#         pass
# #Parameterized constructors
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#         print("adding a new student in database..")


# s1 = student("karan",98)
# print(s1)
# print(s1.name,s1.marks)
# s2 = student ("arjun",88)
# print(s2.name,s2.marks )

# class car:
#     colour = "Blue"
#     brand =  "Mercedes"

# car1 = car()
# print(car1)
# print(car1.brand,car1.colour)


#########________init__Function_______________##############
# class student
# def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#         print("adding a new student in database..")


# s1 = student("karan",98)
# print(s1)
# print(s1.name,s1.marks)
# s2 = student ("arjun",88)
# print(s2.name,s2.marks )



############_________Class & Instance ATTRIBUTES________##########
#Class.attr
#obj.attr


#class student:
#      name = "karan"
# s1 = student()
# print(s1.name)


########__________Methods_________#########
# class student :
#     college_name = "ABC College "

#     def __init__(self,name,marks):
#         self.name = name 
#         self.marks = marks 

#     def Welcome(self):
#         print("Welcome student",self.name)

# s1 = student ("karan",98)
# s1.Welcome()
# print(s1.name,s1.marks)



#class student:
#      name = "karan"
# s1 = student()
# print(s1.name)


##########@staticmethod########

# class Account :
#     def __init__(self,bal,acc):
#         self.bal = bal
#         self.acc = acc

#     def debit(self,amount):
#         self.bal -= amount
#         print("Rs",amount,"was debited")
#         print("Total balance = " ,self.get_bal())

#     def credit(self,amount):
#             self.bal += amount
#             print("Rs",amount,"credited")
#             print("total balance = ",self.get_bal())

#     def get_bal(self):
#             return self.bal
        


# acc1 = Account(100000,125050)
# acc1.debit(1000)
# acc1.credit(5000)

#######_____Del keyword_____#####
#del s1.name 
#del s1


# class student :
#     def __init__ (self,name):
#         self.name = name 
# s1 = student("arjun")
# print(s1.name )
# del s1 
# print(s1.name )#ERROR 

#######_______Private (like) attributes & methods ______############

# class Account:
#     def __init__ (self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass ## to make it private just add two __ first and then write your attribute 

#     def reset_pass (self):
#         print(self.__acc_pass)


# acc1 = Account("12345","abcde")
 
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person :
#     __name = "anonymous"


#     def __hello(self):
#         print("hello person!")


#     def welcome(self):
#        self.__hello()


# p1 = Person()
# print(p1.welcome())
        
#######____INHERITANCE____######
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Toyotacar(Car):
#     def __init__(self,name):
#         self.name = name 


# car1 = Toyotacar("Fortuner")
# car2 = Toyotacar("Prius")

# print(car1.name)
# print(car2.name)


# class Fortuner():
#     def __init__(self,type):
#         self.type = type

# car1.start()

# car1 = Fortuner("Diesel")
# car2 = Fortuner("Petrol")
# car3 = Fortuner("CNG")
# car4 = Fortuner("EV")




# print(type(car1))

# print(car1.type)

# print(car2.type)

# print(car3.type)

# print(car4.type)

# class  A:
#     varA = "Welcome to class A "

# class B:
#     varB = "Welcome to class B "

# class C(A,B):
#     varC = "Welcome to class C "

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

##########______Supermethod______############
#super() method is used to access methods of the parent class
 
# class Car:

#     def __init__(self,type):
#         self.type = type


#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped..")

# class Toyotacar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name 
#         super().start()

# car1 = Toyotacar("Fortuner","Electric")
# print(car1.type)


# class Person :
#     name = "anonymous"

#     def changename(self,name):
#         Person.name = name ## or self.__class__.name= "Rahul Kumar"
# ##or can use @classmethod
# p1 = Person() 
# p1.changename ("Rahul kumar")
# print(p1.name)
# print(Person.name)


#########_______PROPERTY_______#########
# class Student :
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math 
#         self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        

#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        


# student1 = Student(98,85,87)
# student2 = (89,86,97)
# student3 = (82,96,79)

# print(student1.percentage)

# student1.phy = 86
# print(student1.phy)
# student1.calcPercentage()
# print(student1.percentage)

########_______@Property__________#########
##We use @property decorator pn any method in the class to use the method as a property.

#######_______Polymorphism________#######
##When the same operator is allowed to have different meaning according to the context.
##Operators & Dunder functions (__)


# class Complex :
#     def __init__(self,real,imag):
#         self.real = real
#         self.imag = imag
#     def shownumber(self):
#         print(self.real,"i+",self.imag,"j")

#     def __add__ (self,num2):
#         newreal = self.real + num2.real
#         newimag = self.imag + num2.imag

#         return Complex(newreal,newimag)
   

# num1 = Complex(10, 20)
# num1.shownumber()

# num2 = Complex(4, 8)
# num2.shownumber()

# num3 = num1+num2
# num3.shownumber ()




# print([i for i ,x in enumerate (a) if x == "$"])
# a = "Hello$world$"
# print(a.count("$"))
# parts = a.split("$")
# print(parts)

# x = 5
# y = 3
# temp = x
# x = y
# y = temp 
# print("value sfter swapping ",x)

# print("value sfter swapping ",y)

# x = 2
# y = 10
# x, y = y, x

# print("value sfter swapping ",x)

# print("value sfter swapping ",y)


# def is_prime (num):
#     #check if the no. is less than 2
#     if num < 2:
#         return False
#     #Check for factors from 2 to the square root of the number 
#     for i in range (2,int(num ** 0.5)+1):
#         if num%i == 0:
#             return False 
#         #if no factors are found, the no. is prime 
#         return True 
    
# num = int(input("enter a number = "))
# if is_prime (num):
#     print(f'{num} is a prime')
# else:
#     print(f'{num} is not a prime ')
   

#### Find out the factorial of a no. ######
num = 5
factorial = 1
for i in range (1,num+1):
    factorial =  factorial * i
    print(factorial)


