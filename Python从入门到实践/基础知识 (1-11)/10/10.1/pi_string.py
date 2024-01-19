from pathlib import Path
path=Path('Python从入门到实践/10/10.1/pi_million_digits.txt')
contents=path.read_text()

lines=contents.splitlines()
pi_string=""
for line in lines:
    pi_string+=line.lstrip()

print(f"{pi_string[:52]}...")