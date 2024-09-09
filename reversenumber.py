'''num = 1234
add = 0
while(num !=0):
    add = (add*10) + (num % 10)
    num //= 10
print(add)
'''

n = 121
add = 0
c = n
while(n != 0):
    add = (add*10) + (n%10)
    n //= 10
if(c==add):
    print(c,add, "palindrome")
else:
    print(c,add,'not palindrome')