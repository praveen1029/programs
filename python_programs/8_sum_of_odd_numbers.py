# Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers
x=0
for i in range(1,50):
    if i%2!=0:
        print(i)
        x+=i
print("Sum of odd numbers between 1 and 50:",x)