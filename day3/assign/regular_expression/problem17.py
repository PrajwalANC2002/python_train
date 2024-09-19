# P17. Make a histogram with requests per hour
#
import re

def histogram_for_each_hour(filename):

    pattern = re.compile(r"(\d{2}):(\d{2}):(\d{2}\.\d{6})")

    hour_freq = {}

    with open(filename,"r") as my_file:
        for line in my_file:
            pattern_check = pattern.search(line)
            count = pattern_check.group(1)
            if(count in hour_freq):
                hour_freq[count] += 1
            else:
                hour_freq[count] = 1
    
    for count in sorted(hour_freq):
        print("hour:",count+"#"*hour_freq[count])

histogram_for_each_hour("webapp.log")
