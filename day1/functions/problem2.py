# Write a function to print all the numbers between 1 and 10 whose English language name has 'n' letters,
# by looping over numbers array
numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

def print_numbers_with_n_letter(n):
    for i in numbers:
        if(len(i) == n):
            print(i)
print_numbers_with_n_letter(3)

print_numbers_with_n_letter(4)
