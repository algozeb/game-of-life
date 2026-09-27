# Terminal Cellular Automaton Engine

A modular, Python-based implementation of Conway's Game of Life running directly in the command-line interface. Built with a clean separation of concerns, managing grid states, neighbor calculations, and real-time terminal rendering.

## Features
- **Modular Architecture:** Separated logic across `grid.py`, `engine.py`, and `main.py`.
- **Real-Time Simulation:** Dynamic frame-by-frame updates using standard library components.
- **Cross-Platform CLI:** Compatible with Windows, macOS, and Linux terminals.

## How to Run
1. Ensure you have Python installed.
2. Clone the repository and navigate to the folder.
3. Run the simulation:
   ```bash
   python main.py