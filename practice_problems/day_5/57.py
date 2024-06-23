class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def login(self):
        print("Admin logged in")

class Guest(User):
    def login(self):
        print("Guest logged in")

obj1 = Admin()
obj2 = Guest()
obj1.login()
obj2.login()