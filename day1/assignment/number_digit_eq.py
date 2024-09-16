# Write a function which takes two arguments, 'n' and 'ndigits'. If 'n' has 'n' digits return True else False.

def digit_count_eq(n,ndigits):
    if(ndigits == len(str(n))):
        return True
    else:
        return False

print(digit_count_eq(1234,4))
print(digit_count_eq(123,4))
print(digit_count_eq(123,2))
