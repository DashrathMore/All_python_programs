'''
# int
n=10
nm=int()
print(type(n),n)
print(type(nm),nm)
#print(len(n),len(nm))

# Float
n=15.89
nm=float()
print(type(n),n)
print(type(nm),nm)
#print(len(n),len(nm))

# Boolien
n=True
nm=bool()
print(type(n),n)
print(type(nm),nm)
#print(len(n),len(nm))

# Complex
n=5j+3j
nm=complex()
print(type(n),n)
print(type(nm),nm)
#print(len(n),len(nm))

# String
s='Dashrath'
ss=str()
print(s, type(s))
print(ss, type(ss))
print(len(s))
print(len(ss))

# List
l=[1,20,'abcd']
lf=list()
ll=[]
print(l, type(l))
print(lf, type(lf))
print(ll, type(ll))
print(len(l))
print(len(lf))
print(len(ll))

# Tuple
l=(1,20,'abcd')
lf=tuple()
ll=()
print(l, type(l))
print(lf, type(lf))
print(ll, type(ll))
print(len(l))
print(len(lf))
print(len(ll))

# Set
l={1,2,3,0,True,False, 'ab'}
lf=set()
ll={10}
print(l, type(l))
print(lf, type(lf))
print(ll, type(ll))
print(len(l))
print(len(lf))
print(len(ll))

# Dict
l={'a':10, 1:20}
lf=dict()
ll={}
print(l, type(l))
print(lf, type(lf))
print(ll, type(ll))
print(len(l))
print(len(lf))
print(len(ll))
'''

"""
import sys
d_s={'I':10,'if':int(),'f':10.10,'ff':float(),'b':True,'bf':bool(),
     'c':7j+25j,'cf':complex()}
d_c={'s':'Dashrath','sf':str(),'l':[10,20,'1bc'],
     'lf':list(),'t':(1,2,3,1,'Dashrath'),'tf':tuple(),
     'st':{1,2,0,True,False,'Das'},'stf':set(),
     'd':{2:10,'a':20, 1:'Dashrath'},'df':dict()}
d.
"""
'''
import sys
l=[10,int(),10.10,float(),True,bool(),7j,complex()]
ll=['abc',str(),[10,20,'abc'],list(),{1,2,3},(12,23,34), tuple() ,
    set(),{1:20,'a':100},dict(),range(10),]
l.extend(ll)
for val in l:
    print(val, type(val),' size:',sys.getsizeof(val))
'''
'''
import sys

l=[10,int(),1000000000000000000,
10.10,float(),
True,bool(),
7j,complex(),
'abc',str(),
[10,20,'abc'],list(),
(12,23,34), tuple(),
{1,2,3},set(),
{1:20,'a':100},dict(),
range(10),]
for val in l:
    print(val, type(val),' size:',sys.getsizeof(val))

#print[1,2,3]*2

'''
'''
# String

comp_name='1,2,32,3,4'
#comp_name=comp_name.split()
for ch in comp_name:
        print(eval(ch))
print(comp_name)
'''

#ACCEPT10 NAMES WHICH IS START WITH VOVELS
'''
import re
rejected_names=[]
accepted_names=[]
#while len(accepted_names) < 10:
for i in range(10):
    name=input('Enter person name')
    if re.match('[aeiouAEIOU]',name):
        accepted_names.append(name)
    else:
        rejected_names.append(name)
print('accepted_names :',accepted_names)
print('rejected_names :',rejected_names)
'''

products,price,quantity=[],[],[]
for i in range(2):
    products.append(input('Enter Product Name : '))
    price.append(int(input('Enter Price of Product :')))
    quantity.append(int(input('Enter Product Quantity :')))
while True:
    print('''Choose Option :
    1. Total price
    2. Maximun selling product
    3. update the quantity''')
    option=int(input('input option (1/ 2/ 3) : '))
    if option==1:
        print('Total price of the products :',sum([price[i]*quantity[i] for i in range(len(price))]))
    elif option==2:
        print('maximum selling product :',products[quantity.index(max(quantity))])
    elif option==3:
        prod_name=input('enter name of product which value you want to chang :')
        ind=products.index(prod_name)
        quantity[ind]=quantity[ind]+int(input('Enter only additional quantity :'))
    else:
        print('invalid option!!!...')
    print('products :',products)
    print('price :',price)
    print('quantity :',quantity)