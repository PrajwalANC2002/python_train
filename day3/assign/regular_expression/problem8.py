# P8. In the words1.txt file, replace all occurences of two or more consecutive vowels by an '_'
import re
def replace_two_or_more_vowels_with_underscore(filename,outputfilename):
    with open(filename,"r") as my_file:
        with open(outputfilename,"w") as output_file:
            for line in my_file:
                output_file.write(re.sub(r"[AEIOU]{2,}","_",line.upper()))


replace_two_or_more_vowels_with_underscore("words1.txt","problem8.txt")
