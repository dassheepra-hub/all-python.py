# print("Hello" ,"World" )
# print('Hello' ,'World' ,sep="-" )
# print('Hello', end=" " )
# print('World' )
# print('Hello', end="\n" )
# print('World' )
# print("hello","world",sep="  ")

# name=input('Enter your name here :- ')
# print(name)
# import math
# print(math.sqrt(25))
# num1=10
# num2=0.00
# print(num1/num2)#zero division error 
            #DATA TYPES 
# num=1
# print(type(num))#int
# name="krishna" 
# print(type(name))#string
# floatvalue=2.66
# print(type(floatvalue))#float
# a= True
# print(type(a))#Boolean

# import sys
# c=90
# print(sys.getsizeof(c))

# a=820005325632563832353652835353835345744212312344567891234567891234567891234567891212345678123456789123456789123456789987654321
# print(sys.getsizeof(a))#DYNAMICALLY MANAGED SIZE JUST LIKE A BALOON
# a=20
# b=-20
# c=20.5
# d=12+2j
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(d.real)
# print(d.imag)
# a='''This
# is a multiple line
# code '''
# print(a)
# s="ASTERISK"
# print(len(s))
# print(s[0])
# print(s[-1])
# print((s))
# a= "HELLO" 
# b= "World"
# print(a+":"+b)#CONCATENATION
# print(a*10)
# s1="Hello world"
# print(s1[0:5])
                 
                     #Step/Stride value 
# s1="PYTHON"
# # print(s1[0:5:1]) positive 
# print(s1[-6:3:2])  negative
# print(s1[-5:3:1])
#                      #REVERSE STRING 
# a="PYTHON is a programming language "
# # print(a[::-1])
# print(a[-1:-34:-1])#take +1 in step so that it will take all the values present in your sentence 
                   #Type conversion 
#1)implicit type conversion (Python automatically convert one data type to another )
#2)Ecplicit type conversion (We have to explicitly convert one data type to another)
                           #1)implicit type conversion 

# a=2
# b=5.2
# c=a+b
# print(c)
# a1=1
# b1=True#True is counted as 1 and false is 0 
# c=a1+b1
# print(type(c))
# print(c)
                           #2)Ecplicit type conversion
# a=1
# b="5"
# c=a+int(b)#b is a string so first change the string into integer 
# print(c)
# a= float("5")
# print(a)
# b= int(5.2)
# print(b)
# c=bool(1)
# print(c)
# d=str(10)
# print(d)
# print(type(d))
# e=bool("python")#any string will show true in bool 
# print(e)
# f=bool(None)
# print(f)
# a= (str((1, 2)))
# print(type (a))
# print(len(a))
                #OPERATORS
#1)ARITHMETIC OPERATORS 
#2)Comparison/Relational Opearators
#3)Logical Operators 
#4)Assignment Operators 
#5)Identity Operators 
#6)Membership Operators 
#7)Binary Operators 
                        
                    #1)ARITHMETIC OPERATORS(+,-,*,/,%,**,//) 
# (% Modulo sign return remainder )
# print(7%2)#Remainder 1
# # (** Exponential sign return powers )
# print(2**3)
# # (// Floor division return integer part only in division )
# print(8/3)#floor data type 
# print(8//3)#floor division 
                      #2)Comparison/Relational Opearators with strings
# a=2
# b=5
# print(a==b)
# print(a<b)
# print(a>b)
# print(a<=b)
# # print(a>=b)
# s1="abde"
# s2="abd"
# print(ord("a"))
# print(ord("c"))
# print(s1>s2)

#Multiple relational operators in single line  
#Python return True if all individual conditions are True else False 
# a=1
# s=5
# b=6
# d=25
# n=61
# print(a<s<b<d<n)
# print(a<s>b>d<n)
#Equal to operator 
# print(5==5.00)
# print(5==5.01)
# print(False==0)
# print(5 != "5")
# #AND OPERATOR & OR OPERATOR 
# a= 5
# b= 8
# c= 6
# print(a and b > 2)
# print(a<b and b>c)
# print(a>b or b>c)
# print(a>b or b<c)

# # NOT OPERATOR 
# a=20
# b=50
# print(not a>b)
# print(not(a<b))

#ASSIGNMENT OPERATORS 
#(Used to assig values to declared values )
# x=5
# x=x+5
# print(x)
# a = 100
# b = 200
# x,y,z=100,200,300
# print(x+y*2+z)
# y= 5
# y=5+2+y # Do not assign new values to already declared values it is not seen as a good coder 

# print(y)
# y += 2
# print(y)
# #Python does not have any increament operators like (++ or --) this works in other programming languages 
# # 10++ (Return syntax error ) Does not makes any sense in python 
# # ++10 makes sense it works
# print(+ +10)  
# print(+ -10)
# print(- - 10)
# print(- + 10)
               #IDENTITY OPERATOR (is operator & is not operator )
#use to verify the reference point to the some memory location or not 
#To determine if the values is of certain class or type 
# is  :- Returns True if the operands are identical else false 
# is not :- Return True if the operands are not identical else False 
# a = 1
# b = 2
# print(a is b)
# a = 5
# b = 5
# c = 6
# print(id(a))
# print(id(b))
# print(id(c))
# print(a is b)
# print(b is c)
                # Difference between is and == operator 
# x=[1,2,3]
# y=[1,2,3]
# print(id(x))
# print(id(y))
# print(x is y) #False 
# print(x == y) #True 
# x= 10
# y = 12
# print( x is not y  )
# a = [1,2,4]
# b = [1,2,4]
# print(a is not b)
#             Precedence of operators 
# When more than one operators is present in an expression 
# print(  6/2+3**4) study more about this and learn the order of all the operators
#                     ASSOCIATIVITY OF OPERATORS 
# When 2 operators have same precedence python follows associativty 
#I am the best coder in the world 
a = "best coder "
b = "world"
# print ("i am the %s""in the "  "%s" %(a,b) )



# # String functions 
# str = "i am a coder."
# print(str.endswith("er."))
# print(str.capitalize())#capitalize first character 
# print(str.replace("am","m")) #replace all occurences of old with new 
# print(str.find("coder") )#return 1st index of 1st occurence 
# print(str.count("am")) #counts the occurence of substr in string 

# name = input("Username: ")
# print(name)
# print(len(name))
# a = "two"
# print(len(a))
# name = input("username: ")
# print(name)

# a =  "I am working Harder and Harder every day" 
# print(str.count(a,"a"))

        #Conditional statements 
#if-elif-else(syntax)
# if(condition):
#     statement1
# light = "yellow"
# if(light == "red"):
#     print("stop") #Indentation 
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")

# elif(condition):
#     statement2
# else(condition):
#     statementN 



# marks = int(input("enter student marks here:"))

# if marks >= 90:
#     grade = "A"
# elif marks >= 80:
#     grade = "B"
# elif marks >= 70:
#     grade = "C"
# else : 
#     grade = "D"
# print("grade of the students -> ", grade  )

# NESTING 
# if(condition 1)
#     if (condition 2)
# print()
# sri radharaman

# age = 18
# if (age >= 18):
#     if(age>= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

# num = int(input("Enter number = "))
# if(num%2 == 0):
#     print("even")
# else:
#     print("odd")

# a = int(input("first no.: "))
# b = int(input("second no.: "))
# c = int(input("third no.: "))

# if(a>= b and a>= c):
#     print("first no. is largest",a)
# elif(b>=a and b>=c):
#     print("second no. is largest",b)
# else:
#     print("third no. is largest",c)

# a = int(input("enter a no."))

# if (a % 8 == 0):
#     print("multiple of 8")
# else:
#     print("not a multiple")

# name = "python"
# print(name.upper() ) 
# name = "PYTHON"
# print(name.lower() ) 
# name = "APRAJITA"
# print(name.title ())
# name = "aprajita"
# print(name.title ())
# name = " Python    "
# print(name.strip())   
# name = " Aprajita 98 "
# print(name.split()) 
# name = "python is an easy coding language to learn as a beginner "
# print(len(name.split()))

# marks = [89.5, 65.5, 35.5, 85, 64.5, 98.5]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(len(marks))

# student = ["aprajita", 95.5, 18, "Delhi"] 
# print(student[0])
# student [0] = "arjun"
# print(student)#strings are mutable


# list = [2,3,1]
# list.append(5)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# print(list)
# list.append(4)
# print(list)
# list.sort()
# print(list)
# #list.insert(index,element) insert element at index 
# list.insert(1,1.8)
# print(list)
# list.remove(1) #list.remove(element) firt element in the list will be removed
# print(list)
# list.pop(2)#list.pop(index)elemeent in index wiil be removed 
# print(list)





# a = [5,6,2,8]
# a[0] = 9
# print(a)




# #Tuples in python (tuple data is immutable )
# tup = (87,98,58,68,98)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# tup = ()
# print(tup)
# print(type(tup))

# # slicing in tuple 
# tup = (1,2,3,4,5,6,7,8,)
# # print(tup[1:6])
# print(tup.index(5))#print(tup.index(element) will give index no. for the first occurence of element 
# print(tup.count(2))#print(tup.count(element) will give how many times an element occurs 

# movies = []
# movie1 = input("enter first movie : ")
# movie2 = input("enter second movie : ")
# movie3 = input("enter Third movie : ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)



# movies = []
# movies.append(input("movie 1"))
# movies.append(input("movie 2"))
# movies.append(input("movie 3"))
# print(movies)

# list = ["m","a","m",]
# copy = list.copy()
# copy.reverse()
# if (copy == list ):
#         print("palindrome")
# else:
#         print("not a palindrome")


# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))

# grade1 = ["C","D","A","A","B","B","A"]
# grade1.sort()
# print(grade1)

# DICTIONARY & SET
#DICTIONARIES ARE MUTABLE 
# info = {
#         "key" : "value" , 
#         "subjects" : ["Mathematics","Physics","Chemistry","English"],
#         "topics" : ("algebra", "Thermodynamics", "Periodic Table", "Verb"),
#         "name" : "apnacollege" ,
#         "learning" : "coding" ,
#         "age" : 18
# }
# print(info["name"])
# print(type(info))
# info["name"] = "Sheepra Das" #overwrite
# info["weight"] = ("45.2 kg")
# print(info)

# null_dict = {}
# null_dict["name"] = ["Apna College"]

# print(null_dict)
# print(type(null_dict))


# Nested dictionaries 
# students = {"name" : "Sheepra Das ",
#                 "scores" : {
#                       "Stats" : 82.5,
#                        "Mathematics" : 88.2,
#                        "English" : 87.5,
#                        "programming for python" : 97.6 ,
#                         "Posh" : 85.6
           
#                        }
            
#             }
# print(students.keys())
# print((list(students.keys())))

# print(students.values())
# print((list(students.values())))
#print(students)
# print(students["scores"])

# Dictionary methods
# student_A = {"name" : "apnacollege",
#              "age" : 18,
#              "scores" : "98.5%",
#              "Weight" : "45kg",
#              "subjects" : {"physics": 98,
#                            "chemistry":88,
#                            "mathematics":89.2}
             
#              }
#methods for dictionary
# print(student_A.keys())
# print(student_A.values())
# print(student_A.items())
# print(student_A.get("scores"))#print(student_A.get(keys name))
# new_dict = {"name":"neha","city ": "delhi"} 
# student_A.update(new_dict)
# print(student_A)
# new_dict

#set
# Set is mutable but set elements are immutable 
#  (you cannot add mutable things in a set, ex: list,dict)
# num = {1,2,3,4,5,6,7,8,"world","string","world",5}
# print(num)
# print(type(num))
# print(len(num))#set ignore duplicate values while printing or in counting the length)
# collect = {}
# print(type(collect))#this is an empty dict
# collection = set()# this is an empty set 
# print(type(collection))

#set methods 
# set = {1,2,3,4}
# print(set)
# set.add(5)
# print(set)
# set.remove(4)
# print(set)
# set.clear()
# print(set)

# set.add("a,b,c,d")
# print(set)

  
# collection = {"world","college","code","python"}
# print(collection.pop())
# print(collection.pop())

# set_1 = {1,2,3,4,5}
# set_2 = {3,5,2,4,6,7,8}
# print(set_1.union(set_2))
# print(set_1)
# print(set_2)
# print(set_1.intersection(set_2))


# dict = {"table" : ["a piece of furniture" , "list of facts and figures",],
#         "cat " : "a small animal"}
# print(dict.keys())

# set = {"python", "java", "c++","python","javascript","java","python","java","c++","C"}
# print(len(set))
# print(set)

# dict = {}
# physics = input("physics marks :")
# dict.update({"physics": physics})
# Chem = input("Chem marks :")
# dict.update({"Chemistry":Chem})
# Mathematics = input("Mathematics marks :")
# dict.update({"mathematics":Mathematics})
# print(dict)


# value = {9,9.0}
# print(value)

# value = {"9",9.0}
# print(value)

# value = {(9,9.0)}
# print(value)
# print(type(value))

# value = {
#     ("float",9.0),
     
#    ("int",9)}
# print(value)



# LOOPS (WHILE LOOP, FOR LOOP)(loops are used to repeat instructions )
# while loops
# while condition :
# some work

# count = 1 #("iterators")
# while count <=5:
#     print("hello")
#     count += 1

#     print(count)

# i = 1
# while i <= 16:
#     print("radhe radhe",i)
#     i += 1


# print("loop ended")

#print(1 to 100 using while loop)
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1


#print(1 to 100 using while loop)
# i = 100
# while i >= 1 :
#     print(i)
#     i -= 1





#print a table for any no. using whhile loop
# i = 1
# while i <= 10:
#     print(3*i)
#     i += 1


#print(the members of the list )(traverse)
# num = [1,4,9,16,25,36,49,64,81,100]
# heroes = ["iron man","thor","batman","captain america","superman"]
# idx2 = 0
# while idx2 < len(heroes):
#     print(heroes[idx2])
#     idx2 += 1





# # find any no. x from the list 
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 81
# x = 0
# while x < len(num) :
#     if (num[x]==i):
#         print("found at idx",x)
#     x += 1



# idx = 0
# while idx < len(num) :
#     print(num[idx])
#     idx += 1

#Break and Continue 
# i = 1
# while i<=5:
#     print(i)
#     if (i==4):
#         break 
   
#     i += 1


# print("end of loop")

#Break & Continue 
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 100
# x = 0
# while x < len(num) :
#     if (num[x]==i):
#         print("found at idx",x)
#     else:
#         print("finding.....")
#     x += 1






# i = 0
# while i <= 4:
#     if(i == 2):
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i <= 10:
#     if(i%2==0):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1


    # For loops
    #loops are used for sequential traversal. For traversing list,string,tuples etc.

# list = [ 1,2,3,4,5]
# for val in list:#val = element 
#     print(val)
# else:
#     print("final")


# list = [1,4,9,16,25,36,49,64,81,100,49]
# x = 49
# idx = 0
# for el in list :
#     if (el == x):
#         print("numder found at idx ", idx)
#         break 
#     idx += 1


#range (start,stop,step)
#range functions returns a sequence of numbers,starting from 0 by default, and increment by 1 (by default ),and stops before a specified number. 
# seq = range(5)
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])


# for i in range (10):
#     print(i)

# for i in range (2,101,2):
#     print(i)






# nums = [1, 2, 3, 4, 5, 6]
# total = 0
# for num in nums :
#     if num % 2 == 0:
#         total += num **2
# print( total) 


# nums = [1,2,3,4,5,6,7,8,9]
# idx=0
# while idx < len(nums):
#     print(nums[idx])#nums[0],nums[1],nums[2]..
#     idx += 1
    
    #search for a number x in this tuple using loop:
# num = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(num):
#     if (num[i] == x):
#         print("found at idx",i)
#     i += 1

# i = 1
# x = 100
# while i <= x:
#     print(i)
#     i+=1 

# # QUESTIONS USING FOR & RANGE

# for i in range (1, 101):
#     print(i)

# for i in range (100, 0, -1):
#     print(i)


# # Print a table for any no. X using for and range 
# n = int(input("enter a number: "))

# for i in range (1, 11):
#     print(n * i)

# USE OF PASS STATEMENT 
# for i in range (5):
#     #empty 
#     pass

# if i > 5:
#     pass
# print("some useful work ")

# Functions & Recurssion 

#Function in python 
#Block of statements that performs a specific task.

# a = 5
# b = 10

# sum = a+b
# print(sum)
# #more lines of code 


# a = 12
# b = 18


# sum = a+b
# print(sum)
# #more lines of code 
# FUNCTION DEFINITION 
# def cal_sum(a,b):# PARAMETERS
#     return a+b

# sum = cal_sum (178,2222) #function call, Argument 
# print(sum)
# def print_hello():
#     print("hello")

# output = print_hello()
# print(output) #return none 


# # Function for average of 3 numbers 
# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg 

# calc_avg (97,85,98)

# print("apna college ",end=" ")
# print("sara")
#two types functions 
#1)Built in function ex.(print(),len(),type(),range())
#2)User defined functions (those functions which are written by us)


#Default parameters
# def cal_prod(a, b=5):
#      print(a*b)
#      return a*b

# cal_prod(a = 2)

#Questions 
#WAF to print the length of a list. (list is the paremeter)
# num = ("delhi","gurgaon","pune","mumbai")
# heroes = ("1","2,","3","4","5")

# def print_len(list):
#     print(len(list))

# print(len(num))
# print(len(heroes))

#Q2 WAF to print the elements of a list in a single line.(list is the parameter)
# num = ("delhi","gurgaon","pune","mumbai")
# heroes = ("1","2,","3","4","5")

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(num)
# print()



#Q3 WAF to find the fctorial of n!.(n is the parameter)


# def calc_fact(n):
#     fact= 1
#     for i in range (1, n+1):
#         fact *= i
#     print(fact)

# calc_fact(8)

#Q4 WAF to convert USD to INR.


# def  rate_usd(usd):
#     inr = 93.42
#     change =  usd * inr
#     print("current 1 usd value = ",inr,"INR")
#     print(usd,"USD = ",change,"INR")

# rate_usd (85) 

# def func(n):
#     if n%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")

# func(8)

# RECURSION 
# def  show(n):#CALL STACK 
#     if(n == 0):#BASE CASE 
#         return 
#     print(n)
#     show(n-1) 

# show(5)


# def fact(n):
#     if (n == 0 or n== 1):
#         return 1
#     else:
#         return fact(n-1) * n
    

# print(fact(5))

#QUESTION ON RECURSION 
#Q1 write a recursive function to calculate the sum of first n antural numbers.
# def natural(n):
#     if n == 0:
#         return 0
#     return natural(n-1)+n

# sum = natural(5)
# print(sum)

#Q2 Write a recursive function to print all elements in a list.
# Hint : use List & Index as parameters 


# def   print_list(list, idx = 0):
#     if idx == len(list):
#         return 
#     print(list[idx])
#     print_list(list,idx+1)  

# fruits = ["apple", "banana","litchi","mango","watermelon"]  

# print_list(fruits)


# LECTURE 7 (FILE INPUT/OUTPUT) File I/O in python 


#Tyepes of files 
#1) Text files : .txt, .docx, .log etc.
#2) Binary Files : .mp4, .mov, .png, .jpeg etc.



# BASIC OPERATIONS (OPEN , READ, WRITE  & CLOSE FILE )


# f = open("demo.txt","r")
# data = f.readline()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")#"r" means reading. 
# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)

# f.close()#Always close your file after working on it.

#Writing to a file 

# f = open("demo.txt", "w")#OVERWRITE DATA
# f.write("I want to learn javascript tomorrow. 123456789")#Overwrite the entire file 

# f.close()


# f = open("demo.txt", "a")# APPEND DATA
# f.write("\nWORK FOR IT ")#Overwrite the entire file 

# f.close()




# f = open("sample.txt","w")
# f.close()

#with syntax (as = alias)
# with open("demo.txt","r")as f :
#     data = f.read()
#     print(data)
# f.close()


# with open("demo.txt","w") as f:
#     f.write("new data")

# f = open("sample.txt","w")
# f.close()

# #Deleting a file 
# #using the os module 
# import os
# os.remove("sample.txt")


# with open("Practice.txt","r")as f: 
#     data = f.read()

# new_data = data.replace("Java","python")
# print(new_data)

# with open("Practice.txt","w")as f: 
#     data = f.write(new_data)


# def check_for_word():
#     word = "learning"
#     with open("practice.txt","r") as f:
#             data = f.read()
#             if(data.find(word) != -1):
#              print("Found")
#             else:
#              print("Not Found")
# check_for_word()



# def check_for_line():
#     word = "programming"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1 
#     return -1
# (check_for_line())

# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
#METHOD 1 (WITHOUT SPLIT METHOD USE)
    # num= ""
    # for i in  range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

#METHOD 2 (USING SPLIT METHOD USE)
# count = 0
# with open("practice.txt","r")as f:
#     data = f.read()

#     nums = data.split(",")
#     for val in nums:
#         if val.strip() and int(val.strip()) % 2 == 0:
#             count += 1
# print(count)








