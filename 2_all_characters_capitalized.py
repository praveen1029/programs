# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

exit=False
new_word=''
while not exit:
    option=int(input("\nEnter option:\n1.Capitalize Given Input\n2.Exit\n"))
    if option ==1:
        word=input("\nEnter a string:")
        for i in word:
            if i.isalpha()==True:
                i=i.capitalize()
                new_word+=i
            else:
                new_word+=i
        print("\n Result String:\n",new_word)

    elif option==2:
        exit=True
