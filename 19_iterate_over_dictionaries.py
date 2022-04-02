# Write a Python program to iterate over dictionaries using for loop


exit=False

a_dict={}
while not exit:
    option=int(input("\nChoose option:\n1.Create dictionary\n2.Exit\n"))
    if option==1:
        end=False
        while not end:
            choose=int(input("\nChoose option:\n1.Enter element\n2.print Dictionary\n3.Exit\n"))
            if choose==1:
                key=input("Enter the key:")
                value=input("Enter the corresponding value:")
                a_dict.update({key:value})
            elif choose==2:
                for keys,values in a_dict.items():
                    print("\n")
                    print(values,keys)

            elif choose==3:
                end=True

            else:
                print("Invalid")

    elif option==2:
        exit=True

    else:
        print("Invalid")

