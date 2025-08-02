# Maze Runner

## Description

Maze Runner is a Python application that generates random mazes and visually solves them using a recursive backtracking algorithm. The application features a graphical interface built with Tkinter that displays the maze generation process and the pathfinding solution in real-time.

The project implements:
- **Maze Generation**: Creates random mazes using a depth-first search algorithm with wall breaking
- **Maze Solving**: Finds a path from the top-left corner to the bottom-right corner using recursive backtracking
- **Visual Animation**: Real-time visualization of both maze generation and solving processes
- **Configurable Parameters**: Customizable maze dimensions, cell sizes, and starting positions

## Why?

This project was created to:
- **Learn Algorithm Visualization**: Demonstrate how classic algorithms like maze generation and pathfinding work step-by-step
- **Practice Object-Oriented Programming**: Implement clean, modular code structure with proper separation of concerns
- **Explore GUI Development**: Build an interactive graphical application using Python's Tkinter library
- **Educational Purpose**: Provide a visual tool for understanding how recursive algorithms solve complex problems
- **Problem-Solving Skills**: Tackle the classic computer science problem of maze generation and solving

Whether you're a student learning algorithms, a developer wanting to see these concepts in action, or someone who simply enjoys watching mazes being solved, this project offers an engaging visual experience.

## Quick Start

### Prerequisites
- Python 3.x
- Tkinter (usually included with Python)

### Installation & Running
1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd maze_runner
   ```
3. Run the application:
   ```bash
   python3 main.py
   ```
   Or use the provided shell script:
   ```bash
   ./main.sh
   ```

The application will open a window displaying a 10x10 maze that generates and then solves itself automatically.

## Usage

### Basic Usage
Run `python3 main.py` to start the application with default settings:
- 10x10 maze grid
- 50x60 pixel cells
- Automatic solving after generation

### Customizing the Maze
You can modify the maze parameters in `main.py`:

```python
# Maze(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window)
maze = Maze(10, 10, 8, 10, 50, 60, win)
```

Parameters:
- `x1, y1`: Starting position for drawing the maze
- `num_rows`: Number of rows in the maze
- `num_cols`: Number of columns in the maze  
- `cell_size_x, cell_size_y`: Pixel dimensions of each cell
- `win`: The window object for rendering

### Running Tests
Execute the test suite:
```bash
python3 tests.py
```
Or use the test script:
```bash
./test.sh
```

### Project Structure
```
maze_runner/
├── main.py          # Entry point and main application
├── maze.py          # Maze class with generation and solving logic
├── cell.py          # Cell class representing individual maze cells
├── window.py        # Window class for GUI rendering
├── point.py         # Point class for coordinate management
├── line.py          # Line class for drawing operations
├── tests.py         # Test suite
├── main.sh          # Shell script to run the application
└── test.sh          # Shell script to run tests
```

## Contributing

Contributions are welcome! Here are some ways you can help improve Maze Runner:

### Getting Started
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run the tests: `python3 tests.py`
5. Commit your changes: `git commit -am 'Add new feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

### Areas for Contribution
- **Algorithm Improvements**: Implement different maze generation algorithms (Kruskal's, Prim's, etc.)
- **Solving Algorithms**: Add alternative pathfinding methods (A*, Dijkstra's, BFS)
- **UI Enhancements**: Improve the graphical interface, add controls for speed/pause
- **Configuration**: Add command-line arguments or configuration files
- **Performance**: Optimize rendering and algorithm performance
- **Testing**: Expand test coverage and add integration tests
- **Documentation**: Improve code comments and add more usage examples

### Code Style
- Follow PEP 8 Python style guidelines
- Add docstrings to new functions and classes
- Keep functions focused and modular
- Add appropriate comments for complex logic

### Reporting Issues
If you find bugs or have feature requests, please open an issue with:
- Clear description of the problem or feature
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Your Python version and operating system

Thank you for your interest in contributing to Maze Runner!
