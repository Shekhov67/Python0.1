class House():
    '''Описание дома'''
    def __init__(self, number, street):
        '''Свойства дома'''
        self.number = number
        self.street = street

        self.age = 0

    def build(self):
        '''Строит дом'''

        print('Дом на улице ' + self.street + ', построен под номером ' + str(self.number))
    def age_of_house(self, year):
        '''Возраст дома'''
        self.age += year

class Prospect(House):
    def __init__(self, prospect, street):
        super().__init__(self, street)
        self.prospect = prospect
    def info(self):
        print(self.street)

PrHouse = Prospect('Lenina', 'ss')

print(PrHouse.prospect)
print(PrHouse.street)
PrHouse.info()