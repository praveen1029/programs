#  Write a program to find the largest and smallest element from a list

exit=False
end=False
a_list=[]
while not exit:
    choose=int(input("\nChoose option:\n1.Create List\n2.Find Largest element\n3.Find smallest element\n4.Exit\n"))
    if choose==1:
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
        large=a_list[0]
        for i in a_list:
            for j in a_list:
                if i>j:
                    if i>large:
                        large=i
        print("\nThe largest element in list:",large)

    elif choose==3:
        small=a_list[0]
        for i in a_list:
            for j in a_list:
                if i<j:
                    if i<small:
                        small=i
        print("\nThe smallest element in list:",small)


    elif choose==4:
        exit=True

    else:
        print("\nInvalid")