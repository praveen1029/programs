# Program to implement Linear-Search Algorithm


def l_search(a_list,num):
    count=0
    for i in a_list:
        count+=1
        if i==num:
            return count
    else:
        return 0        


exit=False
while not exit:
    a_list=[]
    option=int(input("\nChoose option:\n1.Perform linear search\n2.Exit\n"))
    end=False
    if option==1:
        while not end:
            choose=int(input("\nChoose option\n1.Enter into list\n2.Perform Seach\n3.Exit\n"))
            if choose==1:
                element=int(input("\nEnter element into list:"))
                a_list.append(element)

            elif choose==2:
                print("\nThe list\n",a_list)
                num=int(input("Enter the number to be searched:"))
                result=l_search(a_list,num)
                if result==0:
                    print("\nElement Not found\n")
                else:
                    print("\nThe Element is present at position ",result)

            elif choose==3:
                end=True

            else:
                print("Invalid")

    elif option==2:
        exit=True

    else:
        print("Invalid")


