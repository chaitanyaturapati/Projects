import tkinter as tk
import random

window = tk.Tk()
window.title("Rock Paper Sissor Game")
window.geometry("400x450")
window.config(bg="#fffacd")  

choices = ['rock', 'paper', 'sissor']  # lowercase for consistency

title_label = tk.Label(window, text="🎮 Rock Paper Sissor 🎮", font=('Comic Sans MS', 18, 'bold'), bg="#fffacd", fg="#333")
title_label.pack(pady=20)

user_choice_label = tk.Label(window, text="", font=('Arial', 12), bg="#fffacd")
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="", font=('Arial', 12), bg="#fffacd")
computer_choice_label.pack()

result_label = tk.Label(window, text="", font=('Arial', 16, 'bold'), bg="#fffacd")
result_label.pack(pady=20)

def play(user_choice):
    user_choice = user_choice.lower()
    comp_choice = random.choice(choices)

    user_choice_label.config(text=f"🧍 You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"💻 Computer chose: {comp_choice.capitalize()}")

    if user_choice == comp_choice:
        result_label.config(text="😐 It's a Tie!", fg='blue')
    elif (user_choice == 'rock' and comp_choice == 'sissor') or \
         (user_choice == 'paper' and comp_choice == 'rock') or \
         (user_choice == 'sissor' and comp_choice == 'paper'):
        result_label.config(text="🎉 You win!", fg='green')
    else:
        result_label.config(text="😢 You lose!", fg='red')

# Button style
btn_style = {'font': ('Arial', 12, 'bold'), 'width': 12, 'bg': 'black', 'fg': 'white', 'bd': 2, 'relief': 'raised'}

tk.Button(window, text="🪨 Rock", command=lambda: play('rock'), **btn_style).pack(pady=5)
tk.Button(window, text="📄 Paper", command=lambda: play('paper'), **btn_style).pack(pady=5)
tk.Button(window, text="✂️ Sissor", command=lambda: play('sissor'), **btn_style).pack(pady=5)

# Exit Button
tk.Button(window, text="❌ Exit", command=window.quit, font=('Arial', 11), bg='red', fg='white').pack(pady=15)

window.mainloop()
