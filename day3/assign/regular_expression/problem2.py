# P2. In the words1.txt file, find all strings which end with a vowel
import re
def print_string_ending_with_vowel(filename):
    with open(filename,"r") as my_file:
        for line in my_file:
            if(re.search(r".*[AEIOU]$" , line.strip().upper())): 
                print(line)

print_string_ending_with_vowel("words1.txt")
