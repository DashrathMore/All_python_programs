''' a square of given number should be end with same number
6**2= 36  at end 6 is same then it is automorphic number
25**2 = 625 so 25 is a automorphic number
n = 7
l = n**2
print(l)
while(n != 0):
    if((n%10)!=(l%10)):
        print("not automorphic")
        break
    n//=10
    l//=10
else:
    print("automorphic")



TRIMORPHIC
A CUBE OF GIVEN NUMBER SHOULD BE END WITH SAME NUMBER
'''
n = 7
cb = n**3
print(cb)
while(n != 0):
    if((n%10) != (cb%10)):
        print("not trimorphic")
        break
    n //= 10
    cb //= 10
else:
    print(" Trimorphic")