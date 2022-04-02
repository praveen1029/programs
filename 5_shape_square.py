# Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default


class Shape:
    def area(self):
        print("Area=",0) 

class Square(Shape):
    def __init__(self,length):
        self.length=length

    def area(self):
        print("Area=",self.length**2)

exit=False
while not exit:
    option=int(input("\nEnter a choice:\n1.Find area\n2.Exit\n"))
    if option==1:
        choice=int(input("\nEnter a choice:\n1.Area of shape\n2.Area of square\n"))
        if choice==1:
            a=Shape()
            a.area()

        elif choice==2:
            length=int(input("Enter lenth of a side of square:"))
            b=Square(length)
            b.area()

        else:
            print("Invalid")

    elif option==2:
        exit=True

    else:
        print("Invalid")