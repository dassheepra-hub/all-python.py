word =input("enter your sentence here = ").split()
final =""
for i in word:
    tempword =""
    c = i.lower()
    tempword+= c[0].upper()
    tempword += c[1:len(c)]
    final += tempword 
print(final)