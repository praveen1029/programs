# Write a Python program to iterate over two lists simultaneously
a_list=[]
b_list=[]
exit=False
end_first=False
end_second=False
while not exit:
    option=int(input("Enter option:\n1.Input First List\n2.Input Second list\n3.Print list\n4.Exit\n"))
    if option ==1:
        while not end_first:
            choose=int(input("Enter Choice:\n1.Enter Element into list\n2.Exit\n"))
            if choose==1:
                a_list.append(input("Enter Element:"))
            elif choose==2:
                end_first=True
            else:
                print("Invalid")
        print("First list:\n",a_list)


    elif option ==2:
        while not end_second:
            choose=int(input("Enter Choice:\n1.Enter Element into list\n2.Exit\n"))
            if choose==1:
                b_list.append(input("Enter Element:"))
            elif choose==2:
                end_second=True
            else:
                print("Invalid")

        print("Second list:\n",b_list)   
           

    elif option==3:
        print("Result List:\n")
        for i in zip(a_list,b_list):
                print(i)

    elif option==4:
        exit=True

    else:
        print("Invalid")