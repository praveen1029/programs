# Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.
x=0
for i in range(100,200):
    if i%7==0:
        x+=i
print("Sum of odd numbers between 100 and 200 divisible by 7:",x)