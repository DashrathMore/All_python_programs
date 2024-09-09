class company:
    cname = 'WIPRO'
    code = 'wipro000122'
    office = 'mumbai'
class b1(company):
    branch = 'bangaluru'
    bcode = 'wipro012'
class b2(company):
    branch = 'mumbai'
    bcode = 'wipro01'
ob = b2()
ob1 = b1()
print(ob.cname,ob.office,ob.branch,ob.bcode)
print(ob1.cname,ob1.office,ob1.branch,ob1.bcode)
print(b2.mro())