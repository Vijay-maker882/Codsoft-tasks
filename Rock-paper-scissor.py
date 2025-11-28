from tkinter import *
from random import choice

window = Tk()
window.title("ROCK PAPER SCISSORS GAME")
window.configure(background="black")

# -----------------------
# SCORE VARIABLES
# -----------------------
p1_score_val = 0
p2_score_val = 0
computer_score_val = 0

# CURRENT MODE & TURN
mode = "single"   # single / multi
turn = 1          # Player turn for multiplayer


# -----------------------
# LABELS
# -----------------------
label_player1 = Label(window, text="❓", font=("Arial", 80), bg="black", fg="white")
label_player2 = Label(window, text="❓", font=("Arial", 80), bg="black", fg="white")
label_player2.grid(row=1, column=0, padx=20)
label_player1.grid(row=1, column=4, padx=20)

# Score labels
p1_score = Label(window, text=p1_score_val, font=('arial', 50, "bold"), fg="red", bg="black")
p2_score = Label(window, text=p2_score_val, font=('arial', 50, "bold"), fg="red", bg="black")
p1_score.grid(row=1, column=3)
p2_score.grid(row=1, column=1)

# Turn indicator
turn_label = Label(window, text="Mode: SINGLE PLAYER", font=("Arial", 22), bg="black", fg="yellow")
turn_label.grid(row=0, column=0, columnspan=5, pady=10)


# -----------------------
# EMOJIS
# -----------------------
emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}


# -----------------------
# SCORECARD POPUP
# -----------------------
def view_scorecard():
    score_win = Toplevel(window)
    score_win.title("Scorecard")
    score_win.configure(background="black")

    Label(score_win, text="🏆 SCORECARD 🏆", font=("Arial", 30, "bold"), fg="gold", bg="black").pack(pady=20)

    Label(score_win, text=f"Player 1 Wins: {p1_score_val}", font=("Arial", 20), fg="white", bg="black").pack(pady=5)
    Label(score_win, text=f"Player 2 Wins: {p2_score_val}", font=("Arial", 20), fg="white", bg="black").pack(pady=5)
    Label(score_win, text=f"Computer Wins: {computer_score_val}", font=("Arial", 20), fg="white", bg="black").pack(pady=5)

    Button(score_win, text="Close", font=("Arial", 15), command=score_win.destroy).pack(pady=20)


# -----------------------
# PLAYER CHOICE HANDLER
# -----------------------
def player_choice(pick):
    global p1_score_val, p2_score_val, computer_score_val, turn

    if mode == "single":
        # ---------- SINGLE PLAYER MODE ----------
        comp_pick = choice(["rock", "paper", "scissors"])

        label_player1.config(text=emoji[pick])
        label_player2.config(text=emoji[comp_pick])

        # win logic
        if pick == comp_pick:
            pass
        elif (pick == "rock" and comp_pick == "scissors") or \
             (pick == "paper" and comp_pick == "rock") or \
             (pick == "scissors" and comp_pick == "paper"):
            p1_score_val += 1
        else:
            computer_score_val += 1
            p2_score_val = computer_score_val  # show in P2 slot

    else:
        # ---------- MULTIPLAYER MODE ----------
        if turn == 1:
            # First player's turn
            player_choice.p1_pick = pick
            label_player1.config(text=emoji[pick])
            turn = 2
            turn_label.config(text="Player 2's Turn (Multiplayer Mode)")
            return

        elif turn == 2:
            # Second player's turn
            p2_pick = pick
            label_player2.config(text=emoji[p2_pick])

            p1_pick = player_choice.p1_pick

            # Determine winner
            if p1_pick == p2_pick:
                pass
            elif (p1_pick == "rock" and p2_pick == "scissors") or \
                 (p1_pick == "paper" and p2_pick == "rock") or \
                 (p1_pick == "scissors" and p2_pick == "paper"):
                p1_score_val += 1
            else:
                p2_score_val += 1

            # Reset to Player 1 turn
            turn = 1
            turn_label.config(text="Player 1's Turn (Multiplayer Mode)")

    # Update scores
    p1_score.config(text=p1_score_val)
    p2_score.config(text=p2_score_val)


# -----------------------
# SWITCH MODES
# -----------------------
def switch_mode():
    global mode, turn
    if mode == "single":
        mode = "multi"
        turn = 1
        turn_label.config(text="Player 1's Turn (Multiplayer Mode)")
        label_player1.config(text="❓")
        label_player2.config(text="❓")
    else:
        mode = "single"
        turn_label.config(text="Mode: SINGLE PLAYER")
        label_player1.config(text="❓")
        label_player2.config(text="❓")


# -----------------------
# BUTTONS
# -----------------------
button_rock = Button(window, text="🪨 Rock", font=("Arial", 20, "bold"), width=10,
                     command=lambda: player_choice("rock"))
button_rock.grid(row=2, column=1)

button_paper = Button(window, text="📄 Paper", font=("Arial", 20, "bold"), width=10,
                      command=lambda: player_choice("paper"))
button_paper.grid(row=2, column=2)

button_scissors = Button(window, text="✂️ Scissors", font=("Arial", 20, "bold"), width=10,
                         command=lambda: player_choice("scissors"))
button_scissors.grid(row=2, column=3)

# Mode switch button
mode_button = Button(window, text="Switch Mode", font=("Arial", 18), command=switch_mode)
mode_button.grid(row=3, column=1, pady=20)

# Scorecard button
scorecard_button = Button(window, text="View Scorecard", font=("Arial", 18), command=view_scorecard)
scorecard_button.grid(row=3, column=3, pady=20)

window.mainloop()
