n = 17
a = 0
c = n
while(n != 0):
    a = (a*10) + (n%10)
    n //= 10
print(a)
if(a != c):
    for i in range(2,c//2+1):
        if(c % i == 0):
            print("not EMIRP")
            break
    else:
        for j in range(2,a//2+1):
            if(a % j==0):
                print('NOT EMIRP')
                break
        else:
            print("EMIRP")
else:
    print("Not Emirp")