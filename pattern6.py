n = 5
for i in range(1, 6):
    for j in range(1,n+1):
        print(j, end = ' ')
    print()
n = 5
for i in range(1, n):
    for j in range(i, n+1):
        print(j, end = '  ')
    print()