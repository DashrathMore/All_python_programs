n = 327
s = str(n*1)+str(n*2)+str(n*3)
for i in range(1,10):
    if(str(i) not in s):
        print("not fascinating")
        break
else:
    print("fascinating")