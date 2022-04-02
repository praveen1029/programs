# Write a program to find whether given no. is Armstrong or not

num=int(input("Enter a number:"))
i=num
sum=0
while i!=0:
    n=i%10
    sum+=(n**3)
    i=int(i/10)
if num==sum:
    print("The number is Armstrong Number")
else:
    print("The number is not Armstrong Number")
    