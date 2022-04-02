# Write a Python program to insert a given string at the beginning of all items in a list. 

exit=False
end=False
a_list=[]
while not exit:
    choose=int(input("\nChoose option:\n1.Create list\n2.print list\n3.Exit\n"))
    if choose==1:
        while not end:
            choice=int(input("\nchoose option:\n1.Enter an element\n2.Exit\n"))
            if choice==1:
                element=input("\nEnter the elment:")
                a_list.append(element)
            elif choice==2:
                print("List=",a_list)
                end=True
                continue
            else:
                print("Invalid")
    
    elif choose==2:
        n=len(a_list)
        word=input("\nEnter the word to be inserted into the begning of elemets in list:")
        for i in range(n):
            
            x=word+a_list[i]
            a_list.pop(i)
            a_list.insert(i,x)
        print(a_list)
    elif choose==3:
        exit=True

    else:
        print("Invalid")   