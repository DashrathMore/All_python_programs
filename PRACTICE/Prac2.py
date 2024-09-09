def SingleTon(arg):
    d={}
    def inner():
       if arg not in d:
           d[arg]=arg()
       return d[arg]
    return inner
@SingleTon
class FFX:
    def __init__(self):
        self.tickets=100
    def Booking(self):
        t = int(input("Enter Tickets"))
        if self.tickets >= t:
            self.tickets-=t
            print('Ticket Booked Successgfully...')
        else:
            print('Tickets Not Avaliable...')
@SingleTon
class AADIPURUSH:
    def __init__(self):
        self.tickets=100
    def Booking(self):
        t = int(input("Enter Tickets"))
        if self.tickets >= t:
            self.tickets-=t
            print('Ticket Booked Successgfully...')
        else:
            print('Tickets Not Avaliable...')

def Tic():
    print('''CHOOSE OPTION...
    1=FFX
    2=AADIPURUSH''')
    i = int(input('Enter option'))
    if (i ==1):
        ob=FFX()
        ob.Booking()
    elif (i==2):
        ob = AADIPURUSH()
        ob.Booking()
    else:
        print('invalid option....')

Tic()
Tic()
Tic()