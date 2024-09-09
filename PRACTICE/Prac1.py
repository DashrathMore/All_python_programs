'''# FIRST HALF LIST
l = [10,20,30,40,50,60,70,80,90,100]
n = []
for i in range(len(l)//2):
    n.append(l[i])
print(n)


# LAST HALF LIST
l = [10,20,30,40,50,60,70,80,90,100]
n = []
for i in range(len(l)//2,len(l)):
    n.append(l[i])
print(n)

# SUM VALUES IN LIST
l=[11,12,13,14,15,16,17,18,19,20,22,33,44,55,66,77,88,99]
n = []
for i in l:
    if(i%2==0):
        n.append(i)
print(n)

# VALUES IN EVEN INDEX POSITION
l=[11,12,13,14,15,16,17,18,19,20,22,33,44,55,66,77,88,99]
n = []
for i in range(0,len(l)):
    if(i%2==0):
        n.append(l[i])
print(n)
'''
# REVERSING STRING WITHOUT
'''s = '   DASHRATH MORe'
l = list(s)
a =-1
for i in range(0,len(l)//2):
    l[i],l[a]=l[a],l[i]
    a -= 1
print(''.join(l))
'''
# PALINDROME STRING
''''s = 'abcdrdcba'
a = -1
for i in range(0,len(s)//2):
    if(s[i] != s[a]):
        print('not palindrome')
        break
    a -= 1
else:
    print('palindrome')
'''

# REVERSE WORD WHITHOUT
'''s = 'DASHARATH VILAS MORE'
ss = ''
res = ''
for ch in s:
    if ch != ' ':
        ss = ch + ss
    else:
        res = ' ' +ss+ res
        ss = ''
res = ss + res
print(res)'''

'''nums = [3,2,4]
target = 6
for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if(nums[i])+nums[j]==target:
            print([i,j])

s = ' dasharath vilas more'
f = ''
ss = ''
for ch in s:
    if ch != ' ':
        ss= ch + ss
    else:
        f=' '+ss+f
        ss = ''
f =ss+f
print(f)



l = [1,2,2,1,2,3,4,3,5,6,7]
x = []
for i in l:
    if l.count(i)>1 and i not in x:
        x+=[i]
print(x)
'''
# spy
'''
def add(n):
    if n == 0:
        return 0
    return n%10 + add(n//10)
def mul(n):
    if n == 0:
        return 1
    return n%10 * mul(n//10)
n = 1412
if(mul(n)==add(n)):
    print('spy')
else:
    print('not')
'''
#niven
'''
def niv(n):
    if n == 0:
        return 0
    print(n)
    return n%10 + niv(n//10)
n = 21
if (n % niv(n) == 0):
    print('niv')
else:
    print('not')'''

# Perfect number
'''n = 28
add= 0
for i in range(1,n//2+1):
    if n%i==0:
        add+=i
if add==n:
    print('perfect')
else:
    print('not')'''
# function
'''def p(n):
    add = 0
    for i in range(1,n//2+1):
        if n%i==0:
            add+=i
    return add
n = 28
print(n==p(n))
'''
# recurssion
'''def p(n,i,add):
    if i == (n//2+2):
        return add
    if n%i==0:
        add += i
    return p(n,i+1,add)
n = 28
print(p(n,1,0))'''

# evil
'''n = 15
x=1
add = 0
while n!=0:
    r=n%2
    add +=r
    n//=2
    x*=10
if add%2==0:
    print('evil')
else:
    print('not')'''
#LAMBDA FUNCTION
'''mul = lambda x,y,z:x*y*z
print(mul(2,2,2))
'''
# MAP FUNCTION
'''l=[1,2,3,4,5]
m =list(map(lambda n:n**2,l))
print(m)
for i in m:
    print(i)'''

#FILTER FUNCTION
'''def eve(n):
    return n%2==0
f =filter(eve, [1,2,3,4,5,6,7,8,9,0])
print(list(f))
for i in f:
    print(i)'''
#reeverse
'''s =[1,3,4,5,6,5,43,44,55,55,44,33,44]
x =[]
for i in s:
    if i not in x:
        x.append(i)
x.sort(reverse = True)
print(x[1])'''
#
'''s =[1,3,4,5,6,5,43,44,55,44,33,44]
a = -1
for i in range(0,len(s)//2):
    s[i],s[a] = s[a],s[i]
    a -= 1
print(s)'''

# 'aaabbcd' '3a2b1c1d'
'''s = '3A2b1c3d'
c= ''
ss = ''
for ch in s:
    if '0'<= ch <= '9':
        c += ch
    else:
        ss += ch * int(c)
        c = ''
print(ss)
'''

#'aaabbcd' '3a2b1c1d'
'''s = 'aaabbbbccdddddddddeeeoooddd'
ss=''
c =1
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        ss+=str(c)+s[i]
        c=1
ss+=str(c)+s[-1]
print(ss)
'''
'''
s = 'this is not good for your health'
ss = ''
l = s.split()
for i in l:
    w = list(i)
    w[0],w[-1]=w[-1],w[0]
    ss += ''.join(w) +" "
print(ss.strip())'''

#
'''
n = 19
sp = 9
a = b=  11
for i in range(1,n+1):
    for s in range(sp):
        print(' ', end=' ')
    for j in range(10,sp,-1):
        print(j,end=' ')
    for l in range(a,b):
        print(l,end=' ')
    print()
    if(i <= n//2):
        sp -=1
        a -= 1
    else:
        sp+=1
        a+=1
   '''

'''
n = 9
x = ['E','D','C','B','A']
sp = 4
a = 5
for i in range(1,n+1):
    for s in range(sp):
        print(' ', end=' ')
    for j in range(4,sp-1,-1):
        print(x[j],end=' ')
    if 2 <= i <= 8:
        for l in range(a,5):
            print(x[l],end=' ')
    print()
    if(i <= n//2):
        sp -=1
        a -= 1
    else:
        sp+=1
        a+=1
'''
'''
n = 9
b = 2
a = 1
sp = (n//2)
for i in range(1,n+1):
    print('  ' * sp, end='')
    for j in range(a,b):
        print(j,end=' ')
    print()
    if (i<n//2+1):
        b+=2
        sp -=1
    else:
        b = n+1
        a +=2
        sp+=1

n = 9
a = 1
for i in range(n):
    if a>2:
        print('*',' '*(a-2),'*')
    else:
        print('* '*a)
    a=a+1 if i<n//2 else a-1
'''
def singleton(arg):
    d={}
    def inner():
        if arg not in d:
            d[arg]=arg()
        return d[arg]
    return inner
@singleton
class Flash():
    def __init__(self):
        self.tickets=100
    def book(self):
        #print("Booked Tickets Here....")
        t=int(input('enter number of tickets : '))
        if self.tickets >= t:
            print('ticket booked successfully...!!!!')
            self.tickets-=t
        else:
            print('Tickets not avaliable')
@singleton
class Ravana:
    def __init__(self):
        self.tickets=100
    def book(self):
        t=int(input('Enter Number Of Tickets : '))
        if t <= self.tickets:
            print('Tickets Booked Successyfully!!!...')
            self.tickets-=t
        else:
            print('Tickets Not Avaliable....')

def BMS():
    print("""option of Movies
    1.The Flash
    2.Ravana
    Select Option..
    """)
    o=int(input('Enter: '))
    if o==1:
        ob=Flash()
        ob.book()
    elif o==2:
        ra=Ravana()
        ra.book()
    else:
        print("Invalid Option")
BMS()
BMS()
BMS()
BMS()