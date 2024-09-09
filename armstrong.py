# An armstrong numberr is ONE WHOSE SUM OF DIGITS RAISED TO THE
# POWER OF (COUNT OF NUMBERS) EQUALS THE NUMBER ITSELF.
#154:-> 1**3 + 5**3 + 4**3 = 190 is not equal to 154 then its not armstrong
#9474:-> 9**4 + 4**4 + 7**4 + 4**4 = 9474 is equal to given number is armstrong

n = 9474
l = len(str(n))
a = 0
c = n
while(n != 0):
    a += (n%10)**l
    n //= 10
if(a == c):
    print(a,"armstrong number")
else:
    print(a,"not armstrong")