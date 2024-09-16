# 2. Write a loop to print all the numbers between 1 and 10 whose English language name has 3 letters,
# by looping over numbers array
numbers = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
for i in numbers:
    if(len(i) == 3):
        print(i)
