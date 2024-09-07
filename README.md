# Game of Life Simulation

This project is an implementation of Conway's Game of Life using Pyglet. It provides a visual simulation of cellular automaton evolution on a grid, where cells live or die based on their neighboring cells' states.

## Features

- Grid-based cellular automaton simulation
- Random initial state generation
- Customizable grid size and cell size
- Visual representation of cell states
- Automatic updates at regular intervals

## Requirements

- Python 3.x
- Pyglet library

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install pyglet
```

## Usage

Run the `main.py` file to start the simulation:

```
python main.py
```

The simulation will automatically start with a randomly generated initial state.

## Files

- `main.py`: Sets up the Pyglet window and runs the main simulation loop
- `grid.py`: Implements the Grid class, which handles the cellular automaton logic and rendering

## How It Works

1. The simulation creates a window using Pyglet.
2. A grid is initialized with random cell states (alive or dead).
3. For each update cycle:
   - The state of each cell is updated based on its neighbors.
   - Cells with exactly 3 live neighbors come to life.
   - Live cells with 2 or 3 live neighbors survive.
   - All other cells die or remain dead.
4. The grid is redrawn to reflect the new state.
5. This process repeats at regular intervals, creating the illusion of cellular evolution.

## Customization

You can customize the simulation by modifying the following parameters in the code:

- In `main.py`:
  - Change the window size in the `Space` class initialization
  - Adjust the update interval in `pg.clock.schedule_interval()`

- In `grid.py`:
  - Modify `self.size_of_box` to change the cell size
  - Alter the cell colors by changing `self.color` and `self.cell_color`

## Contributing

Contributions to improve the simulation or add new features are welcome. Please feel free to submit pull requests or open issues for any bugs or enhancements.

## License

This project is open-source and available under the MIT License.

## Acknowledgements

This project is based on Conway's Game of Life, a cellular automaton devised by mathematician John Conway in 1970.