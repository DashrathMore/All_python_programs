#question 1
'''
n=11
h=n//2+1
msp=n-2
osp=0
for i in range(1,n+1):
    if i == h:
        print('{}{}'.format(' ' * osp, '*'))
        osp-=1
        msp+=2
    elif i!=h and i<h:
        #print(' '* osp, '*', ' '*msp, '*')
        print('{}{}{}{}'.format(' '*osp,'*',' '*msp,'*'))
        osp+=1
        msp-=2
    elif i!=h and (i>h):
        print('{}{}{}{}'.format(' ' * osp, '*', ' ' * msp, '*'))
        osp -= 1
        msp += 2
#
n=9
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==j or i+j==n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==j or i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''


#Question 2
'''
from functools import reduce
import re
s=input('enter :')
l=re.findall('\d',s)
sl=[]
el=[]
for val in l:
    val=int(val)
    c=0
    for i in range(1,val+1):
        if val%i==0:
            c+=1
    if c==2:
        sl.append(val)
    if val%2==0:
        el.append(val)
print(el)
print(sum(el))
print(sl)
print(sum(sl))
x=reduce(lambda a,b:a+b, el)
print(x)
'''

# Question 3
"""
f,s=0,1
n=5
l=[]
nn=n*2-1
for i in range(nn):
    l.append(f)
    f,s=s,f+s
print(l)
sp=0
s=n-2
a=0
b=len(l)-2
for i in range(nn):
    if i <= nn//2:
        print(f'{"- "*sp}{l[a]}')
        sp+=1
        a+=2
    elif ( i > nn // 2 ):
        print(f"{'- ' * s}{l[b]}")
        b-=2
        s-=1
    '''
    elif(i==nn//2):
        sp=n-1
        a=len(l)-1
        print(f'{"- " * sp}{l[a]}')
        '''
"""
# Question 4
# print sum of asci vallues of each character
'''
s=input('enter String : ')
add=0
for ch in s:
    add+=ord(ch)
    #print(ch, ord(ch))
print(add)
'''
# take number
#find count of prime numbers
# if count is even add 1 in only prime number upto it is not prime
# if count is odd minus 1 im only prime numbers upto it is not prime
# print number
'''
import re
mn=int(input('enter mno no. : '))
mn=str(mn)
el=[]
ol=[]
count=0
for ch in mn:
    c=0
    ch=int(ch)
    for i in range(1,ch+1):
        if ch % i==0:
            c+=1
    if c==2:
        el.append(ch+1)
        ol.append(ch-1)
        count+=1
    else:
        el.append(ch)
        ol.append(ch)
print('el',el)
print('ol',ol)
print(count)
if count%2==0:
    print('el')
    for n in range(len(el)):
        c=0
        for i in range(1,el[n]+1):
            if el[n]%i==0:
                c+=1
        if c==2:
            el[n]=el[n]+1
    fl=str(el)
else:
    print('ol')
    for n in range(len(ol)):
        c=0
        for i in range(1,ol[n]+1):
            if ol[n]%i==0:
                c+=1
        if c==2:
            ol[n]=ol[n]-1
    fl=str(ol)
fl=re.findall('\d',fl)
print(''.join(fl))
'''

'''
 # question 6
 # create bank application with exception handling
 # for each and method raise exception and handle exception
 # withdraw
 # pin
 # deposite

class bank:
    branch='marthalli'
    IFSC='HDFC000127'
    def __init__(self, nm, mn, bal, pin):
        self.name=nm
        self.mno=mn
        self.balance=bal
        self.pin=pin
    def withdraw(self):
        if self.pin==int(input('enter Password : ')):
            b=int(input('enter amount :'))
            if self.balance>=b:
                self.balance-=b
                print('withdraw successfully!!!')
            else:
                raise Exception('Not Sufficient Balance...')
        else:
            raise Exception('incorrect pin!!!')
    def deposite(self):
        if self.pin==int(input('enter Password : ')):
            add=int(input('enter deposite amount : '))
            self.balance+=add
            print('Deposited Successfully...')
        else:
            raise Exception('Incorrect Pin!!!')
    def CheckBalance(self):
        if self.pin==int(input('enter Password : ')):
            print(self.balance)
        else:
            raise Exception('Incorrect Pin!!!')
try:
    dash = bank('dash', 7083066893, 20000, 1234)
    lara = bank('lara' ,8010739260, 90000, 4321)
    while True:
        nm=input('enter name :')
        if dash.name==nm:
            ob=dash
        elif lara.name==nm:
            ob=lara
        print("""Choose Option :
        1= withdraw
        2=deposite
        3=CheckBalance""")
        option=int(input('enter option'))
        if option==1:
            ob.withdraw()
        elif option == 2:
            ob.deposite()
        elif option == 2:
            ob.CheckBalance()
except Exception as msg:
    print(msg)
'''

'''
# adding sublist in one single list
l=[1,2,3,[4,5,6],[6,7,8],(9,10,11)]
ll=[]
for i in l:
        if type(i)!= int:
                ll.extend(i)
        else:
                ll.append(i)
print(ll)
'''


'''
# converting string into integer or original format
l=['123','[1,2,3]','3445',1,2,4]
ll=[]
for i in l:
        if type(i) == str:
                ll.append(eval(i))
        else:
                ll.append(i)
print(ll)
'''
'''
d={'a':10, 'b':20, 'c':30}
d1={'f':60, 'e':50, 'd':40}dash123.Mor129@gmail.com
d3={}
for i in d:
        d3[i]=d[i]
for i in d1:
        d3[i]=d1[i]
print(d3)
'''
'''
import re
m=input('enter mail id :')
if re.match('[a-zA-Z]\w+[.]?\w*@gmail.com', m):
        print('valid')
else:
        print('not valid')
'''

'''
# INSERTION SORT

l=[12,10,14,19,9]
for i in range(1,len(l)):
    val=l[i]
    j=i-1
    while j>=0 and val<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=val
print(l)
'''


'''
# Merge Sort
def divide(arr):
    if len(arr)==1:
        return
    left=arr[0:len(arr)//2]
    right=arr[len(arr)//2: ]
    divide(left)
    divide(right)
    merge(arr,left,right)
def merge(arr,l,r):
    ind=li=ri=0
    while li<len(l) and ri<len(r):
        if l[li]<r[ri]:
            arr[ind]=l[li]
            ind+=1
            li+=1
        else:
            arr[ind]=r[ri]
            ind+=1
            ri+=1
    while li<len(l):
        arr[ind]=l[li]
        ind+=1
        li+=1
    while ri<len(r):
        arr[ind]=r[ri]
        ind+=1
        ri+=1

l=[12,10,14,19,9,20,8]
divide(l)
print(l)

'''
#divide number and characters
'''
s='ABC1abc122390klJK'
#1
import re
a=re.findall('[a-zA-Z]',s)
n=list(map(int,re.findall('\d',s)))
print(a)
print(n)
#2
a=[ch for ch in s if ch.isalpha()]
n=[int(num) for num in s if num.isdigit()]
print(a)
print(n)
'''
'''
s=['123', '1%7', '1@39']
import re
for i in s:
    x=sum(map(int, re.findall('\d',i)))
    print(x)
'''
'''
# insertion sort
l=[10,29,18,9,18,1,111]
for i in range(1,len(l)):
    val=l[i]
    j=i-1
    while j>=0 and val < l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=val
print(l)
'''


'''
# Merge sort

def divide(arr):
    if len(arr)<=1:
        return
    left=arr[0:len(arr)//2]
    right=arr[len(arr)//2 : ]
    divide(left)
    divide(right)
    Merge(arr,left,right)

def Merge(arr,l,r):
    i=li=ri=0
    while li<len(l) and ri<len(r):
        if l[li]<r[ri]:
            arr[i]=l[li]
            i+=1
            li+=1
        else:
            arr[i]=r[ri]
            i+=1
            ri+=1
    while(li<len(l)):
        arr[i]=l[li]
        i+=1
        li+=1
    while ri<len(r):
        arr[i]=r[ri]
        i+=1
        ri+=1
l=[29,19,10,28,100,1,90,8]
divide(l)
print(l)
'''
'''
# Quiick sort
def Quick (l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[num for num in l if num<pivot]
    right=[num for num in l if num>pivot]
    return Quick(left)+[pivot]+Quick(right)
l=[29,19,10,28,100,80,101,1,90,8]
print(Quick(l))
'''

'''
# Bouble sort
l=[29,19,10,28,100,1,90,8,8]
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''

'''

ll=[]
import re
l=['123','13%4', '98@8']
for val in l:
    ll+=re.findall('\W', val)
print(ll)

n=1500
print(n*0.10)

'''


"""
#find index position of vovels
#multiplay index position with 100
#find sum of prime numbers between 1 to the nymber obtained in 2 step
#reduce the sum of price to single digit by adding individual digits until its single digit
#replace single digit into place of vovels

def prime(n):
    add=0
    for i in range(1,n+1):
        if i>1 and all(i%j!=0 for j in range(2,i//2+1)):
            add+=i
    return add

def adddig(n):
    add=0
    while n>0:
        add+=n%10
        n//=10
    return add

s='hai python'
ss=''
for ch in s:
    if ch not in 'aeiouAEIOU':
        ss+=ch
    else:
        sp=prime(s.index(ch)*100)
        print(sp)
        while len(str(sp))>1:
            sp=adddig(sp)
            print(sp)
        ss+=str(sp)
print(ss)
"""
############
'''
# ab/ac replace with a
#ba/bc replace with b
# after replacing again start from start
#until it unmatched
s='abccbcab'
l=list(s)
i=0
while i<len(l):
    if (''.join(l[i:i+2]) =='ab' or ''.join(l[i:i+2])=='ac'):
        print('if :', ''.join(l[i:i+2]))
        l.remove(l[i+1])
        l[i]='a'
        i=0

    elif (''.join(l[i:i+2])=='ba' or ''.join(l[i:i+2])=='bc'):
        print('elif :',''.join(l[i:i+2]))
        l.remove(l[i + 1])
        l[i] = 'b'
        i = 0
    else:
        i+=1
print(l)
'''
#
'''
s='jjhkjdhsakjhaskhsajdhkjfhdgfhgldldkjahhagjhgdasjlkasjkjgcjhcjvv'
d={k:s.count(k) for k in s }
print(d)
'''















#
'''
n=13
bin=0
p=1
while n>0:
    r=n%2
    bin+=r*p
    n//=2
    p*=10
print(bin)


'''
'''

def unique_names(names1, names2):
    uniquenames=[]
    for name in names1:
        if name not in uniquenames:
            uniquenames.append(name)
    for name in names2:
        if name not in uniquenames:
            uniquenames.append(name)
    return uniquenames

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia
'''


from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        d=dict(self.standings)
        d={k:dict(v) for k, v in d.items()}
        for k, v in d.items():
            v['games_played']*=-1
        l=sorted(d, key= lambda k:[d[k]['score'], d[k]['games_played']], reverse=True)
        return l[rank-1]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    r=int(input('enter rank '))
    print(table.player_rank(r))



#########
'''
while bin>0:
    r=bin%10
    n=(n*10)+r
    bin//=10
print(n)
'''

'''

def find_two_sum(numbers, target_sum):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i]+numbers[j]==target_sum:
                return (i,j)

if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
'''