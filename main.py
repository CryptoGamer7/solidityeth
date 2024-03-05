# Implementing the Game of Life in Python

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to generate a random initial state
def random_initial_state(grid_size):
    return np.random.choice([1, 0], grid_size * grid_size, p=[0.2, 0.8]).reshape(grid_size, grid_size)

# Function to update the state of the grid
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count live neighbors
            live_neighbors = np.sum(grid[i - 1:i + 2, j - 1:j + 2]) - grid[i, j]
            # Apply the Game of Life rules
            if grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and live_neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Function to animate the Game of Life
def animate(i):
    global grid
    grid = update_grid(grid)
    mat.set_data(grid)
    return [mat]

# Main function to run the Game of Life
def main():
    global grid, mat
    grid_size = 50  # Size of the grid
    grid = random_initial_state(grid_size)

    fig, ax = plt.subplots()
    mat = ax.matshow(grid, cmap='binary')
    ani = animation.FuncAnimation(fig, animate, frames=10, interval=200, save_count=50, blit=True)
    plt.show()

# Uncomment this to run the game
# main()

