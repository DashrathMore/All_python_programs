'''
input=[3, 3, 1, 2, 2, 2, 8, 8, 8, 8, 8]
new_list=sorted(input, key=lambda k:input.count(k))
print(new_list)
'''

#
'''
l=[5, 3, 6, 1, 7, 2, 17, 21, 31, 19]
prime=[]
for val in l:
    if lambda val: (val<=1 and all(val%i!=0 for i in range(2,val//2+1))):
        prime.append(val)
print(prime)
'''
##
'''
s='This is a test string'
s=s.replace(' ','')
print(s)
'''
'''
l=['hi',1,6,'wel',2,4,8,'come']
numbers=[]
string=[]
for ele in l:
    if type(ele)==int:
        numbers.append(ele)
    else:
        string.append(ele)
print(string)
print(numbers)
'''
'''
l=[3,2,6,8]
d=[v*v for v in l]
dic={}
for i in range(len(l)):
    dic[l[i]]=d[i]
print(dic)
'''
'''
l=[3,2,6,8]
d={k:k*k for k in l}
print(d)
'''

lis = [1,2,2,2,4,5,6,6,6,7,7,3,3,3,8]
nl=[]
for val in lis:
    if lis.count(val)>1 and  val not in nl:
        nl.append(val)
        print(f'{val} is reapeated {lis.count(val)} times')