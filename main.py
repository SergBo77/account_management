class User:
    def __init__(self, user_id, name, access_level):
        # Инициализация объекта пользователя
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        # Метод для получения идентификатора пользователя
        return self.__user_id

    def get_name(self):
        # Метод для получения имени пользователя
        return self.__name

    def get_access_level(self):
        # Метод для получения уровня доступа пользователя
        return self.__access_level

    def get_info_user (self):
        # Метод для вывода информации о пользователе
        print({self.__user_id})
        print(self.__name)
        print(self.__access_level)

class Admin(User):
    def __init__(self, user_id, name, access_level):
        # Инициализация объекта администратора
        super().__init__(user_id, name, access_level)
        self.__admin_access = access_level
        self.users = []

    def add_user(self, user):
        # Метод для добавления пользователя администратором
        self.users.append(user)

    def remove_user(self, user):
        # Метод для удаления пользователя администратором
        self.users.remove(user)

    def get_admin_access(self):
        # Метод для получения уровня доступа администратора
        return self.__admin_access


# Пример использования создаем объект user:
user1 = User(1, "Мария", 'user')
user2 = User(2, "Виктор", 'user')
user3 = User(3, "Федр", 'user')

# Создаем объект admin класса admin
admin = Admin(4, "Иван", "admin")

# Добавляем список пользователей:
admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(admin)

# Выводим информацию о пользователях
for user in admin.users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Выводим информацию об уровне доступа администратора
print(admin.get_admin_access())

# Удаляем user1 из списка пользователей
admin.remove_user(user1)

# Выводим информацию о пользователях после удаления
for user in admin.users:
    print(f"ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}")

# Выводим информацию о пользователе user1
user1.get_info_user()