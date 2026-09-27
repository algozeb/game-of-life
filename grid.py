import random

def create_grid(width, height):
    """Initializes a grid with random live (1) and dead (0) cells."""
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def count_neighbors(grid, x, y):
    """Counts the 8 surrounding live neighbors for a specific cell coordinate."""
    count = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < height and 0 <= ny < width:
                count += grid[nx][ny]
    return count