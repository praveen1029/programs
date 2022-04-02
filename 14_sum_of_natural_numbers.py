# Write a program to find the sum of n' Natural Numbers
num=int(input("Enter a number:"))
sum=0
for i in range(num+1):
    sum+=i
print("sum of numbers:",sum)