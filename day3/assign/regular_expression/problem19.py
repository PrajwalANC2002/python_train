# P19. Find the number of requests per employee
import re

def number_of_req_per_emp(filename):
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
        print("name: ",count)  
        print(" no of requests",names_dict[count])

number_of_req_per_emp("webapp.log")
