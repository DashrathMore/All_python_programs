class Bank:
    BankName = 'HDFC'
    branch = 'Marthahalli'
    IFSC = 'HDFC000129'
    Roi = 0.07
    def __init__(self,nm,mno,acc,bal,pin):
        self.name=nm
        self.mono=mno
        self.accno=acc
        self.bal=bal
        self.pin=pin
    def checkbal(self):
        if(self.pin==self.getpin()):
            print(f'{self.name} in his avaliable balance is {self.bal}')
        else:
            print('INCORRECT PIN !!!')
    def withdraw(self):
        if (self.pin == self.getpin()):
            amt = int(input('ENTER WITHDRAW AMOUNT :'))
            if self.bal >= amt:
                self.bal-=amt
            else:
                print('INSUFFICIENT BALANCE !!!')
        else:
            print('INCORRECT PIN !!!')
    def deposit(self):
        if (self.pin == self.getpin()):
            amt= int(input('ENTER DEPOSIT AMOUNT : '))
            self.bal+=amt
        else:
            print('INCORRECT PIN !!!')
    @classmethod
    def ROI(self):
        r = float(input('ENTER NEW ROI :'))
        self.Roi= r
    @staticmethod
    def getpin():
        return int(input('ENTER 4 DIGIT PIN : '))

c1=Bank('dashrath',7083066893,50100000013994,30000,1221)
c2=Bank('ram',4090930942,501009343433434,20000,3434)
c3=Bank('sam',2930930923,501000002312131,10000,9090)
c3.withdraw()
c3.checkbal()
c3.deposit()
c3.checkbal()

