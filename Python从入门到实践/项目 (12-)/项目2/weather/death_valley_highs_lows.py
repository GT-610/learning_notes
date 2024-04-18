from pathlib import Path
from datetime import datetime
import csv

path=Path("weather_data/death_valley_2021_simple.csv")
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

dates,highs,lows=[],[],[]
for row in reader:
    date=datetime.strptime(row[2],'%Y-%m-%d')
    high=int(row[3])
    low=int(row[4])
    dates.append(date)