# 3. Extend the dictionary months for other months and the iterate over it to print all the months
# with 31 days
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
for i in months:
    if(months[i] == 31):
        print(i)
