# P12. Check if an email is valid and extract the email and domain name
#
import re
def validate_email_and_extract(email):
    email_pattern = re.compile(r"([\w+_\.-]+)@([\w+_\.-]+\.[\w+_\.-]+)")

    email_pattern_check = email_pattern.match(email)

    if(email_pattern_check):
        print("valid email")
        print("email =",email_pattern_check.group(1))
        print("domain name=",email_pattern_check.group(2))
    else:
        print("invalid email please check again")


validate_email_and_extract("abc@gmail.com")
validate_email_and_extract("_.+ZZZAAAaaazzz999000@yahoo.com")
validate_email_and_extract("xyz@gmail.edu")
validate_email_and_extract("***@###.^^^")

