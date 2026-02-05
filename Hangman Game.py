import random
import tkinter as tk
from tkinter import messagebox

words = ["python", "computer", "security", "network", "program"]
word = random.choice(words)
guessed = []
attempts = 6
buttons = {}   # store keyboard buttons

def update_display():
    display = ""
    for letter in word:
        display += letter + " " if letter in guessed else "_ "
    word_label.config(text=display)
    attempts_label.config(text=f"Attempts Left: {attempts}")

def guess_letter(letter):
    global attempts
    letter = letter.lower()

    if not letter.isalpha() or letter in guessed:
        return

    guessed.append(letter)

    # disable button & show visual effect
    if letter in buttons:
        buttons[letter].config(state=tk.DISABLED, bg="lightgray")

    if letter not in word:
        attempts -= 1

    update_display()

    if all(l in guessed for l in word):
        messagebox.showinfo("Hangman", "🎉 You Win!")
        root.destroy()
    elif attempts == 0:
        messagebox.showinfo("Hangman", f"❌ Game Over!\nWord was: {word}")
        root.destroy()

# 🔑 Keyboard handler
def key_pressed(event):
    guess_letter(event.char)

root = tk.Tk()
root.title("Hangman Game")

# bind physical keyboard
root.bind("<Key>", key_pressed)

word_label = tk.Label(root, font=("Arial", 20))
word_label.pack(pady=10)

attempts_label = tk.Label(root, font=("Arial", 14))
attempts_label.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

# create on-screen keyboard
for c in "abcdefghijklmnopqrstuvwxyz":
    btn = tk.Button(
        frame,
        text=c,
        width=4,
        command=lambda x=c: guess_letter(x)
    )
    btn.pack(side=tk.LEFT)
    buttons[c] = btn   # store button reference

update_display()
root.mainloop()
