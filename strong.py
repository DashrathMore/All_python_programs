# strong number is a number whose sum of all digits factorial is
# equal to the number 'n'
n = 145
a = 0
c = n
while(n != 0):
    rem = n % 10
    f = 1
    for i in range(1, rem+1):
        f *= i
    a += f
    n //= 10
if( a== c):
    print("strong number")
else:
    print('not strong')