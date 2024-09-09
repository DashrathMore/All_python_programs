yer=int(input("enter year"))
if (yer%100==0):
    if(yer%400==0):
        print('century year is leap')
    else:
        print(" century year not leap year")
else:
    if(yer%4==0):
        print("year is leap")
    else:
        print("not leap year")