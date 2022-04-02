#Write a program to print fibonocci series using recursion

exit=False
def fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibonacci(n-1) + fibonacci(n-2))  

while not exit:
    option=int(input("\nChoose option:\n1.Print fibonocci Series\n2.Exit\n"))
    if option==1:

        terms = int(input("\nEnter number of terms:"))   
        if terms <= 0:  
            print("Enter a positive Number")  
        else:  
            print("Fibonacci series:")  
            for i in range(terms):  
                print(fibonacci(i))  
    

    elif option==2:
        exit=True

    else:
        print("Invalid")