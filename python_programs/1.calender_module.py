# 1. Programs to implement the concept of calendar module.

import calendar

exit = False
while not exit:
    choose = int(input("Enter option\n1.Print calandar of a year\n2.print calanedar of a moth in a year\n3.Exit\n"))
    if choose == 1:
        year = int(input("Enter the year:"))
        print(calendar.calendar(year))

    elif choose == 2:
        year = int(input("Enter the year:"))
        month = int(input("Enter the month:"))
        print(calendar.month(year,month))

    elif choose == 3:
        exit = True

    else:
        print("Invalid")