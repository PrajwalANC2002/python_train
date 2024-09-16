# Write a function to check if a string is a palindrome. Should return True if string is palindrome, else False
def is_palindrome(s):
    upper = s.upper()
    return upper == upper[::-1]

print(is_palindrome("cIvIc"))
print(is_palindrome("Civics"))
