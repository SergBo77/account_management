class User:
    def __init__(self, user_id, name, access_level):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def get_info_user (self):
        print({self.__user_id})
        print(self.__name)
        print(self.__access_level)

class Admin(User):
    def __init__(self, user_id, name, access_level):
        super().__init__(user_id, name, access_level)
        self.__admin_access = access_level
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def get_admin_access(self):
        return self.__admin_access


# Пример использования:
user1 = User(1, "Мария", 'user')
user2 = User(2, "Виктор", 'user')
user3 = User(3, "Федр", 'user')

admin = Admin(4, "Иван", "admin")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(admin)

for user in admin.users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

print(admin.get_admin_access())

admin.remove_user(user1)

for user in admin.users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

user1.get_info_user()