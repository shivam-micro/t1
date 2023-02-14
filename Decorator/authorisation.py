
class User:
    regular = 0
    admin = 1
    def __init__(self,username, usertype):
        self.username = username
        self.usertype = usertype

    def authenticate(func):
        def wrapper(self):
            if self.usertype is User.admin:
                return func(self)
            else:
                print("user must be admin")
        return wrapper

    def normal(self):
        print(f"{self.username} is doing normal things to do")

    @authenticate
    def admin(self):
        print(f"{self.username} is having admin access")
me = User("Myusername", "regular")
me.normal()
me.admin()
