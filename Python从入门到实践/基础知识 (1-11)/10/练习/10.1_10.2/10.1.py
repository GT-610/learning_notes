from pathlib import Path
path=Path("learning_python.txt")
content=path.read_text()

print(content)

lines=content.splitlines()

for line in lines:
    print(line)