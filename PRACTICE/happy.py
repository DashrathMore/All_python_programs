# NORMAL HAPPY NUMBER
'''n = 94
while(n > 9):
    a = 0
    while (n != 0):
        r = n % 10
        a = a + (r**2)
        n //= 10
    n = a
if (n == 1):
    print('happy')
else:
    print('not')'''

# FUNCTION
'''def Happy(n):
    while (n > 9):
        c = 0
        while (n!=0):
            c += (n%10)**2
            n //= 10
        n = c
    return n==1
n = 10
c = 0
while(c<5):
    if Happy(n):
        print(n)
        c += 1
    n+=1'''
''' # FOR 1 NUMBER
n = 94
if ( Happy(n)):
    print('HAPPY  NUMBER')
else:
    print('not happy')'''

# RECURSION
def Happy(n,add):
    add += ((n%10)**2)
    if n == 0:
        return add
    return Happy(n//10,add)
def hap(num):
    if num < 10:
        return num ==1
    num = Happy(num,0)
    print(num)
    return hap(num)
n = 28
add = 0
print(hap(n))


'''def sqr(n):
    if n == 0:
        return 0
    return (n%10)**2 + sqr(n//10)
def happy(n):
    if n < 10:
        return n == 1
    n = sqr(n)
    return happy(n)
n = 49
print(happy(n))'''

# STRONG
def Fact(n,i):
    if i == n+1:
        return 1
    return i* Fact(n,i+1)
def Strong(n):
    if n == 0:
        return 0
    return Fact(n%10,1)+Strong(n//10)
n = 145