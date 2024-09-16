# Write a function to print all the letters that appear in a given string along with their count.
# For example, for string "hello", the function should print "h:1, e:1, l:2, o:1"
# Hint: Use a dictionary to store the count of each letter
example = "hello"

def freq_letter(s):
    letter_count = {}
    for i in s:
        if( i in letter_count):
            letter_count[i] +=  1
        else:
            letter_count[i] = 1
    return letter_count

print(freq_letter(example))
