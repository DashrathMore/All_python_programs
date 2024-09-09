class Bank1:
    bankname= 'HDFC'
    branch="Kolhapur"
    IFSC = 'HDFC000129'
    ROI = 0.07
    def __init__(self,name,mno,accno,bal,pin):
        self.cname=name
        self.mno = mno
        self.accno=accno
        self.bal = bal
        self.pin=pin
    def checkbal(self):
        if self.pin == int(input("enter pin")):
            print (self.bal)
        else:
            print('incorrect pin')
class Bank2(Bank1):
    def __init__(self,name,mno,accno,bal,pin,acctyp,pan,aad):
        Bank1.__init__(self,name,mno,accno,bal,pin)
        self.acctype = acctyp
        self.pan = pan
        self.aadhar = aad
class Bank3(Bank2):
    def __init__(self, name, mno, accno, bal, pin, acctyp, pan, aad,mail,nom1,nom2):
        super(). __init__(name,mno,accno,bal,pin,acctyp,pan,aad)
        self.mail=mail
        self.nominee1 = nom1
        self.nominee2 = nom2
c1 = Bank3('DAS',7083066893, 501000000398978, 20000, 1221, 'SAVING', 'FEAPM9090L', 123445455985954, 'd@gmail.com', 'BHAGAVANT', 'MAYA')
print(c1.ROI)
print(c1.IFSC)
print(c1.cname)
print(c1.mno)
print(c1.bal)
print(c1.acctype)
print(c1.mail)
print(c1.nominee1)
print(c1.nominee2)
c1.checkbal()