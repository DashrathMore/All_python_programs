# NORMAL
'''n = 135
add = 0
c = n
while(n!=0):
    p=len(str(n))
    add += (n%10)**p
    n //= 10
if( c == add):
    print('disarium')
else:
    print('Not')'''
# WITH FUNCTION
'''def Dis(n,p):
    add = 0
    while(n!=0):
        add+= (n%10)**p
        n//=10
        p -=1
    return add
n = 10
c = 0
while(c <5):
    if(n==Dis(n,len(str(n)))):
        print(n)
        c += 1
    n+=1
#for single
n = 139
if (n == Dis(n,len(str(n)))):
    print('disarium')
else:
    print('not')'''
# WITH RECURSION
def Dis(n,p):
    if n == 0:
        return 0
    return (n%10)**p + Dis(n//10,p-1)
n = 10
c = 0
while c<5:
    if(n==Dis(n,len(str(n)))):
        print(n)
        c +=1
    n+=1
'''
n = 89
if(n == Dis(n,len(str(n)))):
    print('disarium')
else:
    print('not')'''