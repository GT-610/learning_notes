person0={
    'first_name':'Koji',
    'last_name':'Tadokoro',
    'age':24,
}

person1={
    'first_name':'John',
    'last_name':'Wang',
    'age':55,
}

person2={
    'first_name':'Kobe',
    'last_name':'Bryant',
    'age':42,
}


people=[person0,person1,person2]

for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
