# a number which is multiple with 1, 2, 3 and concatenate all
# and after check 1-9 present in number or not
# 327= 327*1 , 327*2 , 327*3= 327, 654, 981
#concatenate ==>  327654981
# in that number check 1-9 present in number or not!
num = 327
s = str(num*1)+str(num*2)+str(num*3)
print(s)
for i in range(1,10):
    if (str(i) not in s):
        print('not fascinating')
        break
else:
    print('fascinating number')