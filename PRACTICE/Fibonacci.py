#fib series
'''
print('fib series')
def fib(l,f=0,s=1):
    if f>l:
        return
    print(f)
    return fib(l,s,s+f)
print()
l=400
fib(10)
'''
# WAP to print first 7 fibonacci numbers
'''
f,s=0,1
l=7
for i in range(l):
    print(f)
    f,s=s,f+s
'''
# WAP to print 7th fibonacci numbers
'''
f,s=0,1
l=int (input('enter'))
for i in range(l):
    t=f
    f,s=s,f+s
print(t)
'''
# WAP to print 7th fibonacci numbers using Recursion
'''
def fib(n):
    if n==1 or n==2:
        return (n-1)
    return fib(n-1)+fib(n-2)
print(fib(7))
'''
# WAP to check given number is fibonacci number or not
'''
f,s=0,1
num=10
while f<= num:
    if f==num:
        print('Number is Fibonacci')
        break
    f,s=s,f+s
else:
    print('Not a Fibonacei')
'''
# WAP to print fib series using Iterator
'''
class fib:
    def  __init__(self,n):
        self.first=0
        self.second=1
        self.total=n
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        t=self.first
        if self.count == self.total:
            raise StopIteration
        self.first,self.second=self.second,self.first+self.second
        self.count+=1
        return t
ob=fib(7)
i=iter(ob)
while True:
    print(next(i))
'''
# WAPto print fib
'''
l=[0,1]
n=7
while len(l)<n:
    l.append(l[-1]+l[-2])
print(l)
'''
