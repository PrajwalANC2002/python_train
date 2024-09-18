# Write a list comprehension to get all the primes from 1 to 1000
import math                                                     #to use sqrt function
def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if( n % i == 0):
            return False
    return True
prime_numbers = [i for i in range(1,1001) if(is_prime(i))]

print(prime_numbers)
