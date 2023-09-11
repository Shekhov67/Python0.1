class User():
    '''Information of user'''

    def __init__(self, nameUser, surname):
        '''Конструктор'''
        self.nameUser = nameUser
        self.surname = surname

    def infoUser(self):
        '''Метод'''
        print('Name: ' + self.nameUser + '\n' + 'Surname: ' + self.surname)


User1 = User('Andy', 'Jonson')
User2 = User('Bobi', 'Ivanov')
User1.infoUser()
User2.infoUser()


'''class LangUser(User):
    Language of user(потомок класса User)
    def __init__(self, lang, nameUser):
        super().__init__(self, nameUser)
        self.lang = lang


User2 = LangUser("Russ", "Bobi")

print(User2.lang)
print(User2.nameUser)
#print(User2.surname)'''



