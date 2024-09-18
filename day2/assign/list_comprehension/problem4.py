# Write a list comprehension for getting all the months with number of days equal to 30
months = {"jan": 31,
          "feb": 28,
          "mar": 31,
          "apr": 30,
          "may": 31,
          "june": 30,
          "july": 31,
          "aug": 31,
          "sep": 30,
          "oct": 31,
          "nov": 30,
          "dec": 31}

check_month_30_days = [month for month in months if(months[month] == 30)]

print(check_month_30_days)
