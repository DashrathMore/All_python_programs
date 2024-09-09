#""" disarium number when the sum of digits raised to the
# power of their respective position is equal to the number itself
# 135:-> 1**1 + 3**2 + 5**3 = 135 there sum and number is equal then its DISARIUM
# 134:-> 1**1 + 3**2 + 4**3 = 74 there sum is not equal to number is NOT DISARIUM
n = 135
a = 0
c = n
while(n != 0):
    l = len(str(n))
    a += (n%10)**l
    n //= 10
if(a == c):
    print("disarium number")
else:
    print(" not disarium")