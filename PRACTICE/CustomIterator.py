# Custom Iterationn 1 t0 10
'''
class num():
    def __init__(self, st, ed):
        self.start=st
        self.end=ed
    def __iter__(self):
        return self
    def __next__(self):
        cur = self.start
        self.start+=1
        if cur >self.end:
            raise StopIteration
        return cur


ob=num(1,10)
i= iter(ob)
while True:
    print(next(i))
'''


# Custom Iterationn 1 t0 -10
'''
class num:
    def __init__(self,st,ed):
        self.start=st
        self.end = ed
    def __iter__(self):
        return self
    def __next__(self):
        cur = self.start
        self.start-=1
        if cur == self.end-1:
            raise StopIteration
        return cur
x=num(1,-10)
i=iter(x)
while True:
    print(next(x))

'''


# Custom Iterationn 19 t0 -19
'''
class num:
    def __init__(self,st,ed):
        self.start=st
        self.end=ed
    def __iter__(self):
        return self
    def __next__(self):
        cur=self.start
        self.start-=1
        if cur == self.end-1:
            raise StopIteration
        return cur
o=num(19,-19)
for i in o:
    print(i)


'''


'''
n=9
for i in range(n,0,-1):
    for j in range(1,i+1):
        if j == i:
            print(j)
        else:
            print(j,"*",end=' ')

'''
'''
l=[1,12,13,123,12345]
nl=[]
for val in l:
    s=str(val)
    if len(s) > 1:
        add=0
        for v in s:
            add+=int(v)
        nl.append(add)
    else:
        nl.append(val)
print(nl)
sum=0
for val in nl:
    sum+=val
print(sum)
'''
'''
m= filter(lambda a: a%2==0, range(1,11))
while True:
    print(next(m))
'''
class error:
    def __init__(self,st,ed):
        self.start = st
        self.end = ed
    def __iter__(self):
        return self
    def __next__(self):
        c = self.start
        self.start+=1
        if c==self.end+1:
            raise StopIteration
        return c
ob=error(1,10)
i=iter(ob)
while True:
    print(next(i))