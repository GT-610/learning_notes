from pathlib import Path
path=Path("Python从入门到实践/10/练习/learning_python.txt")
content=path.read_text()

print(content)

lines=content.splitlines()

for line in lines:
    print(line)