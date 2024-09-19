# P14. Check is a date is in valid format of year-month-day. If yes, extract year, month and day. Also check for
# day ranges of month i.e. Feb should not have dates after 28 or 29. Bonus: Check for leap year
import re

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def check_date_format(date):
    date_pattern = re.compile(r"^(\d{4})\-(\d{2})\-(\d{2})$",date)

    date_pattern_check = date_pattern.match(date)

    if(date_pattern_check):
        year = date_pattern_check.group(1)
        month = date_pattern_check.group(2)
        day = date_pattern_check.group(3)
        
        if(0 <= int(month) <= 12):

            day_in_months = [0, 31, 28 + is_leap_year(int(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if(1 <= int(day) <= day_in_months[int(month)]):
                print("Valid date :",year + "-" + month + "-" + day)
            else:
                print(month+" month does not have " + " correct day "+ day)
        
        else:
            print("invalid month value please provide between  1 - 12")
    
    else:
        print("invalid date format please provide in YYYY-MM-DD format")

check_date_format("2002-04-24")
check_date_format("hfif-hd-hd")
check_date_format("24-04-2002")
check_date_format("@@@@-@@-@@")
check_date_format("2024-02-29")
check_date_format("2023-02-29")
check_date_format("2023-14-29")
check_date_format("2024-09-35")



