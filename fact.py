#''' the factorial number means to multiply all whole numbers from our chosen number down to 1
# 5:-> 5*4*3*2*1 = 120
n = 5
f = 1
for i in range(1, n+1):
    f*=i
print(f)