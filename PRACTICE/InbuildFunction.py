# INBUILD FUNCTION
'''
# lambda
mul = lambda y: y*y
print(mul(22))

# MAP
m =list(map(lambda n: n**2,[1,2,3,4,5,6,7,8,9]))
print(m)
for i in m:
    print(i)
# 2.
l = ['DASH@gmail.com','dash@GMAIL.COM','DASH@gmail.COM']
n = list(map(lambda s : s.lower(),l))
print(n)
for ch in n:
    print(ch)'''

# FILTER

def eve(n):
    return n%2==0
l = [1,2,3,4,5,6,7,8,9]
f =(filter(eve,l))
print(list(f))
for i in f:
    print(i)
'''
#
l = [1,2,3,4,5,6,7,8,9]
f = filter(lambda n:n%2==0,l)
print(list(f))
print(list(f))
for i in f:
    print(i)'''

# ADDING 2 LIST
'''l1 = [2,3,4,5,6]
l2 = [10,20,30,40,50]
l = list(map(lambda x,y:x+y,l1,l2))
print(l)

#
l = input('enter l : ')
m = l.split()
print(int(m))'''