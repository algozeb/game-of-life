from grid import count_neighbors

def update_grid(grid):
    """Applies Conway's Game of Life rules to generate the next state grid."""
    height = len(grid)
    width = len(grid[0])
    new_grid = [[0 for _ in range(width)] for _ in range(height)]
    
    for x in range(height):
        for y in range(width):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                # Rule: Live cell survives if it has 2 or 3 neighbors
                if neighbors in [2, 3]:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
            else:
                # Rule: Dead cell becomes alive if it has exactly 3 neighbors
                if neighbors == 3:
                    new_grid[x][y] = 1
                else:
                    new_grid[x][y] = 0
    return new_grid