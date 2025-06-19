# Bank account with classes
# Can withdraw
# Can deposit
# Can view balance

class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"The {amount} was deposited, the balance is {self.__balance}")
        else:
            print("Amount have to be positive!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"The {amount} was withdrawed, the balance is {self.__balance}")
        else:
            print("Insufficient balance or amount!")
    
    def __str__(self):
        return f"The balane is {self.__balance}"

def main():
    print("Welcome to the Bank")
    name = input("Enter the name: ")
    try:
        balance = int(input("Enter balance: "))
    except ValueError:
        print("Please enter a valid number")
    account = BankAccount(name, balance)
    while True:
        print("1. Withdraw")
        print("2. Deposit")
        print("3. View balance")
        print("4. Exit")
        print()
        try:
            choice = int(input("Choose a number:"))
            print()
            if choice == 1:
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Please enter a valid number")
            elif choice == 2:
                try:
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Please enter a valid number")
            elif choice == 3:
                print(account)
                print()
            elif choice == 4:
                break
            else: 
                print("Please enter a valid number")
        except ValueError:
            print("Please enter a valid number")
        

if __name__ == "__main__":
    main()
