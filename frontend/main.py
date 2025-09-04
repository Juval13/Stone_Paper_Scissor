import tkinter as tk
import random

# --- Game logic ---
choices = ["rock", "paper", "scissors"]

def play(player_choice):
    ai_choice = random.choice(choices)

    if player_choice == ai_choice:
        result = "It's a draw!"
    elif (player_choice == "rock" and ai_choice == "scissors") or \
         (player_choice == "scissors" and ai_choice == "paper") or \
         (player_choice == "paper" and ai_choice == "rock"):
        result = "You win!"
    else:
        result = "AI wins!"

    label_result.config(
        text=f"You: {player_choice.capitalize()} | AI: {ai_choice.capitalize()}\n{result}"
    )

# --- UI setup ---
root = tk.Tk()
root.title("Rock Paper Scissors AI")
root.geometry("400x300")

label_title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
label_title.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=20)

# Create buttons for Rock, Paper, Scissors
for choice in choices:
    btn = tk.Button(
        frame_buttons,
        text=choice.capitalize(),
        width=12,
        height=2,
        font=("Arial", 12),
        command=lambda c=choice: play(c)
    )
    btn.pack(side=tk.LEFT, padx=10)

label_result = tk.Label(root, text="Make your move!", font=("Arial", 14))
label_result.pack(pady=20)

root.mainloop()