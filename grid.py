import random

def create_grid(width, height):
    """Initializes a grid with random cells and injects a moving Glider pattern."""
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    # Fill with sparse random life (density control)
    for x in range(height):
        for y in range(width):
            if random.random() < 0.2:  # 20% density
                grid[x][y] = 1
                
    # Inject a classic Glider at the top-left corner so it travels across screen
    glider = [
        (0, 1),
        (1, 2),
        (2, 0), (2, 1), (2, 2)
    ]
    start_x, start_y = 2, 2
    for gx, gy in glider:
        if start_x + gx < height and start_y + gy < width:
            grid[start_x + gx][start_y + gy] = 1
            
    return grid

def count_neighbors(grid, x, y):
    """Counts the 8 surrounding live neighbors (toroidal/wrapped edges for infinite feel)."""
    count = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            # Wrapped coordinates using modulo so shapes don't die at walls
            nx = (x + i) % height
            ny = (y + j) % width
            count += grid[nx][ny]
    return count