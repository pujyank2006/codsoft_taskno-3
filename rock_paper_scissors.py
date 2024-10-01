import tkinter as tk
import random as rn


bg_colour = '#3d6465'

root = tk.Tk()
root.title("Game")
root.eval("tk::PlaceWindow . center")

root.configure(bg=bg_colour)

frame = tk.Frame(root, width=300, height=400, bg='#3d6466')
frame.grid(row=1, column=0, columnspan=6, padx=20, pady=20)

#widgets
tk.Label(frame, text="Rock Paper Scissors",
        bg=bg_colour,
        fg='white',
        font = ("TkMenuFont", 20)
        ).grid(row=0, column=1, columnspan=4)

tk.Label(frame, text="User choice: ",
        bg=bg_colour,
        fg='white',
        font = ("TkMenuFont", 12)
        ).grid(row=1, column=0, sticky='e', columnspan=4)

tk.Label(frame, text="computer's choice: ",
        bg=bg_colour,
        fg='white',
        font = ("TkMenuFont", 12)
        ).grid(row=2, column=0, sticky ='e', columnspan=4)

input1 = tk.StringVar()
input2 = tk.StringVar()

tk.Label(frame, textvariable=input1, fg='white', bg=bg_colour, justify='right', width=10, borderwidth=5).grid(row=1, column=4, padx=10, pady=10)
tk.Label(frame, textvariable=input2, fg='white', bg=bg_colour, justify='right', width=10, borderwidth=5).grid(row=2, column=4, padx=10, pady=10)

choices = ["Rock", "Paper", "Scissors"]

def display1(input):
    comp_input = rn.choice(choices)
    input1.set(input)
    input2.set(comp_input)
    winner(input, comp_input)

def replay():
    input1.set(" ")
    input2.set(" ")

def winner(input, comp_input):
    if(input == comp_input):
        result.set("It's a tie")
    elif(input == "Rock" and comp_input == "Scissors") or \
         (input == "Scissors" and comp_input == "Paper") or \
         (input == "Paper" and comp_input == "Rock"):
        result.set("You Win")
    else:
        result.set("Computer Wins")

button1 = tk.Button(root, text="Rock", width=10, height=2, command=lambda: display1("Rock"), bg=bg_colour, fg='white')
button1.grid(row=3, column=1, padx=10, pady=10)

button2 = tk.Button(root, text="Paper", width=10, height=2, command=lambda: display1("Paper"), bg=bg_colour, fg='white')
button2.grid(row=3, column=2, padx=10, pady=10)

button3 = tk.Button(root, text="Scissors", width=10, height=2, command=lambda: display1("Scissors"), bg=bg_colour, fg='white')
button3.grid(row=3, column=3, padx=10, pady=10)

button4 = tk.Button(root, text="Replay", width=10, height=2, command=replay, bg=bg_colour, fg='white')
button4.grid(row=4, column=2, padx=10, pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, bg=bg_colour, fg='white', font=("TkMenuFont", 14)).grid(row=5, column=1, columnspan=3, padx=20, pady=20)
root.mainloop()