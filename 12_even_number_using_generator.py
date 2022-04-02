#  Write a program using generator to print the even numbers 
# between 0 and n in comma separated form while n is input by console.(implement generator)

def even(num):
    for i in range(num):
        if i%2==0:
            yield i


exit=False
while not exit:
    option=int(input("\nChoose an option\n1.Find even numbers \n2.Exit\n"))
    if option==1:
        num=int(input("\nEnter The upper limit:"))
        result=even(num)
        for i in result:
            print(i,",",end="")
    
    elif option==2:
        exit=True

    else:
        print("Invalid")