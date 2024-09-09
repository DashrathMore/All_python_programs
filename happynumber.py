n = 94
while(n > 9):
    a = 0
    while(n != 0):
        r = n % 10
        a += r**2
        n //= 10
    n = a
if(n == 1):
    print("happy number")
else:
    print("not happy number")