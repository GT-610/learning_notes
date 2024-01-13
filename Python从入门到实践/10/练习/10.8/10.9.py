from pathlib import Path
def read_file(path):
    try:
        content=path.read_text(encoding="UTF-8").split()
    except FileNotFoundError:
        print(f"The file {path} does not exist!")
    else:
        for word in content:
            print(word)

filenames=["cats.txt", "dogs.txt"]
for filename in filenames:
    path=Path(filename)
    read_file(path)