# Write a program to find the factorial of a number using recursion
exit=False
def fact(num):
    if num<=1:
        return num

    else:
        return num*fact(num-1)

while not exit:
    option=int(input("\nChoose option:\n1.find Factorial of a Number\n2.Exit\n"))
    if option==1:

        num= int(input("\nEnter the Number:"))   
        if num <= 0:  
            print("Enter a positive Number")  
        else:  
            result=fact(num)
            print("Factorial of Number:\n",result)  
            
    
    elif option==2:
        exit=True

    else:
        print("Invalid")
