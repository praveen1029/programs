#  Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) 
# and the values are square of keys.

a_dict={}
exit=False
while not exit:
    option=int(input("\nChoose option:\n1.Create dictionary\n2.Exit\n"))
    if option==1:
        n=int(input("\nEnter the limit:"))
        if n<=1:
            print("\nInvalid limit\n")
            continue
        else:
            for i in range(1,n+1):
                a_dict.update({i:i**2})
        print("\nThe result dictionary:\n",a_dict)
    elif option==2:
        exit=True

