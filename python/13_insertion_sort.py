# Write a program to implement Insertion-Sort algorithm in python


def i_sort(a_list):
    length=len(a_list)
    for i in range(1,length):
        count=i
        if a_list[i]<a_list[i-1]:
            temp=a_list[i]
            for j in range(i):
                if a_list[count-1]>temp:
                    a_list[count]=a_list[count-1]
                    count-=1
            else:
                a_list[count]=temp
        

    return a_list


exit=False
while not exit:
    a_list=[]
    option=int(input("\nChoose option:\n1.Perform Insertion sort\n2.Exit\n"))
    end=False
    if option==1:
        while not end:
            choose=int(input("\nChoose option\n1.Enter into list\n2.Perform sort\n3.Exit\n"))
            if choose==1:
                element=int(input("\nEnter element into list:"))
                a_list.append(element)
                
                
            elif choose==2:
                print("\nThe list before sort\n",a_list)
                result=i_sort(a_list)
                print("\nThe sorted List ",result)
                end=True

            elif choose==3:
                end=True

            else:
                print("Invalid")

    elif option==2:
        exit=True

    else:
        print("Invalid")

