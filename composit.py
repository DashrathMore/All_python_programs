n = 11
for i in range(2,(n//2)+1):
    if(n % i == 0):
        print("composit number")
        break
else:
    print("not composit")