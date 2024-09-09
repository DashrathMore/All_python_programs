n = 123
add = 0
c = n
while(n != 0):
    rem = n% 10
    add= add+ rem
    n //= 10
print(add)
if(c%add==0):
    print("niven number")
else:
    print("not niven")