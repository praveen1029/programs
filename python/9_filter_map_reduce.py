# Write a program to implement filter(), map() and reduce()

from functools import reduce

exit =False
def is_vowel(word):
    a_list=['A','E','I','O','U']
    for i in a_list:
        if word.upper()==i:
            return True
            break

    else:
        return False


def is_prime(n):
    for num in range(2,n+1):
        if n%num==0:
            return False

        else:
            return True


def mul(a,b):
    return a*b

while not exit:
    option=int(input("\nEnter option:\n1.Map\n2.Filter\n3.Reduce\n4.Exit\n"))
    if option==1:
        print("\nProgram to find a charcter is vowel or not in a given string\n")
        word=input("Enter a string:")
        vowel_obj=map(is_vowel,word)
        print(vowel_obj)
        for vowel in vowel_obj:
            print(vowel)

    elif option==2:
        print("\nProgram to print prime numbers in a given range\n")
        lower=int(input("\nEnter the lower limit:"))
        upper=int(input("\nEnter the upper limit:"))
        if lower<=1:
            print("Invalid range")

        else:
            number=range(lower,upper+1)
            prime_obj=filter(is_prime,number)
            print(prime_obj)
            for num in prime_obj:
                print(num)

    elif option==3:
        print("\nProgram to obtain the multiplicative sum of numbers in a given range\n")
        lower=int(input("\nEnter the lower limit:"))
        upper=int(input("\nEnter the upper limit:"))
        nums=range(lower,upper+1)
        reduce_obj=reduce(mul,nums)
        print(reduce_obj)

    elif option==4:
        exit=True

    else:
        print("Invalid")