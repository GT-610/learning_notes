from pathlib import Path
path=Path("learning_python.txt")
content=path.read_text()

print(content.replace("Python","C++"))
