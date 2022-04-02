# Write a program to implement Dictionary Comprehension
b_dict={"num1":10,"num2":15,"num3":20,"num4":25,"num5":30,"num6":35,"num7":13}

a_dict={key:value for key,value in b_dict.items()  if value>20}

print(a_dict)