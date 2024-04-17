import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Create a randomwalk instance
while True:
    rw=RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig,ax=plt.subplots()


    # Color the dots according to the order
    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)
    # ax.plot(rw.x_values,rw.y_values,linewidth=1)

    ax.set_aspect('equal')

    # Re-draw the start and the finish
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    # Hide the axises
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running=input("Make another walk? [y/n]")
    if keep_running!='y':
        break