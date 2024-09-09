# Linear search
'''
l=[9,0,8,0,7,9,2,2,33,44,555,666]
user=int(input('enter value'))
l.sort()
for i in range(len(l)):
    if l[i]==user:
        print(i)
        break
else:
    print('-1')
'''
# Binery search
'''
l=[9,0,8,0,7,9,2,2,33,44,555,666,-1,-100]
ll=[]
for val in l:
    if val not in ll:
        ll.append(val)
ll.sort()
low = 0
high= len(ll)-1
user=int(input('Enter : '))
while low<=high:
    mid = (low+high)//2
    if user < ll[mid]:
        high=mid-1
    elif user > ll[mid]:
        low=mid+1
    elif user == ll[mid]:
        print(mid)
        break
else:
    print('-1')
'''
# Interpolation Search
'''
l=[9,0,8,0,7,9,2,2,33,44,555,666,-1,-100]
ll=[]
for val in l:
    if val not in ll:
        ll.append(val)
ll.sort()
low=0
high=len(ll)-1
user=int(input('Enter : '))
print(ll)
while low<=high and ll[low]<=user<=ll[high]:
    pos=int(low+((high-low)/(ll[high]-ll[low]))*(user-ll[low]))
    print(pos)
    if user<ll[pos]:
        high=pos-1
    elif user > ll[pos]:
        low=pos+1
    elif user==ll[pos]:
        print(pos)
        break
else:
    print('-1')
'''
# Bobule Sort
'''
l=[9,0,8,0,7,9,2,2,33,44,555,666,-1,-100]
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)
'''
# Selection Sort
'''
l=[99,0,8,0,7,9,2,2,33,44,555,66]
h=0
for i in range(len(l)):
    a=i
    for j in range(i,len(l)):
        if l[a] > l[j]:
            a=j
    l[i],l[a]=l[a],l[i]
print(l)
'''
# Insertion Sort
'''
l=[99,0,8,7,9,2,33,44,55,6]
for i in range(1,len(l)):
    a=i
    val=l[i]
    while a>0 and val < l[a-1]:
        l[a]=l[a-1]
        a-=1
    l[a]=val
print('l =',l)
'''
#
'''
n=int(input('Enter Vlue : '))
sp=0
for i in range(n,0,-2):
    print(' '*sp,end='')
    print('* '*i)
    print()
    sp+=2
'''
# Lengthest Subpalindrome
'''
s='dashrath'
l=0
ll=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])
        if len(s[i:j])>l:
            l=len(s[i:j])
            ll.append(s[i:j])
for sub in ll:
    if l == len(sub):
        print(l,sub)
        print(ll)
'''
# Decimal to Binary
'''
n=13
res=0
x=1
while n!=0:
    r=n%2
    res+=r*x
    n//=2
    x*=10
print(res)
'''
# Dec - Bin REcursion
'''
def bin(n,x,res):
    if n==0:
        return res
    return ((n%2)*x) + bin(n//2,x*10,res)
n=13
print(bin(n,1,0))
'''
# Bin - Dec Recursion
'''
def num(n,x):
    if n==0:
        return 0
    print((n%10)*x)
    return ((n%10)*x) + num(n//10,x*2)
n=1101
print(num(n,1))
'''
