#
'''

s = 'dash5rath ma3ya vila2s bhaga4vant vish1nu'
l = s.split()
d ={}
for word in l:
    k = ''
    v = ''
    for ch in word:
        if '0' <= ch <= '9':
            k += ch
        else:
            v += ch
    d[k]=v
lis = list(d)
lis.sort()
b = []
for i in lis:
    b.append(d[i])
print(' '.join(b))
#
i.sort()
lis = []
for j in i:
    for wrd in l:
        if j in wrd:
            lis.append(wrd)
print(' '.join(lis))

'''
#










'''
s = 'hi i am groot'
l=s.split()
ans = []
for word in l:
    ans.append(word[::-1])
print(' '.join(ans))
'''




'''
s = ' i am groot'
l = s.split()
ll = 0
for wrd in l:
    if( ll < len(wrd)):
        ll = len(wrd)
for word in l:
    if ll==len(word):
        print(word)
        print(ll)
'''





'''
s = 'ENGINEERING'
c = 0
dup = ''
for ch in s:
    if(c<s.count(ch)):
        c = s.count(ch)
for ch in s:
    if (c == s.count(ch) and (ch not in dup)):
        print(ch)
        dup += ch
'''





#
'''

s = 'aaabbbbccd'
c = 0
dup =''
for ch in s:
    if ch not in dup:
        dup+=str(s.count(ch))
        dup += ch
print(dup)
'''



'''
#armstrong number#
def arm(n,p):
    if n == 0:
        return 0
    return (n%10)**p + arm(n//10,p)
n=153
if n==arm(n,len(str(n))):
    print('arm')
else:
    print('not')
'''


'''
# strong number#
def fact(n,i):
    if i>n:
        return 1
    return i* fact(n,i+1)
def str(n):
    if n==0:
        return 0
    return fact(n%10,1)+str(n//10)
n=145
if n==str(n):
    print('str')
else:
    print('not')
'''

'''
# happy number#
def add(n,a):
    a += (n%10)**2
    if n==0:
        return a
    return add(n//10,a)
def happy(n):
    if n<10:
        print(n)
        return n
    b = add(n,0)
    return happy(b)
n=91
if (1 == happy(n)):
    print('happy')
else:
    print(n)
    print('not')
'''
# COUNT WORD WITHOUT USING COUNT METHOD
'''s = 'hi how are you hi i am fine'
l = s.split()
x=[]
for word in l:
    c = 0
    for wrd in l:
        if(word == wrd):
            c+=1
    if word not in x:
        print(c,word)
        x.append(word)'''
'''
# Reverse string using recursion#

def rev(s,i):
    if(i == -len(s)-1):
        return ''
    return s[i] + rev(s,i-1)
s= 'DasharatH'
print(rev(s,-1))
'''

'''
#
s = 'ab4c5dr99' #   'rd4c5ba99"
l = list(s)
ss = ''
for ch in s:
    if 'a' <= ch <= "z":
        ss += ch
a = -1
for j in range(len(l)):
    if 'a' <= l[j] <= 'z':
        l[j] = ss[a]
        a -= 1
print(''.join(l))
'''

#
'''
##reverse string without changing numbers#
s = 'DAS89har99ath090'
l = list(s)
ss = ''
for ch in s:
    if 'A'<= ch <='Z':
        ss+=ch
    elif 'a'<=ch<='z':
        ss+=ch
a = -1
for i in range(len(l)):
    if 'a'<=l[i]<='z':
        l[i] = ss[a]
        a -=1
    elif 'A'<=l[i]<='Z':
        l[i] = ss[a]
        a-=1
print(''.join(l))
'''





'''


# finding prime digit in list#

n='7083066893'
for num in n:
    num=int(num)
    if num>1 and all(num%i != 0 for i in range(2,num//2+1)):
        print(num)
##

'''
'''
# Dividing numbers and strings#
s='abcd123mdndd098sdnn374'
import re
print(list(map(int,re.findall('\d+', s))))
print(re.findall('[a-zA-Z]+',s))
'''

'''
# converting original form and printing type
s=['[1,2,3,]','(1,2,3)','{1,2,3}','123']
for val in s:
    print(eval(val),type(eval(val)))
'''
