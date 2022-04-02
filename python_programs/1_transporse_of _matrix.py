# Write a program to find the transpose of a matrix


outer_list=[]
result_list=[]
a=1
exit=False
while not exit:
    option=int(input("Enter option:\n1.Input Matrix\n2.Find Transpose of Matrix\n3.Exit\n"))
    if option ==1:
        row=int(input("Enter number of rows:"))
        column=int(input("Enter number of column:"))
        while a<=row:
            print("Enter Row ",a,":\n")
            a+=1
            b=1
            inner_list=[]
            while b<=column:
                x=int(input("Enter Element :"))
                inner_list.append(x)
                b+=1
            outer_list.append(inner_list)
            print("Inputed Matrix:\n")
        for i in outer_list:
            print(i)
    elif option==2:

        for i in range(row):
            temp_list=[]
            for j in range(column):
                temp_list.append(outer_list[j][i])
            result_list.append(temp_list)


        print("\n Transpose of the given matrix:\n")
        for i in result_list:
            print(i)

    elif option==3:
        exit=True

    else:
        print("Invalid")