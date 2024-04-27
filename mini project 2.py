class Bank_Account:
    def __init__(self,account_number,account_holder,account_balance=0):
        self.account_number=account_number
        self.account_balance=account_balance
        self.account_holder=account_holder
    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount should be greater than zero")
        else:
            self.account_balance+=amount
            print(f"{amount} deposited successfully. New balance:{self.account_balance}")
    def withdraw(self,amount):
        if amount<=0:
            print("Withdrawal amount should be greater than zero")
        elif amount>self.account_balance:
            print("Insufficient Bank Balance")
        else:
            self.account_balance-=amount
            print(f"{amount} withdrawn. New Balance: {self.account_balance}")
    def account_details(self):
        print(f"Account NUmber :{self.account_number}")
        print(f"Acount Holder :{self.account_holder}")
        print(f"Account Balance :{self.account_balance}")
class Bank_System:
    def __init__(self):
        self.account={}
        self.current_account=None
    def create_account(self,account_number,account_holder):
        if account_number in self.account:
            print("Account already exists ")
        else:
            account=Bank_Account(account_number,account_holder)
            self.account[account_number]=account
            print(f"Account is successfully created for {account_holder}. Account Number :{account_number}")
    def login(self,account_number):
        if account_number not in self.account:
            print("Acconut not found ")
        else:
            self.current_account=self.account[account_number]
            print(f" Logged into the account {account_number}")
    def logout(self):
        if self.current_account:
            print(f" Logged out from acconut {self.current_account}")
            self.current_account= None
        else:
            print("No current login ")
    def deposit_amount(self,amount):
        if self.current_account:
            self.current_account.deposit(amount)
        else:
            print("Please log in to an account first")

    def withdraw_amount(self, amount):
        if self.current_account:
            self.current_account.withdraw(amount)
        else:
            print("Please log in to an account first")

    def account_details(self):
        if self.current_account:
            self.current_account.account_details()
        else:
            print("Please log in to an account first")
def main():
    bank_system=Bank_System()
    while True:
        print("1.Create Account")
        print("2.Login")
        print("3.Logout")
        print("4.Deposit Amount")
        print("5.Withdraw Amount")
        print("6.View Account Details")
        print("7.Exit")
        choice=int(input("Enter  your choice :"))
        if choice==1:
            account_number=input("enter the account number :")
            account_holder=input("enter acconut holder name :")
            bank_system.create_account(account_number,account_holder)
        elif choice==2:
            account_number=input("enter the account number :")
            bank_system.login(account_number)
        elif choice==3:
            bank_system.logout()
        elif choice==4:
            amount=float(input("enter the amount to be deposited :"))
            bank_system.deposit_amount(amount)
        elif choice==5:
            amount=float(input("enter the amonut to withdraw :"))
            bank_system.withdraw_amount(amount)
        elif choice==6:
            bank_system.account_details()
        elif choice==7:
            print("exiting")
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()
                        
    
     
            
            
            
        
