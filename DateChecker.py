# This program inputs a date in dd/mm/yyyy format and outputs whether the date is valid or not
# Also checks if the date is in a leap year

# Ask for input for the day, month and year in numerical values
day = int(input("Enter a day (as a number - in date format): "))
month = int(input("Enter a month (as a number - in date format): "))
year = int(input("Enter a year (in the year digits): "))       

# Checks for dates from day 1 to 30 (applicable to all months, except February)
if (day > 0 and day <= 30):
    if (month > 0 and month <= 12) and month != 2:
        if year > 0:
            if year % 4 == 0:
                if year % 400 == 0:
                    print(day,month,year,"is a valid date and",year,"is a leap year.")
                elif year % 100 == 0:
                    print(day,month,year,"is an valid date but",year,"is not a leap year.")
                else:
                    print(day,month,year,"is a valid date and",year,"is a leap year.")
            else:
                print(day,month,year,"is a valid date but",year,"is not a leap year.")
        else:
            print(day,month,year,"is an invalid date.")
    # February(month 2) is an exception, checks for day 30 and 29 separately
    elif (month == 2):
        if day == 30:
            print(day,month,year,"is an invalid date.")
        elif day == 29:
            if year > 0:
                if year % 4 == 0:
                    if year % 400 == 0:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                    elif year % 100 == 0:
                        print(day,month,year,"is an invalid date because",year,"is not a leap year.")
                    else:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                else:
                    print(day,month,year,"is an invalid date because",year,"is not a leap year.")
            else:
                print(day,month,year,"is an invalid date.")
        elif day > 0 and day <= 28:
            if year > 0:
                if year % 4 == 0:
                    if year % 400 == 0:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                    elif year % 100 == 0:
                        print(day,month,year,"is an valid date but",year,"is not a leap year.")
                    else:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                else:
                    print(day,month,year,"is a valid date but",year,"is not a leap year.")
            else:
                print(day,month,year,"is an invalid date.")    
    else:
        print(day,month,year,"is an invalid date.")
# Checks for day 31
elif (day == 31):
    if (month >= 1 and month <= 7):
        if month % 2 == 1:
            if year > 0:
                if year % 4 == 0:
                    if year % 400 == 0:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                    elif year % 100 == 0:
                        print(day,month,year,"is an valid date but",year,"is not a leap year.")
                    else:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                else:
                    print(day,month,year,"is a valid date but",year,"is not a leap year.")
            else:
                print(day,month,year,"is an invalid date.")
        else:
            print(day,month,year,"is an invalid date.")
    elif (month >= 8 and month <= 12):
        if month % 2 == 0:
            if year > 0:
                if year % 4 == 0:
                    if year % 400 == 0:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                    elif year % 100 == 0:
                        print(day,month,year,"is an valid date but",year,"is not a leap year.")
                    else:
                        print(day,month,year,"is a valid date and",year,"is a leap year.")
                else:
                    print(day,month,year,"is a valid date but",year,"is not a leap year.")
            else:
                print(day,month,year,"is an invalid date.")
        else:
            print(day,month,year,"is an invalid date.")
    else:
        print(day,month,year,"is an invalid date.")
else:
    print(day,month,year,"is an invalid date.")
        
            
                                              
            

            