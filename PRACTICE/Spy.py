# SPY NORMAL
'''n = 6
add = 0
mul = 1
while(n != 0):
    r = n%10
    add+=r
    mul*=r
    n //= 10
if(add==mul):
    print('spy number')
else:
    print('not')'''
# SPY USING FUNCTION
'''def Spy(n):
    add = 0
    mul = 1
    while(n!=0):
        r = n%10
        add += r
        mul *= r
        n //= 10
    return add==mul
n = 10
c = 0
while (c <15):
    if(Spy(n)):
        print(n)
        c +=1
    n+=
#
n = 1241
if Spy(n):
    print('spy number')
else:
    print('not')'''
#First five SPY RECURSSION
def Spy(n,a,m):
    if n == 0:
        return a == m
    r = n %10
    a += r
    m *= r
    return Spy(n//10, a,m)
n = 10
c = 0
while(c<5):
    if Spy(n,0,1):
        print(n)
        c += 1
    n+=1









'''n = 123
a = 0
m = 1
if Spy(n,a,m):
    print('spy')
else:
    print('not')'''