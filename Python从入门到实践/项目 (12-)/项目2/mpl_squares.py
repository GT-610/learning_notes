import matplotlib
matplotlib.use('GTK3Agg')

import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values=[x**2 for x in x_values]

# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic',
# 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright',
# 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid',
# 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper',
# 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks',
# 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()
#ax.scatter(x_values,y_values,s=10)
ax.axis([0,1100,0,1_100_000])

ax.plot(x_values,y_values,color=(0.3,0.5,0.4),linewidth=3)

# Set the texts
ax.set_title("Square numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of value",fontsize=14)
ax.tick_params(labelsize=14)

plt.show()