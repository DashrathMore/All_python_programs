class father:
    fathername = 'VILAS'
    surname = 'MORE'
    add = 'chandgad'
class mother:
    mothername= ' MAYA'
    occupation = 'housewife'
class ch(father,mother):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print(f'{self.name} {self.surname} HE IS SON OF {self.mothername} AND {self.fathername} {self.surname}.')
c1 = ch('DASHRATH', 23)
c2= ch('BHAGAVANT', 25)
c1.print()
c2.print()