# Define a class to represent an Account
class Account:
    #This line defines a special method called the constructor (__init__).
     #the constructor is called automatically whenever a new Account object is created.
    def __init__(self, account_number, pin, balance, transaction_history=[]):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = transaction_history

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def withdraw_cash(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds. Your current balance is ₹{self.balance}.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ₹{amount}")
            print(f"₹{amount} has been withdrawn. Your new balance is ₹{self.balance}. \nThankyou!")

    def deposit_cash(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
            return
        self.balance += amount
        self.transaction_history.append(f"Deposit: ₹{amount}")
        print(f"₹{amount} has been deposited. Your new balance is ₹{self.balance}.")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect old PIN. Please try again.")
        else:
            self.pin = new_pin
            print("Your PIN has been changed successfully.")

    def view_transaction_history(self):
        if not self.transaction_history:
            print("You don't have any transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Create a dictionary to store accounts 
accounts = {
    123451: Account(123451, 123, 1000),
    123452: Account(123452, 124, 2000),
    123453: Account(123453, 456, 50000),
    123454: Account(123454, 116, 2000),
    123455: Account(123455, 198, 21000),
    123456: Account(123456, 965, 89000),
    123457: Account(123457, 324, 63000),
    123458: Account(123458, 544, 2500),
    123459: Account(123459, 129, 7500),
    
}

#This is an ATM simulation. We will check account details and allow transactions.

def atm_simulation():
    print("\nWelcome to the ATM!")

    while True:
        account_number = int(input("Enter your account number: "))

        # Validate account number (optional, assuming accounts dictionary exists)
        if account_number not in accounts:
            print("Invalid account number. Please try again.")
            continue

        account = accounts[account_number]  # Get the Account object for the entered number

        pin = int(input("Enter your PIN: "))

        if pin != account.pin:
            print("Incorrect PIN. Please try again.")
            continue

        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        
         #Loop to keep performing transactions for the same account

        while choice != 6:  # Loop for multiple transactions
            if choice == 1:
                account.check_balance()
            elif choice == 2:
                withdrawal_amount = int(input("Enter amount to withdraw: "))
                account.withdraw_cash(withdrawal_amount)
            elif choice == 3:
                deposit_amount = int(input("Enter amount to deposit: "))
                account.deposit_cash(deposit_amount)
            elif choice == 4:
                old_pin = int(input("Enter your old PIN: "))
                new_pin = int(input("Enter your new PIN: "))
                account.change_pin(old_pin, new_pin)
            elif choice == 5:
                account.view_transaction_history()
            else:
                print("Invalid choice. Please try again.")
            
            #you can choose another transaction for same account,enter number from 1 to 5 for another transaction,6 for exit.
            choice = int(input("Do another transaction? Enter choice: (Yes) or 6 (Exit): "))

        # Exit message
        if choice == 6:
            print("Thank you for using the ATM. Have a nice day!")
            break

# Start the ATM simulation
atm_simulation()






