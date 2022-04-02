# Write a program to count the no:of each vowel in a given string.

word=input("Enter the string:")
count=0
for i in word:
    if i=="a" or i=="A":
        count+=1
    elif i=="e" or i=="E":
        count+=1
    elif i=="i" or i=="I":
        count+=1
    elif i=="o" or i=="O":
        count+=1
    elif i=="u" or i=="U":
        count+=1

print("Number of vowels:",count)