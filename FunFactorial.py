def Fact(n):
    mul = 1
    for i in range(1, n+1):
        mul*=i
    return mul
num = 5
print(Fact(num))