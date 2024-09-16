# Write a function to print first 'n' primes. Use the previous function
def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def first_n_prime(n):
    count = 0
    i = 0
    while count < n:
        if(is_prime(i)):
            print(i)
            count = count + 1
        i = i + 1

first_n_prime(10)
