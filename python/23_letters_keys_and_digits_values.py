# Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.
# It should return a dictionary in which the key should be letter count and value should be digit count. 
# Ignore the spaces or any other special character in the sentence.

exit=False

while not exit:
    letter_count=0
    digit_count=0
    option=int(input("\nEnter option:\n1.Create dictionary\n2.Exit\n"))
    if option==1:
        word=input("\nEnter a sentence:")
        for i in word:
            if i.isdigit()==True:
                digit_count+=1

            elif i.isalpha()==True:
                letter_count+=1

        result_dict={letter_count:digit_count}
        print("\nResult Dictionary:\n",result_dict)

    elif option==2:
        exit=True
