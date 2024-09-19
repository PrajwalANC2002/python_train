# P6. In the words1.txt file, find the number of strings with start with 'A' and end in a vowel
import re
def print_string_with_4_non_vowel(filename):
    with open(filename,"r") as my_file:
        for line in my_file:
            if(re.search(r"^A.*[AEIOUaeiou]$",line.strip())): 
                print(line)

print_string_with_4_non_vowel("words1.txt")
