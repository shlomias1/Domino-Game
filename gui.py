import tkinter as tk
from tkinter import messagebox
from domino_game import DominoGame

class DominoGUI:
    def __init__(self, root, num_players):
        self.root = root
        self.root.title("Domino Game")
        self.game = DominoGame(num_players)
        self.buttons = []

        self.board_label = tk.Label(self.root, text="", font=("Courier", 16))
        self.board_label.pack(pady=10)

        self.info_label = tk.Label(self.root, text=f"Player {self.game.current_player + 1}'s Turn", font=("Arial", 12))
        self.info_label.pack(pady=5)

        self.hand_frame = tk.Frame(self.root)
        self.hand_frame.pack(pady=10)

        self.draw_button = tk.Button(self.root, text="Draw Tile", command=self.draw_tile)
        self.draw_button.pack(pady=5)

        self.update_hand_display()

    def format_domino_board(self):
        board_tiles = self.game.current_board()
        domino_str = "  ".join([f"[{a}|{b}]" for a, b in board_tiles])
        return f"Board: {domino_str}"

    def update_hand_display(self):
        for btn in self.buttons:
            btn.destroy()
        self.buttons.clear()

        player_hand = self.game.player_hand(self.game.current_player)
        for tile in player_hand:
            btn = tk.Button(self.hand_frame, text=f"[{tile[0]}|{tile[1]}]", width=6,
                            command=lambda t=tile: self.play_tile(t))
            btn.pack(side=tk.LEFT, padx=2)
            self.buttons.append(btn)

        self.board_label.config(text=self.format_domino_board())
        self.info_label.config(text=f"Player {self.game.current_player + 1}'s Turn")

    def play_tile(self, tile):
        if self.game.valid_moves(tile):
            success = self.game.play_tile(self.game.current_player, tile)
            if success:
                winner = self.game.has_winner()
                if winner is not None:
                    messagebox.showinfo("Game Over", f"Player {winner + 1} wins!")
                    self.root.quit()
                else:
                    self.game.next_turn()
                    self.update_hand_display()
            else:
                messagebox.showwarning("Invalid Move", "Cannot place this tile.")
        else:
            messagebox.showwarning("Invalid Move", "Tile doesn't match the board.")

    def draw_tile(self):
        tile = self.game.draw_tile(self.game.current_player)
        if tile:
            messagebox.showinfo("Tile Drawn", f"You drew: [{tile[0]}|{tile[1]}]")
        else:
            messagebox.showinfo("No Tiles", "No tiles left to draw.")
        self.update_hand_display()
