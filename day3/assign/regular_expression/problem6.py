# P6. In the words1.txt file, find the number of strings with start with 'A' and end in a vowel
import re
def print_string_with_4_non_vowel(filename):
    with open(filename,"r") as my_file:
        number_of_strings = 0
        for line in my_file:
            if(re.search(r"^A.*[AEIOUaeiou]$",line.strip())):
                number_of_strings += 1
        return number_of_strings


print(print_string_with_4_non_vowel("words1.txt"))
