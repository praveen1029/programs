#  Define a class, which have a class parameter and have a same instance parameter.


class car:
    wheels=4
    def __init__(self,name,model_num,price):
        self.name=name
        self.model_num=model_num
        self.price=price

    def show_details(self):
        text=f"""Car Name:{self.name}
        Car Model Number:{self.model_num}
        Car Price:{self.price}"""

        print(text)


car1=car("Lamborgini",1000,2000000)
car1.show_details()