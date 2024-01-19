try:
    a=int(input())
    b=int(input())
except ValueError:
    print("Are you sure you are inputing a number?")
else:
    print(a+b)