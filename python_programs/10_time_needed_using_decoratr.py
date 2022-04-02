# Program to implement concept of decorator 
# to calculate the time needed to execute one or more function in a program.



from time import time
  
  
def validate(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print('Function executed in' ,(t2-t1),"time")
        return result
    return wrapper
  
@validate
def sum(n):
    num=0
    for i in range(1,n):
        num+=i
    print("sum of numbers:",num)

n=int(input("Enter a number:"))
sum(n)