import matplotlib.pyplot as plt
from RandomWalk import Random_walk
import time

timer = []
start = time.time()

x = 0
# Keep making new walks, as long as the program is active.
while True:

    # Make a random walk, and plot the points.
    rw = Random_walk()
    rw.fill_walk()

    # Screen size modification
    plt.figure(figsize=(10, 6))

    # Create list of all of the points
    point_numbers = list(range(rw.num_points))

    # Color the points based on which ones happened first
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)

    # Plotting the starting and Ending Points
    # Start
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)

    # End
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # Titling and Axes
    plt.title('Random Computer Generated Movement')

    # Legend
    legend = plt.legend()

    plt.show()

    # allow user to see if they want to keep inputting into the graph
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break


