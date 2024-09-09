#NORMAL
'''n = 153
p = len(str(n))
add = 0
c = n
while(n!=0):
    r = n%10
    add += (r**p)
    n //= 10
if (c == add):
    print('armstrong')
else:
    print('not')'''
#FUNCTION
'''def Arm(n):
    c= n
    p = len(str(n))
    add = 0
    while(n !=0):
        add+= (n%10)**p
        n//=10
    return c == add
n = 10
c = 0
while(c<5):
    if(Arm(n)):
        print(n)
        c +=1
    n+=1
#FOR SINGLE VALUE
N = 153
if(Arm(n)):
    print("armstrong")
else:
    print('not')'''
#RECURSION
def Arm(n,p):
    if n == 0:
        return 0
    return (n%10)**p + Arm(n//10, p)
n = 1
c = 0
while(c<10):
    p=len(str(n))
    if (Arm(n, p) == n):
        print(n)
        c +=1
    n+=1

'''n = 9474
p = len(str(n))
if(Arm(n,p) == n):
    print(Arm(n,p),'armstrong')
else:
    print(Arm(n,p),'not')'''