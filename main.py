import os
import time
import sys
from grid import create_grid
from engine import update_grid

# Windows non-blocking keyboard listener setup
if os.name == 'nt':
    import msvcrt
    def check_keyboard():
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore').lower()
        return None
else:
    # Fallback placeholder for Linux/Mac if needed
    def check_keyboard():
        return None

# ANSI Theme Colors
GREEN = "\033[92m"
BRIGHT_GREEN = "\033[1;92m"
DARK_GREEN = "\033[2;32m"
RESET = "\033[0m"
CLEAR_SCREEN = "\033[2J"
CURSOR_HOME = "\033[H"

def get_terminal_size():
    try:
        columns, rows = os.get_terminal_size()
        width = max(40, min(columns - 6, 100))
        height = max(15, min(rows - 9, 30))
        return width, height
    except OSError:
        return 76, 22

def main():
    if os.name == 'nt':
        os.system('')

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
    paused = False
    delay = 0.05
    
    print(CLEAR_SCREEN, end="")
    
    try:
        while True:
            # Check for live user keystrokes without blocking simulation
            key = check_keyboard()
            if key:
                if key == 'q':
                    break
                elif key == ' ':
                    paused = not paused
                elif key == '+' or key == '=':
                    delay = max(0.01, delay - 0.01)  # Speed up
                elif key == '-' or key == '_':
                    delay = min(0.2, delay + 0.01)   # Slow down

            current_population = sum(sum(row) for row in grid)
            peak_population = max(peak_population, current_population)
            if not paused:
                generation += 1

            border = DARK_GREEN + "+" + "-" * width + "+" + RESET
            status_text = "PAUSED [Press SPACE to resume]" if paused else "RUNNING [SPACE=Pause, +/- = Speed, Q=Quit]"
            
            output = [
                f"{BRIGHT_GREEN}╔{'═' * (width + 2)}╗{RESET}",
                f"{BRIGHT_GREEN}║ {'MATRICULAR AUTOMATON ENGINE':^{width}} ║{RESET}",
                f"{BRIGHT_GREEN}╚{'═' * (width + 2)}╝{RESET}",
                f"{GREEN} 📊 [Gen: {generation:04d}] [Pop: {current_population:03d}] [Peak: {peak_population:03d}] [Speed: {int(1/delay)}fps] {RESET}",
                border
            ]
            
            for row in grid:
                row_str = "".join(["█" if cell == 1 else " " for cell in row])
                output.append(f"{DARK_GREEN}|{RESET}{GREEN}{row_str}{RESET}{DARK_GREEN}|{RESET}")
                
            output.append(border)
            output.append(f"{DARK_GREEN} {status_text} {RESET}")
            
            print(CURSOR_HOME + "\n".join(output), end="")
            
            if not paused:
                grid = update_grid(grid)
                
            time.sleep(delay)
            
    except KeyboardInterrupt:
        pass
    
    print(f"\n\n{BRIGHT_GREEN}[!] Simulation terminated. Total Generations: {generation}{RESET}")

if __name__ == "__main__":
    main()