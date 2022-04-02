# Write a python function to create and return a new dictionary from the given dictionary (subject: mark).
# Create a new dictionary with subject having marks more than 50.

marks = {'English': 40,'Maths': 60, 'Hindi': 30,'Chemistry': 46,'Physics': 70}
print("Dictionary:\n",marks)
new_mark={}
for key,value in marks.items():
    if value>50:
        new_mark.update({key:value})

print("new dictionary with subject having marks more than 50=\n",new_mark)