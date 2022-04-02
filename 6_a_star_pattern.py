# Write a program to  generate following pyramid or triangle like  given below using for loop.
num=int(input("Enter number of rows:"))
n=num
for i in range(num):
    print("*"*n)
    n-=1