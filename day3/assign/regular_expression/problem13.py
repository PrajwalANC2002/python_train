# P13. Check if a phone number is correct and if it has international code (like +91), extract it.
import re

def check_phone_no_and_extract(phone_no):

    phone_no_pattern_check = re.match(r"^\+?(\d{2})?[-]?(\d{10})$",phone_no)

    if(phone_no_pattern_check):
        
        phone_number_check = phone_no_pattern_check.group(2)
        international_code_check = phone_no_pattern_check.group(1)
        
        if(international_code_check):
            print("valid phone number and international code =",international_code_check)
        else:
            print("valid phone number but international code is not present")

        print("phone number =",phone_number_check)
    else:
        print("invalid phone number format")

check_phone_no_and_extract("+91-8088932647")
check_phone_no_and_extract("-**0hdjjdjdddd")
check_phone_no_and_extract("+91*9945431145")
check_phone_no_and_extract("+91-fjfjfjfjfj")
check_phone_no_and_extract("8088932647")
        

