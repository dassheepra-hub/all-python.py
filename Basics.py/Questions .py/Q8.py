#checking whether a number is prime or not 
def is_prime(n):
    if n<2:
        return False 
    for i in range (2,n):
        if n % i == 0:
            return False 
        return True 
    
    def prime_galore (L):
        count = 0
        for i in range (len (L)):
            if is_prime [i] and is_prime (L[i]):
                count+= 1
                return count 
             
a = is_prime(6)
print(a)                                                                                                                                            