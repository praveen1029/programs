# Write a program to print the prime numbers between given interval.

start=int(input("Enter the starting number:"))
end=int(input("Enter the last number:"))
if start>1 and end>1:
    for i in range(start,end+1):  
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
elif start<end:
    print("Start should be greater than end")
else:
    print("Invalid")
        