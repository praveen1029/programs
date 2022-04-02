# Write a program to calculate the area and perimeter of a rectangle

len=int(input("Enter the length of Rectangle:"))
bre=int(input("Enter the breadth of rectangle"))
word=input("Enter option:\n1.Area\n2.Perimeter\n")
if word=="Area" or word=="area" or word=="1":
    area = len*bre
    print("Area of rectangle:",area)

elif word=="Perimeter" or word=="perimeter" or word=="2":    
    peri= 2*(len+bre)
    print("Perimeter of rectangle:",peri)
else:
    print("Invalid")