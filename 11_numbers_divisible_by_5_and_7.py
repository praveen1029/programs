# Write a program using generator to print the numbers which can be divisible by 5 and 7 
# between 0 and n in comma separated form while n is input by console.(implement generator)


def divisible(num):
    for i in range(num+1):
        if i%5==0 and i%7==0:
            yield i

exit=False
while not exit:
    option=int(input("\nChoose an option\n1.Find numbers divisible by 5 and 7\n2.Exit\n"))
    if option==1:
        num=int(input("\nEnter The upper limit:"))
        result=divisible(num)
        for i in result:
            print(i,",",end="")
    
    elif option==2:
        exit=True

    else:
        print("Invalid")