'''def Prime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count += 1
    return (count == 2)
n = 1
count = 0
while (count < 5):
    if(Prime(n)):
        print(n)
        count += 1
    n += 1
'''
def Prime(n,i):
    if i==n//2+1:
        return True
    if n%i==0 or n<=1:
        return False
    return Prime(n,i+1)
def Fiv(m,l):
    if(l == 5):
        return 0
    if(Prime(m,2)):
        print(m)
        l += 1
    return Fiv(m+1,l)
Fiv(1,0)
''' n=1
c = 0
while (c < 15):
    if (Prime(n,2)):
        print(n)
        c += 1
    n+=1'''

'''if(Prime(n,2)):
    print("prime")
else:
    print("not")'''