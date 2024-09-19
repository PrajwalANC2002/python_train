# P11. Check if a given IP address is valid and extract the network address and host address
import re
def validate_and_extract_ip_address(ip_address):
    ip_pattern_check = re.match(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})",ip_address)

    if(ip_pattern_check):
        first_3_digit = ip_pattern_check.group(1)
        second_3_digit = ip_pattern_check.group(2)
        third_3_digit = ip_pattern_check.group(3)
        fourth_3_digit = ip_pattern_check.group(4)

        if((0 <= int(first_3_digit) <= 255) and (0 <= int(second_3_digit) <= 255) and (0 <= int(third_3_digit) <= 255) and (0 <= int(fourth_3_digit) <=255) ):
            print("network address =",first_3_digit + "." + second_3_digit + "." + third_3_digit)
            print("host address = ",fourth_3_digit)
        else:
            print("invalid ip address")

    else:
        print("invalid ip address format enter the correct format")


validate_and_extract_ip_address("192.255.1.10")
