# P5. In the words1.txt file, split all strings on vowels
# 
import re
def split_string_on_vowels(filename):
    with open(filename,"r") as my_file:
        for line in my_file:
            print(re.split(r"[AEIOUaeiou]",line.strip())) 

split_string_on_vowels("words1.txt")
