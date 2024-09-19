# P7. In the words1.txt file, replace all vowels with an '_' and write out to another file
#
import re
def replace_vowels_with_underscore(filename,outputfilename):
    with open(filename,"r") as my_file:
        with open(outputfilename,"w") as output_file:
            for line in my_file:
                output_file.write(re.sub(r"[AEIOU]","_",line.upper()))


replace_vowels_with_underscore("words1.txt","problem7.txt")
