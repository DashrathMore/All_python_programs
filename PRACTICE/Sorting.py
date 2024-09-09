# Bouble Sort
#ascending
'''
l = [99,21,3, 4,5,-2,9,2,1]
for k in range(len(l)-1):
    for q in range(len(l)-1-k):
        if l[q]>l[q+1]:
            l[q],l[q+1]=l[q+1],l[q]
print(l)
'''
# Descending Order
'''
l = [99,21,3, 4,5,-2,9,2,1]
for k in range(len(l)-1):
    for q in range(len(l)-1-k):
        if l[q]<l[q+1]:
            l[q],l[q+1]=l[q+1],l[q]
print(l)
'''

# Selection Sort
'''
# Ascending Order
l = [99,21,3, 4,5,-2,9,2,1,33,44,55,22,-11]
for m in range(len(l)-1):
    a=m
    for n in range(m+1, len(l)):
        if l[a]>l[n]:
            a=n
    l[a],l[m]=l[m],l[a]
print(l)

#Descending Order

l =[99,21,3, 4,5,-2,9,2,1,33,44,55,22,-11]
for k in range(len(l)-1):
    a=k
    for n in range(k+1, len(l)):
        if l[a] < l[n]:
            a=n
    l[a],l[k]=l[k],l[a]
print(l)
'''
# Insertion Sort
'''
#ascending Order
l=[1,2,3,-1,-5,99,90,100,20,12]
for a in range(1,len(l)):
    val=l[a]
    b=a-1
    while b>=0 and val < l[b]:
        l[b+1]=l[b]
        b-=1
    l[b+1]=val
print(l)

# Descending order
l=[1,2,3,-1,-5,99,90,100,20,12]
for i in range(1,len(l)):
    h = i
    val = l[h]
    while h>0 and val>l[h-1]:
        l[h]=l[h-1]
        h-=1
    l[h]=val
print(l)
'''
#boble
'''
l=[1,2,3,-1,-5,99,90,100,20,12]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''
#1
'''
d ={1:'Abc',2:"dash",3:'ram'}
D={}
for i in d:
    D[d[i]]=i
print(D)
'''
#2
'''
l=[2,3,[3,4,5,6],8]
ll=[]
for val in l:
    if type(val)==int:
        ll.append(val)
    else:
        for i in val:
            ll.append(i)
print(ll)
'''
#3
'''
s='Actualize It Solutions'
ss=''
for ch in s:
    if ch not in 'aeiouAEIOU':
        ss+=ch
print(ss)
'''
#4
'''
l=[1,2,3,2,1,3,4,5]
print(l)
s=set(l)
print(s)
ll=list(s)
ll.sort()
print(ll)
print(ll[-2])
'''
#5
'''
l=[1,2,3,2,1,3,4,5,1,2,10,22,10,10,10,10]
ll=[]
for val in l:
    if val not in ll:
        ll.append(val)
        c=0
        for i in l:
            if val == i:
                c+=1
        print(val,c)
'''
#6
'''
s='abcdefghijklmnopqrstuvwxyz'
ss='hello'
add=0
for ch in ss:
    if ch in s:
        add+=s.index(ch)+1
        print(ch,s.index(ch)+1)
print(add)
'''
#7
n=5
a=11
sp=0
for i in range(n):
    print('   '*sp,end='')
    for j in range(i,n):
        print(a,end=' ')
        a+=1
    sp+=1
    print()

n=11
sp=0
for i in range(n,0,-2):
    print('  '*sp,end='')
    print('* '*i)
    sp+=1