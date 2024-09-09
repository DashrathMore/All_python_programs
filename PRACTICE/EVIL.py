#RECURSSION
def Rev(n,x):
    if n == 0:
        return 0
    return (n%10)*x + Rev(n//10, x//10)
def Prime(n,c,i):
    if i > n:
        return c == 2
    if n%i==0:
        c+=1
    return Prime(n,c,i+1)
n = 91
l = len(str(n)) - 1
rev = Rev(n,10**l)
if(n != rev) and Prime(n,0,1) and Prime(rev,0,1):
    print('EMIRP')
else:
    print('not emirp')