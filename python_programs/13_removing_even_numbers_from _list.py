# Write a Python program to print the numbers of a specified list after removing even numbers from it
exit=False
end=False
a_list=[]
b_list=[]
i=0
while not exit:
    choose=int(input("\nChoose option:\n1.Create List\n2.Print list\n3.Exit\n"))
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
        for i in a_list:
            if i%2!=0:
                b_list.append(i)
        print(b_list)
    
    elif choose==3:
        exit=True

    else:
        print("Invalid")