# Write a program to  Determine If Year Is Leap Year

num=int(input("Enter the year to check:"))

if num%4==0 and num%100!=0 and num%400!=0:
    print("The year is a leap year")
    
else:
    print("The year is not a leap year")