n = 5
j = 1
for i in range(1, n+1):
    print('* ' *j)
    j=j+1 if i<n//2+1 else j-1