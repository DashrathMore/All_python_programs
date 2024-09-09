# Facinating
def Fasc(i,s):
    if i == 10:
        return True
    if(str(i) not in s):
        return False
    return Fasc(i+1, s)
n = 1
count = 0
while count != 10:
    if(Fasc(1,str(n*1)+str(n*2)+str(n*3))):
        print(n)
        count+=1
    n+=1

'''

if Fasc(1, s):
    print('fasc')
else:
    print('not')
'''