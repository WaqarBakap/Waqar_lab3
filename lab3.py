import tkinter as tk
import random
import string


def generate_block():
    letters = random.choices(string.ascii_uppercase, k=3)
    digit = random.choice(string.digits)
    block = letters + [digit]
    random.shuffle(block)
    return "".join(block)


def generate_key():
    blocks = [generate_block() for _ in range(4)]
    key = "-".join(blocks)
    key_var.set(key)


root = tk.Tk()
root.title("Game Keygen")
root.geometry("600x400")


try:
    bg = tk.PhotoImage(file="art.png")
    bg_label = tk.Label(root, image=bg)
    bg_label.place(relwidth=1, relheight=1)
except:
    pass

key_var = tk.StringVar()

title = tk.Label(root, text="Game Key Generator", font=("Arial", 16), bg="black", fg="white")
title.pack(pady=10)

btn = tk.Button(root, text="Generate Key", font=("Arial", 12), command=generate_key)
btn.pack(pady=10)

label = tk.Label(root, textvariable=key_var, font=("Courier", 18), bg="black", fg="lime")
label.pack(pady=20)

root.mainloop()
