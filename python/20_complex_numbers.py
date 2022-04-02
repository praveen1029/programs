# Program to perform Addition,Subtraction,Multiplication and division on Complex-No's

option=input("Enter option:\n1.Addition\n2.Substraction\n3.Multipilcation\n4.Division\n")
first= complex(input("Enter of first complex number:"))
second=complex(input("Enter of second complex number:"))

if option == "Addition" or option=="addition" or option=="1":
    sum=first +second
    print(sum)

elif option == "substraction" or option=="Substraction" or option=="2":
    sum=first -second
    print(sum)

elif option=="Multiplication" or option=="multiplication" or option=="3":
    sum=first*second
    print(sum)

elif option=="division" or option=="Division" or option=="4":
    sum=first/second
    print(sum)
else:
    print("invalid")