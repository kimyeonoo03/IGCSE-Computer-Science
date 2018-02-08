def leap_year(year):
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

years = [230,1999,2018,4096,1986,2020,512,2054,1837,1945,1360,3000,2048,1066,4,930,1024,32]
for x in years:
    if x < 2018:
        leap_year(x)
        if leap_year(x):
            print (x, "was a leap year.")
        else:
            print (x, "was not a leap year.")
    elif x == 2018:
        leap_year(x)
        if leap_year(x):
            print (x, "is a leap year.")
        else:
            print (x, "is not a leap year.")
    else:
        leap_year(x)
        if leap_year(x):
            print (x, "will be a leap year.")
        else:
            print (x, "won't be a leap year.")

import random
numyear = []
for i in range(1, 11):
    num = random.randint(1, 10000)
    numyear.append(num)

for x in numyear:
    if x < 2018:
        leap_year(x)
        if leap_year(x):
            print (x, "was a leap year.")
        else:
            print (x, "was not a leap year.")
    elif x == 2018:
        leap_year(x)
        if leap_year(x):
            print (x, "is a leap year.")
        else:
            print (x, "is not a leap year.")
    else:
        leap_year(x)
        if leap_year(x):
            print (x, "will be a leap year.")
        else:
            print (x, "won't be a leap year.")
