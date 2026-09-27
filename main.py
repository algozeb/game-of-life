import time
from grid import create_grid
from engine import update_grid

# Upgraded configuration (Bigger grid dimensions)
WIDTH = 80
HEIGHT = 30
ALIVE_CHAR = "█"
DEAD_CHAR = " "

# ANSI escape codes for Matrix Green color and smooth rendering
GREEN = "\033[92m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

def main():
    grid = create_grid(WIDTH, HEIGHT)
    
    # Clear the terminal screen once at start
    print(CLEAR_SCREEN, end="")
    
    try:
        while True:
            # Build the frame buffer
            output = [f"{GREEN}=== MATRIX CELLULAR AUTOMATON ENGINE (80x30) ==={RESET}"]
            for row in grid:
                output.append(GREEN + "".join([ALIVE_CHAR if cell == 1 else DEAD_CHAR for cell in row]) + RESET)
            output.append(f"\n{RESET}[Status: Running Smoothly | Press Ctrl+C to exit]")
            
            # Move cursor back to top-left and print instantly (Eliminates flicker)
            print(CURSOR_HOME + "\n".join(output), end="")
            
            # Compute next generation
            grid = update_grid(grid)
            
            # Frame delay for smooth animation speed
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\n\033[0mSimulation terminated gracefully.")

if __name__ == "__main__":
    main()