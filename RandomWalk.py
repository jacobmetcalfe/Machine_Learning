from random import choice


class Random_walk():
    # A class to generate random walks

    # Constructor
    def __init__(self, num_points=5000):
        self.num_points = num_points

    # Start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # Calculate the points in the walk

        # Runs until walk is filled with correct num of points
        while len(self.x_values) < self.num_points:
            # Movement pattern, how far to go and in what direction
            # Right or left movement
            x_direction = choice([1, -1])

            # How far to move by randomly selecting an int 0 - 4
            x_distance = choice([0, 1, 2, 3, 4])

            # find length of each step
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # if steps go nowhere, just continue to keep the walk going
            if x_step == 0 and y_step == 0:
                continue

        # Get the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

        # Store step into array
            self.x_values.append(next_x)
            self.y_values.append(next_y)
