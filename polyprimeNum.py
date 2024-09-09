n = 11
add= 0
c=n
while(n!=0):
    add = (add * 10) + (n % 10)
    n //= 10
if(c == add and c >  1):
    for i in range(2,c//2+1):
        if(c % i == 0):
            print("Not PolyPrime")
            break
    else:
        print("PollyPrime")
else:
    print("Not PollyPrime   ..")