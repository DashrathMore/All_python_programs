# perfrct number means sum of all factors equal to given number
# 28 factors have=> 1, 2, 4, 7, 14 sum of all factors is equal to
# given number then its PERFECT NUMBER.
# 27 factors have=> 1, 3, 9 sum of all factors is not equal to given
# number then its not PERFECT NUMBER.
n = 27
a = 0
c = n
for i in range(1, (n//2+1)):
    if(n % i== 0):
        a += i
        print(i)
print(a)
if (a == c):
    print('perfect number')
else:
    print("not perfect")