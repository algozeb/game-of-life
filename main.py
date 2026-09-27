import time
from grid import create_grid
from engine import update_grid

# Grid Configuration
WIDTH = 76
HEIGHT = 22
ALIVE_CHAR = "█"
DEAD_CHAR = " "

# ANSI Escape Codes for Matrix Theme & UI
GREEN = "\033[92m"
BRIGHT_GREEN = "\033[1;92m"
DARK_GREEN = "\033[2;32m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

def main():
    grid = create_grid(WIDTH, HEIGHT)
    generation = 0
    peak_population = 0
    
    print(CLEAR_SCREEN, end="")
    
    try:
        while True:
            # Calculate active population
            current_population = sum(sum(row) for row in grid)
            peak_population = max(peak_population, current_population)
            generation += 1

            # Build the Terminal HUD Dashboard
            border = DARK_GREEN + "+" + "-" * (WIDTH) + "+" + RESET
            
            output = [
                f"{BRIGHT_GREEN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}",
                f"{BRIGHT_GREEN}║                 CONWAY'S CELLULAR AUTOMATON ENGINE v2.4                      ║{RESET}",
                f"{BRIGHT_GREEN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}",
                f"{GREEN} 📊 STATS: [Generation: {generation:04d}]  [Population: {current_population:03d}]  [Peak: {peak_population:03d}] {RESET}",
                border
            ]
            
            # Render grid rows inside a glowing border
            for row in grid:
                row_str = "".join([ALIVE_CHAR if cell == 1 else DEAD_CHAR for cell in row])
                output.append(f"{DARK_GREEN}|{RESET}{GREEN}{row_str}{RESET}{DARK_GREEN}|{RESET}")
                
            output.append(border)
            output.append(f"{DARK_GREEN} [Status: Running]  [Controls: Press Ctrl+C to safely exit terminal] {RESET}")
            
            # Print frame instantly at cursor home to completely eliminate screen flicker
            print(CURSOR_HOME + "\n".join(output), end="")
            
            # Compute next generation state
            grid = update_grid(grid)
            
            # Simulation speed (0.04s for a smooth fluid pace)
            time.sleep(0.04)
            
    except KeyboardInterrupt:
        print(f"\n\n{BRIGHT_GREEN}[!] Simulation terminated. Final Generation: {generation}{RESET}")

if __name__ == "__main__":
    main()