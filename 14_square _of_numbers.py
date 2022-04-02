# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30

sqr_list=[]
res_list=[]
i=0
for i in range(2,30):
    sqr_list.append(i**2)
print("list=",sqr_list)
print("First five numbers=",sqr_list[0:5])
print("last five numbers=",sqr_list[-1:-6:-1])
