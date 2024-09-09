n = 124
a = 0
m = 1
while(n != 0):
    a += (n%10)
    m *= (n%10)
    n //= 10
if(m == a):
    print("spy number")
else:
    print("not spy number")