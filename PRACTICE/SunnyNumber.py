# SUNNY NUMBER
'''
n = 8
l = n+1
for i in range(1, l//2+1):
#while(i**2<=l):
    if(i**2==l):
        print('sunny number')
        break
    i+=1
else:
    print('not sunny')
'''
'''def Sunny(n,i):
    s=n+1
    while(i**2<=s):
        if(i**2==s):
            return True
        i+=1
    return False
n = 35
if(Sunny(n,1)):
    print('sunny')
else:
    print('not')'''
# First five sunny
def Sunny(n,i):
    if(i**2 > n+1):
        return False
    if(i**2==n+1):
        return True
    return Sunny(n,i+1)
n = 1
c = 1
while c < 6 :
    if(Sunny(n,1)):
        print(n)
        c +=1
    n+=1

'''if(Sunny(n,1)):
    print('sunny')
else:
    print("not sunny")'''