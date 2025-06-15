# main.py
import tkinter as tk
from gui import DominoGUI

def Game():
    root = tk.Tk()
    root.title("Domino - Start Game")

    def start_game():
        try:
            num_players = int(entry.get())
            if not 2 <= num_players <= 4:
                raise ValueError
            start_frame.destroy()
            DominoGUI(root, num_players)
        except ValueError:
            error_label.config(text="Please enter a number between 2 and 4")

    start_frame = tk.Frame(root)
    start_frame.pack(pady=40)

    title = tk.Label(start_frame, text="Welcome to Domino!", font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    prompt = tk.Label(start_frame, text="Enter number of players (2 to 4):", font=("Helvetica", 12))
    prompt.pack(pady=5)

    entry = tk.Entry(start_frame, font=("Helvetica", 12), justify="center")
    entry.pack(pady=5)

    start_button = tk.Button(start_frame, text="Start Game", font=("Helvetica", 12), command=start_game)
    start_button.pack(pady=10)

    error_label = tk.Label(start_frame, text="", fg="red", font=("Helvetica", 10))
    error_label.pack()

    root.mainloop()

if __name__ == "__main__":
    Game()