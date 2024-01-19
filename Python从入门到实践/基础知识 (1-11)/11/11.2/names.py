from name_function import get_formatted_name
print("Enter 'q' to quit")
while True:
    first=input("\nPlease enter your first name: ")
    if first=='q':
        break
    last=input("\nPlease enter your last name: ")
    if last=='q':
        break

    formatted_name=get_formatted_name(first,last)
    print(f"Welcome, {first} {last}! ")