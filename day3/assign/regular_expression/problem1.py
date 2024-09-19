# P1. In the words1.txt file, find all strings of length 5
import re
def print_string_of_five_length(filename,n):
    with open(filename,"r") as my_file:
        for line in my_file:
            if(re.match("." * n + "$" , line)):  
                print(line)

print_string_of_five_length("words1.txt",5)
