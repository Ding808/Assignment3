class Bank:
    def openAccount(self):
        Bank.user1 = ["111","A", 0.1, 10, 15]#saving and checquing
        Bank.user2 = ["112","A", 0.1, 10, 15]
        Bank.user3 = ["113","A", 0.1, 10, 15]
        Bank.user4 = ["114","A", 0.1, 10, 15]
        Bank.user5 = ["115","A", 0.1, 10, 15]
        print("",Bank.user1,"\n", Bank.user2, "\n", Bank.user3, "\n", Bank.user4, "\n",Bank.user5,)
        Bank.search = [Bank.user1[0],Bank.user2[0],Bank.user3[0],Bank.user4[0],Bank.user5[0]]
        Bank.search1 = [Bank.user1,Bank.user2,Bank.user3,Bank.user4,Bank.user5]
        Bank.AccountNumber = input("Please type in your correct account number")
        return Bank.user1,Bank.user2,Bank.user3, Bank.user4, Bank.user5
    def searchAccount(self):
        ii = -1
        while True:
            for i in Bank.search:
                ii = ii+1
                if i == Bank.AccountNumber:
                    user = Bank.search1[ii]
                    self.Number = user[0]
                    self.Name = user[1]
                    self.interest = user[2]
                    self.balance = user[3]
                    self.Balance = user[4]
                    global pp
                    pp = Account(int(self.Number), self.Name, self.interest, self.balance, self.Balance)
                    break
            break
            
class Account:
    def __init__(self, number, name, interest, balance, Balance):
        self._accountNumber = number
        self._accountHolderName = name
        self._rateOfInterest = interest
        Account._currentBalance = float(balance)
        Account._CurrentBalance = float(Balance)

    def getAccountNumber(self):
        return self._accountNumber

    def getAccountHolderName(self):
        return self._accountHolderName

    def getRateOfInterest(self):
        return self._rateOfInterest
    
    def getCurrentBalance(self):
        return Account._currentBalance

    def getChecquingBalance(self):
        return Account._CurrentBalance
    
    def deposit(self,deposit):
        Account._currentBalance = Account._currentBalance+deposit
        return Account._currentBalance
    
    def withdraw(self,Withdraw):
        Account._currentBalance = Account._currentBalance-Withdraw
        return Account._currentBalance


    def Deposit(self,deposit):
        Account._CurrentBalance = Account._CurrentBalance+deposit
        return Account._CurrentBalance

    def Withdraw(self,Withdraw):
        Account._CurrentBalance = Account._CurrentBalance-Withdraw
        return Account._CurrentBalance


class SavingAccount(Account):
    def __init__(self):
        self._minimumBalance = 5000
    def withdraw(self,num):
        aa = super().withdraw(num)
        if aa < self._minimumBalance:
            print("You can't withdraw that much money")
            print(super().withdraw(-num))
        else:
            print("Your current balance is: ",aa)

class ChecquingAccount(Account):
    def __init__(self):
        self._overAllowed = 5000
    def Withdraw(self,num):
        a = super().Withdraw(num)
        if a < (self._overAllowed - self._overAllowed*2):
            print("You can't withdraw that much money")
            super().Withdraw(-num)
        else:
            print("Your current balance is: ",a)
    
def run():
    global o
    showAccountMenu()
    Bank().searchAccount()
    showMainMenu()
    while True:
        o = input ("What do you you want to do? \n").upper()
        if o == "change".upper():
            run1()
        elif o == "check checquing balance".upper():
            print(pp.getChecquingBalance())
        elif o == "check saving balance".upper():
            print(pp.getCurrentBalance())
        elif o == "exit".upper():
            break
        
        
def run1():
    while True:
        Input = input("Which account you want to change? Checquing or Saving? \n").upper()
        if Input == "Checquing".upper():
            while True:
                p = input("Withdraw or Deposit? \n").upper()
                if p == "Withdraw".upper():
                        m = input ("How much you want to withdraw? \n")
                        ChecquingAccount().Withdraw(float(m))
                        return
                elif p == "Deposit".upper():
                    while True:
                        m = input ("How much you want to deposit? \n")
                        pp.Deposit(float(m))
                        return
                p = ""
                m = ""
        elif Input == "Saving".upper():
            while True:
                p = input("Withdraw or Deposit? \n").upper()
                if p == "Withdraw".upper():
                        m = input ("How much you want to withdraw? \n")
                        SavingAccount().withdraw(float(m))
                        return
                elif p == "Deposit".upper():
                    while True:
                        m = input ("How much you want to deposit? \n")
                        pp.deposit(float(m))
                        return
                p = ""
                m = ""
        



def showMainMenu():
    print("""\033[91m\033[1mType: "change" to deposit or withdraw money
Type: "check checquing balance" to check your checquing balance
Type: "check saving balance" to check you saving balance\033[0m""")

def showAccountMenu():
    Bank().openAccount()

run()

