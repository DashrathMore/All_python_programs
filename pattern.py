n = 5
for m in range(n, 0, -1):
    print('{}{}{}'.format('  ' * (n-m), '* ' * m, '* ' * (m-1)))