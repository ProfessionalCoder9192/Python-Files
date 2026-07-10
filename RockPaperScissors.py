import random
import tkinter as tk

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

player_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]


def play_round(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a tie!"
        color = "#555555"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        color = "#2e7d32"
        player_score += 1
    else:
        result = "Computer Wins! 😢"
        color = "#c62828"
        computer_score += 1

    lbl_choices.config(
        text=f"You chose: {player_choice}\nComputer chose: {computer_choice}"
    )
    lbl_result.config(text=result, fg=color)
    lbl_score.config(text=f"Score - You: {player_score} | Comp: {computer_score}")


def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    lbl_choices.config(text="Make your move to start the game!")
    lbl_result.config(text="", fg="#000000")
    lbl_score.config(text="Score - You: 0 | Comp: 0")


lbl_header = tk.Label(
    root,
    text="Rock, Paper, Scissors",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
lbl_header.pack(pady=15)

btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

btn_rock = tk.Button(
    btn_frame,
    text="🪨 Rock",
    font=("Arial", 12),
    width=10,
    command=lambda: play_round("Rock"),
)
btn_rock.grid(row=0, column=0, padx=5)

btn_paper = tk.Button(
    btn_frame,
    text="📄 Paper",
    font=("Arial", 12),
    width=10,
    command=lambda: play_round("Paper"),
)
btn_paper.grid(row=0, column=1, padx=5)

btn_scissors = tk.Button(
    btn_frame,
    text="✂️ Scissors",
    font=("Arial", 12),
    width=10,
    command=lambda: play_round("Scissors"),
)
btn_scissors.grid(row=0, column=2, padx=5)

lbl_choices = tk.Label(
    root,
    text="Make your move to start the game!",
    font=("Arial", 12),
    bg="#f0f0f0",
    fg="#666666",
    justify="center",
)
lbl_choices.pack(pady=20)

lbl_result = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f0f0")
lbl_result.pack(pady=5)

lbl_score = tk.Label(
    root,
    text="Score - You: 0 | Comp: 0",
    font=("Arial", 12, "bold"),
    bg="#f0f0f0",
    fg="#333333",
)
lbl_score.pack(pady=15)

btn_reset = tk.Button(
    root,
    text="Reset Game",
    font=("Arial", 10),
    bg="#e0e0e0",
    command=reset_game,
)
btn_reset.pack(side="bottom", pady=20)

root.mainloop()
