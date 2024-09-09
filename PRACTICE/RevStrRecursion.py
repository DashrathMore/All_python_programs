# REVERSE STRING
def Rev(s,i):
    if(i == len(s)):
        return ''
    return Rev(s,i+1) + s[i]
s = 'DaShArAtH'
print(Rev(s,0))
##
'''
def Rev(s,i):
    if(i == -(len(s)+1)):
        return ''
    return s[i]+ Rev(s,i-1)
s = 'DaShArAtH MoRe'
print(Rev(s,-1))

def rev(s,i):
    if(i == -len(s)-1):
        return ''
    return s[i] + rev(s,i-1)
s= 'DasharatH'
print(rev(s,-1))'''