# Advent of Code Python Solutions

## Project Structure
- `advent_of_code/`: Main package directory
  - `solutions/`: Individual day solutions
  - `utils/`: Utility functions and helpers
- `inputs/`: Input files for each day
- `tests/`: Pytest test files
- `main.py`: Primary script to run solutions

## Setup
1. Clone the repository
2. Install uv for https://github.com/astral-sh/uv
3. Create a virtual environment
   ```bash
   uv init
   source .venv/bin/activate  
   or run with just uv run main.py
   ```
4. Install requirements
   ```bash
   uv install
   ```

## Running Solutions
- Run a specific day: `uv run main.py`
- Run tests: `uv runpytest`

## Tips
- Place your puzzle inputs in the `inputs/` directory
- Use utility functions in `utils/` for common parsing tasks
- Follow the template in `solutions/day_template.py` for new days