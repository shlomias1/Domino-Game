---

# Domino Game (JavaScript Version)

This is a fully interactive Domino game for 2 to 4 players, featuring drag-and-drop functionality, real domino tile images, rotation animation for flipped tiles, and a board built for visual clarity and performance.

---

## Features

* **Supports 2–4 Players**
* **Custom Linked List Implementation** for efficient board management (O(1) insertions at head/tail)
* **Domino Tiles with Transparent Backgrounds** (split from sprite image)
* **Visual Rotation** for flipped tiles using CSS
* **Drag & Drop Interface** (WIP / optional)
* **Game Logic**: tile matching, drawing from stock, win detection
* **Custom Styling** using `style.css` and `Tahoma` font
* **Image Converter Script** in Python for generating 28 domino images from a single image sheet (with optional background removal)

---

## Project Structure

```
DominoGame/
│
├── index.html             # Main game entry point (DOM + layout)
├── style.css              # Visual styling for board, tiles, buttons
├── game.js                # Game logic (domino rules, turns, etc.)
├── ui.js                  # DOM rendering and UI updates
├── images/
│   ├── domino-0-0.png     # All 28 tile images
│   └── ...
├── convertor_dominos_images.py  # Python script for image slicing + background removal
```

---

## Data Structure: Linked List Board

The game board is implemented using a **custom Linked List** data structure (`LinkedList`) with `head` and `tail` references.
This provides **O(1)** insertion at either end of the board — a perfect fit for Domino where players add tiles to either side.

### Benefits:

* Fast updates without shifting elements
* Clean board representation using `to_list()` method
* Minimal memory overhead

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/domino-game-js
cd domino-game-js
```

### 2. Prepare Tile Images (Optional)

You can generate 28 tile images from a sprite using:

```bash
python convertor_dominos_images.py
```

This script:

* Splits the image into 28 domino tiles
* Optionally removes background using `rembg`
* Saves each tile with the name `domino-A-B.png`

### 3. Run the Game

Just open `index.html` in a browser:

```bash
start index.html  # or double-click
```

---

## Images & Assets

You can download a full set of domino tile sprites or use the included Python script to create them.
Be sure your images are in the `/images/` folder and named as:

```
domino-0-0.png, domino-0-1.png, ..., domino-6-6.png
```

---

## Styling

* All UI buttons use `Tahoma` font and rounded corners
* Valid playable tiles are **green**, invalid ones are **red**
* Rotated tiles are visually flipped using CSS transforms

---

## To Do / Future Enhancements

* [x] Flipped tile visual indicator
* [x] Background-transparent tiles
* [x] Highlight legal moves
* [ ] Drag & Drop support for placing tiles
* [ ] AI Opponent (Optional)
* [ ] Score tracking

---

## Credits

* Developed by: **\[Your Name]**
* Tile image processing powered by [rembg](https://github.com/danielgatis/rembg)
* Font: [Tahoma](https://en.wikipedia.org/wiki/Tahoma)

---
