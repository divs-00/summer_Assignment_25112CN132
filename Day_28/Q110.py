"""
PROBLEM STATEMENT:
Write a program to Create bank account system.
"""

class BankAccount:

    """Represents an individual bank account.
       This class stores the account holder's details, unique account number, 
       and handles financial operations like deposits, withdrawals, and balance lookups."""

    def __init__(self, account_number, name, initial_deposit):
    
        self.account_number = account_number
        
        self.name = name
        
        self.balance = initial_deposit


    def deposit(self, amount):
    
        """Deposits a positive amount into the account.
           Validates that the input amount is greater than zero."""
           
        if amount <= 0:
        
            print("\nError: Deposit amount must be positive.")
            
            return
            
        self.balance += amount
        
        print(f"\nSuccessfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")


    def withdraw(self, amount):
    
        """Withdraws a specific amount from the account if funds are sufficient.
           Ensures the account does not go into a negative balance."""
           
        if amount <= 0:
        
            print("\nError: Withdrawal amount must be positive.")
            
            return
            
        if amount > self.balance:
        
            print(f"\nError: Insufficient funds. Available Balance: ${self.balance:.2f}")
            
            return
            
        self.balance -= amount
        
        print(f"\nSuccessfully withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")


    def display_details(self):
    
        """Prints the current account details including the number, name, and total balance."""
        
        print(f"Account No: {self.account_number} | Holder: {self.name} | Balance: ${self.balance:.2f}")


class BankSystem:

    """Manages multiple bank accounts using a structural registry.
       It uses a dictionary for account storage to ensure lightning-fast operations.
       The time complexity for creating an account, finding an account, and processing 
       transactions is O(1) on average."""

    def __init__(self):
    
        self.accounts = {}


    def create_account(self, account_number, name, initial_deposit):
    
        """Registers a brand new bank account into the system.
           Prevents creation if the provided account number already exists."""
           
        if account_number in self.accounts:
        
            print(f"\nError: Account number {account_number} already exists.")
            
            return
            
        if initial_deposit < 0:
        
            print("\nError: Initial deposit cannot be negative.")
            
            return
            
        new_account = BankAccount(account_number, name, initial_deposit)
        
        self.accounts[account_number] = new_account
        
        print(f"\nAccount created successfully for {name}!")


    def get_account(self, account_number):
    
        """Retrieves an account object based on its account number.
           Returns None if the account number is not found in the database."""
           
        if account_number not in self.accounts:
        
            print("\nError: Account not found.")
            
            return None
            
        return self.accounts[account_number]


bank = BankSystem()

bank.create_account("1001", "Alice Smith", 500.0)

bank.create_account("1002", "Bob Jones", 1200.50)

while True:

    print("\n==============================")
    
    print("      BANK ACCOUNT SYSTEM")
    
    print("==============================")
    
    print("1. Create New Account")
    
    print("2. Deposit Money")
    
    print("3. Withdraw Money")
    
    print("4. Check Account Balance")
    
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == "1":
    
        acc_num = input("Enter a new account number: ")
        
        name = input("Enter account holder name: ")
        
        try:
        
            initial_amount = float(input("Enter initial deposit amount: "))
            
            bank.create_account(acc_num, name, initial_amount)
            
        except ValueError:
        
            print("\nError: Invalid monetary input.")
            
    elif choice == "2":
    
        acc_num = input("Enter your account number: ")
        
        account = bank.get_account(acc_num)
        
        if account:
        
            try:
            
                amount = float(input("Enter amount to deposit: "))
                
                account.deposit(amount)
                
            except ValueError:
            
                print("\nError: Invalid monetary input.")
                
    elif choice == "3":
    
        acc_num = input("Enter your account number: ")
        
        account = bank.get_account(acc_num)
        
        if account:
        
            try:
            
                amount = float(input("Enter amount to withdraw: "))
                
                account.withdraw(amount)
                
            except ValueError:
            
                print("\nError: Invalid monetary input.")
                
    elif choice == "4":
    
        acc_num = input("Enter your account number: ")
        
        account = bank.get_account(acc_num)
        
        if account:
        
            print("\n--- Account Details ---")
            
            account.display_details()
            
    elif choice == "5":
    
        print("\nThank you for using our banking system. Goodbye!")
        
        break
        
    else:
    
        print("\nInvalid choice. Please enter a number between 1 and 5.")