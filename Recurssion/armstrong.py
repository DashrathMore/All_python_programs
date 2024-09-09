#armstrong
def Arm(n, s):
    if n==0:
        return True
    if(n%10 != s%10):
        return False
    return Arm(n//10, s//10)
n = 1
count = 0
while( count < 5):
    if(Arm(n,n**2)):
        print(n)
        '''print(n**2)'''
        count+=1
    n+=1







'''n = 25
s = n ** 2
if(Arm(n, s)):
    print('armstrong')
else:
    print("not")'''