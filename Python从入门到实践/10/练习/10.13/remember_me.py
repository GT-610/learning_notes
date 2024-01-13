from pathlib import Path
import json

def get_stored_user(path):
    if path.exists():
        contents=path.read_text()
        user=json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    new_user={
        "username":"",
        "age":0,
        "hobby":"",
    }
    new_user["username"]=input("What is your name? ")
    new_user["age"]=int(input("And how old are you? "))
    new_user["hobby"]=input("And what do you like? ")
    contents=json.dumps(new_user)
    path.write_text(contents)

def greet_user():
    path=Path('user.json')
    user=get_stored_user(path)
    if user:
        print("Welcome back, "+user['username']+'!')
    else:
        user=get_new_user(path)
        print("We'll remember you when you come back, "+user['username']+'!')

greet_user()
