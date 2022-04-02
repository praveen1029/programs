# Write a Python script to concatenate following dictionaries to create a new one

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
print("dictionary 1=",dic1)
print("dictionary 2=",dic2)
print("dictionary 3=",dic3)
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print("Combibed Dictionary:\n",dic4)
