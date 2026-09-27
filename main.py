import os
import time
import sys
from grid import create_grid
from engine import update_grid

# Enable ANSI escape code interpretation on Windows terminals
if os.name == 'nt':
    os.system('')

# ANSI Theme Colors
GREEN = "\033[92m"
BRIGHT_GREEN = "\033[1;92m"
DARK_GREEN = "\033[2;32m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

def get_terminal_size():
    """Dynamically fetches terminal dimensions with safe fallbacks."""
    try:
        columns, rows = os.get_terminal_size()
        # Leave room for HUD headers and borders
        width = max(40, min(columns - 6, 100))
        height = max(15, min(rows - 8, 35))
        return width, height
    except OSError:
        return 76, 22

def main():
    print(CLEAR_SCREEN)
    print(f"{BRIGHT_GREEN}=== CONWAY'S CELLULAR AUTOMATON ENGINE ==={RESET}")
    print(f"{GREEN}Select Initial Pattern Preset:{RESET}")
    print(" 1. Random Chaos Grid")
    print(" 2. Travelling Glider")
    print(" 3. Pulsar Oscillator")
    
    choice = input(f"{BRIGHT_GREEN}Enter choice [1-3, default 1]: {RESET}").strip()
    pattern_map = {"1": "random", "2": "glider", "3": "pulsar"}
    selected_pattern = pattern_map.get(choice, "random")

    width, height = get_terminal_size()
    grid = create_grid(width, height, pattern=selected_pattern)
    
    generation = 0
    peak_population = 0
    print(CLEAR_SCREEN, end="")
    
    try:
        while True:
            current_population = sum(sum(row) for row in grid)
            peak_population = max(peak_population, current_population)
            generation += 1

            border = DARK_GREEN + "+" + "-" * width + "+" + RESET
            
            output = [
                f"{BRIGHT_GREEN}╔{'═' * (width + 2)}╗{RESET}",
                f"{BRIGHT_GREEN}║ {'MATRICULAR AUTOMATON ENGINE':^{width}} ║{RESET}",
                f"{BRIGHT_GREEN}╚{'═' * (width + 2)}╝{RESET}",
                f"{GREEN} 📊 [Gen: {generation:04d}]  [Pop: {current_population:03d}]  [Peak: {peak_population:03d}]  [Size: {width}x{height}] {RESET}",
                border
            ]
            
            for row in grid:
                row_str = "".join(["█" if cell == 1 else " " for cell in row])
                output.append(f"{DARK_GREEN}|{RESET}{GREEN}{row_str}{RESET}{DARK_GREEN}|{RESET}")
                
            output.append(border)
            output.append(f"{DARK_GREEN} [Status: Running]  [Press Ctrl+C to exit] {RESET}")
            
            # Print frame instantly to eliminate flicker
            print(CURSOR_HOME + "\n".join(output), end="")
            
            grid = update_grid(grid)
            time.sleep(0.04)
            
    except KeyboardInterrupt:
        print(f"\n\n{BRIGHT_GREEN}[!] Simulation ended. Total Generations: {generation}{RESET}")

if __name__ == "__main__":
    main()