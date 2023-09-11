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


class LangUser(User):
    '''Language of user(потомок класса User)'''
    def __init__(self, lang, nameUser):
        super().__init__(self, nameUser)
        self.lang = lang
    def infoLang(self):
        return print(self.lang + '\n' + str(self.nameUser))

User3 = LangUser('Russ', 'Jack')
User3.infoLang()

'''Потому что по факту происходило 2 вещи:

мне выдавался ответ из конструктора
печатался мой принт, в которые по факту передавался объект экземпляра класса, он и давал эту __main__.Data object at 0x0000012A9357BFD0'''