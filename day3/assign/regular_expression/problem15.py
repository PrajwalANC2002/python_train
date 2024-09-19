# P15. Extract times from the log.

import re

def extract_time_from_log(filename):
    pattern = re.compile(r"\d{2}:\d{2}:\d{2}\.\d{6}")

    with open(filename,"r") as my_file:
        for line in my_file:
            pattern_check = pattern.search(line)
            print(pattern_check.group())


extract_time_from_log("webapp.log")


