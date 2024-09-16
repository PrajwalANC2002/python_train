# Write a function to print first 'n' odd numbers.
def print_first_n_odd(n):
    for i in range(n):
        if(i % 2 != 0):
            print(i)

print_first_n_odd(20)


