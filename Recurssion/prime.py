# first Five prime numbers
def Prime(n,i):
    if(i==n+1):
        return 0
    return(1 if n%i==0 else 0) + Prime(n,i+1)
def Fiv(p, l):
    if(l == 15):
        return 0
    if(Prime(p,1) == 2):
        print(p)
        l += 1
    return Fiv(p+1, l)
n = 1
Fiv(n,0)

# prime number
n = 1
c = 0
while(c != 5):
    if(Prime(n,1)==2):
        print(n)
        c += 1
    n += 1'''
'''n= 14
if(Prime(n,1)==2):
    print("prime")
else:
    print('not')