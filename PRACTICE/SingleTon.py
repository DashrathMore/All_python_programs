def SingleTon(cls):
    d={}
    def Inner():
        if cls not in d:
            d[cls] = cls()
        return d[cls]
    return Inner


@SingleTon
class Spy:
    def __init__(self):
        self.Tickets=300
    def Booking(self):
        n = int(input("Enter Number of Tickets : "))
        if self.Tickets>=n:
            self.Tickets -= n
            print("Tickets Booked Sucessfully ! ! !")
        else:
            print("Tickets are Not Availiable...")
            print(f'Only Availiable Tickets are {self.Tickets}')


@SingleTon
class Flash:
    def __init__(self):
        self.Tickets=300
    def Booking(self):
        n = int(input('Enter Number of Tickets : '))
        if n <= self.Tickets:
            self.Tickets -= n
            print('Tickets Booked Successfuly ! ! !')
        else:
            print('Tickets are Not Availiable ...')
            print(f'Only Avaliable Tickets are  {self.Tickets}')


@SingleTon
class Sargent:
    def __init__(self):
        self.Tickets=300
    def Booking(self):
        n = int(input('Enter Number of Tickets : '))
        if self.Tickets >= n:
            self.Tickets -= n
            print('Tickets Booked Successfully!!!')
        else:
            print('Tickets are not avliable...')
            print('only {} are avaliable'.format(self.Tickets))

def BookMyShow():
    option = int(input("""Choose Option...
    1.SPY
    2.FLASH
    3.Sargent
    """))
    if option==1:
        ob=Spy()
        ob.Booking()
    elif option == 2:
        obj = Flash()
        obj.Booking()
    elif option == 3:
        ob = Sargent()
        ob.Booking()
    else:
        print("Invalid Option")
    print("-------------------------")
while True:
    BookMyShow()