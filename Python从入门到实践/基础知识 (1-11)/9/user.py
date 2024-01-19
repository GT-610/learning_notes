class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=0

    def describe_user(self):
        print(f"Name:{self.first_name} {self.last_name}\nAge: {self.age}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self,count):
        self.login_attempts+=count
    
    def reset_login_attempts(self):
        self.login_attempts=0

class Privileges:
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=Privileges()
    def show_privileges(self):
        print(f"Admin {self.first_name} {self.last_name} {self.privileges.privileges}.")