import random
import math
class Bank:
    def __init__(self):
        self.accounts = {}
        self.currentAccountNo = None
        self.name = None
        self.password = None
        self.initialDeposit = None
        print("\t\tWelcome from NCC Bank!!!")

    def createAccount(self,name,password,initialDeposit):
        accountNumber = random.randint(100,999)
        self.accounts[accountNumber] = [name,password,initialDeposit]
        self.beautifyPrint(f"Account created Successfully!, your account number is {accountNumber}")
        self.name = self.accounts[accountNumber][0]
        self.password = self.accounts[accountNumber][1]
        self.initialDeposit = self.accounts[accountNumber][2]
        self.currentAccountNo = accountNumber

    def beautifyPrint(self, message):
        print("---------------------------------------")
        print(message)
        print("---------------------------------------")

    def register(self):
        print("This is from registration")
        uname = input("Please enter your name to register: ")
        upassword = input("Please enter your password to register: ")
        conpassword = input("Enter password again to confirm: ")
        if upassword == conpassword:
            uamount = int(input("PLease enter your amount to register: "))
            self.createAccount(uname,upassword,uamount)
            print(self.accounts)
            print("Your current Account Number: ",self.currentAccountNo)
            print(self.allInfo())
        else:
            print("Passwords are not equal!!!")
            self.register()

    def allInfo(self):
        for x,y in self.accounts.items():
            print("Account No : ",x)
            print("Username: ",y[0])
            print("Password: ", y[1])
            print("Amount: ", y[2])
            print("*******************************")

    def authenticate(self,uname,accountNo):
        if accountNo in self.accounts.keys() and uname == self.accounts[accountNo][0]:
            return True
        else:
            return False

    def login(self):
        print("This is from login")
        laccountNo = int(input("Enter account no to login: "))
        luname = input("Enter usename to login: ")
        if self.authenticate(luname,laccountNo):
            self.beautifyPrint("Account authenticated!Login successful!")
            self.exchange()
        else:
            print("Login Fail!!!Try again!!")
            self.mainMenu()

    def exchange(self):
        print("This is from exchange option")
        while 1:
            self.allInfo()#to comment later
            print(self.accounts)
            print("Enter 1 to Withdraw")
            print("Enter 2 to Deposit")
            print("Enter 3 to transfer")
            print("Enter 4 to Display current balance")
            print("Enter 5 to update information")
            print("Enter 6 to go back")
            choice = int(input())
            if choice == 1:
                self.withdraw()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.transfer()
            elif choice == 4:
                self.displayCurrentBalance()
            elif choice == 5:
                self.updateMenu()
            elif choice == 6:
                self.mainMenu()

    def transfer(self):
        receiverAccNo = int(input("Enter account No to transfer: "))
        tAmount = int(input("Enter amount to transfer: "))
        senderAmount = self.accounts[self.currentAccountNo][2]
        print("Sender amount",senderAmount)
        receiverAmount = self.accounts[receiverAccNo][2]
        print("Receiver amount", receiverAmount)
        if senderAmount > tAmount:
            senderAmount -= tAmount
            print("Sender amount", senderAmount)
            self.accounts[self.currentAccountNo][2] = senderAmount
            print("Sender amount", senderAmount)
            receiverAmount += tAmount
            print("Receiver amount", receiverAmount)
            self.accounts[receiverAccNo][2] = receiverAmount
            print("Receiver amount", receiverAmount)
        else:
            print('Insufficient Amount to transfer!')
            self.exchange()

    def updateMenu(self):
        while 1:
            print("Enter 1 to update username")
            print("Enter 2 to update password")
            print("Enter 3 to go back")
            choice = int(input())
            if choice == 1:
                self.updateName()
            elif choice == 2:
                self.updatePassword()
            elif choice == 3:
                self.exchange()
            else:
                print("Invalid option")
                self.updateMenu()

    def updateName(self):
        newName = input("Enter your new name to update")
        self.accounts[self.currentAccountNo][0] = newName
        self.beautifyPrint("Updating Name successful!")
        print(self.allInfo())

    def updatePassword(self):
        newPassword = input("Enter your new password to update")
        self.accounts[self.currentAccountNo][1] = newPassword
        self.beautifyPrint("Updating Password successful!")
        print(self.allInfo())

    def displayCurrentBalance(self):
        print("---------------------------------------")
        print("Current Balance is", self.accounts[self.currentAccountNo][2])
        print("---------------------------------------")

    def withdraw(self):
        print("This is from withdraw option")
        withdrawAmount = int(input("Enter your withdraw amount: "))
        if self.initialDeposit < withdrawAmount:
            self.beautifyPrint("Insufficient Balance!")
        else:
            self.accounts[self.currentAccountNo][2] -= withdrawAmount
            self.beautifyPrint("Amount Withdrawal Successfull!")
            self.displayCurrentBalance()

    def deposit(self):
        print("This is from deposit option")
        depositAmount = int(input("Enter your deposit amount: "))
        self.accounts[self.currentAccountNo][2] += depositAmount
        self.beautifyPrint("Amount Deposit Successfull!")
        self.displayCurrentBalance()

    def bubbleSort(self,array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
        return array

    def jump_search(self,array, n, x):
        step = math.sqrt(n)

        prev = 0
        while array[int(min(step, n) - 1)] < x:
            prev = step
            step += math.sqrt(n)
            if prev >= n:
                return -1

        while array[int(prev)] < x:
            prev += 1
            if prev == min(step, n):
                return -1

        if array[int(prev)] == x:
            return prev
        return -1

    def search_by_acc_no(self,find_acc_no):
        keysList = list(self.accounts.keys())
        print("Testing : ",type(keysList),keysList)
        newArray = self.bubbleSort(keysList)
        print("New Sorted array: ",newArray)
        n = len(keysList)
        result = self.jump_search(newArray, n, find_acc_no)
        return result

    def mainMenu(self):
        while 1:
            print("\t\tPress 1 to Register")
            print("\t\tPress 2 to Login")
            print("\t\tPress 3 to Quit")
            print("\t\tPress 4 to search useraccount no: ")
            ch = input("\t\tPlease chose 1,2,3: ")
            if ch == '1':
                self.register()
            elif ch == '2':
                self.login()
            elif ch == '3':
                print("Bye Bye")
                exit(1)
            elif ch == '4':
                find_acc_no = int(input("Enter account no to search: "))
                result = self.search_by_acc_no(find_acc_no)
                if result == -1:
                    print("Element not found")
                else:
                    print("Number", find_acc_no, "is at index", "%.0f" % result)
            else:
                print('Invalid option')
                self.mainMenu()

if __name__ == "__main__":
    bank = Bank()
    bank.mainMenu()


