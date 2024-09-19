# P3. In the words1.txt file, find all strings have 3 non-vowels together like "cdg", or "xyz". 
# Think about using the caret.
import re
def print_string_with_3_non_vowel(filename):
    with open(filename,"r") as my_file:
        for line in my_file:
            if(re.search(r"[^AEIOUaeiou]{3}",line.strip())): 
                print(line)

print_string_with_3_non_vowel("words1.txt")
