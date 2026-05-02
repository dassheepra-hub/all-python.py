##### Q1) Python Program to Add Two Numbers
#####solution with predefined variables 

# num1 = 20
# num2 = 35
# sum = num1+num2
# print("the sum of given two numbers is = ",sum)



##### with user input()
 
# num1 = float(input("Enter the First no. here = ",))
# num2 = float(input("Enter the second no.here = ",))
# sum= num1+num2 
# print("sum of given two no.=",sum)

##### Q2) Hello world Program in python 

# print("Hello World")
# a = "Hello world"
# print(a)

###### Q3) Find and claculate square root program in python
###### using=g exponentiation 
# num = 64
# square = num ** (1/2)

# print(square)

# #2)user input
# num1 = int(input("enter a no. here = "))
# square = num1 ** (1/2)
# print(square)


###### Using math module 

# import math
# num = int (input("Enter your no."))
# sr = math.sqrt(num)
# print(sr)

#####Q4) How to calculate area of triangle 

# height = float(input("enter height",) )
# base = float(input("enter base ",))
# Area = (1/2)*height * base 
# print("area of triangle is",Area)


######Q5) print ( 1 to 5 ) in list format 
# i = 0
# for i in range (1,6):
#     print(i, end=" ")

######Q6) print squares of the numbers from 1 to 5 
# i = 0
# for i in range (1,6):
#     print(i**2,end= " ")

#####Q7) print even numbers from 1 to 10

# i = 0
# for i in range (1,11):
#     if i % 2 == 0:
#         print(i,end =" ")


#####Q8) calculate sum of numbers from 1 to 100

# total = 0
# for i in range (1,101):
#     total += i
# print(f'sum is {total}')

#####Q9) reverse a word 
# word  = "python"
# for i in range (len(word)-1,-1,-1):
#     print(word[i],end = "")

#####Q10) Count vowels in a string 
# count = 0
# vowels = "aeiou"
# word = "python"
# for char in (word):
#     if char in vowels:
#         count += 1
# print(f"total vowels in {word} is {count}")

####Q11) Printfibonacci sequence up to 10 terms 
# a = 0
# b = 1
# print (a,b , end =" ")
# for _ in range (10):
#     next_term = a+b
#     print(next_term,end=" ")
#     a,b = b,next_term

#####Q12) Calculate a Factorial of a number 
# n = int(input("enter your no. here = "))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(f"factorial of {n} is {factorial} ")

####Q13) Check if noo. is prime no. or not 
# num = 10
# is_prime = True 
# for i in range (2, int(num **0.5)+1):
#     if num % i == 0:
#         is_prime = False 
#         break 
# if is_prime and num > 1:
#     print(num , "is a prime member")
# else:
#     print(num,"is not a prime member")



####Q14) Count occurrences of each character in a string 
word = "Programming"
char_count = {}

for char in word :
    if char in char_count:
         char_count[char] += 1
    else:
         char_count[char] = 1

for char ,count in char_count.items ():
     print(char + ":" , count)















