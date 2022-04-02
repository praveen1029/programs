#Write a program to implement List Comprehension
exit=False
end=False
while not exit:
    choice =int(input("Choose option:\n1.Enter the range of numbers\n2.Print Even numbers\n3.Print Odd numbers\n4.Exit\n"))
    if choice==1:
        start=int(input("Enter starting number:"))
        end=int(input("Enter ending number:"))
    elif choice==2:
        even=[x for x in range(start,end+1) if x%2==0]
        print("List containing Even numbers=",even)       
    elif choice==3:
        odd=[x for x in range(start,end+1) if x%2!=0]
        print("List containing odd numbers=",odd)
    elif choice==4:
        exit=True
    else:
     print("Invalid")
