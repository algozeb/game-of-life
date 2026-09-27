import random

def create_grid(width, height, pattern="random"):
    """Initializes a grid with dynamic dimensions and selectable patterns."""
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    if pattern == "random":
        for x in range(height):
            for y in range(width):
                if random.random() < 0.25:
                    grid[x][y] = 1
                    
    elif pattern == "glider":
        glider = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        start_x, start_y = height // 4, width // 4
        for gx, gy in glider:
            if start_x + gx < height and start_y + gy < width:
                grid[start_x + gx][start_y + gy] = 1
                
    elif pattern == "pulsar":
        # Classic Pulsar oscillator centered on the grid
        cx, cy = height // 2, width // 2
        offsets = [
            (-2, -4), (-1, -4), (1, -4), (2, -4),
            (-2, 4), (-1, 4), (1, 4), (2, 4),
            (-4, -2), (-4, -1), (-4, 1), (-4, 2),
            (4, -2), (4, -1), (4, 1), (4, 2),
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (-2, 1), (-1, 2), (1, 2), (2, 1),
        ]
        for ox, oy in offsets:
            nx, ny = cx + ox, cy + oy
            if 0 <= nx < height and 0 <= ny < width:
                grid[nx][ny] = 1
                
    return grid

def count_neighbors(grid, x, y):
    """Counts 8 neighbors using toroidal (wrapped) edge physics."""
    count = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx = (x + i) % height
            ny = (y + j) % width
            count += grid[nx][ny]
    return count