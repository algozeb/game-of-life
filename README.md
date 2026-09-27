# Terminal Cellular Automaton Engine

An advanced, feature-rich implementation of Conway’s Game of Life running entirely in the command-line interface. Built with a clean separation of concerns, modern object-oriented principles, dynamic terminal auto-sizing, and live interactive controls.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## 🚀 Key Features

- **Modular Architecture:** Clean software design separated across core logic modules (`grid.py`, `engine.py`, `main.py`).
- **Dynamic Terminal Sizing:** Automatically detects terminal dimensions and scales the simulation grid to fit any window size safely.
- **Cross-Platform Support:** Native ANSI color escape code handling for smooth, glowing Matrix-green rendering across Windows, macOS, and Linux.
- **Interactive Runtime Controls:** Pause, resume, speed up, or slow down the simulation live in real-time using non-blocking keyboard inputs (`SPACE`, `+`, `-`, `Q`).
- **Pattern Presets:** Selectable startup presets including Random Chaos, Travelling Gliders, and Pulsar Oscillators.
- **Toroidal Grid Physics:** Edge-wrapping boundaries ensuring cellular shapes never clip or die prematurely at walls.
- **Live HUD Dashboard:** Real-time generation counting, active population tracking, and peak population metrics.
- **Automated Unit Tests:** Includes a dedicated unit test suite (`test_engine.py`) verifying neighbor calculations and rule state transitions.

---

## 🛠️ Project Structure

```text
game_of_life/
│
├── grid.py         # Grid initialization, pattern presets, and neighbor counting
├── engine.py       # Conway's Game of Life state transition rules
├── main.py         # Real-time CLI rendering loop and live keyboard listener
├── test_engine.py  # Automated unit test suite
└── README.md       # Project documentation