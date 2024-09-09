def Armstrong(n,p,c):
    add = 0
    while (n != 0):
        add += (n%10)**p
        n //= 10
    return add==c

num = 153
if (Armstrong(num,len(str(num)), num)):
    print("Armstrong")
else:
    print('Not Armstrong')