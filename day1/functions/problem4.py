# Write a function to check if a number is a prime. Should return True if number is prime, else False

def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

print(is_prime(0))
print(is_prime(1))
print(is_prime(7))
print(is_prime(3))
print(is_prime(10))
