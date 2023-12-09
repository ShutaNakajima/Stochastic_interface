import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def move_point(point, length):
    x, y = point
    move = random.choice(['+e1', '-e1', '+e2', '-e2'])

    if move == '+e1':
        x += 1
    elif move == '-e1':
        x -= 1
    elif move == '+e2':
        y += 1
    elif move == '-e2':
        y -= 1

    x = max(-length, min(length, x))
    y = max(-length, min(length, y))

    return (x, y)

def update(frame):
    global fstate_array, fplaces_array, scatter
    new_points = []  # List to accumulate new point locations
    temp_state_array = np.copy(fstate_array)  # Temporary array for state updates

    # Loop to move points and mark new positions
    for i in range(size):
        for j in range(size):
            if fstate_array[i][j] == 1:
                x, y = move_point(fplaces_array[i][j], length)
                if 0 <= x - range_min < size and 0 <= y - range_min < size:
                    temp_state_array[x - range_min, y - range_min] = 1
                    fplaces_array[x - range_min, y - range_min] = (x, y)  # Update the position in fplaces_array
                    new_points.append((x, y))  # Add the new point location to the list

    # Update the scatter plot with new points
    scatter.set_offsets(new_points)

    # Loop to reset the states
    for i in range(size):
        for j in range(size):
            if temp_state_array[i][j] == 1:
                fstate_array[i][j] = 1

    fstate_array = temp_state_array  # Update the main state array

# Initialize parameters
n=100
num_steps = int(5*n)
length = n
size = 2 * n + 1
range_min = -n

# Create arrays
fstate_array = np.zeros((size, size), dtype=int)
fstate_array[length, length] = 1
fplaces_array = np.empty((size, size), dtype=object)

for i in range(size):
    for j in range(size):
        n = range_min + i
        m = range_min + j
        fplaces_array[i, j] = (n, m)

# Set up the plot
fig, ax = plt.subplots()
plt.xlim(-length, length)
plt.ylim(-length, length)
plt.title('Random Walk Animation')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.grid(True)

# Initialize the scatter plot
initial_positions = [(i, j) for i in range(size) for j in range(size) if fstate_array[i][j] == 1]
scatter = ax.scatter([p[0] for p in initial_positions], [p[1] for p in initial_positions])

# Create animation
ani = FuncAnimation(fig, update, frames=num_steps, repeat=True)

plt.show()
