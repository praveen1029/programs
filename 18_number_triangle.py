# Write a program to  Display number Triangle 
num=int(input("Enter number of rows:"))
n=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(n,end=" ")
    print()
    n+=1
           