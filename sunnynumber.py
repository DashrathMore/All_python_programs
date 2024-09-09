n = 14
a = 1
while(a**2 <= n+1):
    print(a)
    if((n+1) == (a**2)):
        print('sunny number')
        break
    a += 1
else:
    print('not sunny number')

'''n = 15
for i in range(1,n//2+1):
    print(i)
    if(n+1 == i**2):
        print('sunny number')
        break
else:
    print('not sunny')'''