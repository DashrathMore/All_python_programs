''' n = 12
for i in range(1, n//2+1):
    if(i*(i+1)==n):
        print("pronic")
        break
else:
    print("not pronic") '''

n = 13
i = 1
while(i*(i*1)<= n):
    if(i*(i+1) == n):
        print("pronic")
        break
    i+=1
else:
    print("not pronic")