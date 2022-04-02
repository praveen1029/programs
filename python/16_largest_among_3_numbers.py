# Write a program to find the largest among 3 numbers

one=int(input("Enter the first number:"))
two=int(input("Enter the secomd number:"))
three=int(input("Enter the third number:"))
if one>two and one>three:
    temp=one
elif one==two and one>three:
    temp=one
elif one==two and one<three:
    temp=three
elif one==three and one>two:
    temp=one
elif one==three and one<two:
    temp=two


elif two>one and two>three:
    temp=two
elif two==three and one>two:
    temp=one
elif two==three and one<two:
    temp=two
elif three>one and three>two:
    temp=three

elif one==two and one==three and two==three:
    temp=one
print("Largest number:",temp)