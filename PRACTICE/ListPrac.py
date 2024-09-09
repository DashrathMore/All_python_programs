# Arenging list according to occurance
'''
l=[1,2,21,21,1,2,1,1,2,3,4,5,99,5,4]
nl= [(l.count(val),val) for val in l]
nl.sort()
print(nl)
fl=[val for i,val in nl]
print(fl)
'''
# Aranging list based on reminderr of 5
'''
l=[31,13,15,16,1,19,18]
nl=[[val%5, val] for val in l]
nl.sort()
print(nl)
fl=[val for r,val in nl]
print(fl)
'''
# Aranging list based on reminderr of 5(Using sorted method)
'''
l=[31,13,15,16,1,19,18]
nl=sorted(l,key=lambda val :(val%5,val))
print(nl)
'''
# Arenging list according to occurance(using Sorted)
l=[1,2,21,21,1,2,1,1,2,3,4,5,99,5,4]
fl = sorted(l,key=lambda val:(l.count(val),val))
print(fl)