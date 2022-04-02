# Write a program to display Powers of 2  using Anonymous functions?(lambda,map)


exit=False

while not exit:
    option=int(input("\nChoose option:\n1.Print Series\n2.Exit\n"))
    if option==1:
        n=int(input("\nEnter Number of limit:"))
        num=range(n)
        map_obj=map(lambda num:2**num,num)
        for i in map_obj:
            print(i)
    elif option==2:
        exit=True

    else:
        print("Invalid")