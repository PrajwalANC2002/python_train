# Write a function which converts the first letter of every word in a string to upper case. Assume that words are separated by one space.
# You may use string.split() function to split the string into words
company = "mirafra software technologies pvt. ltd."

def first_letter_to_upper(s):
    words = s.split(" ")
    new_string = ""
    for word in words:
        new_word = (word[0].upper() + word[1:])
        new_string = new_string + new_word + " "
    return new_string
            
print(first_letter_to_upper(company))


