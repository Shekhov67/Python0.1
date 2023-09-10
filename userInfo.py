class User():
    '''Information of user'''

    def __init__(self, name, surname, age, dateOfBirth):
        self.name = name
        self.surname = surname
        self.age = age
        self.dateOfBirth = dateOfBirth

    def infoUser(self):
        print('Name: ' + self.name + '\n' + 'Surname: ' + self.surname + '\n' + 'Age: ' + str(
            self.age) + '\n' + 'Birthday: ' + self.dateOfBirth)


user1 = User('Andy', 'Jonson', 23, '12.05.2000')

user1.infoUser()


class UserAnketa(User):

    def __init__(self, work, name):
        super().__init__(self, name)
        self.work = work


user2 = UserAnketa('IT', 'Bob')
print(user2.work)
