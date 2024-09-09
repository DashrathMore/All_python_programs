'''
lis = [1,2,2,2,4,5,6,6,6,7,7,3,3,3,8]
new=[]
for val in lis:
    if lis.count(val)>1 and val not in new:
        new.append(val)
        print(f'{val} is repeted {lis.count(val)} times')


'''

import json
d={'a':'hello', 'b':'good afternoon', 'c':'bye'}
with open('js.json','w') as fo:
    x=fo.writelines(str(d))
    json.dumps(x)

select * from table_name;
select count(*) from table_name;

select distinct(*) from table_name;


select count(address) from table_name groupp by addresses;
