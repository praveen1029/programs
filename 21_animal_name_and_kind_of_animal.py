# Create a dictionary to hold information about pets.
# Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}
# Put at least 3 key-value pairs in your dictionary.
# Use a for loop to print out a series of statements such as "Willie is a dog."

exit=False 

while not exit:
    option=int(input("\nEnter option:\n1.Create a Dictionary\n2.Exit\n"))
    a_dict={}
    if option==1:
        end =False
        while not end:
            choose=int(input("\nEnter option:\n1.Enter into the dictionary\n2.print data\n3.Exit\n"))
            if choose==1:
                key=input("Enter the key:")
                value=input("Enter the corresponding value:")
                a_dict.update({key:value})

            elif choose==2:
                if len(a_dict)<3:
                    print("Insufficent Data")
                    continue
                else:
                    for keys,values in a_dict.items():
                        print("\n")
                        print(values," is a ",keys)

            elif choose==3:
                end=True
                break

            else:
                print("Invalid")

    elif option==2:
        exit=True

    else:
        print("Invalid")

