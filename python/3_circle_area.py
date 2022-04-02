# Define a class named Circle which can be constructed by radius. 
# The Circle class has a method which can compute the area


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def circle_area(self):
        area=3.14*self.radius**2
        print(area)


exit=False
while not exit:
    option=int(input("\nChoose opton:\n1.Find Area of circle\n2.Exit\n"))
    if option==1:
        num=int(input("Enter the radius of the circle:"))
        obj=Circle(num)
        obj.circle_area()

    elif option==2:
        exit=True

    else:
        print("Invalid")