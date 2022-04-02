# With a given integral number n, write a program to generate a dictionary that contains(i,i*i) 
# such that i is an integral number between 1 and n. 
# And then the program should print the dictionary

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
            for i in range(1,n):
                a_dict.update({i:i*i})
        print("\nThe result dictionary:\n",a_dict)
    elif option==2:
        exit=True

