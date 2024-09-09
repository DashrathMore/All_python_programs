'''n = 'dashrath'
l = len(n)
for i in range(1, l+1):
    a = -1
    for j in range(1,i+1):
        print(n[a], end=' ')
        a-=1
    print()


n = 19
c = n
r = 0
while( n != 0):
    r=(r*10)+(n%10)
    n //= 10
if(r != c):
    for i in range(2, c//2+1):
        if(c % i == 0):
            print("no emirp")
            break
    else:
        for j in range(2, r//2+1):
            if(c % j == 0):
                print('not')
                break
        else:
            print('emirp')
else:
    print('not emirp')


def pronic(n):
    i = 1
    while (i*(i+1)<=n):
        if (i*(i+1) == n):
            return True
        i += 1
    return False
n=56
if(pronic(n)):
    print("pronic")
else:
    print("not")

'''
'''

def sunny(n):
    a =1
    while(a**2<=n+1):
        if(a**2==n+1):
            return True
        a+=1
    return False
n = 23
if(sunny(n)):
    print('sunny')
else:
    print('not')



def Rev(s, i):
    if (i == -1):
        return " "
    print (s[i], end='')
    return Rev(s, i-1)
s='Dashrath'
i = len(s)
print(Rev(s, i-1))
'''

'''def Prime( n ,i):
    print(i)
    if (n%i==0):
        return False
    if (i > n//2+1):
        return True
    return Prime(n, i+1)
n = 23
if(Prime(n,2)):
    print('prime')
else:
    print('not')'''

'''i = 0
while i < 10:
    i+= 1
    if i==3 or i==6:
        continue
    print(i, end=" ")'''

'''number = [1,2,3,4,5]
res = [n for n in number if n %2==0]
print(res)'''
'''
r = ""
for i in range(1,11):
    if i % 2==0:
        r+= str(i) + " "
print(r.strip())'''
'''a = 5
b = 10
print(a<b and "a<b") or( a>b and "b>a")'''

'''n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or j==n or i==n or (i==n//2+1 and j==n//2+1)):
            print("*", end=' ')
        else:
            print("  ", end="")
    print()'''

'''n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if( i==j or j==1 or i==n):
            print("*", end=" ")
        else:
            print('  ', end='')
    print()
    '''
'''
n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or i==n or j==n or (i==n//2+1 and j==n//2+1) or (i==2 and j==2) or (i==4 and j==4) or (i==2 and j==4) or (i==4 and j==2) ):
            print('*', end=' ')
        else:
            print("  ", end='')
    print()'''
'''n = 5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1 or j==n or (i==2 and j==2) or (i==2 and j==4) or (i==3 and j==3)):
            print("*", end=" ")
        else:
            print('  ', end='')
    print()'''

n=5
for i in range(1,n+1):
    for j in range(1,n+2):
        if (j==1 or (i==2 and j==2) or (i==1 and j==3) or (i==4 and j==3) or (i==5 and j==5)):
            print("*", end=" ")
        else:
            print('  ', end='')
    print()