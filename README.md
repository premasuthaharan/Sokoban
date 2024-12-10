# Sokoban Game

This repository contains an implementation of a simple Sokoban-like game. Sokoban is a classic puzzle game where the player moves boxes to target locations within a grid-based board.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sokoban-game.git
   cd sokoban-game
   ```
2. Ensure all dependencies are satisfied. This game requires a `game_settings.py` file, which defines the game board and constants. An example of its structure might look like:
   ```python
   EMPTY = ' '
   WALL = '#'
   TARGET = '.'
   SPRITE = '@'
   SPRITE_T = '+'
   BOX_NS = '$'
   BOX_S = '*'

   board = [
       ['#', '#', '#', '#', '#'],
       ['#', ' ', '@', '$', '#'],
       ['#', '.', ' ', ' ', '#'],
       ['#', '#', '#', '#', '#']
   ]
   ```

### Running the Game

Run the game script using Python:

```bash
python sokoban.py
```

### Controls

- `w`: Move up
- `s`: Move down
- `a`: Move left
- `d`: Move right
- `q`: Quit the game
- `space`: Reset the board

### Win Condition

The game ends with a win message when all targets (`.`) are covered by boxes (`*`).
