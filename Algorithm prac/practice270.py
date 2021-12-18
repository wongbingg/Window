import random

class Account():

    account_count = 0

    def __init__ (self,name,balance):
        self.deposit_count = 0
        self.deposit_log=[]
        self.withdraw_log=[]

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_num = num1 + '-' + num2 +'-'+num3
      
        Account.account_count += 1
    @classmethod    
    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self,amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01


    def withdraw(self,amount):
        if amount <= self.balance:
            self.withdraw_log.append(amount)
            self.balance -= amount


    def display_info(self):
        print("은행이름: {}".format(self.bank))
        print("예금주: {}".format(self.name))
        print("계좌번호: {}".format(self.account_num))
        print("잔고: {0:,}원".format(self.balance))

    def deposit_history(self):
        print(self.deposit_log)
    def withdraw_history(self):
        print(self.withdraw_log)


lee = Account("이원빈",1000000)
lee.deposit(10000)
lee.withdraw(5000)
lee.deposit(15000)
lee.withdraw(6000)
lee.deposit(60000)
lee.withdraw(4500)

lee.deposit_history()
lee.withdraw_history()




