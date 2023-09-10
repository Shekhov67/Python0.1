class House():
    '''Описание дома'''
    def __init__(self, street, number):
        '''Свойства дома'''

        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        '''Строит дом'''

        print('Дом на улице ' + self.street + ', построен под номером ' + str(self.number))
    def age_of_house(self, year):
        '''Возраст дома'''
        self.age += year



House1 = House("Moskovskia", 27)
House2 = House("Moskovskia", 28)

'''House1.build()
House2.build()
House1.age_of_house(5)
print(House1.age)
print(House1.street)'''

class Prospect(House):
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = Prospect('Lenina', 9)
print(PrHouse.prospect)
print(PrHouse.number)