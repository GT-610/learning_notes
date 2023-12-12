favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
}

# language=favourite_languages['sarah'].title()
# print(f"Sarah's favourite language is {language}.")

# for name in favourite_languages:
#    print(f"{name.title()}")

friends=['phil','sarah']

for name in favourite_languages.keys():
    print(f"Hi, {name.title()}.")

    if name in friends:
        language=favourite_languages[name].title()
        print(f"\t{name.title()},I see you love {language}!")
