# Write a function named inverse that accepts a fibonacci string as argument  and returned its position in the sequence.

s1 = "a"
s2 = "b"
print(f's_1= "{s1}"')

print(f's_2= "{s2}"')

for i in range (3, 11):
    s_next = s1 + s2
    print(f"s_{i}) = '{s_next}'")
    s1,s2 = s2,s_next


def fib_string(n):
    if n ==  1:
        return "a"
    elif n==2:
        return "b"
    else:
        return fib_string(n-2) + fib_string(n-1)
for i in range (1,11):
    print(f"s_{i} = '{fib_string(i)}'")



def inverse (s):
    for i in range (1,20):
        if (fib_string (i) == s):
            return i 
        

print(inverse("ab"))
print(inverse("abbabbababbab"))

    



