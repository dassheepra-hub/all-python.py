####Q5) Write a program to reverse each word in sentence " Hello World" using a while loop 
sentence = "Hello World"
words = sentence.split()
for word in words:
    i = len(word)-1
    while i >= 0:
        print(word[i],end ="")
        i -= 1
    print(end=" ")
    
