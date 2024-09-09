def pal(n,c):
    rev=0
    while n>0:
        rev=(rev*10)+(n%10)
        n//=10
    return rev==c
n=121
print(pal(n,n))

def rev(s):
    ss=''
    for ch in s:
        ss=ch+ss
    return ss
print(rev('dash'))