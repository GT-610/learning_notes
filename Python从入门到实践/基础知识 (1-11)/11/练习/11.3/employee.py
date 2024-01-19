class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    def give_raise(self,value=0):
        if value:
            self.salary+=value
        else:
            self.salary+=5000
