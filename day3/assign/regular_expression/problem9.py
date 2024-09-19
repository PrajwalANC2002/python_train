# P9. Check if a number is a power of 2. Use bin fn and then a regex on the resulting string
#
import re
def check_num_is_power_of_2(n):
    binary_number = bin(n)
        return True
    if(re.search(r"^10*$",binary_number[2:])):
    else:
        return False

print(check_num_is_power_of_2(0))
print(check_num_is_power_of_2(2))
print(check_num_is_power_of_2(10))
print(check_num_is_power_of_2(1024))
print(check_num_is_power_of_2(1023))
print(check_num_is_power_of_2(65536))
print(check_num_is_power_of_2(1))
print(check_num_is_power_of_2(5))
