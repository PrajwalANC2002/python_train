# P10. In the words1.txt file, find all strings have 3 non-vowels together like "cdg", or "xyz". 
# Print the matching string and matching sub-string
import re
def print_string_and_substring_with_3_non_vowel(filename):
    with open(filename,"r") as my_file:
        for line in my_file:
            match = re.search(r"([^AEIOUaeiou]{3})",line.strip())
            if(match): 
                print(match.group(),":",line)

print_string_and_substring_with_3_non_vowel("words1.txt")
