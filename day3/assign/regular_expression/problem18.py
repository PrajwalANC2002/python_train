# P18. Extract employee names
import re

def extract_employee_name(filename):
    pattern = re.compile(r"e:(( \w*){1,})")

    names_dict = {}

    with open(filename,"r") as my_file:
        for line in my_file:
            pattern_check = pattern.search(line)
            count = pattern_check.group(1)
            if(count in names_dict):
                names_dict[count] += 1
            else:
                names_dict[count] = 1

    for count in sorted(names_dict):
        print("name:",count)

extract_employee_name("webapp.log")
