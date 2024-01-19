from pathlib import Path
import json

def input_number(path):
    while True:
        try:
            number=int(input("Please enter your favourite number: "))
        except ValueError:
            print("Well, you're not entering a number.")
        else:
            contents=json.dumps(number)
            path.write_text(contents)
            break

def read_number(path):
    if path.exists():
        contents=path.read_text()
        numbers=json.loads(contents)
        print(f"I know your favourite number! It's {contents}!")

filename=input("So where do you want to save your number? ")
path=Path(filename+'.json')
input_number(path)

print("Now I'll read what your favourite number is...")
read_number(path)