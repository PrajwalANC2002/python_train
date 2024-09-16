# Write a function to print all the months with 'n' days
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
def print_month_with_n_days(n):
    for i in months:
        if(months[i] == n):
            print(i)

print_month_with_n_days(28)

print_month_with_n_days(31)
