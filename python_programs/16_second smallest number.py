# Write a Python program to find the second smallest number in a list using function

def small_num(a_list):
    '''function to find smallest umber in list'''
    temp=a_list[0]
    for i in a_list:
        if temp>i:
            temp=i 
    return temp


def sec_small_num(a_list):
    """functon to find second smallest number in list"""
    num=small_num(a_list) 
    for i in a_list:
        if i!=num:
            b_list.append(i)
    temp=b_list[0]
    for i in b_list:
        if i!=num:
            if num<i and i<=temp:
                temp=i
    return temp


b_list=[]

exit=False
while not exit:
    option=int(input("\nChoose an option:\n1.Enter List\n2.Print Second smallest number\n3.Exit\n"))
    if option==1:       
        end=False
        a_list=[]
        while not end:
            choose=int(input("\nChoose option:\n1.Enter an Element into list\n2.Exit\n"))
            if choose==1:
                element=input("\nEnter Element:")
                a_list.append(element)
            elif choose==2:
                print("List =\n",a_list)
                end=True
            else:
                print("Invalid")

    elif option==2:

        result=sec_small_num(a_list)

        print("The Second Smallest Number is ",result)

    elif option==3:
        exit=True

    else:
        print("Invalid*-")