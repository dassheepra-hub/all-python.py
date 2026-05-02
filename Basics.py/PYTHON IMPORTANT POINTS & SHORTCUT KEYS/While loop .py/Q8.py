#####Q8) write a program to calculate 3 to the power of 4
base = float(input( "write the base no. here = "))
exponent = float(input("write the exponent no. here = "))
count = 0
result = 1
while count < exponent :
    result = result * base 
    count += 1
    print(f"{base} to the power {exponent} is {result}")
   
