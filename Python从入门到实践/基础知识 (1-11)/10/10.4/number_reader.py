from pathlib import Path
import json

path=Path("numbers.json")
try:
    contents=path.read_text()
except FileNotFoundError:
    print(f"File {path} not found.\n")
else:
    numbers=json.loads(contents)
    print(numbers)
