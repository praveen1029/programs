# Write a program to  generate following pyramid or triangle like  given below using for loop.
num=int(input("Enter number of rows:"))

if num%2==0:
    n=int(num/2)
    x=n
    for i in range(n+1):
        print("*"*i)

    for i in range (n):  
             
        print("*"*x)
        x-=1


else:
    n=int(num/2)
    n+=1
    x=n
    for i in range(n+1):
        print("*"*i)

    for i in range (n):  
        x-=1     
        print("*"*x)
        