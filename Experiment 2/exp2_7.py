#Display the next date of the calendar
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if day < 30:
    day += 1
else:
    day = 1
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print("Next Date:", day, "/", month, "/", year)
