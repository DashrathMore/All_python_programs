def Strong(n, c):
    add = 0
    while (n != 0):
        rem = n % 10
        fact = 1
        for i in range(1,rem+1):
            fact *= i
        add += fact
        n //= 10
    return add == c
num = 145
if (Strong(num, num)):
    print("strong Number")
else:
    print("not strong")