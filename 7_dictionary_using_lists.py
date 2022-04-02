# Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.


result_dict={}

exit=False
while not exit:
    option=int(input("\nChoose an option:\n1.Enter List\n2.Print Dictionary\n3.Exit\n"))
    if option==1:       
        choice=int(input("\nChoose:\n1.List 1\n2.List 2\n"))
        end=False
        if choice==1:
            a_list=[]
            while not end:
                choose=int(input("\nChoose option:\n1.Enter an Element into list\n2.Exit\n"))
                if choose==1:
                    element=input("\nEnter Element:")
                    a_list.append(element)
                elif choose==2:
                    print("List 1=",a_list)
                    end=True
                else:
                    print("Invalid")

        elif choice==2:
            b_list=[]
            while not end:
                choose=int(input("\nChoose option:\n1.Enter an Element into list\n2.Exit\n"))
                if choose==1:
                    if len(a_list)>len(b_list):
                        element=input("\nEnter Element:")
                        b_list.append(element)

                    else:
                        print("\nBoth list Should be of Equal Length")

                elif choose==2:
                    if len(a_list)>len(b_list):
                        print("\nBoth list Should be of Equal Length")

                    else:
                        print("List 2=",b_list)
                        end=True

                else:
                    print("Invalid")
        
        else:
            print("Invalid")
    elif option==2:
        print(a_list)
        print(b_list)
        for key,value in zip(a_list,b_list):
            result_dict.update({key:value})
        print("Dictionary=\n",result_dict)

    elif option==3:
        exit=True

    else:
        print("Invalid")
        
