"""
def balancing(s):
    while True:
        if '()' in s:
            s = s.replace('()', '')
        elif '{}' in s:
            s = s.replace('{}','')
        elif '[]' in s:
            s = s.replace('[]','')
        else:
            print(s)
            return not s

'''
            if s:
                return False
            else:
                return True
'''
s='{}[]()[]{}'
print(balancing(s))
"""
###############
'''
l=[1,2,3,4,5,6,7,8,9]
d={k:k**2 for k in l}
print(d)
'''
###################
'''
input = [3, 3, 1, 2, 2, 2, 8, 8, 8, 8, 8, 10,]
new = sorted(input, key=lambda k:input.count(k))
print(new)
'''
####################
'''
def bal(s):
    while True:
        if '()' in s:
            s=s.replace('()','')
        elif '{}' in s:
            s=s.replace('{}','')
        elif '[]' in s:
            s=s.replace('[]','')
        else:
            return not s
s='()[]{[]{}'
print(bal(s))
'''
#####################
'''
l=[1,2,3,4,[12,31,45,90,(99,88,'abc')],1,2,3]
n=0
while n<len(l):
    s=l[n]
    if type(s) != int and len(s)>1:
        l.remove(l[n])
        l.extend(s)
        n=0
    n+=1
print(l)
'''
'''
l=[1,2,9,16,25,10]
for j in l:
    for i in range(1,j):
        if i**2 == j:
            print('perfect square ', i)
            break
        elif i**2 > j:
            print('not perfect square')
            break
'''
'''
from math import sqrt
l=[1,2,3,9,10,14,24,16,25]
nl=[]
for val in l:
    if val==int(sqrt(val))**2:
        nl.append(val)
print(nl)
'''
#####################
'''
def one(l,i):
    if i == len(l):
        return l
    elif type(l[i]) != int and len(l[i])>1:
        s=l[i]
        l.remove(s)
        l.extend(s)
        i=-1
    return one(l,i+1)
l=[1,2,3,4,5,[11,22,33,44,'abcd',('xyz',99),999],100,200]
print(one(l,0))
'''
##########################
