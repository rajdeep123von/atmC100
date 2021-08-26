import time
import random
import decimal
class atm:
    def __init__(self,cardNumber,pin,StartingBalance=None):
        self.cardNumber = cardNumber
        self.pin = pin
        if StartingBalance == None:
            StartingBalance = 1000
            self.balance = StartingBalance
            print("\n──────────────────────𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐒𝐢𝐠𝐧-𝐔𝐩 𝐏𝐨𝐫𝐭𝐚𝐥──────────────────────\nSince you have not entered the default amount of your bank account,\nWe have deposited ₹1000 by default :)\nCurrent balance: ₹",self.balance,"\n")

        else:    
            self.StartingBalance = StartingBalance
            self.balance = StartingBalance
            print("\n──────────────────────𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐒𝐢𝐠𝐧-𝐔𝐩 𝐏𝐨𝐫𝐭𝐚𝐥──────────────────────\nBravo! You have created your bank account!\nCurrent balance: ₹",self.balance,"\n")
        
        self.loanLimit = StartingBalance*5
        self.Dloan = 0
        self.Wloan = 0
        self.Cloan = 0
        self.rTime = 12
        self.rRate = 3
        self.DivideRate = 100

    
    def CashWithdrawal(self,Wcash=None):
        if Wcash == None:
            Wcash = 0
        print("\n────────────────────𝐂𝐚𝐬𝐡 𝐖𝐢𝐭𝐡𝐝𝐫𝐚𝐰 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────")
        if Wcash<self.balance:
            print("Cash Withdrawed: ₹",Wcash,"\nRemaining balance: ₹",self.balance-Wcash,"\n")  
            self.balance = self.balance-Wcash 
            
        elif Wcash == self.balance:
            print("All Cash Withdrawed: ₹",Wcash,"\nRemaining balance: ₹",self.balance-Wcash,"\n")  
            self.balance = self.balance-Wcash 

        elif Wcash>self.balance:
            print("Invalid amount!\nInsufficient balance: ₹",self.balance-Wcash,"\nRemaining balance: ₹",self.balance,"\n")  
           
    def DepositCash(self,Dcash=None):
        if Dcash == None:
            Dcash = 0
        print("\n────────────────────𝐂𝐚𝐬𝐡 𝐃𝐞𝐩𝐨𝐬𝐢𝐭 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────")
        if Dcash>=0:
            print("Cash deposited: ₹",Dcash,"\nRemaining balance: ₹",self.balance+Dcash,"\n")
            self.balance = self.balance+Dcash   
        else:
            print("Invalid value!","\nPlease type a positive value.\nRemaining balance: ₹",self.balance,"\n")
        
    def WithdrawAllCash(self):
        print("\n────────────────────𝐂𝐚𝐬𝐡 𝐖𝐢𝐭𝐡𝐝𝐫𝐚𝐰 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────\nWithdrawed all cash from bank: ₹",self.balance,"\nRemaining balance: ₹",self.balance-self.balance,"\n")
        self.balance = self.balance-self.balance  
    
    def BalanceEnquiry(self):
        print("\n────────────────────𝐁𝐚𝐥𝐚𝐧𝐜𝐞 𝐄𝐧𝐪𝐮𝐢𝐫𝐲 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────\nYour current bank balance: ₹",self.balance,"\n")

    def LoanEnquiry(self):
        print("\n────────────────────𝐋𝐨𝐚𝐧 𝐄𝐧𝐪𝐮𝐢𝐫𝐲 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────\nYour current loan dues: ₹:",self.Cloan,"\nYour current Loan Limit: ₹",self.loanLimit,"\n")

    def WithdrawLoan(self,wloan=None):
        if wloan == None:
            wloan = 0
        self.Wloan=wloan
        print("\n────────────────────𝐋𝐨𝐚𝐧 𝐄𝐧𝐪𝐮𝐢𝐫𝐲 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────")
        self.Dloan = int(decimal.Decimal(wloan+(self.Wloan*self.rTime*self.rRate/self.DivideRate)))
        
        if self.Dloan>self.balance or self.Dloan==self.balance:
            print("The Loan is not approved!\nPlease enter a lesser amount to approve the loan.\nRemaining Loan Limit: ₹",self.loanLimit,"\n")
            self.Wloan=0
            self.Dloan = 0
        elif self.Dloan == 0 or self.Wloan ==0:
            print("The Loan is not approved!\nPlease enter some value!\nRemaining Loan Limit: ₹",self.loanLimit,"\n")
            self.Wloan=0
            self.Dloan = 0
        elif self.Cloan != 0:
            print("The Loan is not approved!\nPlease return the previous loan of ₹",self.Cloan,"\nRemaining Loan Limit: ₹",self.loanLimit,"\n")
            self.Wloan=0
            self.Dloan= 0
            return
        elif self.Dloan<self.balance and self.Cloan == 0:
            self.loanLimit =self.loanLimit-self.Wloan
            print("Your loan of ₹",self.Wloan,"is approved at a rate of interest",self.rRate,"%\nReturn the loan with the applied interest: ₹", self.Dloan,"\n\nRemaining Balance: ₹",self.balance+self.Wloan,"\nRemaining Loan Limit: ₹",self.loanLimit,"\n")
            self.balance = self.balance+self.Wloan
            self.loanLimit =self.loanLimit-self.Wloan
            self.Cloan = self.Dloan
    
    def ReturnLoan(self,rLoan=None):
            #time.sleep(rTime)            
            #sLoan = str(self.Dloan)
            print("\n────────────────────𝐋𝐨𝐚𝐧 𝐄𝐧𝐪𝐮𝐢𝐫𝐲 𝐏𝐨𝐫𝐭𝐚𝐥────────────────────")
           # self.Dloan = int(self.Wloan*self.rTime*self.rRate/self.DivideRate)
            if rLoan == None:
                rLoan =0
            #self.loanLimit = self.loanLimit+ self.Dloan
            
            if 0<rLoan<self.Cloan:
                self.Cloan = self.Cloan-rLoan
                self.balance = self.balance-rLoan
                self.loanLimit=self.loanLimit+rLoan
                print("Loan returned: ₹",rLoan,"\nRemaining Loan to be returned: ₹",self.Cloan,"\nRemaining Balance: ₹",self.balance,"\nRemaining Loan Limit: ₹",self.loanLimit,"\n")
            elif rLoan ==0:
                print("Please enter a value!\nRemaining Loan to be returned: ₹",self.Cloan,"\nRemaining Balance: ₹",self.balance,"\nRemaining Loan Limit: ₹",self.loanLimit,"\n")   
                return
            elif self.Cloan<rLoan or rLoan<0:
                print("Please enter a valid amonut!\nRemaining Loan to be returned: ₹",self.Cloan,"\nRemaining Balance: ₹",self.balance,"\n")
                return
            elif rLoan == self.Cloan:
                self.Cloan = self.Cloan-rLoan
                self.balance = self.balance-rLoan
                self.loanLimit=self.loanLimit+rLoan

                print("Loan returned successfully: ₹",rLoan,"\nRemaining Loan to be returned: ₹",self.Cloan,"\nRemaining Balance: ₹",self.balance,"\nRemaining Loan Limit: ₹",self.loanLimit,"\n")

p1= atm(200,200)
p1.CashWithdrawal()
p1.BalanceEnquiry()
p1.DepositCash()
p1.LoanEnquiry()
#p1.WithdrawLoan(2000)
p1.WithdrawLoan(100)
#
#p1.WithdrawAllCash()
p1.ReturnLoan(136)

p1.WithdrawLoan(333)
p2= atm(200,200,50000)
p2.LoanEnquiry()
p2.WithdrawLoan(1000)
p2.ReturnLoan(1100)