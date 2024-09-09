class bankv1:
    branch='KOLHAPUR'
    IFSC = 'HDFC000129'
    ROI = 0.07
    def __init__(self,n,ac,mn,p,bal):
        self.name=n
        self.accno = ac
        self.mno = mn
        self.pin = p
        self.bal = bal
class bankv2(bankv1):
    def __init__(self,n,ac,mn,p,bal,add,pan,ad):
        bankv1.__init__(self,n,ac,mn,p,bal)
        self.address=add
        self.pan = pan
        self.aadhar = ad
c1 = bankv2('das',1234567890, 7082066893,1212, 50000, 'Kolhapur', "feapm34498n", 70669283839839)
print(c1.name)
print(c1.IFSC)
print(c1.pin)
print(c1.bal)
print(c1.pan)