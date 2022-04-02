# Write a program to implement all built-in methods of list

a_list=[1,2,"hello","world",3.5]
c_list=a_list.copy()
print(a_list)
print("print(a_list)=",a_list)
print("c_list=a_list.copy()=",c_list)
print(id(a_list))
print("print(id(a_list))=",a_list)
print(id(c_list))
print("print(id(c_list))=",a_list)
a_list.append("tuesday")
print("a_list.append('tuesday')=",a_list)
a_list.insert(5,"world")
print("a_list.insert(5,'world')=",a_list)
a_list.remove("hello")
print("a_list.remove('hello')=",a_list)
num=a_list.count("world")
print("num=a_list.count('world')=",a_list)

print(len(a_list))
print("print(len(a_list))=",a_list)
