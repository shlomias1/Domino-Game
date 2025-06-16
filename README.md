# Domino Game in Python

This is a GUI-based **Domino game** built using `tkinter`, supporting 2–4 players.

The project is structured with clear separation between:
- **Game logic (`DominoGame`)**
- **Graphical interface (`DominoGUI`)**
- **Data structure foundation (custom `LinkedList`)**

---

## Features

- Turn-based logic for 2–4 players
- Color-coded playable tiles (green = valid, red = invalid)
- Automatic tile rotation when placing
- End-of-game win detection
- User-friendly GUI with Tahoma font and rounded buttons

---

## Data Structure Optimization

A key design decision in this project is the use of a **custom Linked List** to represent the domino board.

### Why?

In Domino, new tiles can be added to either the **head** (left side) or **tail** (right side) of the board.  
Using a standard list would require shifting elements (O(n)) if inserting at the head.

### Instead:

We implemented a `LinkedList` class with:
- `self.head` – pointing to the first node
- `self.tail` – pointing to the last node

This allows:
- **O(1)** time complexity for:
  - `add_to_head()`
  - `add_to_tail()`
- Efficient board updates and easy expansion from both ends

### LinkedList methods used:

```python
add_to_head(value)  # O(1)
add_to_tail(value)  # O(1)
to_list()           # for rendering
````

---

## GUI Design

* Built with `tkinter`
* Buttons are styled with:

  * Rounded edges (`relief='groove'`)
  * Font: `Tahoma`
* The player's hand shows playable tiles in **green**, invalid tiles in **red**

---

## Folder Structure

```
├── linked_list.py
├── domino_game.py
├── gui.py
├── main.py
└── README.md
```

---

## Running the Game

```bash
python main.py
```

Then:

* Choose number of players (2–4)
* Click on tiles to play
* Use "Draw Tile" to take from the stock if stuck

---

## TODO / Future Features

* AI opponent for single-player
* Scorekeeping & round history
* Sound effects & animations
* Multiplayer over network

---
