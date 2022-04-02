#  Write a program to define a function that can accept an integer number as input 
# and print the "It is an even number" if the number is even, otherwise print "It is odd"


def is_even(a):
    if a%2==0:
        return True

    else:
        return False
exit=False
while not exit:
    option=int(input("\nChoose an opton:\n1.Check Even or Odd Number\n2.Exit\n"))
    if option==1:
        num=int(input("Enter a Number:"))
        result=is_even(num)
        if result==True:
            print("The number is even")

        else :
            print("The number is odd")

    elif option==2:
        exit=True

    else:
        print("Invalid")