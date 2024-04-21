from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

# Show the plot thru GTK3 frontend
import matplotlib
matplotlib.use("Gtk3Agg")

path=Path("weather_data/sitka_weather_2021_full.csv")
lines=path.read_text().splitlines()

reader=csv.reader(lines)
header_row=next(reader)

# Get the date and PRCP
dates,prcps=[],[]
for row in reader:
    date=datetime.strptime(row[2],"%Y-%m-%d")
    try:
        prcp=float(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        prcps.append(prcp)

# Draw the highest temperature
plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
ax.plot(dates,prcps,color='green',alpha=0.5)

# Set the format
ax.set_title("Daily rainfall, 2021\nSitka, AK",fontsize=20)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall",fontsize=16)
ax.tick_params(labelsize=16)


# Show
plt.show()