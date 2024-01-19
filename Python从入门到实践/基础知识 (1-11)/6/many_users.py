users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    },
}

for username,userinfo in users.items():
    print(f"Username: {username}")
    full_name=f"{userinfo['first']} {userinfo['last']}"
    location=userinfo['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")