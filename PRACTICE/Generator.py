# Generator Without Function
'''
g=(i**2 for i in range(1,11))
while True:
    print(next(g))
'''
# Generator using function for loop
'''
def sample():
    yield 10
    yield 20
    yield 30
try:
    x=sample()
    for i in x:
        print(i)
except StopIteration:
    print('Completed....')
else:
    print('cool....')
finally:
    print('finally.....')
'''
# Generator using function while loop
'''
def num():
    a=10
    yield a
    a+=a
    yield a
    a+=a
    yield a
    a+=a
    yield a
try:
    x = num()
    while True:
        print(next(x))
except StopIteration:
    print("Completed.....")
'''
'''
g = ( i for i in range(1,10))
while True:
    print(next(g))
'''

def gen():
    yield 10
    yield 20
    yield 30
a=gen()
try:
    while True:
        print(next(a))
except StopIteration:
    print('completed...')
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x=(i for i in l if i%2==0)
print(list(x))


s='1000000000000000000000000000000000000000000020.3.6'
l=s.split('.')
ll=[]
for val in l:
    if len(val)==1:
        00.val='0'+val
        ll.append(val)
    else:
        ll.append(val)
print('.'.j.oin(ll))