import os
import time
from grid import create_grid
from engine import update_grid

# Configuration constants
WIDTH = 40
HEIGHT = 20
ALIVE_CHAR = "█"
DEAD_CHAR = " "

def render(grid):
    """Clears the terminal and renders the current grid frame."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    output = []
    for row in grid:
        output.append("".join([ALIVE_CHAR if cell == 1 else DEAD_CHAR for cell in row]))
    
    print("=== TERMINAL CELLULAR AUTOMATON SIMULATION ===")
    print("\n".join(output))
    print("\n[Running... Press Ctrl+C to exit]")

def main():
    grid = create_grid(WIDTH, HEIGHT)
    try:
        while True:
            render(grid)
            grid = update_grid(grid)
            time.sleep(0.1) # Controls animation speed
    except KeyboardInterrupt:
        print("\nSimulation terminated gracefully.")

if __name__ == "__main__":
    main()