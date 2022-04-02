# Write a program to print the fibonocci series
num=int(input("Enter number of digits:"))
x=0
y=1
sum=1
for i in range(num):
    print(sum)
    sum=x+y
    x=y
    y=sum