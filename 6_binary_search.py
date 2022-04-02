# Program to implement binary-Search Algorithm

def asending(a_list):
    '''function To check if the inputed list is sorted or not'''
    for i in range(len(a_list)-1):
        if (a_list[i]>a_list[i+1]):
            return 0
    else:
        return 1

def b_search(a_list,num):
    """function for binary search"""
    count=0
    length=len(a_list)
    middle=int(length/2)
    if num<a_list[middle]:
        for i in range(0,middle):
            count+=1
            if a_list[i]==num:
                return count
    elif num>a_list[middle]:
        for i in range(middle,length):
            count+=1
            if a_list[i]==num:
                return count+middle

    elif num==a_list[middle]:
        return middle+1
    else:
        return 0        


exit=False
while not exit:
    a_list=[]
    option=int(input("\nChoose option:\n1.Perform binary search\n2.Exit\n"))
    end=False
    if option==1:
        while not end:
            choose=int(input("\nChoose option\n1.Enter into list\n2.Perform Search\n3.Exit\n"))
            if choose==1:
                element=int(input("\nEnter element into list:"))
                a_list.append(element)

            elif choose==2:
                n=asending(a_list)
                if n==0:
                    a_list=[]
                    print("The list must be a sorted list")
                    continue
                elif n==1:
                    print("\nThe list\n",a_list)
                    num=int(input("Enter the number to be searched:"))
                    result=b_search(a_list,num)
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


