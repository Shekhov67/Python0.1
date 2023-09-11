class User():
    '''Information of user'''

    def __init__(self, name, surname, age, dateOfBirth):
        '''Конструктор'''
        self.name = name
        self.surname = surname
        self.age = age
        self.dateOfBirth = dateOfBirth

    def infoUser(self):
        '''Метод'''
        print('Name: ' + self.name + '\n' + 'Surname: ' + self.surname + '\n' + 'Age: ' + str(
            self.age) + '\n' + 'Birthday: ' + self.dateOfBirth)


User1 = User('Andy', 'Jonson', 23, '12.05.2000')

User1.infoUser()


class langUser(User):
    '''Language of user(потомок класса User)'''
    def __init__(self, lang, name, age, dateOfBirth):
        super().__init__(self, name, age, dateOfBirth)
        self.lang = lang


User2 = langUser("Russ", "Bobi", 26, '21.05.1999')

print(User2.lang)

