'''
Parent Classes >
1.Holds the details about an user
2.has a function to show user details

Child Classes >

1.Stores details about account balance
2.Stores details about the amount
3.Allows for deposites,withdraw,view_balance
'''

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_user_details(self):
        print("Personal Information >\n")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age,gender)
        self.balance = 0
    
    def deposite(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account details are updated -> $",self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance | current balance -> $",self.balance)
        else:
            self.balance -= self.amount
            print("Account details are updated -> $",self.balance)
    
    def view_balance(self):
        self.show_user_details()
        print("Account balance is -> $",self.balance)

a = Bank("Gabb4r",20,"Male")

a.withdraw(1000)

a.deposite(1000)

a.withdraw(300)

a.view_balance()