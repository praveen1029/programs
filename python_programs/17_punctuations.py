# Write a program to remove all punctuations from given string

word=input("Enter a string:")
new_word=""
for i in word:
    if i=="!" or i=="?" or i=="@" or i=="#" or i=="$" or i=="(" or i==")" or i=="%" or i=="&":
        continue
    else:
        new_word+=i
print(new_word)
