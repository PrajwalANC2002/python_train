# 5. Find the number of upper case letters in the company name.
company = "Mirafra Software Technologies Pvt. Ltd."
count = 0;
for i in company:
    if( i >= "A" and i <= "Z"):
        count = count +1
print(count)

