# print("Hello world")
# print("HARE KRISHNA ")
# print("hello")
# print ("Namaste india ")

# print('Hello' ,'World' ,sep="-" )
# print('Hello', end=" " )
# print('World' )
# print('Hello', end="\n" )
# print('World' )
# print("hello","world",sep="  ")


# print("*")
# print("**")
# print("***")
# print("****")
# print("*****")
# print("******")
# print("*******")
# print("********")
# print("*********")
# print("**********")
# print("         *")
# print("        **")
# print("       ***")
# print("      ****")
# print("     *****")
# print("    ******")
# print("   *******")
# print("  ********")
# print(" *********")
# print("**********")
# print(2.5)
# print(10+2)
#                    LECTURE 1.4 ( A QUICK INTRO TO VARIABLES )
# print("\n")
# a= 10
# print(a)
# b=20
# print(b)
# print(a+b)
# print(a*b)
# print("\n")
# a= 10
# print(a)
# a=a+1
# print(a)
# a=a+1
# print(a)
# a=a+1
# print(a)
# a=a+1
# print(a)
# ("\n")
# print("Enter a Number:")
# n=int(input())
# print(n)
# print(n+1)
# print(n+2)
# print(n+3)
# print(n+4)

# print("\n")

#                     LECTURE 1.5 VARIABLES AND INPUT STATEMENT
# print("Hello, type in your name: ")
# n=str(input())
# print("Which place are you in ")
# p=str(input())
# print("welcome",n,"How is the weather in",p)
# m=str(input())
# print("What is your age",n)
# age=int(input())
# print("good to know you are" ,age ,"year old" )

           
           
            #lecture 1.6 variable and literals

# p=str(input("What is your name: "))
# m=str(input("type your location : "))
# print("Hello",p,"How is the weather in",m,"?")
# age=int(input("What is your age?"))
# print("good to know that your are",age,"years old")
# r = int(input('Enter the radius of the circle : '))
# area = 3.14*r*r
# print('Area of the circle with radius',r,'is',area)

            #Lecture 1.7 (DATA TYPES)
# n = 10
# print(n)
# print('n is type of :',(type(n)))
# K = 6.5
# print(K)
# print('n is type of :', type(K))
# s = 'sudarshan'
# print(s)
# print('s is type of :',type(s))
 
# l=[10,20,30]
# print(l[0])
# print(l[1])
# print(l[2])
# print(type(l))
# print(type(l[2]))
            #Lecture 1.8(Data types 2)

# # i=10
# # j=5.2
# # str='India'
# # b1=True
# # b2=False
# # print(type(i))
# # print(type(j))
# # print(type(str))
# # print(type(b1))
# # print(type(b2))


# # a=int(5.7)#it is a float type data but we are using this as an integer 
# # b=int('10')#we have written 10 as string but it is an integer and the data type is also an integer 


# # print(a,type(a))
# # print(b,type(b))

# #         #BOOLEAN DATA TYPES 
# # a=bool(10)
# # b=bool(0) #this will give false as output 
# # b2=bool(0.0)#this will give false as output 
# # c=bool(25)

# # print(a,type(a))
# # print(b,type(b)) # 0 is always false as boolean value 
# # print(b2,type(b2))# 0 is always false as boolean value
# # print(c,type(c))

# a=bool('0') #This is True
# print(a,type(a)) #because 0 is printed as string here 

#                  #Lecture 1.9  OPERATORS AND EXPRESSIONS 1

    
# n = 10+13*2
# # MY guess is 46
# print(n)# but it's not 46 it's 36 becos it answers the way it is taught to the languange and it uses bodmas
# n = (10+13)*2# now it will give 46 as the answer 
# print(n)

                 #Lecture 1.10 OPERATORS AND EXPRESSIONS 2

# #ARITHMETIC OPERATORS (+,-,*,/,//,%,**)
# print('Addition',3+5)
# print('Subtraction',8-2)
# print('Multiplication',5*5)
# print('Division',8/3)
# print('Floor Division',8//3)#GIVE ANSWERS IN INTEGERS
# print('Modulo',8%3)#FIND REMINDERS
# print('Exponentiation',6**2)#FIND SQUARE 

# #RELATIONAL OPERATORS (<,>,<=,>=,!=)
# print()#RELATIONAL WILL ANSWER AS BOOLEAN VALUE ALWAYS
# print(5>10)#FALSE
# print(5<10)#TRUE
# print(5>=5)#TRUE
# print(5<=5)#TRUE
# print(5==50)#FALSE
# print(5!=50)#TRUE
                  
# print()
#                   #LOGICAL OPERATORS (and,or,not)
# print(True and True)#True
# print(True and False)#False
# print(False and True)#False
# print(False and False)#False
# print()
# print(True or False)#True
# print(False or True)#True
# print(True or False)#True
# print(False or False)#False
# print()
# print(not(True))#False
# print(not False)#True 

#                         #Lecture 1.11(Introduction to Strings)
# # s='coffee'
# # t='bread'
# # print(s)
# # print(t)
# # print(s+t)# THIS IS CALLED CAONCATENATION 
# # print(s[0])
# # print(t[1:5])
# # a=s[0]
# # b=s[4]
# # print(a)
# # print(b)
# # print(a+b)

# s='0123456789'
# a=int(s[1])
# b=int(s[5])
# print(a)
# print(b)
# print(a+b)
# a=s[5]
# b=s[8]
# n=int(a+b)
# print(n)
# print()

# a=int(s[6])
# b=int(s[8])
# n=a+b
# print(n)

#                     #Lecture 1.12(More on Strings)
# a='good'
# print(a*5)
# print(a[0]*5)
# a=('abcde'=='abde')
# print(a)
# b=('abcde'<='abcde')
# print(b)
# c=('abcd'<'abcde')
# print(c)
# d=('abde'<'abcde')
# print(d)
# a='PYTHON'
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print()
# print()
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
# print(a[-5])
# print(a[-6])
# a='jadlkjlsufrowefjlsdjfoufrosjdenk'
# print(len(a))
# print(a[31])

                       #Lecture 1.13()
# print("a+'b'+c+''+d")
# print(13 % 5 // 2 * 30 ** 5)
# print(" week 1 completed ")




