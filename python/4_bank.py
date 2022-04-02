# Define a class named BankAccount. 
# This class should contain methods withdraw() and deposit to calculate the balance amount remained in your account

class Customer:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        self.account_num  =  None
        self.balance = 0.0

class BankAccount:  
    def __init__(self,name,place,ifsc):
        self.name = name
        self.place = place
        self.ifsc = ifsc
        self.last_acc_num = None
        self.customers = {}
        

    def generate_account_num(self):
        if self.last_acc_num is None:
            self.last_acc_num  =  1000
        else:
            self.last_acc_num += 1            
        return self.last_acc_num

    def add_customer(self,customer):      
        if isinstance(customer,Customer):
            ac_num  =  self.generate_account_num()
            customer.account_num = ac_num
            self.customers.update({ac_num:customer})
            print("Account number of",customer.name,ac_num)

        else:
            print("This is not a valid customer")

    def get_customer_by_acc_num(self,ac_num):
        return self.customers[ac_num]

    def withdraw(self,customer,amount):
        if customer.balance > amount:
            customer.balance -= amount
            print("witdraw Sucessful",customer.balance)
        else:
            print("Insufficient Balance",customer.balance)

    def deposit(self,customer,amount):
        customer.balance += amount
        print("Deposit Sucessful",customer.balance)


def create_bank():
    name = input("Enter Bank name:")
    address = input("Enter bank location:")
    ifsc = input("Enter the Ifsc code:")
    bank = BankAccount(name,address,ifsc)
    return bank


def create_customer():
    name = input("Enter Name:")
    age = int(input("Enter age:"))
    address = input("Enter address:")
    customer = Customer(name,age,address)
    return customer



# bank=create_bank()
# customer=create_customer()
# bank.add_customer(customer)
# amount=float(input("Enter amount to deposit: "))
# bank.deposit(customer,amount)
# amount=float(input("Enter an amount to be withdrawn: "))
# bank.withdraw(customer,amount)


exit = False
while not exit:
    option = int(input("\nEnter an option:\n1.Create Bank\n2.Create Customer\n3.Deposit amount\n4.Withdraw amount\n5.Exit\n"))
    if option == 1:
        bank = create_bank()

    elif option == 2:
        customer = create_customer()
        bank.add_customer(customer)
    
    elif option == 3:
            ac_num = int(input("Enter account number:"))
            amount = int(input("Enetr a amount to be deposited:"))
            customer = bank.get_customer_by_acc_num(ac_num)
            bank.deposit(customer,amount)

    elif option == 4:
            ac_num = int(input("Enter account number:"))
            amount = int(input("Enetr a amount to be withdrawn:"))
            customer = bank.get_customer_by_acc_num(ac_num)
            bank.withdraw(customer,amount)


    elif option == 5:
        exit = True

    else:
        print("Invalid")