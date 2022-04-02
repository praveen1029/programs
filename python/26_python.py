# Write a python function to add ‘python’ at the end of a given string and return the new string. 
# If the given string already ends with ‘python’ then add ‘java’. 
# If the length of the given string is less than 5, then add ‘php’.

word=input("Enter a string:")
new_word=word.upper()
n=len(word)
if n>=5:

    if new_word[n-6:n]=="PYTHON":
        word += " Java"
    else:
        word+=" python"
else:
    word+=" php"

print("New string:",word)