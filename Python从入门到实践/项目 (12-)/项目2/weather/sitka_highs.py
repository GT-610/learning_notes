from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Show the plot through GTK3 frontend
import matplotlib
matplotlib.use("Gtk3Agg")


path=Path('weather_data/sitka_weather_2021_simple.csv')
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

# Get the date and the highest temperature
dates,highs,lows=[],[],[]
for row in reader:
    date=datetime.strptime(row[2],"%Y-%m-%d")
    high=int(row[4])
    low=int(row[5])
    dates.append(date)
    highs.append(high)
    lows.append(low)

# Draw the highest temperature
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates,highs,color='red',alpha=0.5)
ax.plot(dates,lows,color='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# Set the format
ax.set_title("Daily High and Low Temperatures, 2021",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize=16)
ax.tick_params(labelsize=16)
ax.xticks=(10,80,10)

# Show
plt.show()