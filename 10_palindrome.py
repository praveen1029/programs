# Write a program to Check if the given string  is Palindrome or not
word=input("Enter a string:")
word=word.upper()
l=len(word)
new_word=word[::-1]
if word==new_word:
    print("String is a palindrome")
else:
    print("String is not palindrome")
