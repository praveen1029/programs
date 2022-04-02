# Write a program to define a function which can print a dictionary 
# where the keys are numbers between 1 and 20 (both included) and the values are square of keys.


def dictionary(num):
    a_dict.update({num:num**2})

    return a_dict


a_dict={}
for num in range(1,21):
    a_dict=dictionary(num)

print("result dictionary=\n",a_dict)