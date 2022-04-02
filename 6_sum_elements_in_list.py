# Write a program to find the sum of all the elements in a list

exit=False

a_list=[]
sum=0
while not exit:
    choose=int(input("\nChoose option:\n1.Create List\n2.Find sum of element in list\n3.Exit\n"))
    if choose==1:
        end=False
        while not end:
            choice=int(input("\nchoose option:\n1.Enter an element\n2.Exit\n"))
            if choice==1:
                element=int(input("\nEnter the element:"))
                a_list.append(element)
            elif choice==2:
                print("List=",a_list)
                end=True
                continue
            else:
                print("\nInvalid")

    elif choose==2:
        for i in a_list:
            sum+=i
        print("Sum of elements:",sum)

    elif choose==3:
        exit=True

    else:
        print("Invalid")