
class Data():
    # '''Information of user'''

    def __init__(self, nameUser, surname):
        # '''Конструктор'''
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
    def __init__(self, lang, nameUser, surname):
        super().__init__(nameUser, surname)
        self.lang = lang

    def infoLang(self):
        # Info to lang
        print(self.lang + '\n' + str(self.nameUser))


User3 = Lang('Russ', 'Jack', 'Glinka')

# print(User3.infoLang())
print(User3.nameUser)
# print(User3.infoLang())
# User4 = LangUser('USA', 'Indian')
# print(str(User4.nameUser))
# print(User4.nameUser)
