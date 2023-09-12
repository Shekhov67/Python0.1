class Data(object):
    '''Информация о юзере'''

    def __init__(self, nameUser, surname):

        self.nameUser = nameUser
        self.surname = surname

    def infoUser(self):
        # '''Метод'''
        print('Name: ' + self.nameUser + '\n' + 'Surname: ' + self.surname)


'''User1 = Data('Andy', 'Jonson')
User2 = Data('Bobi', 'Ivanov')
User1.infoUser()
User2.infoUser()'''


class Lang(Data):
    # Info to lang
    def __init__(self, lang, nameUser):
        super().__init__(self, nameUser)
        self.lang = lang

    def infoLang(self):
        # Info to lang
        print(self.nameUser)


User3 = Lang('Russ', 'Jack')

print(User3.nameUser)
# print(User3.infoLang())
# print(User3.infoLang())
# User4 = LangUser('USA', 'Indian')
# print(str(User4.nameUser))
# print(User4.nameUser)
