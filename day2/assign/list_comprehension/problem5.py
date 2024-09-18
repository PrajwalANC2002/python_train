# Write a list comprehension for all the months that start with 'j'
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

check_month_start_with_j = [month for month in months if(month[0] == "j")]

print(check_month_start_with_j)
