# Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)

exit= False
a_list=[]
def rm_vowels(word):
    new_word=""
    vowel_list=['a','e','i','o','u','A','E','I','O','U']
    for i in word:
        for j in vowel_list:
            if i==j:
                break
        else:
            new_word+=i

    return new_word

while not exit:
    option=int(input("Choose option:\n1.Remove vowels from string\n2.Exit\n"))
    if option==1:
        word=input("Enter a string:")   
        a_list=[rm_vowels(word)]
        print(a_list)

    elif option==2:
        exit=True

    else:
        print("Invalid")