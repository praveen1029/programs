# Write a program to demonstrate all built-in methods of dictionary

a_dict={"name1":"abi","name2":"zack","name3":"manu","num1":1,"num2":26,"num3":13,"num4":13}
print("Dictionary=\n",a_dict)

a_dict.update({"name4":"biju"})
print("Update Dictionary=\n",a_dict)


a_dict.pop("name3")
print("Pop/Remove a random element from Dicitionary=\n",a_dict)

x=a_dict.keys()
print("Print Keys Of Dictionary Elements=\n",x)
print("Print Values Of Dictionary Elements=\n",a_dict.values())
print("Print key Values pairs Of Dictionary=\n",a_dict.items())

