# to print the nth prime number using is_prime function
def is_prime(n):
    if(n <= 1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    return True

def nth_prime(n):
    count = 0
    i = 0
    while count < n:
        if(is_prime(i)):
            count = count + 1
        if(count == n):
            print(i)
        i = i + 1

nth_prime(10000)
