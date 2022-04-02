# Write a program that accepts a sentence and calculate the number of letters & digits

exit=False
while not exit:
    letter_count=0
    digit_count=0
    option=int(input("\nEnter option:\n1.Obtain Count\n2.Exit\n"))
    if option==1:
        word=input("\nEnter a sentence:")
        for i in word:
            if i.isdigit()==True:
                digit_count+=1

            elif i.isalpha()==True:
                letter_count+=1

        print("\nNumber of Letters:",letter_count)
        print("\nNumber of Digits:",digit_count)

    elif option==2:
        exit=True
