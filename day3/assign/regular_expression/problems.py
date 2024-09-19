# Reference: https://www.programiz.com/python-programming/regex

# regex is a sequence of characters that defines a text pattern.

# Example:

# ^a...s$ defines a pattern that matches any five letter string starting with 'a' and ending with 's'. 
# Some examples
# "alias", "abyss"

# Regex in python

import re
pattern = 'a...s'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

# Meta characters

# [] - Square brackets specifies a set of characters you wish to match.
# Examples: [abc] means any of 'a', 'b', 'c' which is same as [a-c]

# You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.
# [^abc] means any character except a or b or c.
# [^0-9] means any non-digit character.

# . A period matches any single character (except newline '\n'). Example in the code above

# ^ The caret symbol ^ is used to check if a string starts with a certain character.

# $ The dollar symbol $ is used to check if a string ends with a certain character.

# * The star symbol * matches zero or more occurrences of the pattern left to it.

# + The plus symbol + matches one or more occurrences of the pattern left to it.

# ? The question mark symbol ? matches zero or one occurrence of the pattern left to it.

# {} Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

# | Vertical bar | is used for alternation (or operator).

# () Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

# \ Backlash \ is used to escape various characters including all metacharacters.

# Special Sequences - Look up at https://www.programiz.com/python-programming/regex

# Methods in re

# The re.findall() method returns a list of strings containing all matches.


# Program to extract numbers from a string

import re

string = 'hello 12 hi 89. Howdy 34'
pattern = r'\d+'

result = re.findall(pattern, string) 
print(result)

# Output: ['12', '89', '34']

# The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.

# re.sub method returns a string where matched occurrences are replaced with the content of replace variable.

# Program to remove all whitespaces
import re

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = r'\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Output: abc12de23f456

# Problems:

# Use regex for the following problems

# P1. In the words1.txt file, find all strings of length 5

# P2. In the words1.txt file, find all strings which end with a vowel

# P3. In the words1.txt file, find all strings have 3 non-vowels together like "cdg", or "xyz". 
# Think about using the caret.

# P4. In the words1.txt file, find all strings have 4 non-vowels together like "cdg", or "xyz". 

# P5. In the words1.txt file, split all strings on vowels

# P6. In the words1.txt file, find the number of strings with start with 'A' and end in a vowel

# P7. In the words1.txt file, replace all vowels with an '_' and write out to another file

# P8. In the words1.txt file, replace all occurences of two or more consecutive vowels by an '_'

# P9. Check if a number is a power of 2. Use bin fn and then a regex on the resulting string

# re.search v/s re.match

# re.search and re.match return a match object that can be used to get the matched sub-string for the whole pattern
# or for sub-patterns

# Groups

# Examples:

string = '39801 356, 2102 1111'
# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

print(match.group())

# Output: 801 35

print(match.group(1))

# Output: 801

print(match.group(2))

# Output: 35

# Problems
# P10. In the words1.txt file, find all strings have 3 non-vowels together like "cdg", or "xyz". 
# Print the matching string and matching sub-string

# P11. Check if a given IP address is valid and extract the network address and host address

# P12. Check if an email is valid and extract the email and domain name

# P13. Check if a phone number is correct and if it has international code (like +91), extract it.

# P14. Check is a date is in valid format of year-month-day. If yes, extract year, month and day. Also check for
# day ranges of month i.e. Feb should not have dates after 28 or 29. Bonus: Check for leap year

# Use the file webapp.log for the following:

# P15. Extract times from the log.

# P16. Find the number of requests for each hour

# P17. Make a histogram with requests per hour

# P18. Extract employee names

# P19. Find the number of requests per employee

# P20. Plot a histogram for employee v/s number of requests
