# Write a program to find the factorial of the given number.

num=int(input("Enter a number:"))
sum=1
for i in range(1,num+1):
    sum*=i
print("factorial of number",sum)