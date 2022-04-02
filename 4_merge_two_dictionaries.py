# Write a program to read dictionary values through keyboard and merge two dictionaries

exit=False
result_dict={}
b_dict={}
a_dict={}
while not exit:
    option=int(input("\nChoose option:\n1.Create dictionary\n2.Print merged Dictionary\n3.Exit\n"))
    if option==1:
        choice=int(input("\nChoose option:\n1.Dictionary 1\n2.Dictionary 2\n"))
        if choice==1:
            end=False
            while not end:
                choose=int(input("\nChoose option:\n1.Enter element\n2.Exit\n"))
                if choose==1:
                    key=input("Enter the key:")
                    value=input("Enter the corresponding value:")
                    a_dict.update({key:value})

                elif choose==2:
                    print("Dictionary 1=\n",a_dict)
                    end=True
                
                else:
                    print("Invalid")

        elif choice==2:
            end=False
            while not end:
                choose=int(input("\nChoose option:\n1.Enter element\n2.Exit\n"))
                if choose==1:
                    key=input("Enter the key:")
                    value=input("Enter the corresponding value:")
                    b_dict.update({key:value})

                elif choose==2:
                    print("Dictionary 2=\n",b_dict)
                    end=True
                
                else:
                    print("Invalid")

    elif option==2:
        result_dict.update(a_dict)
        result_dict.update(b_dict)          
        print("\n Merged Dictionary=\n",result_dict)      

    elif option==3:
        exit=True

    else:
        print("Invalid")