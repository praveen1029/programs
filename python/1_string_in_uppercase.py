# Define a class which has at least two methods one, to get a string from console  input 
# and other is to print the string in uppercase.


class Uppercase:
    def __init__(self,word):
        self.word=word


    def convert(self):
        new_word=self.word.upper()
        print(new_word)

exit=False
while not exit:
    option=int(input("\nChoose opton:\n1.Convert to uppercase\n2.Exit\n"))
    if option==1:
        word=input("Enter a string:")
        obj=Uppercase(word)
        obj.convert()

    elif option==2:
        exit=True

    else:
        print("Invalid")