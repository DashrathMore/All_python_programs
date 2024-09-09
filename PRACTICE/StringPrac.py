# reverse the word without reversing string
'''
s= 'hi my love you 3000'
res=''
ss=''
for ch in s:
    if ch != ' ':
        ss=ch+ss
    else:
        res+=ss+' '
        ss=''
res+=ss
print(res)
'''
# Reverse string without reversing word
'''
s= 'hi my love you 3000'
res=''
ss=''
for ch in s:
    if ch != ' ':
        ss+=ch
    else:
        res=' '+ss+res
        ss=''
res=ss+res
print(res)
'''
#Count Vovels
'''
s= 'hi I am Dashrath More I joined Jspiders in janaury'
count = 0
for ch in s:
    if ch in 'aeiouAEIOU':
        count+=1
        print(ch)
print(count)
'''
#Count Unique Vovels
'''
s= 'hi I am Dashrath More I joined Jspiders in janaury'
count=0
ss=''
for ch in s:
    if ch in 'aeiouAEIOU' and ch not in ss:
        count+=1
        ss+=ch
        print(ch)
print(count)
'''
#count consucative character
'''
s='aaabbbcccAAAAMMMAMmmm'
ss=''
c=1
for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        ss+=str(c)+s[i]
        c=1
ss+=str(c)+s[-1]
print(ss)
'''
#solve numand char:
'''
s='3a3b3c4A3M1A1M3m'
c=0
ss=''
for ch in s:
    if '0' <= ch <= '9':
        c+=int(ch)
    else:
        ss+=c*ch
        c=0
print(ss)
'''
# Highest Consuctive character
'''
s='aaabbbbcccAAAMMMAMmmmmm'
ss=''
c=1
h=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        if c>h:
            h=c
            ss=s[i]
        elif c==h:
            ss+=s[i]
        c=1
if c>h:
    h=c
    ss=s[i]
elif c==h:
    ss+=s[i]
print(h,ss)
'''
#count length of character:
'''
s= 'hi I am Dashrath More I joined Jspiders in janaury month'
c=0
h=0
ss=''
l=s.split()
for wrd in l:
    if len(wrd)>c:
        c=len(wrd)
        ss=wrd
    elif len(wrd)==c:
        ss+=' '+wrd
print(c,ss)
'''
#character in Clockwise
'''
s='Dashrath'
l=list(s)
for v in range(len(l)):
    l.append(l.pop(0))
    print(''.join(l))
'''
# Characters in anticlockwise
'''
s= 'ABCDE'
l=list(s)
for i in range(len(l)):
    l.insert(0,(l.pop(-1)))
    print(''.join(l))
'''
# Arange word based on length with list comprience
'''
s='ji meri jann kaisi hai'
l=s.split()
nl = [(len(wrd),wrd) for wrd in l]
nl.sort()
fl = [wrd for len, wrd in nl]
print(fl)
'''
# Arange word based on length
'''
s='hi meri jann kaisi hai my love darling'
ll=[]
l=s.split()
for wrd in l:
    ll.append((len(wrd),wrd))
ll.sort()
a=[]
for ln, wrd in ll:
    #a.append(wrd[1])
    a.append(wrd)
print(' '.join(a))
'''
# Aranging word based on last characcter / length/word
'''
s='hi meri jann kaisi hai my love darling'
l=s.split()
nl =[(wrd[-1],len(wrd),wrd) for wrd in l]
nl.sort()
fl=[wrd for ls,ln,wrd in nl]
print(' '.join(fl))
'''
# Aranging word based on last characcter / length/word
'''
s='hi meri jann kaisi hai my love darling'
l=s.split()
nl=[]
fl=[]
for wrd in l:
    nl.append((wrd[-1],len(wrd),wrd))
nl.sort()
for lc,ln,wrd in  nl:
    fl.append(wrd)
print(' '.join(fl))
'''
# Aranging word based on last characcter / length/word
'''
s='hi meri jann kaisi hai my love darling'
l=s.split()
nl=sorted(l,key=lambda wrd:(wrd[-1],len(wrd),wrd))
print(nl)
#print(list(nl))
'''
# UPPER TO LOWER AND LOWER TO UPPER WITHOUT USING INBUILT METHODS
s='hi hello my LOVE YOU 3000'
ss=''
for ch in s:
    c=''
    if 'a' <= ch <='z':
        ss+=chr(ord(ch)-32)
    elif "A" <= ch <= 'Z':
        ss+=chr(ord(ch)+32)
    else:
        ss+=ch
print(ss)