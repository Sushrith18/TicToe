import tkinter as tk
import random

board = [" " for _ in range(9)]
buttons = []

def check_win(player):
    win_sets = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for ws in win_sets:
        if board[ws[0]] == board[ws[1]] == board[ws[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def system_move():
    empty_pos = [i for i in range(9) if board[i] == " "]
    if empty_pos:
        pos = random.choice(empty_pos)
        board[pos] = "O"
        buttons[pos].config(text="O", state="disabled")

        if check_win("O"):
            status_label.config(text="System wins")
            disable_buttons()
        elif is_draw():
            status_label.config(text="Game Draw")

def player_move(pos):
    if board[pos] == " ":
        board[pos] = "X"
        buttons[pos].config(text="X", state="disabled")

        if check_win("X"):
            status_label.config(text="You win")
            disable_buttons()
        elif is_draw():
            status_label.config(text="Game Draw")
        else:
            system_move()

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    status_label.config(text="Your turn")

root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

for i in range(9):
    btn = tk.Button(
        root,
        text=" ",
        width=10,
        height=4,
        font=("Arial", 14),
        command=lambda i=i: player_move(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="Your turn", font=("Arial", 12))
status_label.grid(row=3, column=0, columnspan=3, pady=5)

reset_btn = tk.Button(root, text="Reset Game", command=reset_game)
reset_btn.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
